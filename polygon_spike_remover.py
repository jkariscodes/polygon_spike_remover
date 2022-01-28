# -*- coding: utf-8 -*-
"""
/***************************************************************************
 PolygonSpikeRemover
                                 A QGIS plugin
 This QGIS plugin application reads polygon from a GeoPackage file, checks
 the polygon for existing spikes, removes the spikes and saves the output
 in a new GeoPackage file.
                              -------------------
        begin                : 2022-01-23
        git sha              : $Format:%H$
        copyright            : (C) 2022 by Joseph Kariuki
        email                : contact@josephkariuki.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it is under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from qgis.PyQt.QtCore import QSettings, QTranslator, QCoreApplication, Qt
from qgis.PyQt.QtGui import QIcon, QPixmap
from qgis.PyQt.QtWidgets import (
    QAction, QWidget, QVBoxLayout, QPushButton, QFileDialog, QMessageBox
)
from qgis.core import QgsProject
from qgis.gui import QgsMapCanvas

from .resources import *
from .spike_remover_utils import *
from .polygon_spike_remover_dockwidget import PolygonSpikeRemoverDockWidget
import os.path
from osgeo import ogr


class PolygonSpikeRemover:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # QGIS items
        self.map_canvas = QgsMapCanvas()
        self.map_canvas.refresh()
        self.qgs_project = QgsProject()

        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)

        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'PolygonSpikeRemover_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)
            QCoreApplication.installTranslator(self.translator)

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&Polygon Spike Remover')
        self.toolbar = self.iface.addToolBar(u'PolygonSpikeRemover')
        self.toolbar.setObjectName(u'PolygonSpikeRemover')
        self.pluginIsActive = False
        self.dockwidget = None
        self._btn_icons = None
        self.widget = None
        self.file_dlg = None
        self.vbox_layout = None
        self.btn_load_gpkg = None
        self.btn_remove_spike = None
        self.btn_clear_map = None

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('PolygonSpikeRemover', message)

    def add_action(
            self,
            icon_path,
            text,
            callback,
            enabled_flag=True,
            add_to_menu=True,
            add_to_toolbar=True,
            status_tip=None,
            whats_this=None,
            parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToVectorMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/polygon_spike_remover/img/icons/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'Polygon Spike Remover'),
            callback=self.run,
            parent=self.iface.mainWindow())

    # --------------------------------------------------------------------------

    def onClosePlugin(self):
        """Cleanup necessary items here when plugin dockwidget is closed"""

        # print "** CLOSING PolygonSpikeRemover"

        # disconnects
        self.dockwidget.closingPlugin.disconnect(self.onClosePlugin)
        # when closing the docked window:
        # self.dockwidget = None

        self.pluginIsActive = False

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginVectorMenu(
                self.tr(u'&Polygon Spike Remover'),
                action)
            self.iface.removeToolBarIcon(action)
        del self.toolbar

    def run(self):
        """Run method that loads and starts the plugin"""

        if not self.pluginIsActive:
            self.pluginIsActive = True
            if not self.dockwidget:
                self.dockwidget = PolygonSpikeRemoverDockWidget()
            # connect to provide cleanup on closing of dockwidget
            self.dockwidget.closingPlugin.connect(self.onClosePlugin)
            # Set button text
            if not self.btn_load_gpkg:
                self.btn_load_gpkg = QPushButton()
                self.btn_load_gpkg.setText('Open geopackage...')
            if not self.btn_remove_spike:
                self.btn_remove_spike = QPushButton()
                self.btn_remove_spike.setText('Remove spike(s)')
            if not self.btn_clear_map:
                self.btn_clear_map = QPushButton()
                self.btn_clear_map.setText('Clear map view')
            # Set button icons
            if not self._btn_icons:
                self._btn_icons = {
                    'load_data': QPixmap(
                        ':/plugins/polygon_spike_remover/img/icons/load_data.png'
                    ),
                    'remove_spike': QPixmap(
                        ':/plugins/polygon_spike_remover/img/icons/remove_spike.png'
                    ),
                    'clear_map': QPixmap(
                        ':/plugins/polygon_spike_remover/img/icons/clear_map.png'
                    )
                }
            self.btn_load_gpkg.setIcon(
                QIcon(self._btn_icons.get('load_data'))
            )
            self.btn_remove_spike.setIcon(
                QIcon(self._btn_icons.get('remove_spike'))
            )
            self.btn_clear_map.setIcon(
                QIcon(self._btn_icons.get('clear_map'))
            )
            # Connecting signals to slots
            self.btn_load_gpkg.clicked.connect(self._on_load_geopackage)
            self.btn_remove_spike.clicked.connect(self._on_remove_spike)
            self.btn_clear_map.clicked.connect(self._on_clear_map)
            # Add buttons to layout
            if not self.vbox_layout:
                self.vbox_layout = QVBoxLayout()
                self.vbox_layout.addWidget(self.btn_load_gpkg)
                self.vbox_layout.addWidget(self.btn_remove_spike)
                self.vbox_layout.addWidget(self.btn_clear_map)

            if not self.widget:
                self.widget = QWidget()
                self.widget.setLayout(self.vbox_layout)

            self.dockwidget.setWidget(self.widget)
            # show the dockwidget
            self.iface.addDockWidget(Qt.RightDockWidgetArea, self.dockwidget)
            self.dockwidget.show()
            # Check if layers exist in map view
            if len(self.iface.mapCanvas().layers()) == 0:
                self.btn_clear_map.setDisabled(True)
                self.btn_remove_spike.setDisabled(True)
            else:
                self.btn_clear_map.setEnabled(True)
                self.btn_remove_spike.setEnabled(True)

    def _on_load_geopackage(self):
        """
        Slot raised to open a GeoPackage file from the file system.
        """
        if not self.file_dlg:
            self.file_dlg = QFileDialog()
            path, _ = self.file_dlg.getOpenFileName(
                None,
                'Select a GeoPackage file...',
                '~/',
                '*.gpkg'
            )

            if path:
                self._load_layer(path)

    def _load_layer(self, file_path):
        """
        Check geometry type of each layer in the geopackage file.
        :param file_path: String for path of layer.
        :type file_path: str, QString
        """
        # TODO check if layers are polygons
        gpkg_layers = [n.GetName() for n in ogr.Open(file_path)]
        for name in gpkg_layers:
            # vlayer.geometryType() == QgsWkbTypes.PolygonGeometry
            self.iface.addVectorLayer(
                file_path + "|layername=" + name, name, 'ogr'
            )

        if len(self.iface.mapCanvas().layers()) == 0:
            self.btn_remove_spike.setEnabled(True)
            self.btn_clear_map.setEnabled(True)

    def _on_remove_spike(self):
        """
        Slot raised when button for removing spikes is clicked.
        """
        loaded_layers = self.iface.mapCanvas().layers()
        if len(loaded_layers) > 0:
            layer_paths = [layer.dataProvider().dataSourceUri()
                           for layer in self.iface.mapCanvas().layers()]
            self._process_gpkg(layer_paths)

    def _process_gpkg(self, paths):
        """
        Process loaded layers into correct geometry where errors exist.
        :param paths: List containing all paths.
        :type paths: str
        """
        for path in paths:
            path_to_gpkg = path.split('|')[0]
            ds = load_geopackage(path_to_gpkg)
            # Check validity of layer CRS
            if not validate_crs(ds):
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText("Error in processing layer CRS")
                msg_box.setWindowTitle("GeoPackage processing Error")
                msg_box.setDetailedText(
                    f'The geopackage layer {path_to_gpkg} CRS is invalid.'
                )
                msg_box.exec()
            else:
                self._process_azimuths(ds, path)

    def _process_azimuths(self, data_source, file_path):
        """
        Performs forward and inverse geodetic, or Great Circle, computations.
        The forward computation (using the ‘fwd’ method) involves determining
        latitude, longitude and back azimuth of a terminus point given the
        latitude and longitude of an initial point, plus azimuth and distance.
        :param data_source: Container for the data source.
        :type data_source: GeoPandasDataFrame
        :param file_path: Path to the data.
        :type file_path: str
        """
        azimuth_ext = extract_crs_geod(data_source)
        process_geometry = GeometryProcessor(1.0, 100000)
        res = []

        for _item in data_source.itertuples():
            geom = _item.geometry
            ext = process_geometry.process_sequence(
                azimuth_ext,
                geom.exterior.coords
            )
            interiors = []
            for inner in geom.interiors:
                processed_interior_ring = process_geometry.process_sequence(
                    azimuth_ext,
                    inner.coords,
                )

                interiors.append(processed_interior_ring)

            res.append((_item.name, geometry.Polygon(ext, interiors)))

        processed_ds = GeoDataFrame(
            res,
            columns=['name', 'geometry'],
            crs=data_source.crs
        )
        self._save_gpkg(file_path, processed_ds)

    def _save_gpkg(self, output, clean_ds):
        """
        Save the processed GeoPackage to a given location in the file system.
        :param output: Container for the data source.
        :type output: GeoPandasDataFrame
        :param clean_ds: Path to the cleaned data frame.
        :type clean_ds: GeoPandas DataFrame
        """
        path = output.split('|')[0]
        file_path = path.partition('.')
        output_path = file_path[0] + '_output' + '.gpkg'
        if output_path:
            save_geopackage(output_path, clean_ds)
            self._display_cleaned_gpkg(output_path)

    def _display_cleaned_gpkg(self, path):
        """
        Load processed geopackage file in QGIS Map View.
        :param path: Location of the cleaned GeoPackage file..
        :type path: str
        """
        if not path:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Error in loading layer")
            msg_box.setWindowTitle("GeoPackage Loading Error")
            msg_box.setDetailedText(
                f'The geopackage layer {path} could not be loaded.'
            )
            msg_box.exec()
        else:
            # Add processed layer in QGIS Map view
            v_layer = self.iface.addVectorLayer(
                path, 'output', 'ogr'
            )
            if not v_layer:
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText("Invalid GeoPackage layer")
                msg_box.setWindowTitle("GeoPackage Loading Error")
                msg_box.setDetailedText(
                    f'The geopackage layer {path} is invalid.'
                )
                msg_box.exec()

            self.btn_remove_spike.setDisabled(True)

    def _on_clear_map(self):
        """
        Remove all layers from the map view.
        """
        if len(self.iface.mapCanvas().layers()) > 0:
            QgsProject.instance().removeAllMapLayers()
            QgsProject.instance().clear()

        if len(self.iface.mapCanvas().layers()) == 0:
            self.btn_remove_spike.setDisabled(True)
            self.btn_clear_map.setDisabled(True)

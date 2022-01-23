# -*- coding: utf-8 -*-
"""
/***************************************************************************
 PolygonSpikeRemoverDockWidget
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

import os

from qgis.PyQt import QtGui, QtWidgets, uic
from qgis.PyQt.QtCore import pyqtSignal

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'polygon_spike_remover_dockwidget_base.ui'))


class PolygonSpikeRemoverDockWidget(QtWidgets.QDockWidget, FORM_CLASS):

    closingPlugin = pyqtSignal()

    def __init__(self, parent=None):
        """Constructor."""
        super(PolygonSpikeRemoverDockWidget, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://doc.qt.io/qt-5/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)

    def closeEvent(self, event):
        self.closingPlugin.emit()
        event.accept()

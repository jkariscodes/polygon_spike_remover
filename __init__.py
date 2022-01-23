# -*- coding: utf-8 -*-
"""
/***************************************************************************
 PolygonSpikeRemover
                                 A QGIS plugin
 This QGIS plugin application reads polygon from a GeoPackage file, checks
 the polygon for existing spikes, removes the spikes and saves the output in
 a new GeoPackage file.
                             -------------------
        begin                : 2022-01-23
        copyright            : (C) 2022 by Joseph Kariuki
        email                : contact@josephkariuki.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load PolygonSpikeRemover class from file PolygonSpikeRemover.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .polygon_spike_remover import PolygonSpikeRemover
    return PolygonSpikeRemover(iface)

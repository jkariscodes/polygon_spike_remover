## Polygon Spike Remover

This is a QGIS Desktop plugin that reads data in particular polygons from an OGC GeoPackage file residing in the 
computer's file system and loads it in the QGIS Map View. It also checks if the loaded polygon contains spikes and if it
contains, removes them and saves the output in a new GeoPackage file without altering the original.
### Installation
To install this plugin, one requires [QGIS Desktop](https://qgis.org), an Open Source Desktop GIS software, 
[Python](https://python.org) with [pip](https://pip.pypa.io) installed in the computer. Other external dependencies include
1. [Pyproj](https://pypi.org/project/pyproj/) - For handling Coordinate Reference System checks on the data.
2. [GeoPandas](https://geopandas.org/) -  Interface for importing geopackage to a pandas dataframe for processing.
3. [Shapely](https://shapely.readthedocs.io) - Handling processing of coordinates in a plane independent of data format.</br></br>
#### On Windows
To install the requirements (tested on Windows 10 OS):
* Navigate to [QGIS download website](https://www.qgis.org/en/site/forusers/download.html#windows) and download OSGeo4W 
network installer which provides more options for downloading of package dependencies and libraries as opposed to the usual
installer. The network installer appears in the file as shown below.

<img src="https://github.com/jkariukidev/polygon_spike_remover/blob/main/img/readme/osgeo4w_installer.png">

* Running the setup installer displays an installation wizard. The pages of the wizard are as follows:
Ensure the "Advanced Install" radio button is checked below. Click Next button to continue. 

<img src="https://raw.githubusercontent.com/jkariukidev/polygon_spike_remover/main/img/readme/osgeo4w_installer.png">

* For new users, install from the internet by ensuring the selected radio button appears as shown below.

<img src="ihttps://raw.githubusercontent.com/jkariukidev/polygon_spike_remover/main/img/readme/osgeo4w_installer_1.png">

* Install for all users to allow other user accounts to access OSGeo functions. Click Next to continue

<img src="https://raw.githubusercontent.com/jkariukidev/polygon_spike_remover/main/img/readme/osgeo4w_installer_2.png">

* Browse to the preferred download location of the installation files and the selected path shall be shown once
selected. For the start menu name, leave as default.

<img src="https://raw.githubusercontent.com/jkariukidev/polygon_spike_remover/main/img/readme/osgeo4w_installer_3.png">

* In this page you can leave as default and click Next.

<img src="https://raw.githubusercontent.com/jkariukidev/polygon_spike_remover/main/img/readme/osgeo4w_installer_4.png">

* I prefer downloading from osgeo repository but one is at liberty to download from either and also add a repository
that is not on the list show. Once done, click Next button to continue with lis selection of components..

<img src="https://raw.githubusercontent.com/jkariukidev/polygon_spike_remover/main/img/readme/osgeo4w_installer_5.png">

* From the list under commandline utilities, select the shown Python items. This will install Python core items which are
important in our project.

<img src="https://raw.githubusercontent.com/jkariukidev/polygon_spike_remover/main/img/readme/osgeo4w_installer_6_python.png"/>

* From the list search for GeoPandas which is also a requirement for this project.

<img src="https://raw.githubusercontent.com/jkariukidev/polygon_spike_remover/main/img/readme/osgeo4w_installer_6_python_geopandas.png"/>

* Select Python Index Package which can come in handy in upgrading and installing other packages independent of this project.

<img src="https://raw.githubusercontent.com/jkariukidev/polygon_spike_remover/main/img/readme/osgeo4w_installer_6_python_pip.png"/>

* Select Shapely and Pyproj packages which are important for this project.

<img src="https://raw.githubusercontent.com/jkariukidev/polygon_spike_remover/main/img/readme/osgeo4w_installer_6_python_pyproj_shapely_.png"/>

* Select PyQt5 for GUI development and customization if one needs to re-design UI layout or create custom UI widgets.

<img src="https://raw.githubusercontent.com/jkariukidev/polygon_spike_remover/main/img/readme/osgeo4w_installer_6_python_pyqt5_.png"/>

* Finally, ensure that QGIS Desktop is selected. I prefer using the Long Term Release (LTR) for it is most stable. After all that click
Next button to continue

<img src="https://raw.githubusercontent.com/jkariukidev/polygon_spike_remover/main/img/readme/osgeo4w_installer_6_qgis_ltr_.png"/>

* After successful installation, download the plugin from this repository or use [Git](https://git-scm.com) to clone the plugin in the 
QGIS Desktop Plugins folder which can be accessed at `%APPDATA%\QGIS\QGIS3\profiles\default\python\plugins\` where
`%APPDATA%` is a Windows variable for `C:\Users\<Account User>\AppData\Roaming\` and could be hidden in mose 
### Using the Plugin
1. Open QGIS Desktop from the shortcut on Desktop or from Start Menu. For the Start Menu, she shortcuts should appead as shown below.

<img src="https://raw.githubusercontent.com/jkariukidev/polygon_spike_remover/main/img/readme/qgis_shortcut.png"/>

Alternatively, one can run it from OSGeo4W shell. Please refer to the commandline options from [OSGeo4W](https://trac.osgeo.org/osgeo4w/wiki/CommandLine)
2. After the QGIS Desktop has loaded, the toolbar should contain a shortcut for the Polygon Spike Remover plugin as shown below.

<img src="https://raw.githubusercontent.com/jkariukidev/polygon_spike_remover/main/img/readme/toolbar_shortcut.png"/><br> and the menu also appears under Vector Menu in the QGIS Menu Bar as 
shown below.

<img src="https://raw.githubusercontent.com/jkariukidev/polygon_spike_remover/main/img/readme/plugin_menu.png"/>

3. To see the plugins details, click the QGIS Plugin Menu and under that click Manage and Install Plugins... whcih will
try to connect to the [QGIS Plugin Repository](https://plugins.qgis.org/) and then show the list of plugins. In the search bar
at the top, type 'Polygon Spike Remover' and it shall show the plugin and click on it to show more information as shown below.

<img src="https://raw.githubusercontent.com/jkariukidev/polygon_spike_remover/main/img/readme/qgis_plugin_info.png"/>

4. When one clicks the plugin shortcut, it launches a docked widget user interface containing three buttons with icons and 
text as shown below.

<img src="https://raw.githubusercontent.com/jkariukidev/polygon_spike_remover/main/img/readme/user_interface.png"/>



### Support or Contact

Email: contact@josephkariuki.com

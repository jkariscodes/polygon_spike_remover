<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->



<!-- PROJECT LOGO -->
<br />
<div align="center">

  ![Project Logo][logo]

  <h3 align="center">Polygon Spike Remover</h3>

  <p align="center">
    A spike remover QGIS plugin
    <br />
    <br />
    <br />
    <a href="https://github.com/jkariukidev/polygon_spike_remover">View Workflow</a>
    ·
    <a href="https://github.com/jkariukidev/polygon_spike_remover/issues">Report Bug</a>
    ·
    <a href="https://github.com/jkariukidev/polygon_spike_remover/issues">Request Feature</a>
  </p>
</div>



<!-- ABOUT THE PROJECT -->

<div align="center">

## About The Project

![Product Name Screen Shot][product-screenshot]

</div>

The Polygon Spike Remover is a QGIS Desktop plugin that loads an OGC GeoPackage polygon layer,checks for existing spikes
and then removes them saving the cleaned data in a new GeoPackage file.
The main steps are three:
* Clone this repository or download in the correct section.
* Ensuring QGIS Desktop is already installed, copy the plugin to the QGIS Plugin directory
* Load the geopackage data into QGIS and activate the plugin.
* Process the GeoPackge layers and save in the appropriate location.

<p align="right">(<a href="#top">back to top</a>)</p>

### Stack Used

This section should list any major frameworks/libraries used to build this project.

* [Python](https://python.org/)
* [QGIS](https://qgis.org/)
* [PyQt5](https://www.riverbankcomputing.com/software/pyqt/)
* [GeoPandas](https://geopandas.org/)
* [Shapely](https://github.com/shapely/shapely)
* [PyProj](https://pyproj4.github.io/pyproj/)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

Clone this project using ```git```.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* QGIS Desktop 3.0+
* PyQt5
* Python + pip

### Installation

Below is an example of how you can install the components making up the plugin ecosystem. The system has been tested in
Windows only.

1. <b>Download and install QGIS</b> using the OSGEO4W network installer which can be downloaded from the 
[QGIS Download page](https://qgis.org/en/site/forusers/download.html). The network installer has the advantage of 
allowing the user to install additional packages and dependencies such as GeoPandas, Pyproj and Shapely.
2. Navigate into the QGIS plugins directory which is at 
<em>C:\Users\<AccountName>\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins</em>
3. Clone the project using the git command shown below in command prompt or powershell.
   ```sh
   git clone https://github.com/jkariukidev/polygon_spike_remover.git
   ```
4. Run QGIS Desktop from the shortcut in Start Menu. The menu shortcut appears as shown below.

<div align="center">

![QGIS Shortcut][qgis-shortcut]

</div>

5. You will now notice a plugin with the following shortcut in the Vector Menu and in the toolbar.

<div align="center">

![Plugin Menu][plugin-menu]


![Toolbar Shortcut][toolbar-shortcut]

</div>

<p align="right">(<a href="#top">back to top</a>)</p>

### Process Diagram

The process workflow for the working of the plugin is as shown below:
<div align="center">

![Process diagram][process-diagram]

</div>

<p align="right">(<a href="#top">back to top</a>)</p>


### Input

Below is the input layer as it appears in QGIS Desktop map view. The input data is located in the [data](data) directory.
<div align="center">

![Input layer][input-layer]

</div>

<p align="right">(<a href="#top">back to top</a>)</p>

### Output

Below is the output layer as it appears in QGIS Desktop map view after processing.

<div align="center">
  
  ![Output layer][output-layer] 

</div>

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

The usual libraries and processes of QGIS Desktop's geometry checker (from tests) cannot be able to identify spikes in 
polygons as invalid geometries. This is where this plugin comes to play. For details on how to use, please refer to the
**[Documentation Page](https://jkariukidev.github.io/polygon_spike_remover)**.
  

https://user-images.githubusercontent.com/23359514/151496970-a592883b-5567-4711-a89a-a1fb665711b1.mp4


 

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [x] Add Changelog
- [x] Feature Enhancements
- [x] UX/UI improvements

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. 
Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also 
simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the GNU GPL License. See [`LICENSE.txt`](LICENSE) for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Joseph Kariuki - [@jkariukidev](https://twitter.com/jkariukidev)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites 
to kick things off!

* [PQGIS Developer Cookbook](https://docs.qgis.org/3.16/en/docs/pyqgis_developer_cookbook/index.html)
* [QGIS API ](https://www.qgis.org/api/)
* [PyQt5 API](https://doc.qt.io/qtforpython/)
* [GitHub Pages](https://pages.github.com)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/jkariukidev/polygon_pike_remover.svg?style=for-the-badge
[contributors-url]: https://github.com/jkariukidev/polygon_spike_remover/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/jkariukidev/polygon_spike_remover.svg?style=for-the-badge
[forks-url]: https://github.com/jkariukidev/polygon_spike_remover/network/members
[stars-shield]: https://img.shields.io/github/stars/jkariukidev/polygon_spike_remover.svg?style=for-the-badge
[stars-url]: https://github.com/jkariuki/polygon_spike_remover/stargazers
[issues-shield]: https://img.shields.io/github/issues/jkariukidev/polygon_spike_remover.svg?style=for-the-badge
[issues-url]: https://github.com/jkariukidev/polygon_spike_remover/issues
[license-shield]: https://img.shields.io/github/license/jkariukidev/.svg?style=for-the-badge
[license-url]: https://github.com/jkariuki/polygon_spike_remover/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/josephkariuki
[product-screenshot]: img/readme/qgis_plugin_info.png
[qgis-shortcut]: img/readme/qgis_shortcut.png
[plugin-menu]: img/readme/plugin_menu.png
[toolbar-shortcut]: img/readme/toolbar_shortcut.png
[process-diagram]: img/readme/development_workflow.png
[input-layer]: img/readme/input_layer.png
[output-layer]: img/readme/output_layer.png
[logo]: img/icons/icon.png


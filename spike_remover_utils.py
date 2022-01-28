from geopandas import read_file, GeoDataFrame
from pyproj import Geod
from shapely import coords
from shapely import geometry


def get_angle_between_azimuths(azimuth1, azimuth2) -> float:
    """Get the angle between two azimuths.

    :param azimuth1: The first azimuth angle
    :type azimuth1: float

    :param azimuth2: The second azimuth angle
    :type azimuth2: float

    :return: Angle between the given azimuths
    """
    tmp = abs(azimuth1 - azimuth2) % 360
    return 360 - tmp if tmp > 180 else tmp


class GeometryProcessor:
    """
    Processor used to ingest a geometry as a sequence of geographic
    coordinates and remove spikes. Triangles on the boundary of the geometry
    are considered spikes when the angle of the triangle corner is less than
    a specified angle and the edges of the triangle that are part of the
    geometry boundary have a length greater than a specified length.
    """
    min_angle: float = 1.0
    min_distance: float = 100000.0

    def __init__(self, min_angle: float, min_distance: float):
        self.min_angle = min_angle % 360
        self.min_distance = abs(min_distance)

    def process_sequence(
            self,
            geod: Geod,
            sequence: coords.CoordinateSequence
    ) -> list:
        """
        Process a sequence of coordinate points and remove all spikes. If the
        sequence would form a simple triangle, we skip the sequence and return
        it without any changes. This is done in order to avoid generating
        invalid geometries.

        :param geod: Geod used to perform distance and angle calculations
        :type geod: `pyproj.Geod`

        :param sequence: Input coordinate sequence
        :type sequence: `shapely.coords.CoordinateSequence`

        :return: Filtered list with the spikes removed from the input sequence
        """
        if len(sequence) <= 4:
            # If the number of points in the coordinate sequence is 4 or less,
            # this means that the sequence is a triangle and it means that we
            # don't want to process this at the risk of creating an invalid
            # polygon geometry
            return list(sequence)

        vertices = sequence[:-1]  # discard the last vertex
        triplets = [
            ((i - 1) % len(vertices), i, (i + 1) % len(vertices))
            for i in range(len(vertices))
        ]

        final_geometry = []

        for triplet in triplets:
            mark = self.process_triplet(geod, [
                vertices[triplet[0]],
                vertices[triplet[1]],
                vertices[triplet[2]],
            ])

            if not mark:
                final_geometry.append(vertices[triplet[1]])

        return final_geometry

    def process_triplet(self, geod:Geod, triplet: list) -> bool:
        """
        Process a triplet of vertices and check if the second vertex can be
        marked as a spike. A triplet of vertices is a collection of three
        vertices that are contiguous on a certain polygon. We make this test
        for the second vertex since that is the tip of the triangle that is
        formed by the triplet.

        :param geod: Geod used to perform distance and angle calculations
        :type geod: pyproj.Geod

        :param triplet: List with 3 vertices
        :type triplet: list

        :return: True if the second vertex is a spike
        """
        azim10, _, distance10 = geod.inv(*triplet[1], *triplet[0])
        azim12, _, distance12 = geod.inv(*triplet[1], *triplet[2])

        if distance10 < self.min_distance and distance12 < self.min_distance:
            return False

        angle = get_angle_between_azimuths(azim10, azim12)
        if angle < self.min_angle:
            return True

        return False


def load_geopackage(path: str) -> GeoDataFrame:
    """
    Load a geopackage from the disk and return a `GeoDataFrame` instance of
    the loaded file. This method does not check if the input path exists and
    will raise a `DriverError` exception if the input path does not exist.

    :param path: Path to the input file to load
    :type path: str

    :return: `geopandas.GeoDataFrame`
    """
    return read_file(path)


def save_geopackage(path: str, data: GeoDataFrame) -> None:
    """
    Save a `GeoDataFrame` to the disk at the specified path. If the path
    already exists, the existing destination will be overwritten.

    :param path: Path used for the output file
    :type path: str

    :param data: Output `GeoDataFrame` instance
    :type data: GeoDataFrame
    """
    for row in data.itertuples():
        data.to_file(path, driver="GPKG", layer=row.name)


def validate_crs(data: GeoDataFrame) -> bool:
    """
    Validate that a `GeoDataFrame` has a valid CRS for our purposes. In our
    case, the CRS needs to be a geographic CRS.

    :param data: `GeoDataFrame` to validate
    :type data: `GeoDataFrame`

    :return: True if the CRS is an instance of a geographic CRS
    """
    return data.crs.is_geographic


def extract_crs_geod(data: GeoDataFrame) -> Geod:
    """
    Create a `Geod` instance using the properties of the CRS of the input
    GeoDataFrame.

    :param data: input `GeoDataFrame` used to extract the CRS
    :type data: `GeoDataFrame`

    :return: `pyproj.Geod` using the input data CRS
    """
    return Geod(
        a=data.crs.ellipsoid.semi_major_metre,
        rf=data.crs.ellipsoid.inverse_flattening,
    )


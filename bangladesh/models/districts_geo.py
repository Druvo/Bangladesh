from enum import Enum
from typing import List


class GeometryType(Enum):
    MULTI_POLYGON = "MultiPolygon"


class Geometry:
    type: GeometryType
    coordinates: List[List[List[List[float]]]]

    def __init__(self, type: GeometryType, coordinates: List[List[List[List[float]]]]) -> None:
        self.type = type
        self.coordinates = coordinates


class Properties:
    adm2_en: str
    adm1_en: str

    def __init__(self, adm2_en: str, adm1_en: str) -> None:
        self.adm2_en = adm2_en
        self.adm1_en = adm1_en


class FeatureType(Enum):
    FEATURE = "Feature"


class Feature:
    type: FeatureType
    properties: Properties
    geometry: Geometry

    def __init__(self, type: FeatureType, properties: Properties, geometry: Geometry) -> None:
        self.type = type
        self.properties = properties
        self.geometry = geometry


class Welcome3:
    type: str
    name: str
    features: List[Feature]

    def __init__(self, type: str, name: str, features: List[Feature]) -> None:
        self.type = type
        self.name = name
        self.features = features

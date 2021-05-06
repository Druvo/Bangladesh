from typing import List


class Division:
    id: int
    name: str
    bn_name: str
    lat: str
    long: str

    def __init__(self, id: int, name: str, bn_name: str, lat: str, long: str) -> None:
        self.id = id
        self.name = name
        self.bn_name = bn_name
        self.lat = lat
        self.long = long


class DivisionList:
    divisions: List[Division]

    def __init__(self, divisions: List[Division]) -> None:
        self.divisions = divisions

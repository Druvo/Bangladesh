from typing import List


class District:
    id: int
    division_id: int
    name: str
    bn_name: str
    lat: str
    long: str

    def __init__(self, id: int, division_id: int, name: str, bn_name: str, lat: str, long: str) -> None:
        self.id = id
        self.division_id = division_id
        self.name = name
        self.bn_name = bn_name
        self.lat = lat
        self.long = long


class Welcome6:
    districts: List[District]

    def __init__(self, districts: List[District]) -> None:
        self.districts = districts

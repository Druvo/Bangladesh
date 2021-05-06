from typing import List


class Upazila:
    id: int
    district_id: int
    name: str
    bn_name: str

    def __init__(self, id: int, district_id: int, name: str, bn_name: str) -> None:
        self.id = id
        self.district_id = district_id
        self.name = name
        self.bn_name = bn_name


class Welcome10:
    upazilas: List[Upazila]

    def __init__(self, upazilas: List[Upazila]) -> None:
        self.upazilas = upazilas

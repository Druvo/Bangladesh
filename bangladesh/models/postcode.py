from enum import Enum
from typing import Optional, List


class District(Enum):
    CHAPINAWABGANJ = "Chapinawabganj"


class Postcode:
    division_id: int
    district_id: Optional[int]
    upazila: str
    post_office: str
    post_code: int
    district: Optional[District]

    def __init__(self, division_id: int, district_id: Optional[int], upazila: str, post_office: str, post_code: int, district: Optional[District]) -> None:
        self.division_id = division_id
        self.district_id = district_id
        self.upazila = upazila
        self.post_office = post_office
        self.post_code = post_code
        self.district = district


class Welcome8:
    postcodes: List[Postcode]

    def __init__(self, postcodes: List[Postcode]) -> None:
        self.postcodes = postcodes

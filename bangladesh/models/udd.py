from enum import Enum


class Division(Enum):
    BARISAL = "Barisal"
    CHITTAGONG = "Chittagong"
    DHAKA = "Dhaka"
    KHULNA = "Khulna"
    RAJSHAHI = "Rajshahi"
    RANGPUR = "Rangpur"
    SYLHET = "Sylhet"


class Welcome1Element:
    upazila: str
    district: str
    division: Division

    def __init__(self, upazila: str, district: str, division: Division) -> None:
        self.upazila = upazila
        self.district = district
        self.division = division

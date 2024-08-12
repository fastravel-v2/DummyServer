# models.py
from pydantic import BaseModel
from typing import List, Union, Dict, Optional

# 장소 상세 정보 모델
class LocationDetailType(BaseModel):
    spotId: str
    imageUrls: Union[List[str], List[None]]
    description: str
    lat: str
    long: str
    name: str
    category: List[int]
    address: str

    # 추가 상세 정보
    tel: Optional[str] = None
    creditCard: Optional[str] = None
    parking: Optional[str] = None
    openTime: Optional[str] = None
    petsAvailable: Optional[str] = None
    babyEquipmentRental: Optional[str] = None
    closedForTheDay: Optional[str] = None
    playAreaForChildren: Optional[str] = None
    bestMenu: Optional[str] = None
    restDate: Optional[str] = None
    timeAvailable: Optional[str] = None
    saleItems: Optional[str] = None
    takeOut: Optional[str] = None
    fairDay: Optional[str] = None
    smokingSectionAvailable: Optional[str] = None
    reservation: Optional[str] = None
    fee: Optional[str] = None
    occupancy: Optional[str] = None
    ageLimit: Optional[str] = None
    scale: Optional[str] = None
    startDate: Optional[str] = None
    endDate: Optional[str] = None
    showTime: Optional[str] = None
    parkingFee: Optional[str] = None
    travelTime: Optional[str] = None
    discount: Optional[str] = None
    ageAvailable: Optional[str] = None
    seasons: Optional[str] = None
    timeRequired: Optional[str] = None
    program: Optional[str] = None

# 장소 정보 모델
class IPlaceInfo(BaseModel):
    spotId: str
    imageUrl: str
    name: str
    address: str

# 좋아하는 장소 정보 모델
class ILikePlace(BaseModel):
    spotId: str
    name: str
    address: str
    imageUrl: str
    memo: str

# --------------------------------------------------------------------------
class MyTravel(BaseModel):
    planId: int
    planImage: str
    planName: str
    startDate: str
    endDate: Optional[str] = None
    numOfCity: int

class LikeLocationItemRes(BaseModel):
    spotId: str
    name: str
    address: Optional[str] = None
    imageUrl: Optional[str] = None
    memo: Optional[str] = None

class LikeLocation(BaseModel):
    locationId: str
    locationImage: str
    locationName: str
    locationAddress: str
    locationMemo: Optional[str] = None

class SearchLocationInfo(BaseModel):
    id: str
    name: str
    address: Optional[str] = None
    imageUrl: Optional[str] = None

class AddSpotToPlanRequest(BaseModel):
    spotId: str
    planId: str
    date: str

class SurveyItemResInfo(BaseModel):
    spotId: str
    name: str
    address: Optional[str] = None
    imageUrl: Optional[str] = None
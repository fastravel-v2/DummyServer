from typing import List, Optional

from fastapi import FastAPI, HTTPException

from dummy_data import (
    dummy_location_details,
    dummy_recommendations_global,
    dummy_recommendations_local,
    dummy_likes,
    dummy_like_location,
    dummy_my_travel,
    dummy_search_results,
    dummy_survey_list
)
from models import LocationDetailType, IPlaceInfo, ILikePlace, LikeLocationItemRes, MyTravel, AddSpotToPlanRequest, \
    SearchLocationInfo, SurveyItemResInfo

app = FastAPI()


# --------------------------------------------------------------------------
# 장소 상세 정보 조회 엔드포인트
@app.get("/core/spot/{id}", response_model=LocationDetailType)
async def get_location_detail(id: str):
    spot = dummy_location_details[0]
    # DTO 형식으로 데이터 반환
    location = LocationDetailType(
        spotId=spot["spotId"],
        name=spot["name"],
        address=spot["address"],
        imageUrls=spot["depiction"],
        description=spot["description"],
        lat=spot["lat"],
        long=spot["long"],
        category=spot["category"],
        tel=spot["properties"].get("tel"),
        creditCard=spot["properties"].get("creditCard"),
        parking=spot["properties"].get("parking"),
        openTime=spot["properties"].get("openTime"),
        petsAvailable=spot["properties"].get("petsAvailable"),
        babyEquipmentRental=spot["properties"].get("babyEquipmentRental"),
        closedForTheDay=spot["properties"].get("closedForTheDay"),
        playAreaForChildren=spot["properties"].get("playAreaForChildren"),
        bestMenu=spot["properties"].get("bestMenu"),
        restDate=spot["properties"].get("restDate"),
        timeAvailable=spot["properties"].get("timeAvailable"),
        saleItems=spot["properties"].get("saleItems"),
        takeOut=spot["properties"].get("takeOut"),
        fairDay=spot["properties"].get("fairDay"),
        smokingSectionAvailable=spot["properties"].get("smokingSectionAvailable"),
        reservation=spot["properties"].get("reservation"),
        fee=spot["properties"].get("fee"),
        occupancy=spot["properties"].get("occupancy"),
        ageLimit=spot["properties"].get("ageLimit"),
        scale=spot["properties"].get("scale"),
        startDate=spot["properties"].get("startDate"),
        endDate=spot["properties"].get("endDate"),
        showTime=spot["properties"].get("showTime"),
        parkingFee=spot["properties"].get("parkingFee"),
        travelTime=spot["properties"].get("travelTime"),
        discount=spot["properties"].get("discount"),
        ageAvailable=spot["properties"].get("ageAvailable"),
        seasons=spot["properties"].get("seasons"),
        timeRequired=spot["properties"].get("timeRequired"),
        program=spot["properties"].get("program")
    )
    return location


# 글로벌 추천 장소 목록 조회 엔드포인트
@app.get("/core/recommendation/{id}/global", response_model=List[IPlaceInfo])
async def get_recommendation_global(id: str):
    return dummy_recommendations_global


# 로컬 추천 장소 목록 조회 엔드포인트
@app.get("/core/recommendation/{id}/local", response_model=List[IPlaceInfo])
async def get_recommendation_local(id: str):
    return dummy_recommendations_local


# 좋아하는 장소 목록 조회 엔드포인트
@app.get("/core/my_spot/list", response_model=List[ILikePlace])
async def get_like_locations():
    return dummy_likes


# --------------------------------------------------------------------------
# Google 로그인 응답 처리 함수
def get_google_login_response(code: str) -> str:
    return "success" if code else "fail"


# Kakao 로그인 응답 처리 함수
def get_kakao_login_response(code: str) -> str:
    return "success" if code else "fail"


# Google 로그인 API
@app.get("/auth/google")
async def google_login(code: str):
    response_status = get_google_login_response(code)
    if response_status == "success":
        return {"status": "success"}
    else:
        raise HTTPException(status_code=401, detail="Google login failed")


# Kakao 로그인 API
@app.get("/auth/kakao")
async def kakao_login(code: str):
    response_status = get_kakao_login_response(code)
    if response_status == "success":
        return {"status": "success"}
    else:
        raise HTTPException(status_code=401, detail="Kakao login failed")


# --------------------------------------------------------------------------
@app.get("/api/core/recommendation/", response_model=List[IPlaceInfo])
async def fetch_recommendations():
    extended_dummy = dummy_recommendations_local * 5
    return [IPlaceInfo(**item) for item in extended_dummy]


@app.post("/api/core/recommendation/location", response_model=List[IPlaceInfo])
async def get_recommendations_location(lat: float, long: float):
    extended_dummy = dummy_recommendations_local * 5
    return [IPlaceInfo(**item) for item in extended_dummy]


@app.get("/api/core/recommendation/best_list", response_model=List[IPlaceInfo])
async def get_recommendations_random():
    extended_dummy = dummy_recommendations_local * 5
    return [IPlaceInfo(**item) for item in extended_dummy]


# --------------------------------------------------------------------------
# 사용자 여행 목록을 가져옵니다.
@app.get("/core/travel/list", response_model=List[MyTravel])
async def get_my_travel():
    return dummy_my_travel


# 특정 여행 계획을 삭제합니다.
@app.delete("/core/travel/", response_model=str)
async def delete_my_travel(planId: int):
    return "success"


# 사용자 이름 중복 여부를 확인합니다.
@app.get("/core/profile/{name}/duplicate", response_model=str)
async def get_name_is_duplicated(name: str):
    return "valid"


# 사용자 프로필을 업데이트합니다.
@app.put("/core/profile/", response_model=str)
async def put_user_profile(profile_form_data: dict):
    return "success"


# 사용자가 좋아요를 누른 장소 목록을 가져옵니다.
@app.get("/core/my_spot/list", response_model=List[LikeLocationItemRes])
async def get_like_location():
    return dummy_like_location


# 사용자가 새로운 장소를 좋아요 목록에 추가합니다.
@app.post("/core/my_spot/", response_model=LikeLocationItemRes)
async def post_like_location(spot_id: str, memo: Optional[str] = None):
    return "success"


# 좋아요 목록에서 특정 장소를 삭제합니다.
@app.delete("/core/my_spot/{spot_id}", response_model=str)
async def delete_like_location(spot_id: str):
    return "success"


# 특정 장소의 메모를 업데이트합니다.
@app.put("/core/my_spot/memo", response_model=LikeLocationItemRes)
async def put_my_location_memo(spot_id: str, memo: Optional[str] = None):
    return "success"


# 검색어에 맞는 장소 목록을 반환합니다.
@app.get("/search/auto-complete", response_model=List[SearchLocationInfo])
async def get_searched_location(query: str):
    return dummy_search_results


# 여행 계획에 장소를 추가합니다.
@app.post("/core/travel/add-spot-to-plan", response_model=str)
async def post_location_to_travel_plan(request: AddSpotToPlanRequest):
    return "success"


# 임의의 카테고리와 관련된 설문 항목을 반환하는 엔드포인트
@app.get("/core/survey/random_spot", response_model=List[SurveyItemResInfo])
async def get_survey_list(category: Optional[str] = None, count: int = 4):
    return dummy_survey_list[:count]


# 선택한 설문 항목 ID들을 서버에 전송하는 엔드포인트
@app.post("/core/survey/selected")
async def post_survey_ids(survey_ids: List[str]):
    return {"message": "success"}

# dummy_data.py
from models import LocationDetailType, IPlaceInfo, ILikePlace

# 더미 관광지 상세 정보
dummy_location_details = [
    {
        "spotId": "1000981",
        "description": ("통영시는 통영항이 한눈에 내려다보이는 봉평동 옛 한려해상국립공원 동부사무소 "
                        "건물 4층을 리모델링해 2008년 3월 28일 ‘꽃의 시인’으로 불리는 김춘수(金春洙. "
                        "1922~2004) 시인의 유품전시관을 개관하였다. 전체 면적 164.8㎡ 규모의 전시관에는 "
                        "김 시인의 육필원고 126점과 서예작품, 액자, 사진을 비롯해 생전에 사용하던 가구와 "
                        "옷가지 등 유품이 전시된다. 특히 전시관 한쪽에는 김 시인이 생전에 기거하던 것과 "
                        "비슷한 형태로 침대와 10폭 산수화 병풍, 액자 등을 넣어 ‘김춘수 방’을 꾸몄고 "
                        "나머지 공간에는 옷가지와 책, 평소 쓰던 소지품, 사진 등을 전시해 시인의 숨결을 "
                        "가까이 느낄 수 있게 하였다. 통영시 동호동에서 태어난 김 시인은 통영중 교사로 재직하던 "
                        "1947년 첫 시집 ‘구름과 장미’를 출간한 이후 2004년 향년 82세로 타계할 때까지 20권이 "
                        "넘는 시집을 출간해 한국 시문학에 큰 족적을 남겼다."),
        "lat": "34.8333722569",
        "long": "128.4161841816",
        "name": "김춘수 유품전시관",
        "category": [3],
        "address": "경상남도 통영시 해평5길 142-16",
        "depiction": [
            "http://tong.visitkorea.or.kr/cms/resource/25/2367625_image2_1.jpg",
            "http://tong.visitkorea.or.kr/cms/resource/39/1002339_image2_1.jpg"
        ],
        "properties": {
            "tel": "055-650-2670",
            "creditCard": "불가능",
            "parking": "있음",
            "openTime": None,
            "petsAvailable": "불가능",
            "babyEquipmentRental": "불가능",
            "closedForTheDay": "매주 월요일, 1월 1일, 설날 및 추석 연휴",
            "playAreaForChildren": None,
            "bestMenu": None,
            "restDate": None,
            "timeAvailable": "09:00~18:00",
            "saleItems": None,
            "takeOut": None,
            "fairDay": None,
            "smokingSectionAvailable": None,
            "reservation": None,
            "fee": "무료",
            "occupancy": None,
            "ageLimit": None,
            "scale": "지상4층 중 1,2층 (부지 695㎡, 연면적 334㎡)",
            "startDate": None,
            "endDate": None,
            "showTime": None,
            "parkingFee": None,
            "travelTime": None,
            "discount": None,
            "ageAvailable": None,
            "seasons": None,
            "timeRequired": None,
            "program": None,
        }
    },
    {
        "spotId": "1001011",
        "description": ("세계적인 작곡가 윤이상(1917~1995)과 그의 음악을 테마로 한 기념공원이다. 도천동 "
                        "윤이상 생가 옆 6745㎡ 부지에 조성되었으며, 윤이상 선생의 음악 세계를 조명할 수 있는 "
                        "지상 2층, 연면적 865.5㎡ 규모의 기념전시관과 소공연장이 있다. 기념전시관에는 선생이 "
                        "생전 독일 베를린에서 거주하며 남긴 유품 148종 412점이 전시되어 있다. 독일 정부로 "
                        "받은 훈장과 괴테 메달을 비롯해 사무집기, 생전 연주하던 첼로, 항상 품고 다녔던 "
                        "소형태극기 등이 있으며, 사진 500여 점이 있다. 윤이상 관련 유물이 있는 전시실과 카페, "
                        "기념품 매장, 로비의 기능을 복합적으로 가진 에스파체, 각종 공연과 세미나 등의 "
                        "실내행사가 가능한 메모리 홀, 야외행사장인 경사광장 등으로 이루어져 있어 볼거리가 "
                        "많다. 윤이상 기념공원에는 윤이상 거리, 윤이상 생가터, 윤이상 기념관 등이 조성되어 "
                        "있다."),
        "lat": "34.8384272034",
        "long": "128.4137175973",
        "name": "윤이상 기념공원(도천테마파크)",
        "category": [11],
        "address": "경상남도 통영시 중앙로 27",
        "depiction": [
            "http://tong.visitkorea.or.kr/cms/resource/62/1002462_image2_1.jpg",
            "http://tong.visitkorea.or.kr/cms/resource/11/1002411_image2_1.jpg"
        ],
        "properties": {
            "tel": "055-644-1210",
            "creditCard": "불가능",
            "parking": "있음 (약 소형 25대)",
            "openTime": None,
            "petsAvailable": "불가능",
            "babyEquipmentRental": "불가능",
            "closedForTheDay": "공원 연중무휴 / 기념관 매주 월요일",
            "playAreaForChildren": None,
            "bestMenu": None,
            "restDate": None,
            "timeAvailable": "공원 제한없음 / 기념관 09:00~18:00",
            "saleItems": None,
            "takeOut": None,
            "fairDay": None,
            "smokingSectionAvailable": None,
            "reservation": None,
            "fee": None,
            "occupancy": None,
            "ageLimit": None,
            "scale": None,
            "startDate": None,
            "endDate": None,
            "showTime": None,
            "parkingFee": None,
            "travelTime": None,
            "discount": None,
            "ageAvailable": None,
            "seasons": "연중",
            "timeRequired": None,
            "program": None,
        }
    }
]

# 더미 글로벌 추천 장소
dummy_recommendations_global = [
    {
        "spotId": "1000981",
        "imageUrl": "http://tong.visitkorea.or.kr/cms/resource/25/2367625_image2_1.jpg",
        "name": "김춘수 유품전시관",
        "address": "경상남도 통영시 해평5길 142-16"
    },
    {
        "spotId": "1001011",
        "imageUrl": "http://tong.visitkorea.or.kr/cms/resource/62/1002462_image2_1.jpg",
        "name": "윤이상 기념공원(도천테마파크)",
        "address": "경상남도 통영시 중앙로 27"
    }
]

# 더미 로컬 추천 장소
dummy_recommendations_local = [
    {
        "spotId": "1000981",
        "imageUrl": "http://tong.visitkorea.or.kr/cms/resource/25/2367625_image2_1.jpg",
        "name": "김춘수 유품전시관",
        "address": "경상남도 통영시 해평5길 142-16"
    },
    {
        "spotId": "1001011",
        "imageUrl": "http://tong.visitkorea.or.kr/cms/resource/62/1002462_image2_1.jpg",
        "name": "윤이상 기념공원(도천테마파크)",
        "address": "경상남도 통영시 중앙로 27"
    }
]

# 더미 좋아하는 장소
dummy_likes = [
    {
        "spotId": "1000981",
        "name": "김춘수 유품전시관",
        "address": "경상남도 통영시 해평5길 142-16",
        "imageUrl": "http://tong.visitkorea.or.kr/cms/resource/25/2367625_image2_1.jpg",
        "memo": "방문 시 김춘수 시인의 유품을 가까이에서 볼 수 있습니다."
    },
    {
        "spotId": "1001011",
        "name": "윤이상 기념공원(도천테마파크)",
        "address": "경상남도 통영시 중앙로 27",
        "imageUrl": "http://tong.visitkorea.or.kr/cms/resource/62/1002462_image2_1.jpg",
        "memo": "윤이상 선생의 유품을 볼 수 있는 멋진 공원입니다."
    }
]

# --------------------------------------------------------------------------
dummy_my_travel = [
    {
        "planId": 1,
        "planImage": "http://example.com/image1.jpg",
        "planName": "서울 여행",
        "startDate": "2024-08-01",
        "endDate": "2024-08-05",
        "numOfCity": 2
    },
    {
        "planId": 2,
        "planImage": "http://example.com/image2.jpg",
        "planName": "부산 여행",
        "startDate": "2024-08-06",
        "endDate": "2024-08-10",
        "numOfCity": 3
    }
]

dummy_like_location = [
    {
        "spotId": "1000981",
        "name": "김춘수 유품전시관",
        "address": "경상남도 통영시 해평5길 142-16",
        "imageUrl": "http://tong.visitkorea.or.kr/cms/resource/25/2367625_image2_1.jpg",
        "memo": "방문 시 김춘수 시인의 유품을 가까이에서 볼 수 있습니다."
    },
    {
        "spotId": "1001011",
        "name": "윤이상 기념공원(도천테마파크)",
        "address": "경상남도 통영시 중앙로 27",
        "imageUrl": "http://tong.visitkorea.or.kr/cms/resource/62/1002462_image2_1.jpg",
        "memo": "윤이상 선생의 유품을 볼 수 있는 멋진 공원입니다."
    }
]

dummy_search_results = [
    {
        "id": "2782509",
        "name": "해파랑길47코스",
        "address": "강원특별자치도 고성군 죽왕면 공현진리 187-16",
        "imageUrl": "http://tong.visitkorea.or.kr/cms/resource/83/2786583_image2_1.jpg"
    },
    {
        "id": "2663250",
        "name": "신창풍차해안도로",
        "address": "제주특별자치도 제주시 한경면 신창리 1322-1",
        "imageUrl": "http://tong.visitkorea.or.kr/cms/resource/27/2665327_image2_1.jpg"
    }
]

dummy_survey_list = [
    {
        "spot_id": "2755809",
        "name": "궁항",
        "address": "",
        "image_url": "http://tong.visitkorea.or.kr/cms/resource/03/2755803_image2_1.png",
    },
    {
        "spot_id": "127263",
        "name": "계룡산",
        "address": "",
        "image_url": "http://tong.visitkorea.or.kr/cms/resource/81/1978581_image2_1.jpg",
    },
    {
        "spot_id": "127433",
        "name": "강원특별자치도립화목원",
        "address": "",
        "image_url": "http://tong.visitkorea.or.kr/cms/resource/98/2739698_image2_1.jpg",
    },
    {
        "spot_id": "2015553",
        "name": "보문정 (경주)",
        "address": "",
        "image_url": "http://tong.visitkorea.or.kr/cms/resource/09/2654209_image2_1.jpg",
    },
]
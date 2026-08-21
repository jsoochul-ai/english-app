
scenarios = {
    # --- [공항 및 비행기] ---
    "✈️ [공항 1] 탑승 수속 (Check-in)": {
        "description": "공항 카운터에서 비행기 탑승 수속을 하고 수하물을 부치는 상황입니다.",
        "dialogue": [
            ("직원", "Where are you flying to today?", "오늘 어디로 가시나요?"),
            ("나", "I'm flying to New York.", "뉴욕으로 갑니다."),
            ("직원", "May I see your passport and ticket, please?", "여권과 항공권을 보여주시겠습니까?"),
            ("나", "Here you are. Can I get an aisle seat?", "여기 있습니다. 통로 쪽 좌석으로 받을 수 있을까요?"),
            ("직원", "Sure. Are you checking any bags?", "네. 위탁 수하물이 있으신가요?"),
            ("나", "Yes, just this one suitcase.", "네, 이 캐리어 하나입니다.")
        ]
    },
    "✈️ [공항 2] 보안 검색대 (Security Check)": {
        "description": "보안 검색대를 통과하며 직원의 지시에 따르는 상황입니다.",
        "dialogue": [
            ("직원", "Please empty your pockets and put your electronics in the bin.", "주머니를 비우시고 전자기기는 바구니에 넣어주세요."),
            ("나", "Do I need to take off my shoes?", "신발도 벗어야 하나요?"),
            ("직원", "Yes, shoes and jackets off, please.", "네, 신발과 재킷 모두 벗어주세요."),
            ("나", "Okay. Is this laptop fine here?", "알겠습니다. 노트북은 여기 두면 되나요?"),
            ("직원", "Yes. Now step through the scanner, please.", "네. 이제 스캐너를 통과해 주세요.")
        ]
    },
    "✈️ [공항 3] 기내 서비스 요청 (In-flight)": {
        "description": "비행기 안에서 승무원에게 필요한 것을 요청하는 상황입니다.",
        "dialogue": [
            ("승무원", "Would you like something to drink?", "마실 것 좀 준비해 드릴까요?"),
            ("나", "Can I get a cup of water and some apple juice?", "물 한 잔이랑 사과 주스 좀 주시겠어요?"),
            ("승무원", "Here you go. Anything else?", "여기 있습니다. 더 필요한 건 없으신가요?"),
            ("나", "Could I also get an extra blanket? It's a bit cold.", "담요를 하나 더 받을 수 있을까요? 조금 춥네요.")
        ]
    },

    # --- [숙소 및 호텔] ---
    "🏨 [숙소 1] 호텔 체크인 (Hotel Check-in)": {
        "description": "예약한 호텔에 도착해 체크인하고 객실을 안내받는 상황입니다.",
        "dialogue": [
            ("직원", "Welcome! How can I help you?", "환영합니다! 무엇을 도와드릴까요?"),
            ("나", "I'd like to check in. The reservation is under Kim.", "체크인하고 싶습니다. 김 이름으로 예약했습니다."),
            ("직원", "I see your reservation for three nights. May I have your credit card for incidentals?", "3박 예약 확인되었습니다. 보증금 결제를 위해 신용카드를 주시겠습니까?"),
            ("나", "Here you are. What time is breakfast served?", "여기 있습니다. 조식은 몇 시에 제공되나요?"),
            ("직원", "Breakfast is from 7 AM to 10 AM on the first floor.", "조식은 1층에서 오전 7시부터 10시까지입니다.")
        ]
    },
    "🏨 [숙소 2] 룸서비스 및 수건 요청 (Room Service)": {
        "description": "객실에서 프론트 데스크로 전화해 필요한 물품을 요청하는 상황입니다.",
        "dialogue": [
            ("직원", "Front desk, how may I help you?", "프론트 데스크입니다, 무엇을 도와드릴까요?"),
            ("나", "Hi, I'm in room 402. Could we get some extra towels?", "안녕하세요, 402호입니다. 수건 좀 더 받을 수 있을까요?"),
            ("직원", "Of course. Anything else you need?", "물론입니다. 더 필요하신 게 있나요?"),
            ("나", "Yes, could you also send up two bottles of water?", "네, 생수도 두 병 올려보내 주시겠어요?"),
            ("직원", "I'll send someone right up.", "바로 직원을 올려보내겠습니다.")
        ]
    },

    # --- [식당 및 쇼핑] ---
    "🍽️ [식당 1] 메뉴 주문하기 (Ordering)": {
        "description": "메뉴판을 보고 메인 요리와 음료를 주문하는 상황입니다.",
        "dialogue": [
            ("직원", "Are you ready to order?", "주문하시겠습니까?"),
            ("나", "What do you recommend for the main dish?", "메인 요리로 어떤 것을 추천하시나요?"),
            ("직원", "Our signature steak is very popular.", "저희 시그니처 스테이크가 아주 인기가 많습니다."),
            ("나", "I'll have that, please. Medium-rare.", "그걸로 할게요. 미디엄 레어로 부탁합니다."),
            ("직원", "Excellent choice. Anything to drink?", "탁월한 선택입니다. 마실 것은 준비해 드릴까요?"),
            ("나", "Just tap water for now, thank you.", "일단 수돗물로 주세요, 감사합니다.")
        ]
    },
    "🛍️ [쇼핑 1] 은 액세서리 구매 (Buying Jewelry)": {
        "description": "현지 쥬얼리 샵에서 마음에 드는 은반지와 귀걸이를 둘러보고 사이즈를 묻는 상황입니다.",
        "dialogue": [
            ("직원", "Are you looking for anything special?", "특별히 찾으시는 게 있나요?"),
            ("나", "I'm just browsing, but these silver rings caught my eye.", "그냥 둘러보고 있는데, 이 은반지들이 눈에 띄네요."),
            ("직원", "They are our new arrivals. Would you like to try them on?", "신상품입니다. 한번 착용해 보시겠어요?"),
            ("나", "Yes, please. Do you have this one in a smaller size?", "네. 이거 조금 더 작은 사이즈도 있나요?"),
            ("직원", "Let me check the stock for you. Just a moment.", "재고가 있는지 확인해 드릴게요. 잠시만요.")
        ]
    },
    "📸 [관광 1] 사진 촬영 부탁하기 (Taking pictures)": {
        "description": "유명한 관광 명소에서 지나가는 외국인에게 사진을 찍어달라고 부탁합니다.",
        "dialogue": [
            ("나", "Excuse me, could you take a picture of us, please?", "실례지만, 저희 사진 좀 찍어주시겠어요?"),
            ("행인", "Sure! Just press this button?", "물론이죠! 이 버튼을 누르면 되나요?"),
            ("나", "Yes, that's right. Could you get the building in the background?", "네, 맞습니다. 배경에 건물이 다 나오게 찍어주실 수 있나요?"),
            ("행인", "Okay. One, two, three! Say cheese!", "알겠습니다. 하나, 둘, 셋! 치즈!"),
            ("나", "Thank you so much. Have a great day!", "정말 감사합니다. 좋은 하루 보내세요!")
        ]
    }
}

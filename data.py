# data.py : 나만의 맞춤형 심화 대본 도서관 (전체 확장판)

scenarios = {
    # -------------------------------------------------------------
    # ✈️ [여행 필수] 공항 및 기내
    # -------------------------------------------------------------
    "✈️ [공항 1] 탑승 수속 (심화)": {
        "description": "공항 카운터에서 탑승 수속, 좌석 지정, 수하물 무게 확인, 게이트 안내까지 받는 상세한 상황입니다.",
        "dialogue": [
            ("직원", "Good morning. Where are you flying to today?", "좋은 아침입니다. 오늘 어디로 가시나요?"),
            ("나", "I'm flying to New York.", "뉴욕으로 갑니다."),
            ("직원", "May I see your passport and ticket, please?", "여권과 항공권을 보여주시겠습니까?"),
            ("나", "Here you are. Do you have any aisle seats left?", "여기 있습니다. 통로 쪽 좌석이 남아 있나요?"),
            ("직원", "Let me check. Yes, I can give you an aisle seat. Are you checking any bags?", "확인해 보겠습니다. 네, 통로 좌석으로 드릴 수 있습니다. 위탁 수하물이 있으신가요?"),
            ("나", "Yes, just this one suitcase. Please put it on the scale.", "네, 이 캐리어 하나입니다. 저울에 올릴게요."),
            ("직원", "It's exactly 20 kilos, which is perfectly fine.", "정확히 20킬로그램이네요. 완벽합니다."),
            ("나", "That's a relief. Oh, what time does the boarding start?", "다행이네요. 아, 탑승은 몇 시에 시작하나요?"),
            ("직원", "Boarding starts at 10:30 AM at Gate 24. Here is your boarding pass.", "탑승은 오전 10시 30분에 24번 게이트에서 시작합니다. 여기 탑승권입니다."),
            ("나", "Thank you so much. Have a good day!", "정말 감사합니다. 좋은 하루 보내세요!")
        ]
    },
    "✈️ [공항 2] 기내 서비스 요청 (심화)": {
        "description": "비행기 안에서 기내식을 선택하고, 필요한 물품과 입국 신고서를 요청하는 상황입니다.",
        "dialogue": [
            ("승무원", "Chicken or beef for your meal, sir?", "기내식으로 닭고기와 소고기 중 어떤 걸로 하시겠습니까?"),
            ("나", "I'll have the beef, please. And a Coke.", "소고기로 할게요. 그리고 콜라도 부탁합니다."),
            ("승무원", "Here you go. Would you like some ice with that?", "여기 있습니다. 얼음도 같이 넣어드릴까요?"),
            ("나", "Yes, please. Oh, can I also get an extra blanket?", "네, 부탁합니다. 아, 담요도 하나 더 받을 수 있을까요?"),
            ("승무원", "Let me check the overhead bins. ... Here is a blanket for you.", "위쪽 선반을 확인해 보겠습니다. ... 여기 담요 있습니다."),
            ("나", "Thank you. By the way, how long until we land?", "감사합니다. 그나저나 착륙하려면 얼마나 남았나요?"),
            ("승무원", "We will be landing in about two hours.", "약 2시간 후에 착륙할 예정입니다."),
            ("나", "Great. Could you also give me an arrival card?", "좋네요. 입국 신고서도 한 장 주시겠어요?"),
            ("승무원", "Certainly. Please fill it out before we land.", "물론입니다. 착륙 전에 작성해 주세요."),
            ("나", "I will. Thanks for your help.", "그렇게 할게요. 도와주셔서 감사합니다.")
        ]
    },

    # -------------------------------------------------------------
    # 🏨 [여행 필수] 숙소 및 식당
    # -------------------------------------------------------------
    "🏨 [숙소 1] 호텔 체크인 및 부대시설 (심화)": {
        "description": "호텔 체크인을 진행하며 조식, 수영장 위치, 보증금 결제까지 상세히 묻고 답하는 상황입니다.",
        "dialogue": [
            ("직원", "Welcome to the Grand Hotel. How can I assist you today?", "그랜드 호텔에 오신 것을 환영합니다. 오늘 어떤 것을 도와드릴까요?"),
            ("나", "Hello. I'd like to check in, please. The reservation is under Kim.", "안녕하세요. 체크인하고 싶습니다. 김 이름으로 예약했습니다."),
            ("직원", "Let me pull up your reservation. Yes, a standard double room for 3 nights.", "예약 내역을 띄워보겠습니다. 네, 스탠다드 더블룸 3박이시네요."),
            ("나", "That's correct. Does this booking include breakfast?", "맞습니다. 이 예약에 조식이 포함되어 있나요?"),
            ("직원", "Yes, it is served from 7 AM to 10 AM on the first floor.", "네, 1층에서 오전 7시부터 10시까지 제공됩니다."),
            ("나", "Great. And could you tell me where the swimming pool is?", "좋네요. 그리고 수영장이 어디 있는지 알려주시겠어요?"),
            ("직원", "The pool and fitness center are on the 5th floor. They close at 10 PM.", "수영장과 피트니스 센터는 5층에 있습니다. 밤 10시에 닫습니다."),
            ("나", "Perfect. Do I need to pay a deposit now?", "완벽하네요. 지금 보증금을 결제해야 하나요?"),
            ("직원", "Yes, I need a credit card for the $100 deposit. Here is your room key.", "네, 보증금 100달러를 위해 신용카드가 필요합니다. 여기 객실 키입니다."),
            ("나", "Thank you for your help. Have a wonderful day!", "도와주셔서 감사합니다. 멋진 하루 보내세요!")
        ]
    },
    "🍽️ [식당 1] 코스 요리 주문 및 알레르기 (심화)": {
        "description": "레스토랑에서 음료, 에피타이저, 메인 요리를 주문하고 알레르기 유무까지 확인하는 상황입니다.",
        "dialogue": [
            ("직원", "Good evening. Are you ready to order?", "안녕히 주무세요. 주문하시겠습니까?"),
            ("나", "Yes, we are ready. Can we start with some drinks?", "네, 준비됐습니다. 음료부터 시작할 수 있을까요?"),
            ("직원", "Absolutely. What would you like to drink?", "물론입니다. 어떤 음료로 하시겠어요?"),
            ("나", "I'll have a glass of red wine, and my friend will have a Coke.", "저는 레드 와인 한 잔 하고, 제 친구는 콜라로 할게요."),
            ("직원", "Noted. And for your appetizers?", "알겠습니다. 에피타이저는 어떻게 하시겠어요?"),
            ("나", "We will share the Caesar salad. For the main, I'd like the ribeye steak.", "시저 샐러드를 나눠 먹을게요. 메인으로는 립아이 스테이크를 부탁합니다."),
            ("직원", "How would you like your steak cooked?", "스테이크는 어떻게 구워드릴까요?"),
            ("나", "Medium-rare, please. Does it come with any side dishes?", "미디엄 레어로 해주세요. 사이드 디시가 같이 나오나요?"),
            ("직원", "Yes, it comes with mashed potatoes. Do you have any food allergies?", "네, 으깬 감자가 함께 나옵니다. 음식 알레르기가 있으신가요?"),
            ("나", "No, I don't have any allergies. That sounds perfect.", "아니요, 알레르기는 없습니다. 아주 좋네요.")
        ]
    },

    # -------------------------------------------------------------
    # 💼 [일상 & 비즈니스] 내 삶에 맞춘 특별 대본
    # -------------------------------------------------------------
    "💍 [비즈니스] 젤로데이 매장 외국인 응대 (심화)": {
        "description": "젤로데이 매장에 방문한 외국인 고객에게 은 목걸이와 귀걸이를 세트로 추천하는 디테일한 비즈니스 상황입니다.",
        "dialogue": [
            ("나", "Hello! Welcome to Jeloday. Are you looking for anything in particular?", "안녕하세요! 젤로데이에 오신 것을 환영합니다. 특별히 찾으시는 게 있나요?"),
            ("손님", "Hi. I'm looking for a silver necklace for my girlfriend.", "안녕하세요. 여자친구에게 줄 은목걸이를 찾고 있어요."),
            ("나", "That's lovely. We specialize in silver accessories. How about this pendant design?", "아주 좋네요. 저희는 은 액세서리 전문입니다. 이 펜던트 디자인은 어떠신가요?"),
            ("손님", "It's beautiful. Is it pure silver?", "정말 예쁘네요. 순은인가요?"),
            ("나", "Yes, all our products are made of high-quality 925 sterling silver.", "네, 저희의 모든 제품은 고품질 925 스털링 실버로 제작됩니다."),
            ("손님", "Awesome. Do you have matching earrings for this?", "멋지네요. 이것과 세트로 할 수 있는 귀걸이도 있나요?"),
            ("나", "Yes, we do. Here are the matching silver earrings. They look great together.", "네, 있습니다. 여기 세트 은귀걸이입니다. 같이 하면 정말 잘 어울려요."),
            ("손님", "Perfect. I'll take both the necklace and the earrings.", "완벽해요. 목걸이와 귀걸이 둘 다 살게요."),
            ("나", "Excellent choice. Would you like me to gift-wrap them for you?", "탁월한 선택입니다. 선물용으로 포장해 드릴까요?"),
            ("손님", "Yes, please. She will absolutely love it.", "네, 부탁합니다. 여자친구가 정말 좋아할 거예요.")
        ]
    },
    "⚾ [취미 1] 롯데 자이언츠 야구 토크 (심화)": {
        "description": "외국인 친구와 KBO 롯데 자이언츠의 최근 경기력과 다가오는 신인 드래프트에 대해 깊게 토론합니다.",
        "dialogue": [
            ("친구", "Did you watch the Lotte Giants game yesterday?", "어제 롯데 자이언츠 경기 봤어?"),
            ("나", "Of course I did! The game was absolutely amazing.", "당연히 봤지! 경기 정말 최고였어."),
            ("친구", "Their hitting was on fire. I couldn't believe that home run.", "타격이 불을 뿜더라. 그 홈런은 정말 믿기지 않았어."),
            ("나", "I know, right? The stadium atmosphere was crazy.", "내 말이! 경기장 분위기 장난 아니었지."),
            ("친구", "I'm also looking forward to their picks in the rookie draft this year.", "올해 신인 드래프트에서 누굴 뽑을지도 정말 기대돼."),
            ("나", "Me too. I really hope they pick a good high school pitcher this time.", "나도. 이번에는 정말 좋은 고졸 투수를 뽑았으면 좋겠어."),
            ("친구", "Yeah, a strong pitcher would definitely help the team win.", "맞아, 강력한 투수가 있으면 무조건 팀 승리에 도움이 되지."),
            ("나", "Exactly. If our pitching gets better, we can aim for the championship.", "정답이야. 투수진만 좋아지면 우리도 우승을 노려볼 수 있어."),
            ("친구", "Let's go watch a game together at the stadium soon.", "조만간 야구장 가서 같이 경기 보자."),
            ("나", "Sounds like a plan! I'll book the tickets.", "좋은 생각이야! 내가 티켓 예매할게.")
        ]
    },
    "⛳ [취미 2] 파크골프 체크인 및 라운딩 (심화)": {
        "description": "해외 파크골프장에 도착해 장비를 렌탈하고 코스 내 해저드 유무까지 꼼꼼하게 질문하는 상황입니다.",
        "dialogue": [
            ("직원", "Hello! Welcome to the park golf club. Do you have a reservation?", "안녕하세요! 파크골프장에 오신 것을 환영합니다. 예약하셨나요?"),
            ("나", "Yes, I booked a morning tee time under the name Kim.", "네, 김 이름으로 오전 티타임을 예약했습니다."),
            ("직원", "Great! I see your name. Do you need to rent any clubs or balls?", "좋습니다! 이름 확인했습니다. 오늘 채나 공 대여가 필요하신가요?"),
            ("나", "Yes, please. I'd like to rent one park golf club and two balls.", "네, 부탁합니다. 파크골프 채 하나와 공 두 개를 빌리고 싶어요."),
            ("직원", "Here you go. The weather is perfect for a round today!", "여기 있습니다. 오늘 라운딩하기 딱 좋은 날씨네요!"),
            ("나", "It really is. Is there a scorecard or a map I can take?", "정말 그렇네요. 제가 챙겨갈 수 있는 스코어카드나 코스 안내도가 있나요?"),
            ("직원", "Sure, here is your scorecard. Course A is on the left, and it's a 9-hole course.", "물론이죠, 여기 스코어카드 있습니다. 왼쪽이 A코스이고 9홀 코스입니다."),
            ("나", "Thank you. By the way, are there any water hazards on this course?", "감사합니다. 그런데 이 코스에 워터 해저드가 있나요?"),
            ("직원", "Yes, there is a small pond on the 5th hole, so please be careful.", "네, 5번 홀에 작은 연못이 있으니 조심하시기 바랍니다."),
            ("나", "I'll keep that in mind. Let's get started!", "명심할게요. 이제 시작해 봅시다!")
        ]
    }
}

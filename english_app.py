import streamlit as st
from gtts import gTTS
import io
from audio_recorder_streamlit import audio_recorder

st.set_page_config(page_title="나만의 영어 단짝", page_icon="🗣️")

st.title("⛳ 실전 파크골프 영어 회화")
st.caption("상황: 해외 파크골프장에 도착해 체크인, 장비 대여, 코스 안내를 받고 라운딩을 시작합니다.")

# 8개 턴의 풍성한 대화 데이터 (역할, 영어, 한글)
dialogue = [
    ("직원", "Hello! Welcome to our park golf club. Do you have a reservation?", "안녕하세요! 저희 파크골프장에 오신 것을 환영합니다. 예약하셨나요?"),
    ("나", "Yes, I booked a morning tee time under the name Kim.", "네, 김(Kim)이라는 이름으로 오전 티타임을 예약했습니다."),
    ("직원", "Great! Do you need to rent any clubs or balls today?", "확인되었습니다! 오늘 골프채나 공 대여가 필요하신가요?"),
    ("나", "Yes, please. I'd like to rent one park golf club and two balls.", "네, 부탁합니다. 파크골프 채 하나와 공 두 개를 대여하고 싶어요."),
    ("직원", "Here you go. Course A is on the left, and it's a 9-hole course.", "여기 있습니다. 왼쪽이 A코스이고 9홀 코스입니다."),
    ("나", "Thank you. Is there a scorecard or a map I can take?", "감사합니다. 제가 가져갈 수 있는 스코어카드나 코스 안내도가 있나요?"),
    ("직원", "Sure, here is your scorecard. The weather is perfect for a round today!", "물론이죠, 여기 스코어카드 있습니다. 오늘 라운딩하기 딱 좋은 날씨네요!"),
    ("나", "It really is! Thank you so much, shall we get started?", "정말 그렇네요! 정말 감사해요, 이제 시작해 볼까요?")
]

# 3개의 탭 생성
tab1, tab2, tab3 = st.tabs(["📖 전체 대화", "🗣️ 한 문장 연습", "🎭 실전 롤플레잉"])

# -------------------------------------------------------------
# 1. 전체 대화 탭
# -------------------------------------------------------------
with tab1:
    st.subheader("1. 대화 흐름 파악하기")
    
    st.write("🎧 **전체 대화 한 번에 이어서 듣기**")
    full_english_text = " ".join([eng for role, eng, kor in dialogue])
    tts_full = gTTS(text=full_english_text, lang='en', slow=False)
    audio_io_full = io.BytesIO()
    tts_full.write_to_fp(audio_io_full)
    st.audio(audio_io_full, format='audio/mp3')
    
    st.write("---")
    for role, eng, kor in dialogue:
        if role == "직원":
            st.info(f"**직원:** {eng} \n\n({kor})")
        else:
            st.success(f"**나:** {eng} \n\n({kor})")

# -------------------------------------------------------------
# 2. 한 문장 연습 탭 (질문 + 대답 전체 선택 가능)
# -------------------------------------------------------------
with tab2:
    st.subheader("2. 문장별 집중 연습")
    st.caption("직원의 질문과 나의 대답을 모두 골라서 발음을 듣고 따라 해보세요.")
    
    options = [f"[{role}] {eng}" for role, eng, kor in dialogue]
    selected_option = st.selectbox("연습할 문장을 고르세요:", options)
    
    # 선택된 문장 찾기
    idx = options.index(selected_option)
    role, eng_text, kor_text = dialogue[idx]
    
    st.write(f"**한글 뜻:** {kor_text}")
    
    # 해당 문장 발음 듣기
    tts_sentence = gTTS(text=eng_text, lang='en', slow=False)
    audio_io_sentence = io.BytesIO()
    tts_sentence.write_to_fp(audio_io_sentence)
    st.audio(audio_io_sentence, format='audio/mp3')

# -------------------------------------------------------------
# 3. 실전 롤플레잉 탭 (전체 대화 주고받기)
# -------------------------------------------------------------
with tab3:
    st.subheader("3. 실전 롤플레잉 (전체 4단계 대화)")
    st.caption("직원의 음성을 듣고, 아래 마이크를 켜서 '나'의 대사로 직접 대답해 보세요.")
    
    step = st.radio(
        "진행할 대화 단계를 선택하세요:",
        ["1단계: 체크인", "2단계: 장비 대여", "3단계: 코스 및 스코어카드", "4단계: 라운딩 출발"],
        horizontal=True
    )
    
    step_idx_map = {
        "1단계: 체크인": 0,
        "2단계: 장비 대여": 2,
        "3단계: 코스 및 스코어카드": 4,
        "4단계: 라운딩 출발": 6
    }
    
    base_idx = step_idx_map[step]
    staff_turn = dialogue[base_idx]
    my_turn = dialogue[base_idx + 1]
    
    # 직원의 질문 영역
    st.info(f"**직원:** {staff_turn[1]} \n\n({staff_turn[2]})")
    
    # 직원 음성 재생
    tts_staff = gTTS(text=staff_turn[1], lang='en', slow=False)
    audio_io_staff = io.BytesIO()
    tts_staff.write_to_fp(audio_io_staff)
    st.audio(audio_io_staff, format='audio/mp3')
    
    st.write("---")
    
    # 나의 대답 영역
    st.write("👇 **내가 대답할 문장:**")
    st.success(f"**나:** {my_turn[1]} \n\n({my_turn[2]})")
    
    st.write("🎙️ **마이크를 한 번 터치하고 영어로 말해보세요:**")
    audio_value = audio_recorder(text="터치하여 말하기", icon_size="2x", pause_threshold=3.0)
    
    if audio_value:
        st.write("✅ **녹음 완료!** 내 목소리를 들어보세요:")
        st.audio(audio_value)

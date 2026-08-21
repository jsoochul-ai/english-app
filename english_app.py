import streamlit as st
from gtts import gTTS
import io
from audio_recorder_streamlit import audio_recorder

st.set_page_config(page_title="나만의 영어 단짝", page_icon="🗣️")

st.markdown("""
    <style>
        .big-english { font-size: 28px !important; font-weight: bold; text-align: center; color: #1E3A8A; }
        .meaning-korean { font-size: 18px !important; text-align: center; color: #4B5563; margin-bottom: 20px; }
    </style>
""", unsafe_allow_html=True)

st.title("🍽️ 오늘의 회화: 리조트 레스토랑")

# 10개 문장 사전 만들기
sentences = {
    "I'd like to book a table for dinner tonight.": "오늘 저녁 식사 자리를 예약하고 싶습니다.",
    "We have a reservation under the name Kim.": "김 이름으로 예약했습니다.",
    "Could we get a table by the window, please?": "창가 쪽 자리로 앉을 수 있을까요?",
    "Can I see the wine list, please?": "와인 메뉴판 좀 볼 수 있을까요?",
    "What is the signature dish here?": "이곳의 대표 메뉴는 무엇인가요?",
    "I'll have the steak, medium-rare, please.": "스테이크 미디엄 레어로 할게요.",
    "Excuse me, could I get some more water?": "실례하지만, 물 좀 더 주시겠어요?",
    "Everything was delicious, thank you.": "음식은 모두 맛있었습니다, 감사합니다.",
    "Could we have the bill, please?": "계산서 좀 주시겠어요?",
    "Can I charge this to my room?": "이것을 제 객실 요금으로 달아둘 수 있을까요?"
}

# 문장 선택하는 드롭다운 메뉴
english_list = list(sentences.keys())
selected_eng = st.selectbox("👇 오늘 연습할 문장을 선택해 주세요:", english_list)
selected_kor = sentences[selected_eng]

st.write("---")

# 선택된 문장 화면에 크게 보여주기
st.markdown(f'<p class="big-english">{selected_eng}</p>', unsafe_allow_html=True)
st.markdown(f'<p class="meaning-korean">{selected_kor}</p>', unsafe_allow_html=True)

# 원어민 음성 듣기
tts = gTTS(text=selected_eng, lang='en', slow=False)
audio_io = io.BytesIO()
tts.write_to_fp(audio_io)
st.audio(audio_io, format='audio/mp3')

st.write("---")
st.write("🎙️ **스마트폰에서 더 잘 작동하는 마이크 녹음!** 아래 마이크를 눌러 내 발음을 녹음해 보세요.")

# 녹음기
audio_value = audio_recorder(text="터치해서 영어로 대답하세요", icon_size="2x")

if audio_value:
    st.success("✅ 녹음 완료! 내 목소리와 원어민 발음을 비교해 보세요.")
    st.audio(audio_value)

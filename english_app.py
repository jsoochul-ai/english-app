import streamlit as st
from gtts import gTTS
import io
from audio_recorder_streamlit import audio_recorder
import speech_recognition as sr
import re
from data import scenarios

# 📱 1. 페이지 기본 설정
st.set_page_config(page_title="나만의 영어 단짝", page_icon="🎤", layout="centered")

# 💾 내 기록 저장을 위한 메모리 설정
if 'my_records' not in st.session_state:
    st.session_state.my_records = []

# 🎨 2. 사진과 비슷하게 만들기 위한 디자인 마법(CSS)
st.markdown("""
<style>
    .title-text { text-align: center; font-size: 24px; font-weight: bold; color: #1f3b4d; }
    .subtitle-text { text-align: center; font-size: 16px; color: #666; margin-bottom: 30px; }
    .sentence-card { 
        background-color: #ffffff; padding: 15px; border-radius: 15px; 
        box-shadow: 0px 4px 6px rgba(0,0,0,0.05); text-align: center; margin-bottom: 10px; border: 1px solid #f0f0f0;
    }
    .eng-text { font-size: 18px; font-weight: bold; color: #333; }
    .kor-text { font-size: 14px; color: #888; margin-top: 5px; }
</style>
""", unsafe_allow_html=True)

# 📑 3. 하단 메뉴바를 대신할 상단 탭 메뉴 (홈 / 내 기록 / 설정)
tab_home, tab_record, tab_settings = st.tabs(["🏠 홈", "📚 내 기록", "⚙️ 설정"])

with tab_home:
    # 주제 선택 (사진의 제목 부분)
    selected_topic = st.selectbox("오늘의 대화 주제를 선택하세요:", list(scenarios.keys()), label_visibility="collapsed")
    current_data = scenarios[selected_topic]
    dialogue = current_data["dialogue"]
    
    st.markdown(f"<div class='title-text'>{selected_topic.split(']')[1].strip()}</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle-text'>초급 (Beginner Level)</div>", unsafe_allow_html=True)
    
    # 🎤 마이크와 보조 버튼들 (사진과 비슷한 레이아웃)
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        st.write("")
        st.write("")
        if st.button("🔊\n전체 듣기", use_container_width=True):
            full_english = " ".join([eng for role, eng, kor in dialogue])
            tts = gTTS(text=full_english, lang='en', slow=False)
            audio_io = io.BytesIO()
            tts.write_to_fp(audio_io)
            st.audio(audio_io, format='audio/mp3')

    with col2:
        st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
        # 마이크 녹음기 중앙 배치
        audio_value = audio_recorder(text="말씀해 보세요", icon_size="3x", pause_threshold=3.0)
        st.markdown("</div>", unsafe_allow_html=True)

    with col3:
        st.write("")
        st.write("")
        st.button("❤️\n표현 저장", use_container_width=True)

    st.write("---")

    # 📝 문장 카드들 (사진 하단의 네모 박스들)
    st.write("👇 **핵심 문장 연습** (마이크를 켜고 따라해 보세요!)")
    for role, eng, kor in dialogue:
        if role == "나":
            # 나만의 문장 카드 디자인
            st.markdown(f"""
            <div class='sentence-card'>
                <div class='eng-text'>{eng}</div>
                <div class='kor-text'>{kor}</div>
            </div>
            """, unsafe_allow_html=True)

    # 🤖 마이크 녹음 처리 및 내 기록에 저장하기
    if audio_value:
        st.write("⏳ AI가 발음을 분석 중입니다...")
        try:
            r = sr.Recognizer()
            audio_file = io.BytesIO(audio_value)
            with sr.AudioFile(audio_file) as source:
                audio_data = r.record(source)
            
            recognized_text = r.recognize_google(audio_data, language="en-US")
            st.success(f"🗣️ AI 인식 결과: **{recognized_text}**")
            
            # 내 기록에 추가!
            st.session_state.my_records.append({
                "topic": selected_topic,
                "said": recognized_text
            })
            st.info("✅ '내 기록' 탭에 방금 하신 발음이 저장되었습니다!")
            
        except sr.UnknownValueError:
            st.error("앗, 목소리가 잘 안 들렸어요. 다시 시도해 주세요!")
        except Exception as e:
            st.error("오류가 발생했습니다.")

with tab_record:
    st.header("📚 내 학습 기록")
    st.caption("내가 마이크로 연습했던 문장들이 여기에 차곡차곡 쌓입니다. (앱을 새로고침하면 초기화됩니다)")
    
    if len(st.session_state.my_records) == 0:
        st.info("아직 녹음된 기록이 없습니다. 홈에서 마이크를 켜고 말해보세요!")
    else:
        for i, record in enumerate(reversed(st.session_state.my_records)):
            st.markdown(f"""
            <div class='sentence-card' style='text-align: left;'>
                <span style='color: #888; font-size: 12px;'>{record['topic']}</span><br>
                <span class='eng-text'>🗣️ {record['said']}</span>
            </div>
            """, unsafe_allow_html=True)

with tab_settings:
    st.header("⚙️ 설정")
    st.info("앱 테마, 목소리 속도 등을 조절하는 기능이 곧 업데이트될 예정입니다.")

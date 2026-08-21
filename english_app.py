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

# 🎨 2. 앱 디자인 꾸미기 (대본 카드 스타일 추가)
st.markdown("""
<style>
    .title-text { text-align: center; font-size: 24px; font-weight: bold; color: #1f3b4d; }
    .subtitle-text { text-align: center; font-size: 16px; color: #666; margin-bottom: 30px; }
    .sentence-card { 
        padding: 15px; border-radius: 10px; 
        box-shadow: 0px 2px 5px rgba(0,0,0,0.05); margin-bottom: 12px; 
    }
    .role-label { font-size: 12px; font-weight: bold; margin-bottom: 5px; }
    .eng-text { font-size: 18px; font-weight: bold; color: #333; }
    .kor-text { font-size: 14px; color: #777; margin-top: 5px; }
</style>
""", unsafe_allow_html=True)

# 📑 3. 상단 탭 메뉴 (홈 / 내 기록 / 설정)
tab_home, tab_record, tab_settings = st.tabs(["🏠 홈", "📚 내 기록", "⚙️ 설정"])

with tab_home:
    # 주제 선택
    selected_topic = st.selectbox("오늘의 대화 주제를 선택하세요:", list(scenarios.keys()), label_visibility="collapsed")
    current_data = scenarios[selected_topic]
    dialogue = current_data["dialogue"]
    
    st.markdown(f"<div class='title-text'>{selected_topic.split(']')[1].strip()}</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle-text'>초급 (Beginner Level)</div>", unsafe_allow_html=True)
    
    # 🎤 4. 마이크와 보조 버튼들
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
        audio_value = audio_recorder(text="말씀해 보세요", icon_size="3x", pause_threshold=3.0)
        st.markdown("</div>", unsafe_allow_html=True)

    with col3:
        st.write("")
        st.write("")
        st.button("❤️\n표현 저장", use_container_width=True)

    # 🤖 마이크 녹음 처리 (결과를 마이크 바로 밑에 보여줌)
    if audio_value:
        st.write("⏳ AI가 발음을 분석 중입니다...")
        try:
            r = sr.Recognizer()
            audio_file = io.BytesIO(audio_value)
            with sr.AudioFile(audio_file) as source:
                audio_data = r.record(source)
            
            recognized_text = r.recognize_google(audio_data, language="en-US")
            st.success(f"🗣️ AI 인식 결과: **{recognized_text}**")
            
            st.session_state.my_records.append({"topic": selected_topic, "said": recognized_text})
            st.info("✅ '내 기록' 탭에 방금 하신 발음이 저장되었습니다!")
            
        except sr.UnknownValueError:
            st.error("앗, 목소리가 잘 안 들렸어요. 다시 시도해 주세요!")
        except Exception as e:
            st.error("오류가 발생했습니다.")

    st.write("---")
    
    # 📖 5. 전체 대화 대본 (눈으로 보며 학습하기)
    st.write("📖 **오늘의 대화 대본** (전체 듣기를 누르고 눈으로 따라 읽어보세요!)")
    
    for role, eng, kor in dialogue:
        if role in ["직원", "손님", "친구", "승무원", "기사", "행인"]:
            # 상대방 대사 (회색 띠)
            st.markdown(f"""
            <div class='sentence-card' style='background-color: #f8f9fa; border-left: 4px solid #adb5bd;'>
                <div class='role-label' style='color: #6c757d;'>{role}</div>
                <div class='eng-text'>{eng}</div>
                <div class='kor-text'>{kor}</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            # 나의 대사 (파란색 띠)
            st.markdown(f"""
            <div class='sentence-card' style='background-color: #e3f2fd; border-left: 4px solid #1976d2;'>
                <div class='role-label' style='color: #1976d2;'>나</div>
                <div class='eng-text'>{eng}</div>
                <div class='kor-text'>{kor}</div>
            </div>
            """, unsafe_allow_html=True)

with tab_record:
    st.header("📚 내 학습 기록")
    st.caption("내가 마이크로 연습했던 문장들이 여기에 차곡차곡 쌓입니다. (앱을 껐다 켜면 초기화됩니다)")
    
    if len(st.session_state.my_records) == 0:
        st.info("아직 녹음된 기록이 없습니다. 홈에서 마이크를 켜고 말해보세요!")
    else:
        for record in reversed(st.session_state.my_records):
            st.markdown(f"""
            <div class='sentence-card' style='background-color: #ffffff; border: 1px solid #e0e0e0;'>
                <span style='color: #888; font-size: 12px;'>{record['topic']}</span><br>
                <span class='eng-text'>🗣️ {record['said']}</span>
            </div>
            """, unsafe_allow_html=True)

with tab_settings:
    st.header("⚙️ 설정")
    st.info("앱 테마, 목소리 속도 등을 조절하는 기능이 곧 업데이트될 예정입니다.")

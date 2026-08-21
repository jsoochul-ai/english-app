import streamlit as st
from gtts import gTTS
import io
from audio_recorder_streamlit import audio_recorder
import speech_recognition as sr
import re
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="나만의 영어 단짝", page_icon="✈️", layout="wide")

st.markdown("""
    <style>
    div.stButton > button {color: #1D4ED8 !important; font-weight: bold !important; border: 2px solid #1D4ED8 !important; background-color: transparent !important;}
    div.stButton > button p {color: #1D4ED8 !important; font-size: 16px !important;}
    div.stButton > button:hover {background-color: #EFF6FF !important;}
    </style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center;'>✈️ 나만의 영어 단짝</h2>", unsafe_allow_html=True)
st.write("---")

# 💡 엑셀(CSV) 파일에서 데이터 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv("data.csv")
    scenarios = {}
    for topic, group in df.groupby("주제"):
        desc = group["설명"].iloc[0]
        dialogue = list(zip(group["역할"], group["영어"], group["한글"]))
        scenarios[topic] = {"description": desc, "dialogue": dialogue}
    return scenarios

try:
    scenarios = load_data()
except Exception as e:
    st.error("데이터를 불러오는 중 오류가 발생했습니다. data.csv 파일을 확인해 주세요.")
    st.stop()

scenario_list = list(scenarios.keys())
num_scenarios = len(scenario_list)
current_day = datetime.now().timetuple().tm_yday

today_idx = current_day % num_scenarios
yesterday_idx = (today_idx - 1) % num_scenarios
tomorrow_idx = (today_idx + 1) % num_scenarios

topic_today = scenario_list[today_idx]
topic_yesterday = scenario_list[yesterday_idx]
topic_tomorrow = scenario_list[tomorrow_idx]

if "current_topic" not in st.session_state:
    st.session_state.current_topic = None

col1, col2, col3 = st.columns(3)
if col1.button(f"📖 1. 오늘의 학습\n\n({topic_today})", use_container_width=True):
    st.session_state.current_topic = topic_today
if col2.button(f"🔄 2. 어제 복습\n\n({topic_yesterday})", use_container_width=True):
    st.session_state.current_topic = topic_yesterday
if col3.button(f"🚀 3. 내일 예습\n\n({topic_tomorrow})", use_container_width=True):
    st.session_state.current_topic = topic_tomorrow

st.write("---")

if st.session_state.current_topic is None:
    st.info("💡 위 버튼을 눌러 연습을 시작해 보세요!")
else:
    current_data = scenarios[st.session_state.current_topic]
    dialogue = current_data["dialogue"]

    st.subheader(f"📍 {st.session_state.current_topic}")
    st.caption(current_data["description"])

    tab1, tab2, tab3 = st.tabs(["📖 전체 대화", "🗣️ 한 문장 연습", "🎭 실전 롤플레잉"])

    with tab1:
        st.write("🎧 **전체 대화 이어서 듣기**")
        full_english_text = " ".join([str(eng) for role, eng, kor in dialogue])
        tts_full = gTTS(text=full_english_text, lang='en', slow=False)
        audio_io_full = io.BytesIO()
        tts_full.write_to_fp(audio_io_full)
        st.audio(audio_io_full, format='audio/mp3')
        
        st.write("---")
        for role, eng, kor in dialogue:
            if role == "나":
                st.success(f"**나:** {eng} \n\n({kor})")
            else:
                st.info(f"**{role}:** {eng} \n\n({kor})")

    with tab2:
        options = [f"[{role}] {eng}" for role, eng, kor in dialogue]
        selected_option = st.selectbox("연습할 문장을 고르세요:", options)
        idx = options.index(selected_option)
        role, eng_text, kor_text = dialogue[idx]
        st.write(f"**한글 뜻:** {kor_text}")
        tts_sentence = gTTS(text=str(eng_text), lang='en', slow=False)
        audio_io_sentence = io.BytesIO()
        tts_sentence.write_to_fp(audio_io_sentence)
        st.audio(audio_io_sentence, format='audio/mp3')

    def clean_text(text):
        return re.sub(r'[^a-z0-9\s]', '', str(text).lower()).strip()

    with tab3:
        turns = [f"{i+1}단계" for i in range(len(dialogue)//2)]
        if turns:
            step = st.radio("진행할 대화 단계를 선택하세요:", turns, horizontal=True)
            step_idx = turns.index(step) * 2
            
            if step_idx + 1 < len(dialogue):
                staff_turn = dialogue[step_idx]
                my_turn = dialogue[step_idx + 1]
                
                st.info(f"**{staff_turn[0]}:** {staff_turn[1]} \n\n({staff_turn[2]})")
                tts_staff = gTTS(text=str(staff_turn[1]), lang='en', slow=False)
                audio_io_staff = io.BytesIO()
                tts_staff.write_to_fp(audio_io_staff)
                st.audio(audio_io_staff, format='audio/mp3')
                
                st.write("---")
                st.write("👇 **내가 대답할 정답 문장:**")
                st.success(f"**나:** {my_turn[1]} \n\n({my_turn[2]})")
                
                audio_value = audio_recorder(text="터치하여 말하기", icon_size="2x", pause_threshold=3.0)
                
                if audio_value:
                    st.audio(audio_value)
                    st.write("⏳ AI가 발음을 분석 중입니다...")
                    try:
                        r = sr.Recognizer()
                        audio_file = io.BytesIO(audio_value)
                        with sr.AudioFile(audio_file) as source:
                            audio_data = r.record(source)
                        recognized_text = r.recognize_google(audio_data, language="en-US")
                        st.write(f"📝 **AI가 들은 내 목소리:** {recognized_text}")
                        
                        target_clean = clean_text(my_turn[1])
                        recog_clean = clean_text(recognized_text)
                        
                        if target_clean == recog_clean:
                            st.success("🎉 완벽합니다! 원어민과 똑같이 발음하셨네요!")
                        elif recog_clean in target_clean or target_clean in recog_clean:
                            st.warning("👍 좋습니다! 핵심 단어가 전달되어 의사소통이 가능합니다.")
                        else:
                            st.error("💪 다르게 인식되었어요! 원어민 발음을 다시 듣고 시도해 보세요.")
                    except sr.UnknownValueError:
                        st.error("앗, 목소리가 잘 안 들렸어요. 다시 시도해 주세요!")
                    except Exception as e:
                        st.error("마이크 인식 중 오류가 발생했습니다. 잠시 후 다시 시도해 주세요.")

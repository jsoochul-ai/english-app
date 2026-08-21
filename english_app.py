import streamlit as st
from gtts import gTTS
import io
from audio_recorder_streamlit import audio_recorder
import speech_recognition as sr
import re
from data import scenarios

# 📱 1. 페이지 기본 설정 (스마트폰에 최적화된 중앙 정렬)
st.set_page_config(page_title="나만의 영어 단짝", page_icon="🚀", layout="centered")

# 🎨 2. 사이드바: 세련된 메뉴판 디자인
with st.sidebar:
    st.title("🚀 My English App")
    st.caption("나만의 맞춤형 회화 도서관")
    st.write("---")
    
    # 터치하기 편한 라디오 버튼으로 메뉴 변경
    selected_topic = st.radio(
        "👇 학습할 대본을 선택하세요",
        list(scenarios.keys())
    )
    
    st.write("---")
    # 향후 업데이트될 나만의 맞춤 카테고리 예고편
    st.success("💡 **Next Update 예고**\n\n💍 외국인 고객 응대 (Jeloday)\n⛳ 골프장 조인 라운딩\n⚾ 롯데 자이언츠 스몰토크")

# ✨ 3. 메인 화면 헤더 장식
current_data = scenarios[selected_topic]
dialogue = current_data["dialogue"]

st.title(selected_topic)
st.info(f"📍 **상황 설명:** {current_data['description']}")
st.write("---")

# 📑 4. 깔끔해진 탭 메뉴
tab1, tab2, tab3 = st.tabs(["📖 전체 대화", "🗣️ 한 문장 연습", "🎙️ 실전 롤플레잉 (AI 채점)"])

with tab1:
    st.subheader("1. 대화 흐름 파악하기")
    st.write("🎧 **전체 대화 이어서 듣기**")
    full_english_text = " ".join([eng for role, eng, kor in dialogue])
    tts_full = gTTS(text=full_english_text, lang='en', slow=False)
    audio_io_full = io.BytesIO()
    tts_full.write_to_fp(audio_io_full)
    st.audio(audio_io_full, format='audio/mp3')
    
    st.write("---")
    for role, eng, kor in dialogue:
        if role in ["직원", "손님", "친구", "승무원", "기사", "행인"]:
            st.warning(f"**{role}:** {eng} \n\n({kor})")
        else:
            st.success(f"**나:** {eng} \n\n({kor})")

with tab2:
    st.subheader("2. 문장별 집중 연습")
    options = [f"[{role}] {eng}" for role, eng, kor in dialogue]
    selected_option = st.selectbox("연습할 문장을 고르세요:", options)
    
    idx = options.index(selected_option)
    role, eng_text, kor_text = dialogue[idx]
    st.markdown(f"**💡 한글 뜻:** {kor_text}")
    
    tts_sentence = gTTS(text=eng_text, lang='en', slow=False)
    audio_io_sentence = io.BytesIO()
    tts_sentence.write_to_fp(audio_io_sentence)
    st.audio(audio_io_sentence, format='audio/mp3')

def clean_text(text):
    return re.sub(r'[^a-z0-9\s]', '', text.lower()).strip()

with tab3:
    st.subheader("3. 실전 롤플레잉 & AI 발음 채점")
    
    turns = [f"{i+1}단계" for i in range(len(dialogue)//2)]
    step = st.radio("진행할 대화 단계를 선택하세요:", turns, horizontal=True)
    
    step_idx = turns.index(step) * 2
    staff_turn = dialogue[step_idx]
    my_turn = dialogue[step_idx + 1]
    
    st.warning(f"**{staff_turn[0]}:** {staff_turn[1]} \n\n({staff_turn[2]})")
    tts_staff = gTTS(text=staff_turn[1], lang='en', slow=False)
    audio_io_staff = io.BytesIO()
    tts_staff.write_to_fp(audio_io_staff)
    st.audio(audio_io_staff, format='audio/mp3')
    
    st.write("---")
    st.write("👇 **내가 대답할 정답 문장:**")
    st.success(f"**나:** {my_turn[1]} \n\n({my_turn[2]})")
    
    st.write("🎙️ **마이크를 켜고 정답 문장을 말해보세요!**")
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
                st.info("👍 좋습니다! 핵심 단어가 전달되어 의사소통이 가능합니다.")
            else:
                st.error("💪 다르게 인식되었어요! 원어민 발음을 다시 듣고 시도해 보세요.")
        except sr.UnknownValueError:
            st.error("앗, 목소리가 잘 안 들렸어요. 다시 시도해 주세요!")
        except Exception as e:
            st.error("마이크 인식 중 오류가 발생했습니다. 잠시 후 다시 시도해 주세요.")

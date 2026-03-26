import streamlit as st
import requests
import tempfile
import whisper

from audio_recorder_streamlit import audio_recorder

st.set_page_config(page_title="VoxAgent", page_icon="🎤")

st.title("🎤 VoxAgent - Voice AI Assistant")

# model = whisper.load_model("base", device="cpu")
# 🔥 IMPORTANT: use tiny model for deployment
model = whisper.load_model("tiny", device="cpu")

BACKEND_URL = "https://your-render-url.onrender.com/chat"

st.write("Click below and speak")

audio_bytes = audio_recorder()

if audio_bytes:
    st.audio(audio_bytes, format="audio/wav")

    # save temp audio
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
        f.write(audio_bytes)
        audio_path = f.name

    # speech → text
    result = model.transcribe(audio_path)
    text = result["text"]

    st.write(f"📝 You said: {text}")

    try:
        response = requests.post(
            BACKEND_URL,
            json={"message": text},
            timeout=30
        )

        answer = response.json()["response"]

        st.success(answer)

    except Exception as e:
        st.error(f"Backend error: {e}")
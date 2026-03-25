import streamlit as st
import requests
import tempfile
import whisper

from audio_recorder_streamlit import audio_recorder

st.set_page_config(page_title="VoxAgent", page_icon="🎤")

st.title("🎤 VoxAgent - Voice AI Assistant")

# load whisper locally (for browser audio)
model = whisper.load_model("base", device="cpu")

st.write("Click below and speak")

audio_bytes = audio_recorder()

if audio_bytes:
    st.audio(audio_bytes, format="audio/wav")

    # save temp audio
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
        f.write(audio_bytes)
        audio_path = f.name

    # convert speech → text
    result = model.transcribe(audio_path)
    text = result["text"]

    st.write(f"📝 You said: {text}")

    # send to FastAPI
    response = requests.post(
        "http://127.0.0.1:8000/chat",
        json={"message": text}
    )

    answer = response.json()["response"]

    st.success(answer)
import whisper
import sounddevice as sd
from scipy.io.wavfile import write
import tempfile

# load model once
model = whisper.load_model("base", device="cpu")


def record_audio(duration=5, fs=44100):
    print("🎤 Speak now...")

    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()

    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    write(temp_file.name, fs, recording)

    return temp_file.name


def speech_to_text():
    audio_path = record_audio()

    result = model.transcribe(audio_path)
    text = result["text"]

    print(f"📝 You said: {text}")

    return text
if __name__ == "__main__":
    text = speech_to_text()
    print("Final Text:", text)
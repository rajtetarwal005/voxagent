from elevenlabs.client import ElevenLabs
from app.config import settings
import tempfile
import os

# create client
client = ElevenLabs(api_key=settings.ELEVENLABS_API_KEY)


def text_to_speech(text: str):
    audio = client.text_to_speech.convert(
        text=text,
        voice_id="EXAVITQu4vr4xnSDxMaL"
    )

    # save as temp mp3 file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")

    with open(temp_file.name, "wb") as f:
        for chunk in audio:
            f.write(chunk)

    # play using system player
    os.system(f"ffplay -nodisp -autoexit {temp_file.name}")


# test
if __name__ == "__main__":
    text_to_speech("Hello Raj, your voice system is working perfectly")
from openai import OpenAI

def transcribe_whisper(audio_path: str, language: str = "pt") -> str:
    client = OpenAI()
    with open(audio_path, "rb") as f_audio:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=f_audio,
            language=language
        )
    return transcript.text

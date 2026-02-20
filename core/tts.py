import os
import requests

def eleven_tts(text: str, output_path: str):
    api_key = os.environ["ELEVEN_API_KEY"]

    # pegar primeira voz disponível
    r = requests.get(
        "https://api.elevenlabs.io/v1/voices",
        headers={"xi-api-key": api_key}
    )
    voices = r.json()["voices"]
    voice_id = voices[0]["voice_id"]

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

    payload = {
        "text": text,
        "model_id": "eleven_multilingual_v2"
    }

    response = requests.post(
        url,
        headers={
            "xi-api-key": api_key,
            "Accept": "audio/mpeg",
            "Content-Type": "application/json"
        },
        json=payload
    )

    with open(output_path, "wb") as f_audio:
        f_audio.write(response.content)

    return output_path


import os
import json
from pathlib import Path

import requests
from dotenv import load_dotenv
from openai import OpenAI


BASE = Path(__file__).parent
DATA = BASE / "data"
OUT = BASE / "outputs"


def ensure_dirs():
    DATA.mkdir(exist_ok=True)
    OUT.mkdir(exist_ok=True)


def load_keys():
    load_dotenv(BASE / ".env")
    openai_key = os.getenv("OPENAI_API_KEY")
    eleven_key = os.getenv("ELEVEN_API_KEY")
    return openai_key, eleven_key


def transcribe_openai(client: OpenAI, audio_path: Path, language="pt"):
    # modelos podem variar; se der erro, a gente ajusta o nome do modelo
    with audio_path.open("rb") as f:
        t = client.audio.transcriptions.create(
            model="whisper-1",
            file=f,
            language=language
        )
    return t.text


def llm_answer(client: OpenAI, user_text: str):
    prompt_system = (
        "Você é um assistente científico e operacional. "
        "Responda em português, de forma clara, objetiva e útil."
    )
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": prompt_system},
            {"role": "user", "content": user_text}
        ],
        temperature=0.4
    )
    return resp.choices[0].message.content


def eleven_list_voices(eleven_key: str):
    r = requests.get(
        "https://api.elevenlabs.io/v1/voices",
        headers={"xi-api-key": eleven_key, "Accept": "application/json"}
    )
    r.raise_for_status()
    return r.json()["voices"]


def eleven_tts(eleven_key: str, text: str, out_mp3: Path, voice_id: str):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    payload = {
        "text": text,
        "model_id": "eleven_multilingual_v2"
    }
    headers = {
        "xi-api-key": eleven_key,
        "Accept": "audio/mpeg",
        "Content-Type": "application/json"
    }

    r = requests.post(url, headers=headers, json=payload)
    r.raise_for_status()
    out_mp3.write_bytes(r.content)


def main():
    ensure_dirs()
    openai_key, eleven_key = load_keys()

    if not openai_key or not eleven_key:
        print("❌ Faltam chaves no .env (OPENAI_API_KEY e/ou ELEVEN_API_KEY).")
        print("   Crie um arquivo VoiceAI_Operacional/.env baseado no .env.example")
        return

    audio_path = DATA / "input.mp3"
    if not audio_path.exists():
        print("❌ Coloque seu áudio em VoiceAI_Operacional/data/input.mp3")
        return

    client = OpenAI(api_key=openai_key)

    print("🎙️ Transcrevendo...")
    text = transcribe_openai(client, audio_path, language="pt")
    (OUT / "transcricao.txt").write_text(text, encoding="utf-8")

    print("🧠 Gerando resposta do LLM...")
    answer = llm_answer(client, text)
    (OUT / "resposta.txt").write_text(answer, encoding="utf-8")

    print("🔊 Gerando voz ElevenLabs...")
    voices = eleven_list_voices(eleven_key)
    voice_id = voices[0]["voice_id"]  # pega a primeira voz da conta
    out_mp3 = OUT / "resposta_elevenlabs.mp3"
    eleven_tts(eleven_key, answer, out_mp3, voice_id)

    meta = {
        "audio_input": str(audio_path),
        "voice_id": voice_id,
    }
    (OUT / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")

    print("✅ Pronto! Veja outputs/: transcricao.txt, resposta.txt, resposta_elevenlabs.mp3")


if __name__ == "__main__":
    main()

# VoiceAI Operacional 🎙️🤖  
**Pipeline modular de Voice AI** para transcrição (Whisper), processamento com LLM (OpenAI) e síntese de voz humanizada (ElevenLabs) — com foco em aplicações operacionais, pesquisa e produção de conteúdo.

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Ativo-success.svg)](#)
[![Version](https://img.shields.io/badge/Version-1.0.0-informational.svg)](#)

---

## 🔥 O que este projeto faz
A partir de um áudio de entrada (MP3/WAV), o sistema executa:

1. **STT — Speech-to-Text (Whisper)**  
   Transcreve o áudio para texto.
2. **LLM — Processamento inteligente (OpenAI)**  
   Resume, organiza, responde ou transforma a transcrição conforme prompt.
3. **TTS — Text-to-Speech (ElevenLabs)**  
   Gera um áudio final com voz humanizada baseado na resposta do LLM.

---

## 🧠 Arquitetura (Visão Geral)

Áudio (MP3/WAV)
↓
[Whisper - STT] → transcricao.txt
↓
[OpenAI - LLM] → resposta.txt (+ meta.json)
↓
[ElevenLabs - TTS] → resposta_elevenlabs.mp3


---

## 📁 Estrutura do projeto

voiceai-operacional/

├─ core/

│ ├─ stt.py # transcrição (Whisper)

│ ├─ llm.py # processamento (OpenAI)

│ └─ tts.py # narração (ElevenLabs)

├─ data/

│ ├─ raw/ # áudios originais (opcional)

│ ├─ input.wav # áudio padronizado (16kHz mono)

│ └─ logs/ # logs (se ativado)

├─ outputs/

│ ├─ transcricao.txt

│ ├─ resposta.txt

│ ├─ resposta_elevenlabs.mp3

│ └─ meta.json

├─ main.py

├─ requirements.txt

├─ README.md

├─ LICENSE

└─ LICENSE.pt.md


---

## ✅ Requisitos
- Python **3.10+**
- Conta/chave de API para:
  - OpenAI (LLM)
  - ElevenLabs (TTS)

> Obs.: Whisper pode rodar local dependendo do setup; no Colab ele roda tranquilo.

---

## ⚙️ Instalação (Windows / Linux / Mac)
No terminal dentro da pasta do projeto:

```bash
python -m venv .venv
Windows
.venv\Scripts\activate
Linux/Mac
source .venv/bin/activate

Instalar dependências:

pip install -r requirements.txt
🔐 Configurar variáveis de ambiente (.env)

Crie um arquivo .env na raiz do projeto (ou copie .env.example):

Exemplo:

OPENAI_API_KEY=coloque_sua_chave_aqui
ELEVENLABS_API_KEY=coloque_sua_chave_aqui
ELEVENLABS_VOICE_ID=coloque_o_voice_id_aqui
MODEL_NAME=gpt-4o-mini

Dica: NUNCA suba seu .env para o GitHub.

🎧 Como usar

Coloque um áudio em data/

Ideal: data/input.wav (16kHz mono)

Se você tiver MP3, converta para WAV (16kHz mono)

Converter MP3 → WAV (16kHz mono) com FFmpeg
ffmpeg -y -i "seu_audio.mp3" -ar 16000 -ac 1 "data/input.wav"

Rode o pipeline:

python main.py
📤 Saídas geradas (outputs/)

Após rodar, você terá:

outputs/transcricao.txt → texto do áudio

outputs/resposta.txt → resultado processado pelo LLM

outputs/resposta_elevenlabs.mp3 → narração final

outputs/meta.json → metadados do processamento

🧪 Exemplo de uso real

Use este projeto para:

transformar áudio de aula em resumo estruturado

gerar roteiro para vídeo

produzir narração para conteúdo científico

criar “briefing operacional” a partir de gravação

🎥 GIF demonstrativo (como adicionar)

Você pode adicionar um GIF no README para ficar “top portfólio”.

Como fazer (rápido):

Grave a tela rodando python main.py (10–15s)

Windows: Win + G (Xbox Game Bar) ou ScreenToGif

Converta o vídeo para GIF (ScreenToGif faz isso)

Suba o arquivo em: assets/demo.gif

Adicione no README:

![Demo](assets/demo.gif)
🛣️ Roadmap (próximas versões)

 Modo batch (processar vários áudios)

 CLI profissional (--input, --output, --prompt)

 Logs estruturados + níveis (INFO/WARN/ERROR)

 Dockerfile (rodar com 1 comando)

 Testes automatizados

📄 Licença

Este projeto é licenciado sob a MIT License.
Veja: LICENSE

Versão em português: LICENSE.pt.md

👤 Autor

Matheus Florindo de Deus Barboza Gonçalves
GitHub: @matheusflorindo32

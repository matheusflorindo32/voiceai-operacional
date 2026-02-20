# VoiceAI Operacional

Pipeline modular em Python que integra:

- 🎙 Speech-to-Text (Whisper)
- 🧠 Processamento com LLM (OpenAI)
- 🔊 Síntese de voz humanizada (ElevenLabs)

Aplicado a contextos de Segurança Pública e Saúde Ocupacional.

---

## 🚀 Funcionalidades

- Transcrição automática de áudio
- Geração de resposta contextual com LLM
- Conversão da resposta em áudio (TTS)
- Estrutura modular e organizada

---

## 📁 Estrutura do Projeto

voiceai-operacional/

│

├── core/ # Módulos principais (STT, LLM, TTS)

├── data/ # Arquivos de entrada

├── outputs/ # Resultados gerados

│

├── main.py # Orquestrador do pipeline

├── requirements.txt # Dependências do projeto

└── README.md



---

## ⚙️ Requisitos

- Python 3.10+
- pip
- Conta na OpenAI
- Conta na ElevenLabs

---

## 🛠 Instalação

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/matheusflorindo32/voiceai-operacional.git
cd voiceai-operacional

2️⃣ Instale as dependências

pip install -r requirements.txt

🔐 Configuração de Ambiente

Crie um arquivo .env na raiz do projeto contendo:

OPENAI_API_KEY= SUA_CHAVE_OPENAI
ELEVEN_API_KEY= SUA_CHAVE_ELEVENLABS

⚠️ Nunca envie o arquivo .env para o GitHub.

▶️ Como Executar

Coloque um áudio de entrada na pasta data/

Recomendado: .wav 16kHz mono

Execute:

▶️ Como Executar

1 . Coloque um áudio de entrada na pasta data/

Recomendado: .wav 16kHz mono

2 . Execute:

python main.py

📥 Exemplo de Conversão de Áudio

Se tiver um .mp3, converta para .wav:

ffmpeg -y -i input.mp3 -ar 16000 -ac 1 input.wav

📤 Saídas Geradas

Após execução, o sistema cria:

outputs/transcricao.txt → Texto transcrito

outputs/resposta.txt → Resposta gerada pelo LLM

outputs/resposta_elevenlabs.mp3 → Áudio final sintetizado

🧠 Arquitetura do Sistema

Áudio de Entrada
        ↓
Whisper (STT)
        ↓
Texto Transcrito
        ↓
LLM (GPT)
        ↓
Resposta Inteligente
        ↓
ElevenLabs (TTS)
        ↓
Áudio Final

🔒 Boas Práticas

Utilize .gitignore para proteger segredos

Nunca exponha chaves de API

Revogue imediatamente qualquer chave vazada

📈 Roadmap (Próximas Melhorias)

🔄 Processamento em lote (Batch)

🌐 Interface Web (Streamlit/FastAPI)

📊 Logs estruturados

☁ Deploy em ambiente cloud

🧪 Testes automatizados

🎯 Aplicações

Relatórios operacionais por voz

Análise tática de ocorrências

Resumos automatizados de áudio

Produção de conteúdo narrado técnico

📄 Licença

MIT License


👤 Autor

Matheus Florindo
Projeto desenvolvido para fins educacionais, pesquisa e portfólio profissional.


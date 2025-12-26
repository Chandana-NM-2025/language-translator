# HacFy Language Translator

> Instantly translate text to 11+ languages using Google's Gemini AI

A fast, simple, and elegant language translation web application built with Streamlit and powered by Google's advanced Gemini AI model.

## ✨ Features

- **🌐 Multi-Language Support** - Translate to Kannada, Hindi, Telugu, Tamil, Malayalam, Spanish, German, French, Japanese, Korean, Arabic, and more
- **⚡ Real-Time Translation** - Get results instantly using Gemini AI
- **🎨 Modern Interface** - Clean, dark-themed Streamlit UI
- **🔒 Secure** - API keys managed via environment variables
- **📦 Lightweight** - Minimal dependencies, easy to deploy
- **🚀 Production Ready** - Simple setup, scalable architecture

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| Frontend | Streamlit (Python) |
| Backend | Python |
| AI Model | Google Gemini 2.5 Flash |
| API | Google Generative AI |

## 📋 Project Structure

```
language_translator/
├── frontend/app.py              # Web UI
├── backend/translate_backend.py # Translation engine
├── test_models.py               # Model testing utility
├── requirements.txt             # Dependencies
├── .env                         # Config (not committed)
└── README.md                    # This file
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Google Gemini API key ([get it free](https://aistudio.google.com/apikey))

### Installation

1. **Clone & Setup**
   ```bash
   git clone <repository-url>
   cd language_translator
   python -m venv venv
   venv\Scripts\activate        # Windows
   # OR
   source venv/bin/activate     # macOS/Linux
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Key**
   ```bash
   # Create .env file in project root
   GEMINI_API_KEY=your_api_key_here
   GEMINI_MODEL=models/gemini-2.5-flash
   ```

4. **Run Application**
   ```bash
   streamlit run frontend/app.py
   ```
   Opens at: `http://localhost:8501`

## 💻 Usage

1. Paste or type text in the input area
2. Select target language from dropdown
3. Click "🌐 Translate" button
4. View instant translation

## 📦 Dependencies

```
streamlit           # Web framework
google-generativeai # Gemini API client
python-dotenv       # Environment variables
```

## 🔑 Getting Your API Key

1. Go to [Google AI Studio](https://aistudio.google.com/apikey)
2. Sign in with Google
3. Click "Create API Key"
4. Copy & paste into `.env` file

## 📁 Files Overview

### `frontend/app.py`
Streamlit web interface with:
- Text input area
- Language selector (11+ languages)
- Custom dark theme styling
- Real-time translation display

### `backend/translate_backend.py`
Core translation logic:
- Gemini API initialization
- Prompt engineering
- Error handling
- Response processing

### `test_models.py`
Utility to verify available Gemini models:
```bash
python test_models.py
```

## ⚙️ Configuration

| Variable | Default | Required |
|----------|---------|----------|
| `GEMINI_API_KEY` | - | ✅ Yes |
| `GEMINI_MODEL` | `models/gemini-2.5-flash` | ❌ No |

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` |
| `GEMINI_API_KEY not found` | Create `.env` file with your API key |
| Slow translations | Check internet & Gemini API status |
| Invalid API key error | Verify key is correct in `.env` |

## 🚢 Deployment

### Streamlit Cloud (Recommended)
1. Push code to GitHub
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
3. Connect GitHub repo
4. Add secrets: `GEMINI_API_KEY`


## 📈 Roadmap

- [ ] Batch translation
- [ ] File upload support
- [ ] Translation history
- [ ] Language auto-detection
- [ ] Copy to clipboard
- [ ] Multiple model selection

---

**Made with ❤️ using Streamlit & Google Gemini AI API KEY**
[⬆ back to top](#-hacfy-language-translator)

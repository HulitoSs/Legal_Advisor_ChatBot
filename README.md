# ⚖️ LawBuddy — AI-Powered Legal Document Chatbot

An AI-powered legal assistant chatbot that helps users understand contracts and legal documents in plain, simple language — no legal background required.

Built with **LangChain**, **LLaMA 3.1 (8B Instruct)**, and **Streamlit**, LawBuddy analyzes legal documents, flags risks, explains confusing terms, and suggests fixes — all in a friendly, approachable tone.

---

## 🚀 Features

- 📄 **Document Analysis** — Paste any legal text and get a structured breakdown instantly
- ⚠️ **Risk Detection** — Identifies unclear, missing, or potentially harmful clauses
- 🔧 **Suggested Fixes** — Actionable rewrites and improvements for problematic sections
- 📖 **Plain English Explanations** — Legal jargon decoded into everyday language
- 💬 **Multi-turn Conversations** — Remembers previous messages using persistent JSON chat history
- 🧠 **Powered by LLaMA 3.1** — Uses Meta's `Llama-3.1-8B-Instruct` via HuggingFace

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| [LangChain](https://www.langchain.com/) | LLM orchestration & prompt management |
| [HuggingFace](https://huggingface.co/) | Model hosting (`Llama-3.1-8B-Instruct`) |
| [Streamlit](https://streamlit.io/) | Web UI |
| [python-dotenv](https://pypi.org/project/python-dotenv/) | Environment variable management |

---

## 📁 Project Structure

```
lawbuddy/
├── LawBuddy.py           # Main Streamlit app
├── prompt_template.py    # LangChain prompt setup + exports prompt_template.json
├── prompt_template.json  # Serialized system/human prompt templates
├── chat_history.json     # Persistent conversation history (auto-generated)
├── .env                  # Your HuggingFace API token (not committed)
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/HulitoSs/Legal_Advisor_ChatBot.git
cd lawbuddy
```

### 2. Install dependencies
```bash
pip install langchain langchain-huggingface streamlit python-dotenv
```

### 3. Set up your `.env` file
Create a `.env` file in the root directory:
```
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token_here
```
> Get your free token at [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)

### 4. Run the app
```bash
streamlit run LawBuddy.py
```

---

## 💡 How to Use

1. Open the app in your browser (Streamlit will provide a local URL)
2. Paste a legal document excerpt or ask a question about a contract
3. Click **Send**
4. LawBuddy will respond with:
   - Identified problems and risks
   - Suggested fixes and revisions
   - Simple explanations of legal terms
   - Tips to protect your interests
5. Continue the conversation — LawBuddy remembers your chat history

---

## 📌 Example Prompt

```
This agreement shall be governed by the laws of the State of California. 
Either party may terminate this contract with 30 days written notice. 
The contractor shall indemnify the client from any and all claims arising 
from the contractor's performance of services.
```

---

## ⚠️ Disclaimer

LawBuddy is an AI tool for educational purposes only. It is **not a substitute for professional legal advice**. Always consult a qualified attorney before making legal decisions.

---

## 📄 License

MIT License — feel free to use, modify, and distribute.

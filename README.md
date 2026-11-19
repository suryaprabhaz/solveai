# SolveAI — Local AI Code Solver

Solve coding questions directly inside VS Code using your own local [Ollama](https://ollama.ai) LLM. No cloud account required. No data leaves your machine except to your configured Ollama server.

> **Privacy:** SolveAI sends prompts/code only to the Ollama server you configure. No SolveAI cloud server exists. No telemetry. No tracking.

---

## ✨ Features

| Feature | Description |
|---|---|
| **Status-bar Solve button** | Native VS Code status-bar item — `✨ Solve` |
| **Solve with AI** | Generate code from a question or comment |
| **Fix with AI** | Fix broken or buggy code |
| **Explain with AI** | Get a plain-English explanation of selected code |
| **LAN / Wi-Fi support** | Ollama can run on your laptop; VS Code on a lab computer |
| **Model selector** | Pick from installed Ollama models |
| **Privacy-first** | 100% local — no cloud AI required |

---

## Architecture

```
VS Code (lab computer)
        ↓
    SolveAI
        ↓
  Ollama HTTP API  ←── LAN / localhost
        ↓
   Local LLM (qwen3:8b, llama3, etc.)
```

---

## Quick Start

### 1. Install Ollama

Download from [https://ollama.ai](https://ollama.ai) and install it on your laptop.

### 2. Pull a model

```bash
ollama pull qwen3:8b
```

### 3. Start Ollama

```bash
ollama serve
```

### 4. Install SolveAI

Install from the VS Code Marketplace or from a `.vsix` file.

### 5. Configure the server URL

If VS Code runs on a **different computer** than Ollama (LAN use):

1. Open VS Code Settings (`Ctrl+,`)
2. Search for `solveai`
3. Set **Ollama Base URL** to your laptop's IP:

```
http://192.168.1.10:11434
```

---

## Settings

| Setting | Default | Description |
|---|---|---|
| `solveai.ollama.baseUrl` | `http://localhost:11434` | Ollama server URL |
| `solveai.ollama.model` | `qwen3:8b` | Model to use |
| `solveai.ollama.timeout` | `120000` | Timeout in ms (2 min) |
| `solveai.ollama.apiKey` | _(empty)_ | Optional auth header |
| `solveai.ollama.autoApply` | `false` | Auto-apply without preview |

---

## LAN Setup (Lab Computer + Laptop)

```
Lab PC (VS Code + SolveAI)
        192.168.1.20
              ↓
           LAN/Wi-Fi
              ↓
     Laptop (Ollama server)
        192.168.1.10:11434
```

**On your laptop:**

```bash
# Allow Ollama to listen on all interfaces
set OLLAMA_HOST=0.0.0.0
ollama serve
```

**In VS Code on the lab PC:**

```
solveai.ollama.baseUrl = http://192.168.1.10:11434
```

> ⚠️ Only expose Ollama on a trusted local network. Do not expose it to the public internet.

---

## Usage

### Solve a coding question

1. Type your question in the editor:
   ```
   Write a Python program to draw a bar chart for 5 students and their marks.
   ```
2. Click **✨ Solve** in the status bar (or press `Ctrl+Alt+S`)
3. Review the generated answer
4. Click **Apply to Editor** to replace the question with the code

### Fix broken code

1. Select the broken code
2. Right-click → **Fix with AI** (or press `Ctrl+Alt+F`)
3. Review and apply the fix

### Explain code

1. Select the code
2. Right-click → **Explain with AI**
3. Read the explanation in a panel beside the editor

---

## Commands

| Command | Shortcut | Description |
|---|---|---|
| `SolveAI: Solve with AI` | `Ctrl+Alt+S` | Solve selected text or typed question |
| `SolveAI: Fix with AI` | `Ctrl+Alt+F` | Fix selected code |
| `SolveAI: Explain with AI` | — | Explain selected code |
| `SolveAI: Check AI Connection` | — | Verify Ollama is reachable |
| `SolveAI: Select AI Model` | — | Pick from installed Ollama models |
| `SolveAI: Open SolveAI Settings` | — | Open settings panel |

---

## Supported Languages

Python · R · Java · C · C++ · JavaScript · TypeScript · HTML · CSS · SQL · Go · Rust · and more.

---

## Recommended Models

| Model | Size | Good for |
|---|---|---|
| `qwen3:8b` | ~5 GB | General coding, recommended default |
| `qwen3:4b` | ~2.5 GB | Faster, less RAM |
| `codellama` | ~4 GB | Code-focused tasks |
| `llama3` | ~5 GB | General purpose |

---

## Privacy & Security

- **No telemetry.** SolveAI does not phone home.
- **No cloud.** All requests go to your Ollama server only.
- **No accounts.** Nothing to sign up for.
- **API key support.** Optionally secure Ollama with a token via `solveai.ollama.apiKey`.

---

## License

MIT © SolveAI Contributors

# SolveAI — Local AI Code Solver

Solve coding and practical lab questions directly inside VS Code with **instant offline solutions** and local **Ollama** LLM fallback. No cloud account required.

> **Privacy & Offline First:** SolveAI checks its built-in database first for instant offline solutions (0ms latency, no internet, no Ollama needed). For custom questions, it connects to your configured local Ollama server.

---

## ✨ Features

| Feature | Description |
|---|---|
| **Database-First Architecture** | Lab questions solve instantly offline (0ms latency, no Ollama needed) |
| **Shorthand Syntax** | Type `bar plot,py` or `histogram,r` and get instant executable code |
| **Status-bar Solve button** | Native VS Code status-bar item — `✨ Solve` |
| **Solve with AI** | Generate code from questions, comments, or selection (`Ctrl+Alt+S`) |
| **Fix with AI** | Fix broken code with minimal edits (`Ctrl+Alt+F`) |
| **Explain with AI** | Get a plain-English explanation of selected code |
| **LAN / Wi-Fi support** | Connect to Ollama on your laptop from lab computers |
| **100% Local & Privacy-first** | No cloud servers, no telemetry, no tracking |

---

## ⚡ Instant Offline Syllabus Database (No Ollama / No Internet Needed)

SolveAI bundles complete, lab-tested, practical-optimized solutions for the core Python and R visualization syllabus. You can trigger them either normally or via quick shorthand notation:

### Python Main Questions:
1. **Line Chart** — `line chart,py` or `Line Chart in Python`
2. **Bar Chart** — `bar plot,py` or `bar chart,py`
3. **Histogram** — `histogram,py`
4. **Pie Chart** — `pie chart,py`
5. **Scatter Plot** — `scatter plot,py`
6. **Heatmap** — `heatmap,py`
7. **Box Plot** — `box plot,py` or `boxplot,py`

### R Main Questions:
1. **Line Chart** — `line chart,r` or `Line Chart in R`
2. **Bar Chart** — `bar plot,r` or `bar chart,r`
3. **Histogram** — `histogram,r`
4. **Box Plot** — `box plot,r` or `boxplot,r`
5. **Scatter Plot** — `scatter plot,r`
6. **Grouped Bar Chart** — `grouped bar chart,r`
7. **Pie Chart** — `pie chart,r`

---

## 🚀 How to Use

### Method 1: Instant Shorthand
Type in your file:
```text
bar plot,py
```
Click **`✨ Solve`** in the status bar (or press `Ctrl+Alt+S`) → The bar chart code appears immediately!

Or in R:
```text
histogram,r
```
Click **`✨ Solve`** → The R histogram appears immediately!

### Method 2: Custom Question (via Local Ollama)
For any questions not in the offline database:
1. Type or select your question in the editor.
2. Click **`✨ Solve`**.
3. SolveAI connects to your Ollama server and generates the code.

---

## 🌐 LAN Setup (Laptop Ollama + Lab PC)

```text
Lab PC (VS Code + SolveAI)
          ↓
     LAN / Wi-Fi
          ↓
Laptop (Ollama :11434)
```

**On your laptop:**
```bash
set OLLAMA_HOST=0.0.0.0
ollama serve
```

**In VS Code on the lab PC:**
Go to Settings (`Ctrl+,`) -> Search `solveai` -> Set `solveai.ollama.baseUrl`:
```text
http://<YOUR_LAPTOP_IP>:11434
```

---

## ⚙️ Settings

| Setting | Default | Description |
|---|---|---|
| `solveai.ollama.baseUrl` | `http://localhost:11434` | Ollama server URL |
| `solveai.ollama.model` | `qwen3:8b` | Model to use for custom questions |
| `solveai.ollama.timeout` | `120000` | Timeout in ms (2 min) |
| `solveai.ollama.apiKey` | _(empty)_ | Optional auth token |
| `solveai.ollama.autoApply` | `false` | Apply answer without preview prompt |

---

## ⌨️ Keyboard Shortcuts

| Command | Windows/Linux | Mac |
|---|---|---|
| **Solve with AI** | `Ctrl+Alt+S` | `Cmd+Alt+S` |
| **Fix with AI** | `Ctrl+Alt+F` | `Cmd+Alt+F` |

---

## License

MIT © SolveAI Contributors

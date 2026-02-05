# 📚 Offline AI Tutor: Education on 1GB RAM

> **Bridging the Digital Divide:** A fully offline, intelligent tutoring system designed to run on low-cost hardware (Raspberry Pi, old laptops, cheap mobiles) without needing a sustained internet connection.

---

## 🧐 What is this?

Access to quality education often depends on high-speed internet and expensive computers. This project solves that problem by running a **State-of-the-Art Large Language Model (Qwen 2.5 1.5B)** locally on your device.

It uses **4-bit Quantization (GGUF)** to compress the AI brain down to ~1GB, allowing it to act as a Grammar Teacher, Math Tutor, or Science Guide on devices that cost less than $50.

### 🌟 Key Features

* **100% Offline:** No API keys, no cloud servers, no latency.
* **Ultra-Lightweight:** Runs comfortably on systems with **4GB RAM** (and can squeeze into **1GB-2GB** environments).
* **Role-Switching:** Instantly switches personas between Grammar Coach, Math Helper, and Science Tutor.
* **Privacy First:** All data stays on the device.

---

## 🛠️ Tech Stack

* **Language:** Python 3
* **Inference Engine:** [llama-cpp-python](https://github.com/abetlen/llama-cpp-python) (C++ bindings for speed)
* **Model:** Qwen2.5-1.5B-Instruct (GGUF Format)

---

## 🚀 Installation

### 1. Prerequisites

You need Python installed.

```bash
python --version  # Should be 3.8 or higher

```

### 2. Clone the Repository

```bash
git clone https://github.com/yourusername/offline-ai-tutor.git
cd offline-ai-tutor

```

### 3. Install Dependencies

We only need one main library to run the model efficiently.

```bash
pip install llama-cpp-python

```

### 4. Download the "Brain" (The Model)

You need to download the quantized model file (`.gguf`).

1. Go to the [Qwen2.5-1.5B-Instruct-GGUF Hugging Face page](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct-GGUF/tree/main).
2. Download the file named **`qwen2.5-1.5b-instruct-q4_k_m.gguf`** (approx. 1.1 GB).
3. Place this file inside your project folder.

---

## 💻 Usage

Create a file named `tutor.py` (or use the one in this repo) and run it:

```bash
python tutor.py

```

### Code Example

The system dynamically changes its "System Prompt" based on the subject you ask about.

```python
from llama_cpp import Llama
import os

# Initialize the Brain
model_path = "./qwen2.5-1.5b-instruct-q4_k_m.gguf"
llm = Llama(model_path=model_path, n_ctx=2048, verbose=False)

def ask_offline_tutor(student_input, mode="grammar"):
    # ... logic for switching system prompts ...
    return response

# Example Interaction
question = "Why is the sky blue?"
print(ask_offline_tutor(question, mode="Science"))

```

---

## ⚙️ Configuration

You can customize the tutor's behavior by editing the `system_instruction` variables in the code.

| Mode | Behavior |
| --- | --- |
| **Grammar** | Corrects errors and explains the rule in <2 sentences. |
| **Math** | Provides step-by-step logic, not just the final answer. |
| **Science** | Explains concepts simply using analogies. |

To add a new subject (e.g., History), simply add a new `elif mode == "history":` block in the `ask_offline_tutor` function.

---

## 🤝 Contributing

We welcome contributions! Specifically, we are looking for:

1. **Prompt Engineering:** Better system prompts for specific subjects.
2. **UI/UX:** A simple frontend (Streamlit/Gradio) for students.
3. **Optimization:** Settings to run on even lower-end hardware (Raspberry Pi Zero, etc.).

---

## 📜 License

This project is open-source under the **MIT License**.

---

*Built with ❤️ for democratizing education.*

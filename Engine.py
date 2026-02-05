from llama_cpp import Llama
import os

# 1. LOAD THE OFFLINE BRAIN (~1GB RAM)
# context_window=2048 is enough for short lessons.
print("Loading model... (This happens once when App opens)")

model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "qwen2.5-1.5b-instruct-q4_k_m.gguf")

llm = Llama(
    model_path=model_path,
    n_ctx=2048, 
    verbose=False 
)

def ask_offline_tutor(student_input, mode="grammar"):
    """
    This function switches the 'System Persona' based on what the student needs.
    """
    
    # SYSTEM PROMPT: This is the "Secret Sauce" that makes it a Teacher.
    if mode == "grammar":
        system_instruction = (
            "You are a helpful English tutor. "
            "The user will give you a sentence with errors. "
            "1. Correct the sentence. "
            "2. Explain the grammar rule simply. "
            "Keep the explanation under 2 sentences."
        )
    elif mode == "math":
        system_instruction = (
            "You are a math tutor. "
            "Do not just give the answer. "
            "Explain the step-by-step logic to solve the problem."
        )
    else:
        system_instruction = "You are a helpful AI assistant."

    # CONSTRUCT THE CHAT
    messages = [
        {"role": "system", "content": system_instruction},
        {"role": "user", "content": student_input}
    ]

    # RUN INFERENCE (Offline)
    output = llm.create_chat_completion(
        messages=messages,
        temperature=0.2, # Keep it factual/strict
        max_tokens=150   # Keep answers short and fast
    )

    return output["choices"][0]["message"]["content"]

# --- TEST 1: GRAMMAR CORRECTION ---
print("\n--- 📝 Test 1: Grammar Check ---")
student_sentence = "What is newtons 3rd law of motion explain."
print(f"Student: {student_sentence}")

response = ask_offline_tutor(student_sentence,mode="Science")
print(f"AI Tutor: {response}")


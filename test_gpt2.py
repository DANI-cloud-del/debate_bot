# test_gpt2.py

from transformers import pipeline
import torch

def main():
    print("🔍 Checking GPU availability...")
    if torch.cuda.is_available():
        print(f"✅ GPU detected: {torch.cuda.get_device_name(0)}")
    else:
        print("⚠️ GPU not available. Running on CPU.")

    print("\n🚀 Loading GPT-2 model...")
    generator = pipeline("text-generation", model="gpt2")

    prompt = "Explain AI in one sentence."
    print(f"\n🧠 Prompt: {prompt}")
    output = generator(prompt, max_length=50, do_sample=True)

    print("\n📣 Generated Text:")
    print(output[0]["generated_text"])

if __name__ == "__main__":
    main()

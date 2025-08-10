import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Optional: reduce fragmentation
import os
os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen1.5-0.5B")

# Load model in full precision with CPU offloading
model = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen1.5-0.5B",
    device_map="auto",         # Automatically offloads to CPU if needed
    torch_dtype=torch.float16, # Use fp16 to reduce memory footprint
    offload_folder="offload"   # Optional folder for CPU-offloaded weights
)

# Test generation
prompt = "AI is the advancement of technology to create machines capable of"
inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
outputs = model.generate(**inputs, max_new_tokens=50)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))

# qwen_handler.py
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import os

class QwenHandler:
    def __init__(self):
        self.model_name = "Qwen/Qwen1.5-0.5B"
        try:
            # Configure for low memory usage
            os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"
            
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            self.model = AutoModelForCausalLM.from_pretrained(
                self.model_name,
                device_map="auto",
                torch_dtype=torch.float16,
                low_cpu_mem_usage=True,
                attn_implementation="sdpa"
            )
            print("Qwen model loaded with memory optimizations")
        except Exception as e:
            print(f"Failed to load Qwen: {e}")
            raise

    def get_response(self, prompt: str) -> str:
        try:
            inputs = self.tokenizer(
                prompt,
                return_tensors="pt",
                truncation=True,
                max_length=256  # Reduced from 512
            ).to(self.model.device)
            
            with torch.no_grad():  # Disable gradient calculation
                outputs = self.model.generate(
                    **inputs,
                    max_new_tokens=80,  # Reduced from 100
                    temperature=0.7,
                    do_sample=True,
                    top_p=0.9,
                    pad_token_id=self.tokenizer.eos_token_id
                )
            return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        except Exception as e:
            print(f"Generation error: {str(e)[:100]}...")
            return ""
# refinement_handler.py
from transformers import pipeline
import re

class RefinementHandler:
    def __init__(self):
        # Force CPU-only operation
        self.classifier = pipeline(
            "zero-shot-classification",
            model="facebook/bart-large-mnli",
            device="cpu"  # Explicitly use CPU
        )
        
    def clean_response(self, text):
        """Simplified cleaning process"""
        if not text:
            return ""
            
        # Basic instruction removal
        text = re.sub(r'(please|use|provide|argument|rebuttal|position|sentences?):?', '', 
                     text, flags=re.IGNORECASE)
        
        # Take first 3 sentences
        sentences = [s.strip() for s in text.split('.') if s.strip()]
        return '. '.join(sentences[:3]) + '.' if sentences else ""
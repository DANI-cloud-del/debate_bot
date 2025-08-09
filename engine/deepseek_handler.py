import requests
import os
from typing import Optional

class DeepSeekHandler:
    BASE_URL = "https://api.deepseek.com/v1/chat/completions"
    
    def __init__(self):
        self.api_key = os.getenv("DEEPSEEK_API_KEY")
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def get_response(self, prompt: str) -> Optional[str]:
        """Get response from DeepSeek API"""
        payload = {
            "model": "deepseek-chat",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7,
            "max_tokens": 200
        }
        
        try:
            response = requests.post(self.BASE_URL, json=payload, headers=self.headers)
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]
        except Exception as e:
            print(f"DeepSeek API Error: {e}")
            return None
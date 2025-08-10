import random
from abc import ABC, abstractmethod
from typing import Optional
from engine.qwen_handler import QwenHandler
from engine.refinement_handler import RefinementHandler
import re

class DebateBot(ABC):
    @abstractmethod
    def make_argument(self, topic: str) -> str:
        """Generate an initial argument about the topic"""
        pass

    @abstractmethod
    def rebut(self, opponent_argument: str) -> str:
        """Generate a rebuttal to the opponent's argument"""
        pass
    def __init__(self, name: str, stance: str):
        self.name = name
        self.stance = stance
        try:
            self.generator = QwenHandler()
        except Exception as e:
            print(f"Warning: Could not load Qwen ({e}). Using CPU fallback...")
            self.generator = None
        self.refiner = RefinementHandler()
        self.fallback_responses = {
            "Pro": ["Evidence supports this...", "Studies show...", "Logically..."],
            "Con": ["Human cost...", "Emotionally...", "Morally wrong..."]
        }

    def _clean_response(self, response: str) -> str:
        try:
            # Basic cleaning first
            clean = self.refiner.clean_response(response)
            if clean and len(clean.split()) > 5:  # Minimum viable response
                return clean
            return random.choice(self.fallback_responses[self.stance])
        except Exception:
            return random.choice(self.fallback_responses[self.stance])

    def get_ai_response(self, prompt: str) -> str:
        """Main method to get and clean AI responses"""
        if self.generator is None:
            return random.choice(self.fallback_responses[self.stance])
        
        raw_response = self.generator.get_response(prompt)
        return self._clean_response(raw_response)
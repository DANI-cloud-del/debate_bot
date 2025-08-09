from abc import ABC, abstractmethod
from typing import Optional  # Add this import
from engine.deepseek_handler import DeepSeekHandler

class DebateBot(ABC):
    def __init__(self, name: str, stance: str):
        self.name = name
        self.stance = stance
        self.ai = DeepSeekHandler()

    @abstractmethod
    def make_argument(self, topic: str) -> str:
        """Generate an initial argument about the topic"""
        pass

    @abstractmethod
    def rebut(self, opponent_argument: str) -> str:
        """Generate a rebuttal to the opponent's argument"""
        pass

    def get_ai_response(self, prompt: str) -> Optional[str]:
        """Helper method to get AI response"""
        return self.ai.get_response(prompt)
from bots.base_bot import DebateBot
import random

class RandomBot(DebateBot):
    def __init__(self, name, stance):
        super().__init__(name, stance)
        self.responses = [
            "That's an interesting perspective, but consider this...",
            "From a different angle, one might say...",
            "Random studies suggest that...",
            "I'm not entirely convinced because..."
        ]
    
    def make_argument(self, topic):
        return f"{random.choice(self.responses)} Regarding '{topic}', {random.choice(['it seems', 'I contend', 'the data shows'])} we should {self.stance}."

    def rebut(self, opponent_argument):
        return f"{random.choice(self.responses)} {random.choice(['Furthermore,', 'However,', 'On the contrary,'])} {opponent_argument.lower()}"
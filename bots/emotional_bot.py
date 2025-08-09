from bots.base_bot import DebateBot

class EmotionalBot(DebateBot):
    def make_argument(self, topic):
        return f"I believe that '{topic}' touches the very core of human dignity. We must act with compassion."

    def rebut(self, opponent_argument):
        return f"Your argument ignores the emotional impact this issue has on real people."

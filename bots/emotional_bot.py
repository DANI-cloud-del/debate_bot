# emotional_bot.py
from bots.base_bot import DebateBot

class EmotionalBot(DebateBot):
    def make_argument(self, topic):
        prompt = (
            f"Express one emotional perspective about '{topic}' from the {self.stance} viewpoint. "
            "Focus on human impact. Format: '[Emotional appeal]. This matters because [reason].' "
            "Example for Con UBI: 'People need meaningful work for dignity. Handouts destroy self-worth.'"
        )
        return self.get_ai_response(prompt)

    def rebut(self, opponent_argument):
        prompt = (
            f"Respond emotionally to: '{opponent_argument}'. "
            f"Highlight one human aspect overlooked from {self.stance} perspective. "
            "Format: '[Emotional response]. We must consider [human factor].' "
            "Example: 'Cold statistics ignore real suffering. We must consider children going hungry.'"
        )
        return self.get_ai_response(prompt)
from bots.base_bot import DebateBot

class LogicalBot(DebateBot):
    def make_argument(self, topic):
        prompt = (
            f"As a logical debater taking the {self.stance} position on '{topic}', "
            "provide a 2-sentence argument with factual reasoning. "
            "Use bullet points if needed."
        )
        return self.get_ai_response(prompt) or "Default logical argument..."
    
    def rebut(self, opponent_argument):
        prompt = (
            f"Critically analyze this argument: '{opponent_argument}'. "
            "Point out logical fallacies or missing evidence in 1-2 sentences."
        )
        return self.get_ai_response(prompt) or "Default rebuttal..."
# logical_bot.py
from bots.base_bot import DebateBot

class LogicalBot(DebateBot):
    def make_argument(self, topic):
        prompt = (
            f"Generate exactly one factual argument about '{topic}' from the {self.stance} perspective. "
            "Use this format: '[Fact]. Therefore, [conclusion].' "
            "Example for Pro UBI: 'Alaska's Permanent Fund shows basic income reduces poverty. Therefore, UBI works.'"
        )
        return self.get_ai_response(prompt)
    
    def rebut(self, opponent_argument):
        prompt = (
            f"Identify one logical flaw in: '{opponent_argument}'. "
            f"Counter with {self.stance} position. "
            "Format: '[Flaw]. Instead, [counter-point].' "
            "Example: 'Overlooks inflation risks. Instead, studies show UBI stimulates local economies.'"
        )
        return self.get_ai_response(prompt)
from bots.base_bot import DebateBot

class LogicalBot(DebateBot):
    def make_argument(self, topic):
        return f"As a logical thinker, I argue that '{topic}' is best approached through empirical evidence and cost-benefit analysis."

    def rebut(self, opponent_argument):
        return f"Your argument lacks empirical grounding. Can you cite data to support that?"

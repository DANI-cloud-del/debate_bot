class DebateBot:
    def __init__(self, name, stance):
        self.name = name
        self.stance = stance

    def make_argument(self, topic):
        raise NotImplementedError

    def rebut(self, opponent_argument):
        raise NotImplementedError

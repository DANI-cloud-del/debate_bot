from rich import print
from engine.scorer import score_argument

class DebateManager:
    def __init__(self, bot1, bot2, topic):
        self.bot1 = bot1
        self.bot2 = bot2
        self.topic = topic

    def run_debate(self):
        print(f"\n[bold cyan]Topic:[/bold cyan] {self.topic}")
        arg1 = self.bot1.make_argument(self.topic)
        arg2 = self.bot2.make_argument(self.topic)
        print(f"\n[bold]{self.bot1.name}:[/bold] {arg1}")
        print(f"[bold]{self.bot2.name}:[/bold] {arg2}")

        rebut1 = self.bot1.rebut(arg2)
        rebut2 = self.bot2.rebut(arg1)
        print(f"\n[italic]{self.bot1.name} rebuttal:[/italic] {rebut1}")
        print(f"[italic]{self.bot2.name} rebuttal:[/italic] {rebut2}")

        score1 = score_argument(arg1, rebut1)
        score2 = score_argument(arg2, rebut2)
        winner = self.bot1.name if score1 > score2 else self.bot2.name
        print(f"\n[green]Winner:[/green] {winner}")

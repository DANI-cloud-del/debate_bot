from rich import print
from rich.panel import Panel
from typing import List, Dict, Any
from engine.scorer import score_argument
from bots.base_bot import DebateBot  # Add this import

class DebateManager:
    def __init__(self, bot1: DebateBot, bot2: DebateBot, topic: str, rounds: int = 3):
        self.bot1 = bot1
        self.bot2 = bot2
        self.topic = topic
        self.rounds = rounds
        self.scores = {bot1.name: 0, bot2.name: 0}

    def display_header(self) -> None:
        print(Panel.fit(
            f"[bold]Debate Topic:[/bold] {self.topic}\n"
            f"[bold]{self.bot1.name}[/bold] ({self.bot1.stance}) vs "
            f"[bold]{self.bot2.name}[/bold] ({self.bot2.stance})",
            title="[cyan]Debate Session[/cyan]"
        ))

    def run_round(self, round_num: int) -> None:
        print(Panel.fit(f"[bold]Round {round_num}[/bold]", style="blue"))
        
        # Initial arguments
        arg1 = self.bot1.make_argument(self.topic)
        arg2 = self.bot2.make_argument(self.topic)
        
        print(f"\n[bold green]{self.bot1.name}:[/bold green] {arg1}")
        print(f"[bold yellow]{self.bot2.name}:[/bold yellow] {arg2}")
        
        # Rebuttals
        rebut1 = self.bot1.rebut(arg2)
        rebut2 = self.bot2.rebut(arg1)
        
        print(f"\n[italic green]{self.bot1.name} rebuttal:[/italic green] {rebut1}")
        print(f"[italic yellow]{self.bot2.name} rebuttal:[/italic yellow] {rebut2}")
        
        # Scoring
        score1 = score_argument(arg1, rebut1)
        score2 = score_argument(arg2, rebut2)
        
        self.scores[self.bot1.name] += score1
        self.scores[self.bot2.name] += score2
        
        print(f"\n[dim]Scores this round: {self.bot1.name}={score1:.1f}, {self.bot2.name}={score2:.1f}[/dim]")

    def run_debate(self) -> None:
        self.display_header()
        
        for round_num in range(1, self.rounds + 1):
            self.run_round(round_num)
        
        self.display_final_results()

    def display_final_results(self) -> None:
        print(Panel.fit(
            f"[bold]Final Scores:[/bold]\n"
            f"{self.bot1.name}: {self.scores[self.bot1.name]:.1f}\n"
            f"{self.bot2.name}: {self.scores[self.bot2.name]:.1f}\n\n"
            f"[bold]Winner:[/bold] {max(self.scores, key=self.scores.get)}",
            title="[green]Debate Results[/green]"
        ))
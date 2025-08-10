from rich import print
from rich.panel import Panel
from typing import List, Dict, Any
from engine.scorer import score_argument
from bots.base_bot import DebateBot  # Add this import
from bots.random_bot import RandomBot  # Ensure RandomBot is imported

class DebateManager:
    def __init__(self, bot1: DebateBot, bot2: DebateBot, topic: str, rounds: int = 3):
        self.bot1 = bot1
        self.bot2 = bot2
        self.topic = topic
        self.rounds = rounds
        self.scores = {bot1.name: 0, bot2.name: 0}

    def display_header(self):
        title = f"[bold]Debate Topic:[/bold] {self.topic}"
        if isinstance(self.bot1, RandomBot) or isinstance(self.bot2, RandomBot):
            title += "\n[dim](Using simplified mode due to hardware limits)[/dim]"
        print(Panel.fit(title))

    # debate_manager.py (partial update)
    def run_round(self, round_num):
        print(Panel.fit(f"[bold]Round {round_num}[/bold]", style="blue"))
        
        # Initial arguments (strictly limited)
        arg1 = self._limit_response(self.bot1.make_argument(self.topic))
        arg2 = self._limit_response(self.bot2.make_argument(self.topic))
        
        print(f"\n[bold green]{self.bot1.name}:[/bold green] {arg1}")
        print(f"[bold yellow]{self.bot2.name}:[/bold yellow] {arg2}")
        
        # Rebuttals (strictly limited)
        rebut1 = self._limit_response(self.bot1.rebut(arg2))
        rebut2 = self._limit_response(self.bot2.rebut(arg1))
        
        print(f"\n[italic green]{self.bot1.name} rebuttal:[/italic green] {rebut1}")
        print(f"[italic yellow]{self.bot2.name} rebuttal:[/italic yellow] {rebut2}")
        
        # Scoring
        score1 = score_argument(arg1, rebut1)
        score2 = score_argument(arg2, rebut2)
        
        self.scores[self.bot1.name] += score1
        self.scores[self.bot2.name] += score2
        
        print(f"\n[dim]Scores this round: {self.bot1.name}={score1:.1f}, {self.bot2.name}={score2:.1f}[/dim]")

    def _limit_response(self, text, max_sentences=3, max_words=50):
        sentences = [s.strip() for s in text.split('.') if s.strip()]
        limited = '. '.join(sentences[:max_sentences]) + ('.' if sentences else '')
        words = limited.split()
        if len(words) > max_words:
            return ' '.join(words[:max_words]) + '...'
        return limited

    def _trim_argument(self, text, max_words=50):
        words = text.split()
        if len(words) > max_words:
            return " ".join(words[:max_words]) + "..."
        return text

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
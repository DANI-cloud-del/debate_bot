import json
import random
import argparse
from typing import List, Dict
from bots.base_bot import DebateBot  # Add this import
from bots.logical_bot import LogicalBot
from bots.emotional_bot import EmotionalBot
from bots.random_bot import RandomBot
from engine.debate_manager import DebateManager
from dotenv import load_dotenv
load_dotenv()  # Loads the API key from .env

def load_topics(file_path: str = "data/topics.json") -> List[Dict]:
    with open(file_path) as f:
        return json.load(f)["topics"]

def select_topic(topics: List[Dict]) -> Dict:
    print("\nAvailable Debate Topics:")
    for i, topic in enumerate(topics, 1):
        print(f"{i}. {topic['title']} ({' vs '.join(topic['stances'])})")
    
    while True:
        try:
            choice = int(input("\nSelect a topic (number): ")) - 1
            if 0 <= choice < len(topics):
                return topics[choice]
            print("Invalid selection. Try again.")
        except ValueError:
            print("Please enter a number.")

def create_bot(bot_type: str, name: str, stance: str) -> DebateBot:
    if bot_type.lower() == "logical":
        return LogicalBot(name, stance)
    elif bot_type.lower() == "emotional":
        return EmotionalBot(name, stance)
    elif bot_type.lower() == "random":
        return RandomBot(name, stance)
    else:
        raise ValueError(f"Unknown bot type: {bot_type}")

def main():
    parser = argparse.ArgumentParser(description="Run a debate between AI bots.")
    parser.add_argument("--rounds", type=int, default=3, help="Number of debate rounds")
    args = parser.parse_args()

    topics = load_topics()
    selected_topic = select_topic(topics)
    
    # For simplicity, we'll auto-assign stances
    bot1 = create_bot("logical", "LogicMaster", selected_topic["stances"][0])
    bot2 = create_bot("emotional", "HeartHero", selected_topic["stances"][1])
    
    manager = DebateManager(bot1, bot2, selected_topic["title"], rounds=args.rounds)
    manager.run_debate()

if __name__ == "__main__":
    main()
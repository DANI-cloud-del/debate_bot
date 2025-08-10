# main.py
import json
import argparse
import random
from typing import List, Dict
import torch
try:
    from pynvml import nvmlInit, nvmlDeviceGetHandle, nvmlDeviceGetMemoryInfo
except ImportError:
    # Fallback if NVML not available
    pass
from bots.base_bot import DebateBot
from bots.logical_bot import LogicalBot
from bots.emotional_bot import EmotionalBot
from bots.random_bot import RandomBot
from engine.debate_manager import DebateManager
from dotenv import load_dotenv

load_dotenv()

def load_topics(file_path: str = "data/topics.json") -> List[Dict]:
    try:
        with open(file_path) as f:
            return json.load(f)["topics"]
    except FileNotFoundError:
        return [
            {"title": "Should AI be granted rights?", "stances": ["Pro", "Con"]},
            {"title": "Is universal basic income viable?", "stances": ["Pro", "Con"]}
        ]

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

def create_bot(bot_type: str, name: str, stance: str, force_cpu: bool = False) -> DebateBot:
    if force_cpu and bot_type.lower() in ['logical', 'emotional']:
        print(f"DEBUG: Falling back to RandomBot for {name}")
        return RandomBot(name, stance)
        
    try:
        if bot_type.lower() == "logical":
            return LogicalBot(name, stance)
        elif bot_type.lower() == "emotional":
            return EmotionalBot(name, stance)
        elif bot_type.lower() == "random":
            return RandomBot(name, stance)
    except Exception as e:
        print(f"Warning: Could not create {bot_type} bot ({e}). Using RandomBot.")
        return RandomBot(name, stance)

def main():
    # Detect hardware capability
    force_cpu = True
    try:
        nvmlInit()
        if torch.cuda.is_available():
            gpu_mem = nvmlDeviceGetMemoryInfo(nvmlDeviceGetHandle(0)).total
            force_cpu = gpu_mem < 4 * 1024**3  # Less than 4GB
    except:
        force_cpu = True
    
    if force_cpu:
        print("DEBUG: Using CPU-compatible mode")

    parser = argparse.ArgumentParser(description="Run a debate between AI bots.")
    parser.add_argument("--rounds", type=int, default=3)
    parser.add_argument("--bot1", type=str, default="logical")
    parser.add_argument("--bot2", type=str, default="emotional")
    args = parser.parse_args()

    topics = load_topics()
    selected_topic = select_topic(topics)
    
    bot1 = create_bot(args.bot1, f"{args.bot1.capitalize()}Master", 
                     selected_topic["stances"][0], force_cpu)
    bot2 = create_bot(args.bot2, f"{args.bot2.capitalize()}Champion",
                     selected_topic["stances"][1], force_cpu)
    
    manager = DebateManager(bot1, bot2, selected_topic["title"], rounds=args.rounds)
    manager.run_debate()

if __name__ == "__main__":
    main()
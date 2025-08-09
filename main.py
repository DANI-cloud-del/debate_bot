import json
from bots.logical_bot import LogicalBot
from bots.emotional_bot import EmotionalBot
from engine.debate_manager import DebateManager

with open("data/topics.json") as f:
    topics = json.load(f)["topics"]

topic = topics[0]["title"]
bot1 = LogicalBot("LogicMaster", "Pro")
bot2 = EmotionalBot("HeartHero", "Con")

manager = DebateManager(bot1, bot2, topic)
manager.run_debate()

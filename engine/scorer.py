# scorer.py
def score_argument(argument: str, rebuttal: str) -> float:
    """Score an argument based on various factors"""
    # Length scores (normalized)
    arg_len = min(len(argument.split()), 100)  # Max 100 words
    reb_len = min(len(rebuttal.split()), 80)   # Max 80 words
    length_score = (arg_len * 0.3 + reb_len * 0.4) / 100
    
    # Quality indicators
    quality_score = 0.3
    quality_score += 0.1 if any(word in argument.lower() for word in ['because', 'therefore', 'thus', 'study', 'research']) else 0
    quality_score += 0.1 if any(word in rebuttal.lower() for word in ['however', 'but', 'although', 'flaw', 'counter']) else 0
    quality_score += 0.1 if '?' in argument else 0  # Reward questions
    
    # Emotional content detection (for emotional bot)
    emotional_words = ['feel', 'human', 'compassion', 'rights', 'dignity', 'suffer']
    quality_score += 0.1 if any(word in argument.lower() for word in emotional_words) else 0
    
    return (length_score + quality_score) * 100
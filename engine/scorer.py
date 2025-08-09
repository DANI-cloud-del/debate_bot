def score_argument(argument: str, rebuttal: str) -> float:
    """Score an argument based on various factors"""
    length_score = min(len(argument) / 100, 1.0) * 0.3
    rebuttal_score = min(len(rebuttal) / 80, 1.0) * 0.4
    
    # Quality indicators
    quality_score = 0.3
    quality_score += 0.1 if '?' in argument else 0
    quality_score += 0.1 if any(word in argument.lower() for word in ['because', 'therefore', 'thus']) else 0
    quality_score += 0.1 if any(word in rebuttal.lower() for word in ['however', 'but', 'although']) else 0
    
    return (length_score + rebuttal_score + quality_score) * 100
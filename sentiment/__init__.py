"""stock-sentiment — a dependency-free Chinese financial sentiment scorer.

Lexicon-based scoring of news / headlines, aggregated per stock into a
bullish / bearish signal. Ships with a sample dataset; runs offline.
"""

from .lexicon import POSITIVE, NEGATIVE, NEGATORS, INTENSIFIERS, score_text
from .analyzer import NewsItem, SentimentAnalyzer
from .data import SAMPLE_NEWS

__all__ = [
    "POSITIVE", "NEGATIVE", "NEGATORS", "INTENSIFIERS", "score_text",
    "NewsItem", "SentimentAnalyzer", "SAMPLE_NEWS",
]

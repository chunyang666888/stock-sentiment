"""Sentiment aggregation and signaling per stock."""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List

from .lexicon import score_text


@dataclass
class NewsItem:
    symbol: str
    text: str
    timestamp: datetime = None


class SentimentAnalyzer:
    """Score news, aggregate per stock, and emit a trading signal."""

    def __init__(self, bullish_threshold: float = 1.0, bearish_threshold: float = -1.0) -> None:
        self.bullish_threshold = bullish_threshold
        self.bearish_threshold = bearish_threshold

    def score_text(self, text: str) -> float:
        return score_text(text)

    def score_news(self, items: List[NewsItem]):
        """Return ``[(item, score), ...]``."""
        return [(it, score_text(it.text)) for it in items]

    def aggregate(self, items: List[NewsItem]) -> Dict[str, float]:
        """Sum sentiment scores per symbol."""
        totals: Dict[str, float] = defaultdict(float)
        for it in items:
            totals[it.symbol] += score_text(it.text)
        return dict(totals)

    def signal(self, score: float) -> str:
        if score >= self.bullish_threshold:
            return "bullish"
        if score <= self.bearish_threshold:
            return "bearish"
        return "neutral"

    def rank(self, items: List[NewsItem]) -> List[tuple]:
        """Return ``(symbol, score, signal)`` sorted most-bullish first."""
        agg = self.aggregate(items)
        return sorted(
            ((sym, sc, self.signal(sc)) for sym, sc in agg.items()),
            key=lambda x: x[1],
            reverse=True,
        )

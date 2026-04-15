"""Demo: score a few A-share news snippets and rank by sentiment."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from datetime import datetime

from sentiment import SentimentAnalyzer, SAMPLE_NEWS, NewsItem

# SAMPLE_NEWS is already a list of NewsItem objects.
items = SAMPLE_NEWS

analyzer = SentimentAnalyzer()
print("Per-stock aggregated sentiment (most bullish first):")
for symbol, score, signal in analyzer.rank(items):
    print(f"  {symbol:>8}  score={score:+.1f}  {signal}")

print("\nSample text scoring:")
for text in ["业绩超预期，机构大幅增持", "涉嫌财务造假，遭监管立案调查"]:
    print(f"  {analyzer.score_text(text):+.1f}  {text}")

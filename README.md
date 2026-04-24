![smoke](https://github.com/chunyang666888/stock-sentiment/actions/workflows/ci.yml/badge.svg)

# stock-sentiment

**Dependency-free Chinese financial sentiment scorer** — lexicon-based scoring, per-stock aggregation, and bullish/bearish signal generation. Built for quant / trading-system interviews to show NLP + markets domain knowledge without heavy frameworks.

## Features

- 📖 **Lexicon-based scorer** — positive / negative financial phrase dictionary with negation handling (`sentiment/lexicon.py`).
- 📰 **Per-stock aggregation** — sum sentiment across a stock's news flow (`SentimentAnalyzer.aggregate`).
- 📈 **Trading signal** — `bullish` / `bearish` / `neutral` thresholds (`SentimentAnalyzer.signal`).
- 🏆 **Ranking** — rank names by net sentiment (`SentimentAnalyzer.rank`).
- 🧪 **Zero runtime deps** — pure Python stdlib; `numpy` only used in the demo.

## Install

```bash
pip install -r requirements.txt
```

## Quick start

```python
from datetime import datetime
from sentiment import SentimentAnalyzer, NewsItem

items = [
    NewsItem("600519", "业绩超预期，机构上调目标价", datetime(2026, 1, 1)),
    NewsItem("600519", "监管出手整顿，情绪偏谨慎", datetime(2026, 1, 2)),
]
analyzer = SentimentAnalyzer()
print(analyzer.rank(items))
# [('600519', 1.0, 'bullish')]
```

Or run the bundled demo:

```bash
python examples/sentiment_demo.py
```

## Project layout

```
stock-sentiment/
├── sentiment/
│   ├── lexicon.py      # financial phrase dictionary + score_text()
│   ├── analyzer.py     # SentimentAnalyzer: aggregate / signal / rank
│   └── data.py         # sample A-share news dataset
├── examples/
│   └── sentiment_demo.py
└── requirements.txt
```

## Tech signals for recruiters

- Domain-aware **NLP** applied to a quant problem (not a generic model).
- Clean **separation of concerns** (lexicon / analyzer / data).
- **Reproducible, dependency-light** — runs anywhere Python 3.10+ exists.

> Part of a量化 / 交易系统 engineer portfolio. See the profile README for the full project list.

## License

MIT — free for personal and commercial use.

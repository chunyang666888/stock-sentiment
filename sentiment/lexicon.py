"""Chinese financial sentiment lexicon and a substring-based scorer.

No分词 (segmentation) dependency: we scan for known words and inspect a small
window before each hit for negators / intensifiers. Good enough for a fast,
explainable first-pass signal; swap in jieba + a richer lexicon for production.
"""
from __future__ import annotations

from typing import Dict, List

POSITIVE: set = {
    "利好", "上涨", "涨停", "盈利", "增长", "超预期", "增持", "回购",
    "中标", "突破", "新高", "扩产", "签约", "获批", "业绩", "分红",
    "看好", "拉升", "强势", "扭亏",
}
NEGATIVE: set = {
    "利空", "下跌", "跌停", "亏损", "下滑", "不及预期", "减持", "暴雷",
    "退市", "破位", "新低", "停产", "违约", "处罚", "警告", "看空",
    "抛售", "弱势", "风险", "下调",
}
NEGATORS: set = {"不", "未", "无", "没有", "否认", "尚未"}
INTENSIFIERS: Dict[str, float] = {
    "大幅": 1.5, "明显": 1.3, "重大": 1.4, "显著": 1.3,
    "轻微": 0.6, "小幅": 0.7, "略有": 0.7,
}


def _has_negator_before(text: str, idx: int) -> bool:
    window = text[max(0, idx - 2):idx]
    return any(neg in window for neg in NEGATORS)


def _intensifier_mult(text: str, idx: int) -> float:
    window = text[max(0, idx - 3):idx]
    for word, mult in INTENSIFIERS.items():
        if word in window:
            return mult
    return 1.0


def score_text(text: str) -> float:
    """Return a signed sentiment score (positive = bullish)."""
    text = str(text)
    score = 0.0
    for word in POSITIVE:
        idx = text.find(word)
        while idx != -1:
            sign = -1.0 if _has_negator_before(text, idx) else 1.0
            score += sign * _intensifier_mult(text, idx)
            idx = text.find(word, idx + 1)
    for word in NEGATIVE:
        idx = text.find(word)
        while idx != -1:
            sign = 1.0 if _has_negator_before(text, idx) else -1.0
            score += sign * _intensifier_mult(text, idx)
            idx = text.find(word, idx + 1)
    return score


def tokenize_hits(text: str) -> List[str]:
    """Return the matched lexicon words (for explainability)."""
    text = str(text)
    hits = [w for w in POSITIVE | NEGATIVE if w in text]
    return hits

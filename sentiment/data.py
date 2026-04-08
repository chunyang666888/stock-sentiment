"""Sample news dataset (illustrative only, not real events)."""
from __future__ import annotations

from .analyzer import NewsItem

SAMPLE_NEWS = [
    NewsItem("600519", "贵州茅台前三季度业绩增长超预期，机构看好"),
    NewsItem("600519", "茅台拟大手笔回购股份，释放利好信号"),
    NewsItem("300750", "宁德时代海外订单中标，营收突破新高"),
    NewsItem("300750", "宁德时代扩产计划获批，强势拉升"),
    NewsItem("601318", "中国平安盈利稳健增长，分红提升"),
    NewsItem("600276", "恒瑞医药新药获批，但短期业绩下滑"),
    NewsItem("600276", "恒瑞医药被下调评级，机构看空"),
    NewsItem("601012", "隆基绿能业绩不及预期，股价跌停风险"),
    NewsItem("601012", "隆基绿能财务状况警告，存在暴雷风险"),
    NewsItem("000001", "平安银行未出现亏损，拨备覆盖率稳定"),
    NewsItem("002594", "比亚迪销量大幅增长，突破历史新高"),
]

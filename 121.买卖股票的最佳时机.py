#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
# 前i天的最大收益 = max{前i-1天的最大收益，第i天的价格-前i-1天中的最小价格}

# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = int(1e4)
        maxprofit = 0
        for price in prices:
            if price > minprice:
                cur_prof = price - minprice
                if cur_prof > maxprofit:
                    maxprofit = cur_prof
            else:
                minprice = price
        return maxprofit


# @lc code=end

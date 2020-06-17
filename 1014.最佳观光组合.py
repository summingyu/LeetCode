#
# @lc app=leetcode.cn id=1014 lang=python3
#
# [1014] 最佳观光组合
#

# @lc code=start
class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        ans = 0
        pre_max = A[0] + 0
        for j in range(1, len(A)):
            ans = max(ans, pre_max + A[j] - j)
            pre_max = max(pre_max, A[j] + j)
        return ans
        
# @lc code=end


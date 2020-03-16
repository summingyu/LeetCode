#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums,target):
        num2index = {}
        for i,j in enumerate(nums):
            if j in num2index:
                return [num2index.get(j),i]
            num2index[target - j] = i
# @lc code=end


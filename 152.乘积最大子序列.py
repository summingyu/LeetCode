#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子序列
#
# https://leetcode-cn.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (37.44%)
# Likes:    562
# Dislikes: 0
# Total Accepted:    64.5K
# Total Submissions: 164.5K
# Testcase Example:  '[2,3,-2,4]'
#
# 给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
# 
# 
# 
# 示例 1:
# 
# 输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
# 
# 
# 示例 2:
# 
# 输入: [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
# 
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0 :
            return 0
        dpMax = nums[0]
        dpMin = nums[0]
        res = nums[0]
        for i in range(1,len(nums)):
            preMax = dpMax
            dpMax = max(dpMin * nums[i], max(dpMax * nums[i],nums[i]))
            dpMin = min(dpMin * nums[i], min(preMax * nums[i],nums[i]))
            res = max(res, dpMax)
        return res
# @lc code=end


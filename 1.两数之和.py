#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

'''
将目标值与当前值的差值,以及当前值对应的位置,存放到字典中.
如果在后续匹配中,能在字典中找到对应的值,则表示匹配成功
'''


# @lc code=start
class Solution:
    def twoSum(self, nums, target):
        num2index = {}
        for i, j in enumerate(nums):
            if j in num2index:
                return [num2index.get(j), i]
            num2index[target - j] = i
# @lc code=end


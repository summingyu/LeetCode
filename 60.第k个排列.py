#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 第k个排列
#
# https://leetcode-cn.com/problems/permutation-sequence/description/
#
# algorithms
# Medium (48.35%)
# Likes:    199
# Dislikes: 0
# Total Accepted:    26.6K
# Total Submissions: 54.7K
# Testcase Example:  '3\n3'
#
# 给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。
# 
# 按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
# 
# 
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# 
# 
# 给定 n 和 k，返回第 k 个排列。
# 
# 说明：
# 
# 
# 给定 n 的范围是 [1, 9]。
# 给定 k 的范围是[1,  n!]。
# 
# 
# 示例 1:
# 
# 输入: n = 3, k = 3
# 输出: "213"
# 
# 
# 示例 2:
# 
# 输入: n = 4, k = 9
# 输出: "2314"
#[ 1 2 3 4 ]
# index:1, push:2, [1 3 4] k=3
# index:1, push:3, [1,4] k= 1
# index:1, 
# 
# 
#

# @lc code=start
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nList = [str(i) for i in range(1,n+1)]
        numStr = ""
        for i in range(n-1,-1,-1):
            # 计算本次步数间隔
            jc = math.factorial(i)
            index = k // jc 
            k %= jc
            # 如果正好除尽,则还是属于上一个区间
            index = index if k else index-1
            numStr += nList[index]
            nList.remove(nList[index])
        return numStr
# @lc code=end


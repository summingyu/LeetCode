#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#
# https://leetcode-cn.com/problems/powx-n/description/
#
# algorithms
# Medium (34.09%)
# Likes:    290
# Dislikes: 0
# Total Accepted:    62.5K
# Total Submissions: 182.4K
# Testcase Example:  '2.00000\n10'
#
# 实现 pow(x, n) ，即计算 x 的 n 次幂函数。
# 
# 示例 1:
# 
# 输入: 2.00000, 10
# 输出: 1024.00000
# 
# 
# 示例 2:
# 
# 输入: 2.10000, 3
# 输出: 9.26100
# 
# 
# 示例 3:
# 
# 输入: 2.00000, -2
# 输出: 0.25000
# 解释: 2^-2 = 1/2^2 = 1/4 = 0.25
# 
# 说明:
# 
# 
# -100.0 < x < 100.0
# n 是 32 位有符号整数，其数值范围是 [−2^31, 2^31 − 1] 。
# 
# 
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        #最简单,调用函数
        #return x**n
        # 暴力法,最费时
        '''
        if n < 0:
            n = -n
            x = 1/x
        ans = 1
        for i in range(n):
            ans *= x
        return ans
        '''
        # 可以使用分治的方法,注意考虑n为负数的情况
        if n == 0:
            return 1
        if n < 0:
            return 1/self.myPow(x,-n)
        midN = n // 2
        y = self.myPow(x*x,midN)
        if n % 2 == 0 :
            return y
        else:
            return y*x
        
# @lc code=end


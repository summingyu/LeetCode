#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] 最长回文串
#
# https://leetcode-cn.com/problems/longest-palindrome/description/
#
# algorithms
# Easy (52.12%)
# Likes:    119
# Dislikes: 0
# Total Accepted:    21.2K
# Total Submissions: 39.9K
# Testcase Example:  '"abccccdd"'
#
# 给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
# 
# 在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。
# 
# 注意:
# 假设字符串的长度不会超过 1010。
# 
# 示例 1: 
# 
# 
# 输入:
# "abccccdd"
# 
# 输出:
# 7
# 
# 解释:
# 我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
# 
# 
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        '''
        # 所以的偶数都可以作为回文,所有的大于2的奇数n,都可以提供n-1个长度的回文,如果最后还存在多          余的数,只能再使长度+1
        
        flag = 0
        ans = 0
        for i in set(s):
            iLen = s.count(i)
            if iLen % 2 == 0:
                ans += iLen
            else:
                flag = 1
                ans += iLen -1
        ans += flag
        return ans
        '''

        '''
        # 可以使用collections自带的counter()函数减少调用s.count的次数
        '''
        ans = 0
        sCount = collections.Counter(s)
        for v in sCount.values():
            ans += v // 2 * 2
        return ans if ans == len(s) else ans + 1
        
# @lc code=end


#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
# https://leetcode-cn.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (41.07%)
# Likes:    1445
# Dislikes: 0
# Total Accepted:    228.9K
# Total Submissions: 556.2K
# Testcase Example:  '"()"'
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
# 
# 有效字符串需满足：
# 
# 
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 
# 
# 注意空字符串可被认为是有效字符串。
# 
# 示例 1:
# 
# 输入: "()"
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: "()[]{}"
# 输出: true
# 
# 
# 示例 3:
# 
# 输入: "(]"
# 输出: false
# 
# 
# 示例 4:
# 
# 输入: "([)]"
# 输出: false
# 
# 
# 示例 5:
# 
# 输入: "{[]}"
# 输出: true
# 
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        checkMap = {")":"(","]":"[","}":"{"}
        needPush = {v for v in checkMap.values()}
        aStack = []
        if not s:
            return True
        for i in s:
            if i in needPush:
                aStack.append(i)
            elif checkMap.get(i):
                try:
                    if checkMap.get(i) != aStack.pop():
                        return False
                except Exception as e:
                    return False
        return aStack == []

# @lc code=end


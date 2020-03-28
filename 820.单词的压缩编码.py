#
# @lc app=leetcode.cn id=820 lang=python3
#
# [820] 单词的压缩编码
#
# https://leetcode-cn.com/problems/short-encoding-of-words/description/
#
# algorithms
# Medium (40.47%)
# Likes:    100
# Dislikes: 0
# Total Accepted:    19.9K
# Total Submissions: 43.9K
# Testcase Example:  '["time", "me", "bell"]'
#
# 给定一个单词列表，我们将这个列表编码成一个索引字符串 S 与一个索引列表 A。
# 
# 例如，如果这个列表是 ["time", "me", "bell"]，我们就可以将其表示为 S = "time#bell#" 和 indexes = [0,
# 2, 5]。
# 
# 对于每一个索引，我们可以通过从字符串 S 中索引的位置开始读取字符串，直到 "#" 结束，来恢复我们之前的单词列表。
# 
# 那么成功对给定单词列表进行编码的最小字符串长度是多少呢？
# 
# 
# 
# 示例：
# 
# 输入: words = ["time", "me", "bell"]
# 输出: 10
# 说明: S = "time#bell#" ， indexes = [0, 2, 5] 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= words.length <= 2000
# 1 <= words[i].length <= 7
# 每个单词都是小写字母 。
# 
# 
#

# @lc code=start
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        # 如果一个单词属于另一个单词的后缀,则不计算长度
        # 反转之后,排序,如果当前单词完全属于下一个单词,那么就丢弃这个单词
        words = [word[::-1] for word in words]
        words.sort()
        ans = 0
        lenth = len(words)
        for i ,word in enumerate(words):
            if i < lenth-1 and words[i+1].startswith(word):
                continue
            ans += len(word)+1
        return ans
        
# @lc code=end


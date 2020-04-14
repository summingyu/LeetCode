#
# @lc app=leetcode.cn id=445 lang=python3
#
# [445] 两数相加 II
#
# https://leetcode-cn.com/problems/add-two-numbers-ii/description/
#
# algorithms
# Medium (54.45%)
# Likes:    168
# Dislikes: 0
# Total Accepted:    25.5K
# Total Submissions: 45K
# Testcase Example:  '[7,2,4,3]\n[5,6,4]'
#
# 给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。
# 
# 你可以假设除了数字 0 之外，这两个数字都不会以零开头。
# 
# 
# 
# 进阶：
# 
# 如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。
# 
# 
# 
# 示例：
# 
# 输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 8 -> 0 -> 7
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = []
        stack2 = []
        res = ListNode(-1)
        p = l1
        while p:
            stack1.append(p.val)
            p = p.next
        p = l2
        while p:
            stack2.append(p.val)
            p = p.next
        carry = 0
        while stack1 or stack2 or carry:
            tmp1, tmp2 = 0, 0
            if stack1:
                tmp1 = stack1.pop()
            if stack2:
                tmp2 = stack2.pop()
            carry, mod = divmod(tmp1 + tmp2 + carry, 10)
            node = ListNode(mod)
            node.next = res.next
            res.next = node
        return res.next
        
# @lc code=end


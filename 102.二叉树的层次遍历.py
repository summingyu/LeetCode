#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层次遍历
#
# https://leetcode-cn.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (61.08%)
# Likes:    428
# Dislikes: 0
# Total Accepted:    98.5K
# Total Submissions: 160.5K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
# 
# 
# 
# 示例：
# 二叉树：[3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 返回其层次遍历结果：
# 
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
# ]
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        #使用BFS进行层级扫描
        '''
        if not root:
            return []
        ans = []
        # 可以使用双端队列
        # queue = collections.deque()
        queue = [root]

        # 养成判断是否访问过的习惯
        # visited = set()
        while queue:
            level_size = len(queue)
            tmp_level = []

            for _ in range(level_size):
                node = queue.pop(0)
                #去重的判断
                #if node in visited:
                #    continue
                #visited.add(node)
                tmp_level.append(node.val)
                if node.left : queue.append(node.left)
                if node.right: queue.append(node.right)
            ans.append(tmp_level)
        return ans
        '''
        # 也可以使用DFS进行层级扫描
        if not root:
            return []
        self.ans = []
        self._DFS(0,root)
        return self.ans

    def _DFS(self, level: int, node: TreeNode):
        if not node : return
        # 如果level+1比ans的length长,说明是一个新的层级,需要创建
        if len(self.ans) < level + 1:
            self.ans.append([])
        self.ans[level].append(node.val)
        self._DFS(level+1,node.left)
        self._DFS(level+1,node.right)
# @lc code=end


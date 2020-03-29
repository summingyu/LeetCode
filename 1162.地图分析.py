#
# @lc app=leetcode.cn id=1162 lang=python3
#
# [1162] 地图分析
#
# https://leetcode-cn.com/problems/as-far-from-land-as-possible/description/
#
# algorithms
# Medium (38.44%)
# Likes:    52
# Dislikes: 0
# Total Accepted:    11.2K
# Total Submissions: 26.7K
# Testcase Example:  '[[1,0,1],[0,0,0],[1,0,1]]'
#
# 你现在手里有一份大小为 N x N 的『地图』（网格） grid，上面的每个『区域』（单元格）都用 0 和 1 标记好了。其中 0 代表海洋，1
# 代表陆地，你知道距离陆地区域最远的海洋区域是是哪一个吗？请返回该海洋区域到离它最近的陆地区域的距离。
# 
# 我们这里说的距离是『曼哈顿距离』（ Manhattan Distance）：(x0, y0) 和 (x1, y1) 这两个区域之间的距离是 |x0 -
# x1| + |y0 - y1| 。
# 
# 如果我们的地图上只有陆地或者海洋，请返回 -1。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：[[1,0,1],[0,0,0],[1,0,1]]
# 输出：2
# 解释： 
# 海洋区域 (1, 1) 和所有陆地区域之间的距离都达到最大，最大距离为 2。
# 
# 
# 示例 2：
# 
# 
# 
# 输入：[[1,0,0],[0,0,0],[0,0,0]]
# 输出：4
# 解释： 
# 海洋区域 (2, 2) 和所有陆地区域之间的距离都达到最大，最大距离为 4。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= grid.length == grid[0].length <= 100
# grid[i][j] 不是 0 就是 1
# 
# 
#

# @lc code=start
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        # 使用BFS进行搜索
        # 1. 先找出所有的陆地节点,压入栈中
        N = len(grid)
        queue = []
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    queue.append((r,c))
        # 如果队列为空或者队列等于N*N则说明全是海洋或者全是大陆
        if len(queue) % (N*N) == 0:
            return -1
        # 队列为空则退出循环
        depLenght = -1
        while queue:
            depLenght += 1
            n = len(queue)
            for _ in range(n):
                # 弹出最早的一个节点
                r,c = queue.pop(0)
                # 向上遍历
                if r-1 >= 0 and grid[r-1][c] == 0:
                    grid[r-1][c] = -1
                    queue.append((r-1,c))
                # 向下遍历
                if r+1 <N and grid[r+1][c] == 0:
                    grid[r+1][c] = -1
                    queue.append((r+1,c))
                # 向左遍历
                if c-1 >=0 and grid[r][c-1] == 0:
                    grid[r][c-1] = -1
                    queue.append((r,c-1))
                # 向右遍历
                if c+1 < N and grid[r][c+1] == 0:
                    grid[r][c+1] = -1
                    queue.append((r,c+1))
        return depLenght
        
# @lc code=end


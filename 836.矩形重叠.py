#
# @lc app=leetcode.cn id=836 lang=python3
#
# [836] 矩形重叠
#
# https://leetcode-cn.com/problems/rectangle-overlap/description/
#
# algorithms
# Easy (45.81%)
# Likes:    62
# Dislikes: 0
# Total Accepted:    8.2K
# Total Submissions: 17.1K
# Testcase Example:  '[0,0,2,2]\n[1,1,3,3]'
#
# 矩形以列表 [x1, y1, x2, y2] 的形式表示，其中 (x1, y1) 为左下角的坐标，(x2, y2) 是右上角的坐标。
# 
# 如果相交的面积为正，则称两矩形重叠。需要明确的是，只在角或边接触的两个矩形不构成重叠。
# 
# 给出两个矩形，判断它们是否重叠并返回结果。
# 
# 示例 1：
# 
# 输入：rec1 = [0,0,2,2], rec2 = [1,1,3,3]
# 输出：true
# 
# 
# 示例 2：
# 
# 输入：rec1 = [0,0,1,1], rec2 = [1,0,2,1]
# 输出：false
# 
# 
# 说明：
# 
# 
# 两个矩形 rec1 和 rec2 都以含有四个整数的列表的形式给出。
# 矩形中的所有坐标都处于 -10^9 和 10^9 之间。
# 
# 
#

# @lc code=start
class Solution:
    '''
    相交就表示两个维度的区间分别相交,
    最大的开始端小于最小的结束端则相交
    '''
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x_overlap = max(rec1[0],rec2[0]) < min(rec1[2], rec2[2])
        y_overlap = max(rec1[1], rec2[1]) < min(rec1[3],rec2[3])
        return x_overlap and y_overlap
# @lc code=end


/*
 * @lc app=leetcode.cn id=1302 lang=golang
 *
 * [1302] 层数最深叶子节点的和
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func deepestLeavesSum(root *TreeNode) (sum int) {
	maxLevel := 0
	var dfs func(root *TreeNode, level int)
	dfs = func(root *TreeNode, level int) {
		if root == nil {
			return
		}
		if root.Left == nil && root.Right == nil {
			if level > maxLevel {
				maxLevel = level
				sum = root.Val
			} else if level == maxLevel {
				sum += root.Val
			}
		} else {
			if root.Left != nil {
				dfs(root.Left, level+1)
			}
			if root.Right != nil {
				dfs(root.Right, level+1)
			}
		}
	}
	dfs(root, 0)
	return
}

// @lc code=end


/*
 * @lc app=leetcode.cn id=856 lang=golang
 *
 * [856] 括号的分数
 */

// @lc code=start
func scoreOfParentheses(s string) int {
	n := len(s)
	if n == 2 {
		return 1
	}
	for i, bal := 0, 0; ; i++ {
		if s[i] == '(' {
			bal++
		} else {
			bal--
			if bal == 0 {
				if i == n-1 {
					return 2 * scoreOfParentheses(s[1:n-1])
				}
				return scoreOfParentheses(s[:i+1]) + scoreOfParentheses(s[i+1:])
			}
		}
	}
}

// @lc code=end

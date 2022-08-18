/*
 * @lc app=leetcode.cn id=1224 lang=golang
 *
 * [1224] 最大相等频率
 */

// @lc code=start
func maxEqualFreq(nums []int) int {
	freq, count := map[int]int{}, map[int]int{}
	maxFreq, ans := 0, 0
	for i, num := range nums {
		if count[num] > 0 {
			freq[count[num]]--
		}
		count[num]++
		maxFreq = max(maxFreq, count[num])
		freq[count[num]]++
		if maxFreq == 1 ||
			freq[maxFreq]*maxFreq+freq[maxFreq-1]*(maxFreq-1) == i+1 && freq[maxFreq] == 1 ||
			freq[maxFreq]*maxFreq+1 == i+1 && freq[1] == 1 {
			ans = max(ans, i+1)
		}
	}
	return ans

}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

// @lc code=end


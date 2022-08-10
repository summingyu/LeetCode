/*
 * @lc app=leetcode.cn id=17 lang=golang
 *
 * [17] 电话号码的字母组合
 */

// @lc code=start
var num2char []string = []string{
	"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz",
}

var ret []string = []string{}

func letterCombinations(digits string) []string {
	ret = ret[:0]
	if len(digits) == 0 {
		return ret
	}
	backtrace(digits, 0, "")
	return ret
}

func backtrace(digits string, index int, com string) {
	if len(digits) == index {
		ret = append(ret, com)
	} else {
		chList := num2char[digits[index]-'2']
		for i := 0; i < len(chList); i++ {
			backtrace(digits, index+1, com+string(chList[i]))
		}
	}
}

// @lc code=end


/*
 * @lc app=leetcode.cn id=1656 lang=golang
 *
 * [1656] 设计有序流
 */

// @lc code=start
type OrderedStream struct {
	stream []string
	ptr    int
}

func Constructor(n int) OrderedStream {
	return OrderedStream{
		stream: make([]string, n+1), ptr: 1}
}

func (this *OrderedStream) Insert(idKey int, value string) []string {
	this.stream[idKey] = value
	if idKey != this.ptr {
		return []string{}
	}
	start := this.ptr
	for this.ptr < len(this.stream) && this.stream[this.ptr] != "" {
		this.ptr++
	}
	return this.stream[start:this.ptr]

}

/**
 * Your OrderedStream object will be instantiated and called as such:
 * obj := Constructor(n);
 * param_1 := obj.Insert(idKey,value);
 */
// @lc code=end


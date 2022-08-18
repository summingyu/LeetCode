/*
 * @lc app=leetcode.cn id=641 lang=golang
 *
 * [641] 设计循环双端队列
 */

// @lc code=start
type MyCircularDeque struct {
	front, rear, qLen int
	elements          []int
}

func Constructor(k int) MyCircularDeque {
	return MyCircularDeque{
		qLen:     k + 1,
		elements: make([]int, k+1)}
}

func (q *MyCircularDeque) InsertFront(value int) bool {
	if q.IsFull() {
		return false
	}
	q.front = (q.front - 1 + q.qLen) % q.qLen
	q.elements[q.front] = value
	return true
}

func (q *MyCircularDeque) InsertLast(value int) bool {
	if q.IsFull() {
		return false
	}
	q.elements[q.rear] = value
	q.rear = (q.rear + 1) % q.qLen
	return true

}

func (q *MyCircularDeque) DeleteFront() bool {
	if q.IsEmpty() {
		return false
	}
	q.front = (q.front + 1) % q.qLen
	return true
}

func (q *MyCircularDeque) DeleteLast() bool {
	if q.IsEmpty() {
		return false
	}
	q.rear = (q.rear - 1 + q.qLen) % q.qLen
	return true
}

func (q *MyCircularDeque) GetFront() int {
	if q.IsEmpty() {
		return -1
	}
	return q.elements[q.front]

}

func (q *MyCircularDeque) GetRear() int {
	if q.IsEmpty() {
		return -1
	}
	return q.elements[(q.rear-1+q.qLen)%q.qLen]
}

func (q *MyCircularDeque) IsEmpty() bool {
	return q.rear == q.front

}

func (q *MyCircularDeque) IsFull() bool {
	return (q.rear+1)%q.qLen == q.front
}

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * obj := Constructor(k);
 * param_1 := obj.InsertFront(value);
 * param_2 := obj.InsertLast(value);
 * param_3 := obj.DeleteFront();
 * param_4 := obj.DeleteLast();
 * param_5 := obj.GetFront();
 * param_6 := obj.GetRear();
 * param_7 := obj.IsEmpty();
 * param_8 := obj.IsFull();
 */
// @lc code=end


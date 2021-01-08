# 链表反转

# 输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）
'''
输入：head = [1,3,2]
输出：[2,3,1]

0 <= 链表长度 <= 10000
'''

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res[::-1]
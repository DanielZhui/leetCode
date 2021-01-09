# 链表反转

# 输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）
'''
输入：head = [1,3,2]
输出：[2,3,1]

0 <= 链表长度 <= 10000
'''

'''
解题思路：

方法一：反转
获取链表值并添加到列表中，反转获取到的列表

方法二：递归
使用递归 + 列表相加，将链表中的元素最前面的元素放在列表的最后

方法三：堆栈
堆栈的特点是先进先出，可以现将链表中的元素添加到堆栈中在从堆栈中取出
'''

# 方法一
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res[::-1]

# 方法二
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        # 当 head 为 None 时返回 []
        if not head: return []
        # 注意：这里返回的结果是列表，需要列表相加，使用递归将最前面的元素放在最后
        return self.reversePrint(head.next) + [head.val]

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        res = []
        while stack:
            # pop 移除 stack 中最后一个元素
            res.append(stack.pop())
        return res
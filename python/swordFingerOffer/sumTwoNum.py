# 两数只和
'''
给出两个非空的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以

'''

'''
解题方法：

方法一：
链表转 list
1. 将两个链表转为 list
2. 将链表中的数据转为 str
3. 获取list中的数据相加得到两数只和，再将结果反转
4. 将获取到的结果构建链表的形式返回

方法二：
链表循环
'''


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_list = self.conversion_list(l1)
        l2_list = self.conversion_list(l2)
        s_l1 = self.list_num_to_string(l1_list)
        s_l2 = self.list_num_to_string(l2_list)
        res_s = sum([int(s_l1), int(s_l2)])
        res = []
        for s in str(res_s):
            res.append(int(s))
        res.reverse()
        return self.list2link(res)

    # 将链表转换为 list
    def conversion_list(self, l1: ListNode) -> list:
        if not l1: return []
        return self.conversion_list(l1.next) + [l1.val]

    # 将链表中的数据转换为 string
    def list_num_to_string(self, ls) -> str:
        s = ''
        for key in ls:
            s += str(key)
        return s

    # 构建单链表
    def list2link(self, list_) -> ListNode:
        head = ListNode(list_[0])
        p = head
        for i in range(1, len(list_)):
            p.next = ListNode(list_[i])
            p = p.next
        return head


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # head 为头节点 node 为当前节点
        head = node = ListNode()
        # 是否进位和每一步求和的结果
        s = 0
        # 使用 while 循环逐个取出 l1 l2 的数据加上 s
        while l1 or l2 or s:
            # 注意判断节点是否为空直接 if ListNode
            s += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            # 构建当前节点的下一个结点
            node.next = ListNode(s % 10)
            # 当前节点赋值为下一个结点
            node = node.next
            # 取 s 的模（eg: 19 // 10 = 1, 9 // 10 = 0）
            s //= 10
            # l1 l2 向下个节点移动
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        # head 的下一个节点
        return head.next
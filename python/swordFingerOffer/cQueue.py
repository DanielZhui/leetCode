'''
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead,
分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

示例 1：
输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]

示例 2：
输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]

提示：
1 <= values <= 10000
最多会对 appendTail、deleteHead 进行 10000 次调用
'''

class CQueue:

    def __init__(self):
        self.lst_one = []
        self.lst_two = []

    # lst_one 当作栈使用、尾部添加直接 append 即可
    def appendTail(self, value: int) -> None:
        self.lst_one.append(value)


    def deleteHead(self) -> int:
        # 如果 lst_one 中有数据将取出 lst_one 中第一个元素否则返回 0
        return self.lst_one.pop(0) if self.lst_one else -1


class CQueue:

    def __init__(self):
        self.lst_one, self.lst_two = [],[]

    def appendTail(self, value: int) -> None:
        self.lst_one.append(value)

    def deleteHead(self) -> int:
        # 因为此时 lst_two 中均为 lst_one 倒序元素，如果此时 lst_two 还有元素直接返回即可
        if self.lst_two: return self.lst_two.pop()
        if not self.lst_one: return -1
        # 如果 lst_one 中还有元素使用 pop 将 lst_one 中元素倒序加入到 lst_two 中
        while self.lst_one:
            self.lst_two.append(self.lst_one.pop())
        return self.lst_two.pop()
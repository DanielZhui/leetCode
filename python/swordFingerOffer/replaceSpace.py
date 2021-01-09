'''
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

示例 1：
输入：s = "We are happy."
输出："We%20are%20happy."
 

限制：
0 <= s 的长度 <= 10000
'''

'''
解题思路：
方法一：
字符串切割 + 列表合并成字符串

方法二：
使用字符串替换（replace 方法）

方法三：
不使用 string 携带的方法，使用列表求解,使用列表

方法四：
双指针
'''

# 方法一
class Solution:
    def replaceSpace(self, s: str) -> str:
        s_lst = s.split(' ')
        return '%20'.join(s_lst)

# 方法二
class Solution:
    def replaceSpace(self, s: str) -> str:
        return s.replace(' ', '%20')

# 方法三
class Solution:
    def replaceSpace(self, s: str) -> str:
        res = []
        for key in s:
            res.append('%20') if key == ' ' else res.append(key)
        return ''.join(res)

'''
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

示例:
s = "abaccdeff"
返回 "b"

s = ""
返回 " "
 
限制：
0 <= s 的长度 <= 50000

方法一：
散列表（字典）：用字典存储每个字符串出现的次数，存储完字符串出现次数后循环字典里的数据，当获取到 value 为1则返回 key，如果没有则返回空字符串
'''

class Solution:
    def firstUniqChar(self, s: str) -> str:
        s_dict = {}
        for key in s:
            if not s_dict.get(key):
                s_dict[key] = 1
            else:
                s_dict[key] += 1
        for key,value in s_dict.items():
            if value == 1:
                return key
        return ' '

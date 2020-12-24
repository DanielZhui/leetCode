'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。

示例 2：
输入: "cbbd"
输出: "bb"
'''

'''
解题思路：
1. 什么是回文串：字符串顺序和倒序完全相同，eg：'abcba'、'abcddcba'
'''
'''
# 错误实例：回文串理解错误、以为首位和末尾相同即可
注意点：
1. 当字符串长度小于等于1时返回本身
2. 如果字符串中无回文串则返回字符串第一个字符
3. 连续相同的字符串
'''


'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_dict = {}
        s_length_list = []
        s_len = len(s)
        if s_len <= 1:
            return s
        for index in range(s_len):
            # 这里需要排除 0 的情况, 字典中使用 get 方法获取元素时拿不到返回 None
            if s_dict.get(s[index]) == None:
                s_dict[s[index]] = index
            else:
                # 需要判断是否为回文字符串，如果这里还会出现重复的需要更新长度
                s_index = s_dict[s[index]]
                s_length = index - s_index
                if s[s_index:index +1] == s[s_index:index +1][::-1]:
                    s_dict[s[index]] = index
                    s_length_list.append({"length": s_length, "index": '{}-{}'.format(s_index, index)})
        max_length = 0
        index = ''
        if not len(s_length_list):
            return s[0]
        print(s_length_list)
        for item in s_length_list:
            if max_length < item['length']:
                max_length = item['length']
                index = item['index']
        index_list = index.split('-')
        first_index = int(index_list[0])
        secend_index = int(index_list[1]) + 1
        print(first_index, secend_index)
        return s[first_index:secend_index]

solution = Solution()
# s = 'abcddcba'
result = solution.longestPalindrome("aabaa")
print(result)
'''

# 方法一：暴力破解（这种方式回超时）
class Solution:
    def longestPalindrome(self, s):
        if len(s) < 2:
            return s
        s_len = len(s)
        max_len = 0
        palindrome = ''
        for i in range(s_len):
            for j in range(i+1, s_len):
                is_palindrome =True
                # 判断是否为回文字符串
                for k in range(i, int((i+j)/2) + 1):
                    if s[k] != s[j - k + i]:
                        is_palindrome = False
                        break
                # 如果是回文字符串则且但前最大长度大于 max_len, 重置 max_len
                if is_palindrome and max_len < (j - i + 1):
                    max_len = (j - i +1)
                    palindrome = s[i: j+1]
        # 当字符串中无满足的回文子串时，返回字符串第一个字符
        if not palindrome:
            palindrome = s[0]
        return palindrome

solution = Solution()
s = 'abcddcba'
result = solution.longestPalindrome("cbbd")
print(result)
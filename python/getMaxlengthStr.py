# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
'''
示例
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
'''

# 滑动窗口问题（题解答案)
s = 'cbaababcd'
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        no_repeated_set = set()
        # 当前长度
        current_len = 0
        # 最大长度
        max_len = 0
        # 指针位置
        pointer = 0
        for key in s:
            current_len += 1
            # 当 set 中存在相同的字符串则一直从左删除直到 set 中无重复字符串
            while key in no_repeated_set:
                no_repeated_set.remove(s[pointer])
                # 指针记录当前位置
                pointer += 1
                # 指针往右移动一个当前长度减一
                current_len -= 1
            # 如果当前长度大雨最大长度，将当前长度赋值给最大长度
            if max_len < current_len: max_len = current_len
            # set 中添加当前字符串
            no_repeated_set.add(key)
        return max_len

solution = Solution()
result = solution.lengthOfLongestSubstring(s)
print(result)
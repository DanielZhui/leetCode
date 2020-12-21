'''
题目要求
找出数组中重复的数字。

在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。
数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：
输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3

限制：
2 <= n <= 100000
'''

'''
解题思路：
每一道 leetCode 都是一道超难的阅读理解

理解题目：
1. 列表长度在 2 <= len <= 100000
2. 如果列表中无重复的数字返回 -1
3. 最终返回第一个重复的数字即本题答案
'''

class Solution:
    def findRepeatNumber(self, nums) -> int:
        # 使用三列表作为解题思路，以列表 nums 作为 key，重复次数作为 value
        num_dict = {}
        for i in nums:
            if num_dict.get(i):
                num_dict[i] += 1
            else:
                num_dict[i] = 1
        # 查找出最先重复的数字
        for key, value in num_dict.items():
            if 1 < value:
                return key
        return -1

solution = Solution()
result = solution.findRepeatNumber([2, 1])
print(result)
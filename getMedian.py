'''
给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的中位数。

进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？

 

示例 1：
输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2

示例 2：
输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5

示例 3：
输入：nums1 = [0,0], nums2 = [0,0]
输出：0.00000

示例 4：
输入：nums1 = [], nums2 = [1]
输出：1.00000

示例 5：
输入：nums1 = [2], nums2 = []
输出：2.00000
'''

'''
题目解析：
1. 如果两个列表中有相同的元素需要除重吗？ （无需合并）
2. 合并后的列表需要排序吗？ （需要排序）
3. leetCode 中提供 python 以及 python3编译环境、python 环境默认是 2.x 版本
'''

'''
解题思路：
解析该题目化很大一部分时间去推测题目的意思，如列表相加相同项是否需要合并、排序，在解析过程中使用取巧的方式，使用 python 内置函数
sorted 对合并后的列表进行排序。

优化：列表排序这部分需要手写算法实现
'''


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num_res = nums1 + nums2
        # 这里直接使用 set 会导致列表乱序
        set_num = sorted(num_res)
        median_num_index = len(set_num) // 2
        # 判断两个列表合并长度是奇数还是偶数
        if len(set_num) == 0:
            return 0
        if len(set_num) % 2 == 0:
            return (set_num[median_num_index] + set_num[median_num_index - 1]) / 2
        else:
            return set_num[median_num_index]

solution = Solution()
nums1 = [1,3]
nums2 = [1,2]

'''
[0,0,0,0,0]
[-1,0,0,0,0,0,1]
'''
result = solution.findMedianSortedArrays(nums1, nums2)
print(result)

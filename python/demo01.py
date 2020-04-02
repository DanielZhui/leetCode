'''
# 4.1
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''

def getSum(tagert, nums):
    num_dict = {}
    for index, num in enumerate(nums):
        another_num = tagert - num
        if another_num in num_dict:
            return [num_dict[another_num], index]
        if num not in num_dict:
            num_dict[num] = index
    return None

target = 9
nums = [2, 7, 11, 15]
res = getSum(target, nums)
print(res)

# key: 求两数只和, 目标数字减去其中一个就能找到另外一个数,如果另外一个数存在 dict 中,则返回该数字对应的索引
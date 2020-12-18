# 找不同
'''
给定两个字符串 s 和 t，它们只包含小写字母。
字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
请找出在 t 中被添加的字母。
'''

s = 'famale'
t = 'fameale'

class Solution(object):
    def get_difference(self, s, t):
        # 获取长、短字符串
        if len(s) < len(t):
            max_str, min_str = t, s
        else:
            max_str, min_str = s, t
        res_str = max_str
        for key in max_str:
            if key in min_str:
                # 最后返回的字符串中除去重复的字符串
                res_str = self.remove(res_str, key)
                # 短字符串中也需除去重复的字符串
                min_str = self.remove(min_str, key)
        return res_str

    @staticmethod
    def remove(origin_str, move_str):
        # 每次除去一个匹配的字符串，防止重复字符串多删
        str_list = origin_str.split(move_str, 1)
        res_str = ''.join(str_list)
        return res_str

solution = Solution()
res = solution.get_difference(s, t)
print(res)
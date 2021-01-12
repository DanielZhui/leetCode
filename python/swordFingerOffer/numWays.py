'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：
输入：n = 2
输出：2

示例 2：
输入：n = 7
输出：21

示例 3：
输入：n = 0
输出：1
提示：

0 <= n <= 100
'''

'''
解题思路：
0   1
1   1
2   2
3   3
4   5
5   8
6   12
7   21
理解 n = (n-1) + (n-2)

参考：https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/solution/mian-shi-ti-10-i-fei-bo-na-qi-shu-lie-dong-tai-gui/

方法一：
递归：leetCode 运行超时，本机运行也会卡死，这种方法占用太多内存会导致内存溢出

方法二：
动态规划
该问题我们想要明白 fn = f(n-1) + f(n-2)（1.我们可以通过数据规律得到，2.想要求解 fn 那在青蛙最后一步(f(n-1))只能是跳一步或者跳两步(f(n-2)), 则 fn = f(n-1) + f(n-2)）
'''

# 方法一：
class Solution:
    def numWays(self, n: int) -> int:
        if n <= 1:
            return 1

        no_repeated_dict = {}
        if (no_repeated_dict.get(n)):
            return no_repeated_dict.get(n)

        first_num = (self.numWays(n-1)) % 1000000007
        no_repeated_dict[n-1] = first_num
        secend_num = (self.numWays(n-2)) % 1000000007
        no_repeated_dict[n-2] = secend_num
        return (first_num + secend_num) % 1000000007


# 动态规划（通过 fn = f(n-1) + f(n-2) 构建）
class Solution:
    def numWays(self, n: int) -> int:
        first_num = 0
        secend_num = 1
        while n:
            res = first_num + secend_num
            first_num = (secend_num) % 1000000007
            secend_num = (res) % 1000000007
            n -= 1
        return secend_num
class CongruenceToolKit:
    # ░░░░░░░░░░ LeetCode 1015 - 可被 K 整除的最小整数 (Smallest Integer Divisible by K) ░░░░░░░░░░
    def smallestRepunitDivByK(self, k: int) -> int:
        """
        余数迭代 + 鸽巢原理
            1. 若 k 含因子 2 或 5，则不存在答案，返回 -1
            2. 维护 r = (10*r + 1) % k 表示全1数对 k 的余数
            3. 每步长度 +1；一旦 r == 0，当前长度即为答案
            4. 余数范围 [0, k-1]，在 ≤k 次迭代内必出现 0（经步骤1保证不会陷入非零循环）
        """
        if k % 2 == 0 or k % 5 == 0:
            return -1
        r = 1 % k
        length = 1
        while r != 0:
            r = (r * 10 + 1) % k
            length += 1
        return length

class BitMaskManager:
    # ░░░░░░░░░░░░░░ LeetCode 2154 —— Keep Multiplying Found Values by Two（保留当前倍数） ░░░░░░░░░░░░░░
    def findFinalValue(self, nums: List[int], original: int) -> int:
        """
        位运算思路（bitmask + “最小缺失 2 的幂”）：
            - 如果某个元素 x 可以写成：x = original * 2^k
              那么令 k, r = divmod(x, original)，当 r == 0 且 k 是 2 的幂时，
              k 的二进制中只有一位是 1，可以直接把 k 作为一个 bit 掉到 mask 上：mask |= k

            - 如此一来，mask 的二进制中所有被置 1 的位，刚好对应出现过的 2^k
              比如：出现了 original * 1, original * 2, original * 8，则
                    mask = 1 | 2 | 8 = 0b1011

            - 利用经典位运算技巧：
                    (mask + 1) & (~mask)
              可以得到“从低位开始的第一个 0 对应的 2 的幂值”，
              也就是最小缺失的 2^k
        """
        mask = 0
        for x in nums:
            k, r = divmod(x, original)
            if r == 0 and k & (k - 1) == 0:
                mask |= k
        mask = (mask + 1) & (~mask)
        return original * mask

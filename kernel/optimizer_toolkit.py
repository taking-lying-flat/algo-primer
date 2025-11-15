class SubsequenceDPToolkit:
    # ░░░░░░░░░░░ LeetCode 300 —— 最长递增子序列 ░░░░░░░░░░░
    @staticmethod
    def lengthOfLIS(nums: List[int]) -> int:
        """
        贪心 + 二分查找求 LIS 长度
             1. tails[i] 表示长度为 i+1 的递增子序列的最小末尾值
             2. 遍历每个数字，二分查找其在 tails 中的位置
             3. 如果大于所有元素，追加到末尾（子序列变长）
             4. 否则更新对应位置（保持该长度的最小末尾）
             5. tails 长度即为 LIS 长度
        """
        tails: List[int] = []
        for x in nums:
            idx = bisect_left(tails, x)
            if idx == len(tails):
                tails.append(x)
            else:
                tails[idx] = x
        return len(tails)

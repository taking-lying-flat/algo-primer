class GroupedLoopSuite:
    # ░░░░░░░░░░░ LeetCode 228 —— 汇总区间 ░░░░░░░░░░░
    def summaryRanges(self, nums: List[int]) -> List[str]:
        def render(i: int, j: int) -> str:
            return str(nums[i]) if i == j else f"{nums[i]}->{nums[j]}"

        n = len(nums)
        ans = []
        i = 0
        while i < n:
            start = i
            i += 1
            while i < n and nums[i] == nums[i - 1] + 1:
                i += 1
            ans.append(render(start, i - 1))
        return ans


    # ░░░░░░░░░░░ LeetCode 1513 —— 仅含 1 的子串数 ░░░░░░░░░░░
    def numSub(self, s: str) -> int:
        ans = i = 0
        while i < len(s):
            if s[i] == '0':
                i += 1
                continue
            start = i
            i += 1
            while i < len(s) and s[i] == '1':
                i += 1
            ans += (i - start + 1) * (i - start) // 2
        return ans % 1_000_000_007
        
  
    # ░░░░░░░░░░░ LeetCode 2760 —— 带阈值的最长偶奇子数组 ░░░░░░░░░░░
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        ans = i = 0
        while i < n:
            if nums[i] > threshold or nums[i] % 2:
                i += 1  # 直接跳过
                continue
            start = i  # 记录这一组的开始位置
            i += 1  # 开始位置已经满足要求，从下一个位置开始判断
            while i < n and nums[i] <= threshold and nums[i] % 2 != nums[i - 1] % 2:
                i += 1
            # 从 start 到 i-1 是满足题目要求的（并且无法再延长的）子数组
            ans = max(ans, i - start)
        return ans

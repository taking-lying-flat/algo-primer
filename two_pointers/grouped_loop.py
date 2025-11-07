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


    # ░░░░░░░░░░░ LeetCode 2953 —— 统计完全子字符串 ░░░░░░░░░░░
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        def render(s: str) -> int:
            res = 0
            for m in range(1, 27):
                if m * k > len(s):
                    break
                cnt = defaultdict(int)
                for right, c in enumerate(s):
                    cnt[c] += 1
                    left = right - m * k + 1
                    if left >= 0:
                        res += all(x == 0 or x == k for x in cnt.values())
                        cnt[s[left]] -= 1
            return res
        
        ans = i = 0
        n = len(word)
        while i < n:
            start = i
            i += 1
            while i < n and abs(ord(word[i]) - ord(word[i - 1])) <= 2:
                i += 1
            ans += render(word[start:i])
        
        return ans

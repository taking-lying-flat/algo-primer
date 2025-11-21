class PrefixSuffixUtils:
    # ░░░░░░░░░░░░░░░░░░░░░░ LeetCode 238 —— 除自身以外数组的乘积 ░░░░░░░░░░░░░░░░░░░░░░
    def productExceptSelf(
      self, nums: List[int]
    ) -> List[int]:
        n = len(nums)
        pre = [1] * n
        for i in range(1, n):
            pre[i] = pre[i - 1] * nums[i - 1]
        suf = [1] * n
        for i in range(n - 2, -1, -1):
            suf[i] = suf[i + 1] * nums[i + 1]
        return [p * s for p, s in zip(pre, suf)]

    
    # ░░░░░░░░░░░░░░░░░░░░░░ LeetCode 42 —— 接雨水 ░░░░░░░░░░░░░░░░░░░░░░
    def trap(self, height: List[int]) -> int:
        ans = pre_max = suf_max = 0
        left, right = 0, len(height) - 1
        while left < right:
            pre_max = max(pre_max, height[left])
            suf_max = max(suf_max, height[right])
            if pre_max < suf_max:
                ans += pre_max - height[left]
                left += 1
            else:
                ans += suf_max - height[right]
                right -= 1
        return ans

    
    # ░░░░░░░░░░░░░░░░░░░░░░ LeetCode 135 —— 分发糖果 ░░░░░░░░░░░░░░░░░░░░░░
    def candy(
        self, ratings: List[int]
    ) -> int:
        n = len(ratings)
        left = [1] * n
        right = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right[i] = right[i + 1] + 1  
        ans = 0
        for l, r in zip(left, right):
            ans += max(l, r)
        return ans


    # ░░░░░░░░░░░░░░ LeetCode 1930 —— 长度为 3 的不同回文子序列 ░░░░░░░░░░░░░░
    def countPalindromicSubsequence(
        self, s: str
    ) -> int:
        suf_cnt = Counter(s[1:])
        pre_set = set()
        seen = set()
        for i in range(1, len(s) - 1):
            mid = s[i]
            suf_cnt[mid] -= 1
            if suf_cnt[mid] == 0:
                del suf_cnt[mid]
            pre_set.add(s[i - 1])
            for alpha in pre_set & suf_cnt.keys():
                seen.add(alpha + mid)
        return len(seen)

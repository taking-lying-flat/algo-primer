class SlidingWindowUtils:
    # ░░░░░░░░░░░ LeetCode 3 —— 无重复字符的最长子串 ░░░░░░░░░░░
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = left = 0
        cnt = defaultdict(int)
        for right, c in enumerate(s):
            cnt[c] += 1
            while cnt[c] > 1:
                cnt[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans

    
    # ░░░░░░░░░░░ LeetCode 438 · 找到字符串中所有字母异位词 ░░░░░░░░░░░
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        left = 0
        cnt = Counter(p)
        for right, c in enumerate(s):
            cnt[c] -= 1
            while cnt[c] < 0:
                cnt[s[left]] += 1
                left += 1
            if right - left + 1 == len(p):
                ans.append(left)         
        return ans


    # ░░░░░░░░░░░ LeetCode 904 —— 水果成篮 ░░░░░░░░░░░
    def totalFruit(self, fruits: List[int]) -> int:
        ans = left = 0
        cnt = defaultdict(int)
        for right, fruit in enumerate(fruits):
            cnt[fruit] += 1
            while len(cnt) > 2:
                out = fruits[left]
                left += 1
                cnt[out] -= 1
                if cnt[out] == 0:
                    del cnt[out]
            ans = max(ans, right - left + 1)
        return ans
        

    # ░░░░░░░░░░░ LeetCode 1004 —— 最大连续 1 的个数 III ░░░░░░░░░░░
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans = left = cnt0 = 0
        for right, num in enumerate(nums):
            cnt0 += 1 - num
            while cnt0 > k:
                cnt0 -= (1 - nums[left])
                left += 1
            ans = max(ans, right - left + 1)
        return ans


    # ░░░░░░░░░░░ LeetCode 1208 —— 尽可能使字符串相等 ░░░░░░░░░░░
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        dist = [abs(ord(a) - ord(b)) for (a, b) in zip(s, t)]
        ans = left = s = 0
        for right, x in enumerate(dist):
            s += x
            while s > maxCost:
                s -= dist[left]
                left += 1
            ans = max(ans, right - left + 1)
        return ans


    # ░░░░░░░░░░░ LeetCode 1658 —— 将 x 减到 0 的最小操作数 ░░░░░░░░░░░
    def minOperations(self, nums: List[int], x: int) -> int:
        ans, left, s = -1, 0, 0
        target = sum(nums) - x
        for right, x in enumerate(nums):
            s += x
            while left <= right and s > target:
                s -= nums[left]
                left += 1
            if s == target:
                ans = max(ans, right - left + 1)
        return -1 if ans < 0 else len(nums) - ans


    # ░░░░░░░░░░░ LeetCode 1695 —— 删除子数组的最大得分 ░░░░░░░░░░░
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ans = s = left = 0
        cnt = defaultdict(int)
        for right, x in enumerate(nums):
            s += x
            cnt[x] += 1
            while cnt[x] > 1:
                cnt[nums[left]] -= 1
                s -= nums[left]
                left += 1
            ans = max(ans, s)
        return ans


    # ░░░░░░░░░░░ LeetCode 2024 —— 考试的最大困扰度 ░░░░░░░░░░░
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        ans = left = 0
        cnt = defaultdict(int)
        for right, key in enumerate(answerKey):
            cnt[key] += 1
            while cnt['T'] > k and cnt['F'] > k:
                cnt[answerKey[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans


    # ░░░░░░░░░░░ LeetCode 2516 —— 每种字符至少取 K 个 ░░░░░░░░░░░
    def takeCharacters(self, s: str, k: int) -> int:
        ans = left = 0
        cnt = Counter(s)
        if any(cnt[c] < k for c in "abc"):
            return -1
        for right, c in enumerate(s):
            cnt[c] -= 1
            while cnt[c] < k:
                cnt[s[left]] += 1
                left += 1
            ans = max(ans, right - left + 1)
        return len(s) - ans


    # ░░░░░░░░░░░ LeetCode 2958 —— 最多 K 次重复元素的子数组 ░░░░░░░░░░░
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = left = 0
        cnt = defaultdict(int)
        for right, x in enumerate(nums):
            cnt[x] += 1
            while cnt[x] > k:
                cnt[nums[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans

    
    # ░░░░░░░░░░░ LeetCode 3634 —— 使数组平衡的最少移除数目 ░░░░░░░░░░░
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_save = left = 0
        for right, num in enumerate(nums):
            while nums[left] * k < num:
                left += 1
            max_save = max(max_save, right - left + 1)
        return len(nums) - max_save

    
    # ░░░░░░░░░░░ LeetCode 3641 —— 最长半重复子数组 ░░░░░░░░░░░
    def longestSubarray(self, nums: List[int], k: int) -> int:
        ans = left = 0
        cnt = defaultdict(int)
        seen = set()
        for right, x in enumerate(nums):
            cnt[x] += 1
            if cnt[x] > 1:
                seen.add(x)
            while len(seen) > k:
                out = nums[left]
                cnt[out] -= 1
                if cnt[out] == 1:
                    seen.remove(out)
                left += 1
            ans = max(ans, right - left + 1)
        return ans


    # ################################################################################
    # § 越短越合法（统计型滑动窗口）
    #
    # 模板结论：ans += right - left + 1
    #
    # 内层 while 收缩结束后，[left, right] 已经是当前“最左的合法窗口”
    # 对于固定的 right，只要左端点在区间 left..right 之间：
    #   [left..right], [left+1..right], ..., [right..right]
    # 这些子数组都满足题目要求
    # 因此，以 right 为右端点的合法子数组个数为 right - left + 1
    # ################################################################################
    # ░░░░░░░░░░░ LeetCode 713 —— 乘积小于 K 的子数组 ░░░░░░░░░░░
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans = left = 0
        prod = 1
        for right, x in enumerate(nums):
            prod *= x
            while left <= right and prod >= k:
                prod //= nums[left]
                left += 1
            ans += right - left + 1
        return ans

    
    # ░░░░░░░░░░░ LeetCode 2302 —— 统计得分小于 K 的子数组数目 ░░░░░░░░░░░
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = left = s = 0
        for right, x in enumerate(nums):
            s += x
            while (right - left + 1) * s >= k:
                s -= nums[left]
                left += 1
            ans += (right - left + 1)
        return ans


    # ░░░░░░░░░░░ LeetCode 3258 —— 满足 K 约束的子字符串 I ░░░░░░░░░░░
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        ans = left = 0
        cnt = [0, 0]
        for right, c in enumerate(s):
            cnt[ord(c) & 1] += 1
            while cnt[0] > k and cnt[1] > k:
                cnt[ord(s[left]) & 1] -= 1
                left += 1
            ans += right - left + 1
        return ans


    # ░░░░░░░░░░░ LCP 68 —— 美观的花束 ░░░░░░░░░░░
    def beautifulBouquet(self, flowers: List[int], cnt: int) -> int:
        ans = left = 0
        c = defaultdict(int)
        for right, x in enumerate(flowers):
            c[x] += 1
            while c[x] > cnt:
                c[flowers[left]] -= 1
                left += 1
            ans += right - left + 1
        return ans % 1_000_000_007

    
    # ################################################################################
    # § 越长越合法 统计型滑动窗口， 一般要写：ans += left
    #
    # 内层 while 收缩结束后，[left, right] 这个子数组（子串）已经“不满足题目要求”
    # 但在退出循环前的最后一轮，区间 [left-1, right] 还是满足要求的
    #
    # 由于「越长越合法」，只要左端点往左扩，仍然合法：
    #   [left-1, right], [left-2, right], ..., [0, right]
    # 也就是说，当右端点固定在 right 时
    # 所有左端点在 0, 1, 2, ..., left-1 的子数组都是合法的，一共有 left 个
    # 重点：我们关心的是 left-1 的合法性，而不是当前的 left，所以统计答案时写 ans += left
    # ################################################################################
    # ░░░░░░░░░░░ LeetCode 1358 —— 包含所有三种字符的子字符串数目 ░░░░░░░░░░░
    def numberOfSubstrings(self, s: str) -> int:
        ans = left = 0
        cnt = defaultdict(int)
        for c in s:
            cnt[c] += 1
            while len(cnt) == 3:
                out = s[left]  # 离开窗口的字母
                cnt[out] -= 1
                if cnt[out] == 0:
                    del cnt[out]
                left += 1
            ans += left
        return ans


    # ░░░░░░░░░░░ LeetCode 2495 —— 乘积为偶数的子数组数 ░░░░░░░░░░░
    def evenProduct(self, nums: List[int]) -> int:
        ans = left = even = 0
        for x in nums:
            even += (x & 1 == 0)          # 判断是否为偶数，比 % 2 略快
            while even > 0:               # 窗口内已有偶数 -> 当前窗口对应的是「偶数乘积」子数组
                even -= (nums[left] & 1 == 0)
                left += 1
            ans += left                   # 越长越合法
        return ans


    # ░░░░░░░░░░░ LeetCode 2537 —— 统计好子数组的数目 ░░░░░░░░░░░
    def countGood(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        ans = left = pairs = 0
        for x in nums:
            pairs += cnt[x]
            cnt[x] += 1
            while pairs >= k:
                cnt[nums[left]] -= 1
                pairs -= cnt[nums[left]]
                left += 1
            ans += left
        return ans

    
    # ░░░░░░░░░░░ LeetCode 2799 —— 统计完全子数组的数目 ░░░░░░░░░░░
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        k = len(set(nums))
        cnt = defaultdict(int)  # 比 Counter() 快
        ans = left = 0
        for x in nums:
            cnt[x] += 1
            while len(cnt) == k:
                out = nums[left]
                cnt[out] -= 1
                if cnt[out] == 0:
                    del cnt[out]
                left += 1
            ans += left
        return ans

    
    # ░░░░░░░░░░░ LeetCode 2962 —— 统计最大元素至少出现 K 次的子数组 ░░░░░░░░░░░
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        ans = cnt_mx = left = 0
        for x in nums:
            if x == mx:
                cnt_mx += 1
            while cnt_mx == k:
                if nums[left] == mx:
                    cnt_mx -= 1
                left += 1
            ans += left
        return ans

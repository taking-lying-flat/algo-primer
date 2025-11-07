class SlidingWindowUtils:
    # ░░░░░░░░░░░ LeetCode 3 —— 无重复字符的最长子串 ░░░░░░░░░░░
    @staticmethod
    def lengthOfLongestSubstring(s: str) -> int:
        """
        不定长滑动窗口: 返回无重复字符的最长子串长度
            1. 使用滑动窗口维护一个无重复字符的子串
            2. 右指针不断扩展，将字符加入窗口
            3. 当出现重复字符时，收缩左边界直到窗口内无重复
            4. 记录过程中的最大窗口长度
        """
        ans = left = 0
        cnt = defaultdict(int)
        for right, c in enumerate(s):
            cnt[c] += 1
            while cnt[c] > 1:
                cnt[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans


    # ░░░░░░░░░░░ LeetCode 76 · 最小覆盖子串 ░░░░░░░░░░░
    @staticmethod
    def minWindow(s: str, t: str) -> str:
        """
        不定长滑动窗口: 找包含 t 所有字符的最小子串
            1. 使用计数器记录目标串 t 中每个字符的需求量
            2. less 变量记录还有几种字符未满足需求
            3. 右指针扩展窗口，当所有字符都满足时 less==0
            4. 收缩左边界找最小窗口，直到不再满足条件
            5. 记录过程中的最小窗口
        """
        ans_left, ans_right = -1, len(s)
        cnt = defaultdict(int)
        for c in t:
            cnt[c] += 1
        
        less: int = len(cnt)
        left: int = 0
        
        for right, c in enumerate(s):
            cnt[c] -= 1
            if cnt[c] == 0:
                less -= 1
            while left <= right and less == 0:
                if right - left < ans_right - ans_left:
                    ans_right, ans_left = right, left
                if cnt[s[left]] == 0:
                    less += 1
                cnt[s[left]] += 1
                left += 1
        return "" if ans_left < 0 else s[ans_left: ans_right + 1]

    
    # ░░░░░░░░░░░ LeetCode 438 · 找到字符串中所有字母异位词 ░░░░░░░░░░░
    @staticmethod
    def findAnagrams(s: str, p: str) -> List[int]:
        """
        定长滑动窗口: 返回字符串 s 中所有 p 的字母异位词起始索引
            1. 使用计数器记录目标串 p 中每个字符的需求量
            2. 滑动窗口遍历 s，右边界字符进入时减少需求
            3. 当某字符超量 cnt[c] < 0 时，收缩左边界
            4. 当窗口大小等于 p 的长度时，说明找到一个异位词
        """
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
    @staticmethod
    def totalFruit(fruits: List[int]) -> int:
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
        

    # ░░░░░░░░░░░ LeetCode 1004 —— 最大连续1的个数 III ░░░░░░░░░░░
    @staticmethod
    def longestOnes(nums: List[int], k: int) -> int:
        ans = left = cnt0 = 0
        for right, num in enumerate(nums):
            cnt0 += 1 - num
            while cnt0 > k:
                cnt0 -= (1 - nums[left])
                left += 1
            ans = max(ans, right - left + 1)
        return ans


    # ░░░░░░░░░░░ LeetCode 1208 —— 尽可能使字符串相等 ░░░░░░░░░░░
    @staticmethod
    def equalSubstring(s: str, t: str, maxCost: int) -> int:
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
    @staticmethod
    def minOperations(nums: List[int], x: int) -> int:
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
    @staticmethod
    def maximumUniqueSubarray(nums: List[int]) -> int:
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
    @staticmethod
    def maxConsecutiveAnswers(answerKey: str, k: int) -> int:
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
    @staticmethod
    def takeCharacters(s: str, k: int) -> int:
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
    @staticmethod
    def maxSubarrayLength(nums: List[int], k: int) -> int:
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
    @staticmethod
    def minRemoval(nums: List[int], k: int) -> int:
        nums.sort()
        max_save = left = 0
        for right, num in enumerate(nums):
            while nums[left] * k < num:
                left += 1
            max_save = max(max_save, right - left + 1)
        return len(nums) - max_save

    
    # ░░░░░░░░░░░ LeetCode 3641 —— 最长半重复子数组 ░░░░░░░░░░░
    @staticmethod
    def longestSubarray(nums: List[int], k: int) -> int:
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



class SubarrayCountWindowSuite:
    """
    § 越短越合法法  ans += right - left + 1

    内层循环结束后，[left, right] 这个子数组是满足题目要求的。
    由于子数组越短，越能满足题目要求，所以除了 [left, right]，
    还有 [left+1, right]，[left+2, right]，…，[right, right] 都是满足要求的。
    也就是说，当右端点固定在 right 时，左端点在 left, left+1, left+2, …, right
    的所有子数组都是满足要求的，这一共有 right - left + 1 个。
    """
    # ░░░░░░░░░░░ LeetCode 713 —— 乘积小于 K 的子数组 ░░░░░░░░░░░
    @staticmethod
    def numSubarrayProductLessThanK(nums: List[int], k: int) -> int:
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
    @staticmethod
    def countSubarrays(nums: List[int], k: int) -> int:
        ans = left = s = 0

        for right, x in enumerate(nums):
            s += x
            while (right - left + 1) * s >= k:
                s -= nums[left]
                left += 1
            ans += (right - left + 1)
        
        return ans

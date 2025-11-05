from typing import List
from collections import defaultdict


class FixedWindowSuite:
    # ░░░░░░░░░░░ LeetCode 1343 —— 大小为 K 且平均值大于等于阈值的子数组数目 ░░░░░░░░░░░
    @staticmethod
    def numOfSubarrays(arr: List[int], k: int, threshold: int) -> int:
        ans = s = 0  # 维护窗口元素和
        for i, x in enumerate(arr):
            # 1. 进入窗口
            s += x
            if i < k - 1:  # 窗口大小不足 k
                continue
            # 2. 更新答案
            if s >= k * threshold:
                ans += 1
            # 3. 离开窗口
            s -= arr[i - k + 1]
        return ans

    
    # ░░░░░░░░░░░ LeetCode 1456 —— 定长子串中元音的最大数目 ░░░░░░░░░░░
    @staticmethod
    def maxVowels(s: str, k: int) -> int:
        ans = vowel = 0
        for i, c in enumerate(s):  # 枚举窗口右端点 i
            # 1. 右端点进入窗口
            if c in "aeiou":
                vowel += 1

            left = i - k + 1  # 窗口左端点
            if left < 0:      # 窗口大小不足 k，尚未形成第一个窗口
                continue

            # 2. 更新答案
            ans = max(ans, vowel)

            # 3. 左端点离开窗口，为下一个循环做准备
            if s[left] in "aeiou":
                vowel -= 1
        return ans
        

    # ░░░░░░░░░░░ LeetCode 2461 —— 长度为 K 的子数组的最大和（元素互不相同）░░░░░░░░░░░
    @staticmethod
    def maximumSubarraySum(nums: List[int], k: int) -> int:
        ans = s = 0
        cnt = defaultdict(int)
        for i, x in enumerate(nums):
            # 1. 进入窗口
            s += x
            cnt[x] += 1

            left = i - k + 1
            if left < 0:  # 窗口大小不足 k
                continue

            # 2. 更新答案
            if len(cnt) == k:
                ans = max(ans, s)

            # 3. 离开窗口
            out = nums[left]
            s -= out
            cnt[out] -= 1
            if cnt[out] == 0:
                del cnt[out]

        return ans

    
    # ░░░░░░░░░░░ LeetCode 2841 —— 几乎唯一子数组的最大和 ░░░░░░░░░░░
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        ans = s = 0
        cnt = defaultdict(int)
        for i, x in enumerate(nums):
            # 1. 进入窗口
            s += x
            cnt[x] += 1

            left = i - k + 1
            if left < 0:  # 窗口大小不足 k
                continue

            # 2. 更新答案
            if len(cnt) >= m:
                ans = max(ans, s)

            # 3. 离开窗口
            out = nums[left]
            s -= out
            cnt[out] -= 1
            if cnt[out] == 0:
                del cnt[out]

        return ans

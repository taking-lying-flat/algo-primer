from typing import List
from collections import defaultdict


def fixed_window_template(nums: List[int], k: int) -> Any:
    """
    固定长度滑动窗口模板（入 → 更新 → 出）
        1. 入：右端点 i 进入窗口，更新窗口状态 state
        2. 更新：当窗口长度恰好为 k 时，用当前 state 更新答案 ans
        3. 出：左端点 i-k+1 离开窗口，state 回退，为下一轮做准备

        - 根据题目设计：
            - ans：答案（最大值/计数/布尔等）
            - state：窗口内需要维护的统计（和/频次表/元音数等）
        - 在标有 TODO 的位置填入具体逻辑
    """
    ans = ...      # TODO: 初始化答案，比如 0 / -inf / False / []
    state = ...    # TODO: 初始化窗口状态，比如 0 / defaultdict(int) / {}

    for i, x in enumerate(nums):
        # 1. 入：右端点 i 进入窗口，更新 state
        #    例：state += x / cnt[x] += 1 / ...
        ...  # TODO: 按题目更新 state

        left = i - k + 1  # 当前窗口左端点
        if left < 0:
            # 窗口大小不足 k：还没形成第一个完整窗口
            continue

        # 2. 更新：此时窗口 [left, i] 的长度恰好为 k，用 state 更新 ans
        #    例：ans = max(ans, state) / if 满足条件: ans += 1 / ...
        ...  # TODO: 根据题意更新 ans

        # 3. 出：左端点离开窗口，state 回退
        #    out = nums[left]
        #    例：state -= out / cnt[out]-- / ...
        ...  # TODO: 用 nums[left] 把 state 恢复

    return ans


class FixedWindowSuite:
    # ░░░░░░░░░░░ LeetCode 643 —— 子数组最大平均数 I ░░░░░░░░░░░
    @staticmethod
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_s = -inf  # 窗口元素和的最大值
        s = 0  # 维护窗口元素和
        for i, x in enumerate(nums):
            # 1. 进入窗口
            s += x
            if i < k - 1:  # 窗口大小不足 k
                continue
            # 2. 更新答案
            max_s = max(max_s, s)
            # 3. 离开窗口
            s -= nums[i - k + 1]
        return max_s / k

    
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

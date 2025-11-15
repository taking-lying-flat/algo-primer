class InPlaceModifySuite:
    # ░░░░░░░░░░░ LeetCode 2273 —— 移除字母异位词后的结果数组 ░░░░░░░░░░░
    def removeAnagrams(
        self, words: List[str]
    ) -> List[str]:
        k = 1
        for s, t in pairwise(words):
            if sorted(s) != sorted(t):
                words[k] = t
                k += 1
        del words[k:]
        return words

    
    # ░░░░░░░░░░░ LeetCode 41 —— 缺失的第一个正数（地哈希法） ░░░░░░░░░░░
    def firstMissingPositive(
        self, nums: List[int]
    ) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1

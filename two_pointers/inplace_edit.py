class InPlaceModifySuite:
    # ░░░░░░░░░░░ LeetCode 2273 —— 移除字母异位词后的结果数组 ░░░░░░░░░░░
    def removeAnagrams(self, words: List[str]) -> List[str]:
        k = 1
        for s, t in pairwise(words):
            if sorted(s) != sorted(t):
                words[k] = t
                k += 1
        del words[k:]
        return words

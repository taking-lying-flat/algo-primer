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

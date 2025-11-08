class HardTwoPointersSuite:
    # ★★★★★ ░░░░░░░░░░░ LeetCode 76 · 最小覆盖子串 ░░░░░░░░░░░ ★★★★★
    def minWindow(self, s: str, t: str) -> str:
        """
        类型：不定长滑动窗口 + 计数

        不定长滑动窗口: 找包含 t 所有字符的最小子串
            1. 用哈希表 cnt 统计 t 中每个字符需要的数量
            2. less = 需要满足的不同字符种数；当某个字符需求从 > 0 变成 0 时，less -= 1
            3. 右指针 right 向右扩展，将字符加入窗口，更新 cnt 和 less
            4. 当 less == 0 时，说明当前窗口 [left, right] 已经覆盖 t 中所有字符：
               - 用它更新最小区间答案
               - 然后尝试移动 left 收缩窗口：把 s[left] 丢出，恢复 cnt
                 如果某个字符需求从 0 变回 >0，则 less += 1，窗口再次不合法
            5. 在整个过程中维护最小合法窗口的左右端点，最终切片返回
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

  
    # ★★★★★ ░░░░░░░░░░░ LeetCode 3134 · 找出唯一性数组的中位数 ░░░░░░░░░░░ ★★★★★
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        """
        类型：二分答案 + 不定长滑动窗口

        核心思路（离线 + 二分答案）：
            1. 记 total = n*(n+1)/2，为子数组总数, 中位数对应的排名是 k = (total + 1) // 2
            2. 我们不显式构造 uniqueness 数组，而是对 唯一性上界 upper 做二分
               定义 is_blue(upper)：返回「唯一性 ≤ upper 的子数组个数 >= k」是否为真
               若 true 说明中位数 <= upper；若 false 说明中位数 > upper
               中位数在 [1, 去重后的 nums 长度] 之间，用二分查出最小的 upper 使 is_blue(upper) 为真
            3. 如何统计 唯一性 ≤ upper 的子数组个数 ？
               使用不定长滑动窗口 / 双指针：
                 - 右指针 r 向右扩展，cnt 维护每个数字出现次数，len(cnt) 为当前窗口不同元素个数
                 - 若 len(cnt) > upper，则左指针 l 右移收缩窗口，维护 cnt 和 len(cnt)，直到重新满足 ≤ upper
                 - 对于固定的 r，此时窗口 [l, r] 是最左的合法窗口
                   以 r 结尾的合法子数组个数为 r - l + 1，累加到 ans
               整个过程是典型的「越短越合法法」统计子数组数量
            4. is_blue(upper) 具有单调性（upper 越大，合法子数组越多），因此对 upper 做二分搜索即可求出中位数
        """
        n = len(nums)
        k = (n * (n + 1) // 2 + 1) // 2

        def is_blue(upper: int) -> bool:
            ans = l = 0
            cnt = defaultdict(int)
            for r, x in enumerate(nums):
                cnt[x] += 1
                while len(cnt) > upper:
                    out = nums[l]
                    cnt[out] -= 1
                    if cnt[out] == 0:
                        del cnt[out]
                    l += 1
                ans += r - l + 1
                if ans >= k:
                    return True
            return False
        
        left, right = 1, len(set(nums))
        while left < right:
            pivot = (left + right) // 2
            if is_blue(pivot):
                right = pivot
            else:
                left = pivot + 1
        return left


    # ★★★★★ ░░░░░░░░░░░ LeetCode 2953 —— 统计完全子字符串 ░░░░░░░░░░░ ★★★★★
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        """
        类型：分组循环 + 定长滑动窗口

        思路概要：
            1. 若相邻字符的 ASCII 差值 > 2，则不可能出现在同一个「完全子字符串」中
               因此按 |word[i] - word[i-1]| <= 2 把原串切成若干独立段
            2. 对每一段 s 单独处理：枚举不同字符种数 m = 1..26
               此时完全子串长度固定为 L = m * k
            3. 在 s 上用定长滑动窗口长为 L
                 - 右端点 right 扩展，cnt 统计每个字符出现次数
                 - 当形成完整窗口（left >= 0）时，检查窗口是否满足
                       所有字符出现次数要么为 0，要么为 k
                   若满足则贡献 1；随后左端点字符离开窗口，更新 cnt
            4. 累加所有分段的答案
        """
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


    # ★★★★★ ░░░░░░░░░░░ LeetCode 3259 —— 满足 K 约束的子字符串 II ░░░░░░░░░░░ ★★★★★
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        """
        不定长滑窗 + 前缀和 + 二分

        - 预处理：
            left[i] = 以 i 结尾的最小合法左端点
            pre[i+1] = 所有右端点 ≤ i 的合法子串数量（累加 i - left[i] + 1）
        - 查询 [L,R]
            若区间内所有 right 的 left[right] ≤ L，则每个 right 的有效左端点是 [L,right]
            直接按长度求等差数列和
            否则二分找到第一个 j 使 left[j] > L
                * 对 right ∈ [j,R]：pre 里统计的子串起点都 > L，可用 pre 差分
                * 对 right ∈ [L,j-1]：pre 混入了起点 < L 的子串，无法用 pre 直接扣，改成按长度
                  (right-L+1) 累加，化成一段等差数列
        """
        n = len(s)
        pre = [0] * (n + 1)
        left = [0] * n
        cnt = [0, 0]
        l = 0

        for i, x in enumerate(s):
            cnt[ord(x) & 1] += 1
            while cnt[0] > k and cnt[1] > k:
                cnt[ord(s[l]) & 1] -= 1
                l += 1
            left[i] = l                       # 记录合法子串右端点 i 对应的最小左端点 l
            pre[i + 1] = pre[i] + i - l + 1   # 以 i 结尾的合法子串个数做前缀和

        ans = []
        for L, R in queries:
            lo, hi = L, R
            # 在 [L, R] 上二分，找第一个满足 left[mid] > L 的位置 lo
            while lo < hi:
                mid = (lo + hi) // 2
                if left[mid] > L:
                    hi = mid
                else:
                    lo = mid + 1

            if left[R] <= L:
                # 区间内所有 right 的 left[right] <= L：直接等差数列
                ans.append((R - L + 2) * (R - L + 1) // 2)
            else:
                # 把 right 拆成 [L, lo-1] 和 [lo, R] 两段：
                #   [lo,R] 用 pre 差分；[L,lo-1] 用等差数列
                ans.append(pre[R + 1] - pre[lo] + (lo - L) * (lo - L + 1) // 2)

        return ans


    # ★★★★★ ░░░░░░░░░░░ LeetCode 3298 —— 统计重新排列后包含另一个字符串的子字符串数目 II ░░░░░░░░░░░ ★★★★★
    def validSubstringCount(self, word1: str, word2: str) -> int:
        """
        不定长滑动窗口 + 计数

        - 先用 cnt 统计 word2 中每个字符的需求量，kinds 为未满足的字符种数。
        - 右指针 right 扩展 word1，进入一个字符就让 cnt[char]--，
          当某类字符需求从 >0 变成 0 时，kinds--。
        - 当 kinds == 0 时，说明当前窗口 [left,right] 已经覆盖了 word2 的所有需求，
          继续右移 left，把窗口收缩成「最短覆盖」窗口：
              收缩前若 cnt[word1[left]] == 0，则收缩后该类需求会重新变成 >0，
              于是 kinds++，窗口不再覆盖 word2。
        - 此时，对固定的 right，所有起点在 [0,left-1] 的子串都能覆盖 word2，
          一共有 left 个，所以 ans += left。
        """
        def validSubstringCount(self, s: str, t: str) -> int:
        if len(s) < len(t):
            return 0

        # t 的字母出现次数与 s 的字母出现次数之差
        diff = defaultdict(int)  # 也可以用 Counter(t)，但是会慢很多
        for c in t:
            diff[c] += 1

        # 窗口内有 less 个字母的出现次数比 t 的少
        less = len(diff)

        ans = left = 0
        for c in s:
            diff[c] -= 1
            if diff[c] == 0:
                # c 移入窗口后，窗口内 c 的出现次数和 t 的一样
                less -= 1
            while less == 0:  # 窗口符合要求
                if diff[s[left]] == 0:
                    # s[left] 移出窗口之前，检查出现次数，
                    # 如果窗口内 s[left] 的出现次数和 t 的一样，
                    # 那么 s[left] 移出窗口后，窗口内 s[left] 的出现次数比 t 的少
                    less += 1
                diff[s[left]] += 1
                left += 1
            ans += left
        return ans


    # ★★★★★ ░░░░░░░░░░░ LeetCode 992 —— K 个不同整数的子数组 ░░░░░░░░░░░ ★★★★★
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        """
        恰好型滑动窗口

        核心：恰好 K = 至多 K − 至多 (K−1)
          - cnt1 / left1 维护「至多 K」的窗口：当种类数 > K 时收缩。
          - cnt2 / left2 维护「至多 K−1」的窗口：当种类数 ≥ K 时收缩。
          - 对固定 right，合法子数组个数为 left2 - left1，累加到 ans。
        """
        ans = left1 = left2 = 0
        cnt1 = defaultdict(int)
        cnt2 = defaultdict(int)

        for right, x in enumerate(nums):
            cnt1[x] += 1
            cnt2[x] += 1

            while left1 <= right and len(cnt1) > k:
                out = nums[left1]
                cnt1[out] -= 1
                if cnt1[out] == 0:
                    del cnt1[out]
                left1 += 1
            
            while left2 <= right and len(cnt2) >= k:
                out = nums[left2]
                cnt2[out] -= 1
                if cnt2[out] == 0:
                    del cnt2[out]
                left2 += 1
            
            ans += left2 - left1

        return ans



    # ★★★★★ ░░░░░░░░░░░ LeetCode 3306 —— 3306. 元音辅音字符串计数 II ░░░░░░░░░░░ ★★★★★
    def countOfSubstrings(self, word: str, k: int) -> int:
        """
        恰好型滑动窗口：恰好 k 个辅音 + 包含全部 5 个元音（a,e,i,o,u）

        利用恒等式：
            exact(k) = at_least(k) - at_least(k + 1)

        其中 at_least(limit) 统计：
            「辅音数 ≥ limit 且 已经包含全部 5 个元音」的子串个数。

        对 fixed right：
            当窗口满足 (consonants ≥ limit 且 kinds == 5) 时，收缩 left，
            收缩结束后的 left 即合法左端点个数（越长越合法），累加 ans += left。
        """
        vowel = set("aeiou")

        def at_least(limit: int) -> int:
            ans = 0
            left = 0
            consonants = 0
            v_cnt = defaultdict(int)
            kinds = 0

            for right, x in enumerate(word):
                if x in vowel:
                    if v_cnt[x] == 0:
                        kinds += 1
                    v_cnt[x] += 1
                else:
                    consonants += 1

                while consonants >= limit and kinds == 5:
                    out = word[left]
                    if out in vowel:
                        v_cnt[out] -= 1
                        if v_cnt[out] == 0:
                            kinds -= 1
                    else:
                        consonants -= 1
                    left += 1

                ans += left
            return ans
        
        return at_least(k) - at_least(k + 1)

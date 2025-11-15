class SubsequenceDPToolkit:
    # ░░░░░░░░░░░░░░░░░░░░░░ LeetCode 1143 —— 最长公共子序列 ░░░░░░░░░░░░░░░░░░░░░░
    def longestCommonSubsequence(
        self, text1: str, text2: str
    ) -> Tuple[int, Set[str]]:
        m, n = len(text1), len(text2)

        # @cache
        # def dfs(i: int, j: int) -> int:
        #     if i < 0 or j < 0:
        #         return 0
        #     if text1[i] == text2[j]:
        #         return dfs(i - 1, j - 1) + 1
        #     return max(dfs(i - 1, j), dfs(i, j - 1))
        # return dfs(m - 1, n - 1)

        # 前缀 DP：f[i][j] = text1[:i] 和 text2[:j] 的 LCS 长度
        f = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    f[i][j] = f[i - 1][j - 1] + 1
                else:
                    f[i][j] = max(f[i - 1][j], f[i][j - 1])

        @cache
        def rec(i: int, j: int) -> Set[str]:
            if i == 0 or j == 0:
                return {""}
            res: Set[str] = set()
            # 当前字符相等且确实由左上转移过来，则这些 LCS 都要带上这个字符
            if text1[i - 1] == text2[j - 1] and f[i][j] == f[i - 1][j - 1] + 1:
                for s in rec(i - 1, j - 1):
                    res.add(s + text1[i - 1])
            else:
                if f[i - 1][j] == f[i][j]:    # 向上走不减长度
                    res |= rec(i - 1, j)
                if f[i][j - 1] == f[i][j]:    # 向左走不减长度
                    res |= rec(i, j - 1)
            return res

        return f[m][n], rec(m, n)


    # ░░░░░░░░░░░░░░░ LeetCode 72 —— 编辑距离（经典二维 DP · 子序列） ░░░░░░░░░░░░░░░
    def minDistance(
        self, word1: str, word2: str
    ) -> int:
        # 编辑距离 · 二维 DP
        # f[i][j]：word1 前 i 个字符变成 word2 前 j 个字符的最少操作数
        # 转移：增 / 删 / 改 三种操作取最小值 + 1；若当前字符相等则直接继承 f[i-1][j-1]
        # @cache
        # def dfs(i: int, j: int) -> int:
        #     if i < 0:
        #         return j + 1          # 插入 j+1 个字符
        #     if j < 0:
        #         return i + 1          # 删除 i+1 个字符
        #     if word1[i] == word2[j]:
        #         return dfs(i - 1, j - 1)
        #     return min(
        #         dfs(i - 1, j),        # 删除 word1[i]
        #         dfs(i, j - 1),        # 在末尾插入 word2[j]
        #         dfs(i - 1, j - 1),    # 替换 word1[i] 为 word2[j]
        #     ) + 1

        m, n = len(word1), len(word2)
        f = [[0] * (n + 1) for _ in range(m + 1)]
        f[0] = list(range(n + 1))
        for i, x in enumerate(word1):
            f[i + 1][0] = i + 1
            for j, y in enumerate(word2):
                if x == y:
                    f[i + 1][j + 1] = f[i][j]
                else:
                    f[i + 1][j + 1] = min(
                        f[i][j + 1],   # 删除 word1[i]
                        f[i + 1][j],   # 插入 word2[j]
                        f[i][j],       # 替换
                    ) + 1
        return f[m][n]


    # ░░░░░░░░░░░░░░░ LeetCode 44 —— 通配符匹配 ░░░░░░░░░░░░░░░
    def isMatch(
        self, s: str, p: str
    ) -> bool:
        """
        1. dfs(i, j) 判断 s[0..i] 与 p[0..j] 是否匹配（均为闭区间）
        2. 边界：当 j < 0（模式串耗尽），只有 i < 0（文本也耗尽）才匹配
        3. 当 i < 0（文本耗尽），模式串剩余必须全部是 '*' 才匹配
        4. 若 p[j] 为 '*'：
           - 视为匹配空串：dfs(i, j - 1)
           - 视为匹配一个字符并继续吞字符：dfs(i - 1, j)
        5. 普通字符或 '?'：必须与 s[i] 对齐（'?' 视为任意字符），然后 dfs(i - 1, j - 1)
        """
        m, n = len(s), len(p)
        @cache
        def dfs(i: int, j: int) -> bool:
            if j < 0:
                return i < 0
            if i < 0:
                return all(ch == '*' for ch in p[:j + 1])
            if p[j] == '*':
                return dfs(i, j - 1) or dfs(i - 1, j)
            # 普通字符或 '?'
            if p[j] == '?' or p[j] == s[i]:
                return dfs(i - 1, j - 1)
            return False
        return dfs(m - 1, n - 1)


    # ░░░░░░░░░░░░░░░ LeetCode 10 —— 正则表达式匹配 ░░░░░░░░░░░░░░░
    def isMatch(
        self, s: str, p: str
    ) -> bool:
        """
        正则表达式匹配（支持 . 和 * 的记忆化搜索）
             1. dfs(i, j) 判断 s[0:i+1] 与 p[0:j+1] 是否匹配
             2. 边界: 模式串耗尽时，字符串也必须耗尽
             3. 字符串耗尽时，模式串只能是 x*y*z* 形式
             4. 遇到 '*' 时有两种选择：
                - 跳过 "x*" 两个字符（匹配 0 次）
                - 若前一字符匹配，消费 s[i]，继续停在 '*'（匹配多次）
             5. 普通字符或 '.' 必须精确匹配才能继续
        """
        m, n = len(s), len(p)
        @cache
        def dfs(i: int, j: int) -> bool:
            if j < 0:                      # 模式串已耗尽
                return i < 0
            if i < 0:                      # s 耗尽，只能匹配形如 a*b*c*...
                return p[j] == '*' and dfs(i, j - 2)
            if p[j] == '*':
                # 1) 跳过 "x*" 两字符
                if dfs(i, j - 2):
                    return True
                # 2) 若当前字符可匹配，则消费 s[i]，仍停在 '*' 处继续匹配
                if p[j - 1] in {s[i], '.'}:
                    return dfs(i - 1, j)
                return False
            else:
                if p[j] in {s[i], '.'}:
                    return dfs(i - 1, j - 1)
                return False
        return dfs(m - 1, n - 1)


    # ░░░░░░░░░░░ LeetCode 139 —— 单词拆分（DP） ░░░░░░░░░░░
    def wordBreak(
        self, s: str, wordDict: List[str]
    ) -> bool:
        max_len = max(map(len, wordDict))
        words = set(wordDict)
        n = len(s)
        f = [True] + [False] * n
        for i in range(len(s) + 1):
            start = max(0, i - max_len)
            for j in range(start, i):
                if s[j:i] in words and f[j]:
                    f[i] = True
                    break
        return f[n]

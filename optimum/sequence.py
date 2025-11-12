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
    @staticmethod
    def minDistance(
        word1: str, word2: str
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

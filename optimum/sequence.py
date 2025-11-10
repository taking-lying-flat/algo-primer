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

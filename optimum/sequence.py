# ░░░░░░░░░░░ LeetCode 1143 —— 最长公共子序列 ░░░░░░░░░░░
    @staticmethod
    def longestCommonSubsequence(
        text1: str, text2: str
    ) -> Tuple[int, Set[str]]:
        m, n = len(text1), len(text2)

        @cache
        def dfs(i: int, j: int) -> int:
            if i < 0 or j < 0:
                return 0
            if text1[i] == text2[j]:
                return dfs(i - 1, j - 1) + 1
            return max(dfs(i - 1, j), dfs(i, j - 1))

        return dfs(m - 1, n - 1)
        f = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    f[i][j] = f[i - 1][j - 1] + 1
                else:
                    f[i][j] = max(f[i - 1][j], f[i][j - 1])

class MemoizationSearch:
    # ░░░░░░░░░░░░░░ LeetCode 120 —— 三角形最小路径和 ░░░░░░░░░░░░░░
    @staticmethod
    def minimumTotal(triangle: List[List[int]]) -> int:
        """
        三角形自顶向下最小路径和（记忆化搜索）
             1. dfs(i, j) 表示从位置 (i,j) 到底部的最小路径和
             2. 到达底部时，返回当前位置的值
             3. 否则，可以走到 (i+1,j) 或 (i+1,j+1)
             4. 选择两条路径中的最小值，加上当前值
             5. 使用 @cache 装饰器自动记忆化
        """
        n = len(triangle)
        @cache
        def dfs(i: int, j: int) -> int:
            if i == n - 1:
                return triangle[i][j]
            return min(dfs(i + 1, j), dfs(i + 1, j + 1)) + triangle[i][j]
        return dfs(0, 0)

    # ░░░░░░░░░░░░░░ LeetCode 63 —— 不同路径 II ░░░░░░░░░░░░░░
    @staticmethod
    def uniquePathsWithObstacles(obstacleGrid: List[List[int]]) -> int:
        """
        带障碍物的矩阵路径计数（记忆化搜索）
             1. dfs(i, j) 表示从 (0,0) 到 (i,j) 的路径数量
             2. 边界处理：越界或遇到障碍物返回 0
             3. 起点处理：如果是起点且无障碍返回 1
             4. 每个位置可以从上方或左方到达（如果无障碍）
             5. 路径数等于两个方向路径数之和
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        @cache
        def dfs(i: int, j: int) -> int:
            if i < 0 or j < 0 or obstacleGrid[i][j]:
                return 0
            if i == 0 and j == 0:
                return 1
            return dfs(i - 1, j) + dfs(i, j - 1)
        return dfs(m - 1, n - 1)

    # ░░░░░░░░░░░░░░ LeetCode 329 —— 矩阵中的最长递增路径 ░░░░░░░░░░░░░░
    @staticmethod
    def longestIncreasingPath(matrix: List[List[int]]) -> int:
        """
        矩阵最长递增路径（四方向 DFS + 记忆化）
             1. dfs(i, j) 表示从 (i,j) 开始的最长递增路径长度
             2. 尝试向四个方向扩展：上下左右
             3. 只能走到值更小的格子（严格递减）
             4. 取所有可行方向的最大值，加上当前格子（长度+1）
             5. 枚举所有起点，返回全局最大值
        """
        DIRS = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        @cache
        def dfs(i: int, j: int) -> int:
            best = 1
            for dx, dy in DIRS:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and matrix[x][y] < matrix[i][j]:
                    best = max(best, 1 + dfs(x, y))
            return best
        return max(dfs(i, j) for i in range(m) for j in range(n))


class SubsequenceDPToolkit:
    # ░░░░░░░░░░░ LeetCode 300 —— 最长递增子序列 ░░░░░░░░░░░
    @staticmethod
    def lengthOfLIS(nums: List[int]) -> int:
        """
        贪心 + 二分查找求 LIS 长度
             1. tails[i] 表示长度为 i+1 的递增子序列的最小末尾值
             2. 遍历每个数字，二分查找其在 tails 中的位置
             3. 如果大于所有元素，追加到末尾（子序列变长）
             4. 否则更新对应位置（保持该长度的最小末尾）
             5. tails 长度即为 LIS 长度
        """
        tails: List[int] = []
        for x in nums:
            idx = bisect_left(tails, x)
            if idx == len(tails):
                tails.append(x)
            else:
                tails[idx] = x
        return len(tails)


    # ░░░░░░░░░░░ LeetCode 139 —— 单词拆分（DP） ░░░░░░░░░░░
    @staticmethod
    def wordBreak(s: str, wordDict: List[str]) -> bool:
        """
        动态规划：
            1. f[i] 表示 s[:i] 是否可由字典组成
            2. 只需回看长度 ≤ max_len 的前缀
            3. 若存在 j < i 使得 f[j] = True 且 s[j:i] 在字典中，则 f[i] = True
        """
        max_len = max(map(len, wordDict))
        words = set(wordDict)

        n = len(s)
        f = [True] + [False] * n
        for i in range(len(s) + 1):
            start = max(0, i - max_len)
            for j in range(start, i):
                if s[j: i] in words and f[j]:
                    f[i] = True
                    break
        return f[n]

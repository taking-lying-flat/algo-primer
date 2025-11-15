class GridwalksToolKit:
    # ░░░░░░░░░░░░░░ LeetCode 120 —— 三角形最小路径和 ░░░░░░░░░░░░░░
    def minimumTotal(
        self, triangle: List[List[int]]
    ) -> int:
        n = len(triangle)
        @cache
        def dfs(i: int, j: int) -> int:
            if i == n - 1:
                return triangle[i][j]
            return min(dfs(i + 1, j), dfs(i + 1, j + 1)) + triangle[i][j]
        return dfs(0, 0)

    
    # ░░░░░░░░░░░░░░ LeetCode 63 —— 不同路径 II ░░░░░░░░░░░░░░
    def uniquePathsWithObstacles(
        self, obstacleGrid: List[List[int]]
    ) -> int:
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
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
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

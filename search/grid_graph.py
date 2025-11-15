class GridSearchToolkit:
    # ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ LeetCode 79 —— 单词搜索 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    def exist(
        self, board: List[List[str]], word: str
    ) -> bool:
        cnt = Counter(c for row in board for c in row)
        if not cnt >= Counter(word):
            return False
        if cnt[word[-1]] < cnt[word[0]]:
            word = word[::-1]
        m, n = len(board), len(board[0])
        def dfs(i: int, j: int, k: int) -> bool:
            if board[i][j] != word[k]:  # 匹配失败
                return False
            if k == len(word) - 1:      # 匹配成功, 处理单字符情况
                return True
            board[i][j] = ''            # 标记访问过
            for x, y in (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j):  # 相邻格子
                if 0 <= x < m and 0 <= y < n and dfs(x, y, k + 1):
                    return True  # 搜到了！
            board[i][j] = word[k]  # 恢复现场
            return False  # 没搜到
        return any(dfs(i, j, 0) for i in range(m) for j in range(n))


    # ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ LeetCode 200 —— 岛屿数量 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    def numIslands(
        self, grid: List[List[str]]
    ) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        islands = 0
        def bfs(si: int, sj: int) -> None:
            queue: Deque[Tuple[int, int]] = deque([(si, sj)])
            grid[si][sj] = '0'
            while queue:
                x, y = queue.popleft()
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1':
                        grid[nx][ny] = '0'
                        queue.append((nx, ny))
                        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    islands += 1
                    bfs(i, j)    
        return islands

    
    # ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ LeetCode 994 —— 腐烂的橘子 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    def orangesRotting(
        self, grid: List[List[int]]
    ) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        fresh = 0
        queue: Deque[Tuple[int, int]] = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))
        
        minutes = 0
        while queue and fresh:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in (-1, 0), (0, -1), (1, 0), (0, 1):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh -= 1
                        queue.append((nx, ny))
            minutes += 1
        return -1 if fresh else minutes

    
    # ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ LeetCode 417 —— 太平洋大西洋水流问题 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    def pacificAtlantic(
        self, heights: List[List[int]]
    ) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        def bfs(starts: List[Tuple[int, int]]) -> Set[Tuple[int, int]]:
            queue = deque(starts)
            visited = set(starts)
            while queue:
                x, y = queue.popleft()
                for nx, ny in (x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1):
                    if 0 <= nx < m and 0 <= ny < n and heights[nx][ny] >= heights[x][y] and (nx, ny) not in visited:
                        queue.append((nx, ny))
                        visited.add((nx, ny))
            return visited
        pacific = [(0, i) for i in range(n)] + [(i, 0) for i in range(1, m)]
        atlantic = [(m - 1, i) for i in range(n - 1)] + [(i, n - 1) for i in range(m)]
        return list(map(list, bfs(pacific) & bfs(atlantic)))


    # ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ LeetCode 695 —— 岛屿的最大面积 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    def maxAreaOfIsland(
        self, grid: List[List[int]]
    ) -> int:
        m, n = len(grid), len(grid[0])

        def bfs(i: int, j: int) -> int:
            num_island = 0
            q = deque([(i, j)])
            grid[i][j] = 0
            while len(q):
                num_island += 1
                x, y = q.popleft()
                for dx, dy in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                    if 0 <= dx < m and 0 <= dy < n and grid[dx][dy] == 1:
                        grid[dx][dy] = 0
                        q.append((dx, dy))
            return num_island
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans = max(ans, bfs(i, j))
        return ans


    # ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ LeetCode 1162 —— 地图分析 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    def maxDistance(
        self, grid: List[List[int]]
    ) -> int:
        m, n = len(grid), len(grid[0])
        dist = [[float('inf') for _ in range(n)] for _ in range(m)]
        starts = []
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 1:
                    starts.append((i, j))
                    dist[i][j] = 0
        if not len(starts) or len(starts) == m * n:
            return -1
        q = deque(starts)
        while len(q):
            x, y = q.popleft()
            grid[x][y] = 2
            for dx, dy in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                if 0 <= dx < m and 0 <= dy < n and grid[dx][dy] == 0:
                    dist[dx][dy] = dist[x][y] + 1
                    q.append((dx, dy))
                    grid[dx][dy] = 2
        return max(map(max, dist))

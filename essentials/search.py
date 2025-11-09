class SearchToolKit:
    # ★★★★★ ░░░░░░░░░░░░░░░░░░░░ LeetCode 51 —— N 皇后 ░░░░░░░░░░░░░░░░░░░░ ★★★★★
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        N 皇后问题 - 经典回溯算法
            1. 逐行放置：每行必须且只能放一个皇后
            2. 剪枝条件：检查列和两条对角线是否被占用
            3. 对角线规律：
               - 主对角线(↘)：r + c 相同
               - 副对角线(↙)：r - c 相同（加偏移避免负数）
            4. 状态记录：用布尔数组记录占用情况，避免重复计算
        """
        ans: List[List[str]] = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        col = [False] * n
        diag1 = [False] * (2 * n - 1)  # r + c
        diag2 = [False] * (2 * n - 1)  # r - c + (n - 1)

        def dfs(r: int) -> None:
            if r == n:
                ans.append([''.join(row) for row in board])
                return

            for c in range(n):
                d1 = r + c
                d2 = r - c + n - 1
                if not col[c] and not diag1[d1] and not diag2[d2]:
                    board[r][c] = 'Q'
                    col[c] = diag1[d1] = diag2[d2] = True
                    dfs(r + 1)
                    board[r][c] = '.'
                    col[c] = diag1[d1] = diag2[d2] = False

        dfs(0)
        return ans


    # ★★★★★ ░░░░░░░░░░░░░░░░░░░░░ LeetCode 212 —— 单词搜索 II ░░░░░░░░░░░░░░░░░░░░░ ★★★★★
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        Trie + 网格 DFS 

        思路小结
            1. 先把所有 words 插入一棵 Trie，节点记录 children 和 word（若为某单词结尾）。
            2. 从每个格子 (i,j) 出发做 DFS，路径上沿着 Trie 往下走：
                 - 若当前字符不在 now.children 中，剪枝返回。
                 - 若 now.word 不为空，说明找到一个完整单词，加入答案集合。
            3. DFS 过程中用临时标记（比如 '#'）避免重复走回同一个格子，回溯时恢复。
            4. 利用 Trie 共享前缀 + 网格剪枝，避免对每个单词单独在板上暴力搜索。
        """
        class Trie:
            def __init__(self):
                self.children = defaultdict(Trie)
                self.word = None
            
            def insert(self, word: str) -> None:
                node = self
                for ch in word:
                    node = node.children[ch]
                node.word = word

        trie = Trie()
        for word in words:
            trie.insert(word)
        
        m, n = len(board), len(board[0])
        ans = set()

        def dfs(now: Trie, i: int, j: int) -> None:
            if board[i][j] not in now.children:
                return
            ch = board[i][j]
            now = now.children[ch]
            nonlocal ans
            if now.word is not None:
                ans.add(now.word)
            
            board[i][j] = '#'
            for di, dj in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if 0 <= di < m and 0 <= dj < n:
                    dfs(now, di, dj)
            board[i][j] = ch
        
        for i in range(m):
            for j in range(n):
                dfs(trie, i, j)
        
        return list(ans)

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

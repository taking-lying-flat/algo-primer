class BacktrackingToolkit:
    # ░░░░░░░░░░░░░░ LeetCode 78 · 子集 ░░░░░░░░░░░░░░
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        subsets = []
        path = []
        def dfs(u: int) -> None:
            if u == n:
                subsets.append(path[:])
                return 
            dfs(u + 1)
            path.append(nums[u])
            dfs(u + 1)
            path.pop()
        dfs(0)
        return subsets

    
    # ░░░░░░░░░░░░░░ LeetCode 78 · 子集 ░░░░░░░░░░░░░░
    def subsets_bitmask(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        subsets = []
        def dfs(u: int, mask: int) -> None:
            if u == n:
                subset = []
                for i in range(n):
                    if mask & (1 << i):
                        subset.append(nums[i])
                subsets.append(subset)
                return 
            dfs(u + 1, mask)
            dfs(u + 1, mask | (1 << u))
        dfs(0, 0)
        return subsets

    
    # ░░░░░░░░░░░░░░ LeetCode 90 · 子集 II ░░░░░░░░░░░░░░
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        on_path = []
        ans = []
        def dfs(u: int) -> None:
            if u == len(nums):
                ans.append(on_path[:])
                return
            x = nums[u]
            on_path.append(x)
            dfs(u + 1)
            on_path.pop()
            # 不选 x，那么后面所有等于 x 的数都不选
            # 如果不跳过这些数，会导致「选 x 不选 x'」和「不选 x 选 x'」这两种情况都会加到 ans 中
            u += 1
            while u < n and nums[u] == x:
                u += 1
            dfs(u)
        dfs(0)
        return ans

    
    # ░░░░░░░░░░░░░░ LeetCode 46 · 全排列 ░░░░░░░░░░░░░░
    @staticmethod
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        path = []
        visited = [False] * n
        def dfs(u: int) -> None:
            if u == n:
                result.append(path[:])
                return
            for i in range(n):
                if not visited[i]:
                    visited[i] = True
                    path.append(nums[i])
                    dfs(u + 1)
                    path.pop()
                    visited[i] = False      
        dfs(0)
        return result

    
    # ░░░░░░░░░░░░░░ LeetCode 46 · 全排列 ░░░░░░░░░░░░░░
    def permute_bitmask(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        path = []
        def dfs(u: int, mask: int) -> None:
            if u == n:
                result.append(path[:])
                return 
            for i in range(n):
                if not (mask & (1 << i)):
                    path.append(nums[i])
                    dfs(u + 1, mask | (1 << i))
                    path.pop()
        dfs(0, 0)
        return result

    
    # ░░░░░░░░░░░░░░ LeetCode 47 · 全排列 II（有重复） ░░░░░░░░░░░░░░
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        cnt = Counter(nums)
        n = len(nums)
        res: List[List[int]] = []
        on_path = [0] * n  # 预分配
        def dfs(i: int) -> None:
            if i == n:
                res.append(on_path.copy())
                return
            for x in cnt:
                if cnt[x] == 0:
                    continue
                cnt[x] -= 1
                on_path[i] = x
                dfs(i + 1)
                cnt[x] += 1
        dfs(0)
        return res

    
    # ░░░░░░░░░░░░░░ LeetCode 77 · 组合 ░░░░░░░░░░░░░░
    def combine(self, n: int, k: int) -> List[List[int]]:
        result: List[List[int]] = []
        path: List[int] = []
        def dfs(u: int, start: int) -> None:
            if u == k:
                result.append(path[:])
                return
            if k - u > n - start:
                return
            for i in range(start, n):
                path.append(i + 1)
                dfs(u + 1, i + 1)
                path.pop()
        dfs(0, 0)
        return result

    
    # ░░░░░░░░░░░░░░ LeetCode 77 · 组合 ░░░░░░░░░░░░░░
    def combine_bitmask(self, n: int, k: int) -> List[List[int]]:
        result: List[int] = []
        def dfs(u: int, cnt: int, mask: int) -> None:
            if cnt + n - u < k:
                return
            if cnt == k:
                path = []
                for i in range(n):
                    if mask & (1 << i):
                        path.append(i + 1)
                result.append(path)
                return
            if u == n:  
                return
            dfs(u + 1, cnt + 1, mask | (1 << u))
            dfs(u + 1, cnt, mask)
        dfs(0, 0, 0)
        return result

    
    # ░░░░░░░░░░░ LeetCode 22 —— 括号生成 ░░░░░░░░░░░
    def generateParenthesis(self, n: int) -> List[str]:
        ans: List[str] = []
        chosen: List[str] = []
        def dfs(i: int, open_count: int) -> None:
            if i == n * 2:
                ans.append(''.join(chosen))
                return
            if open_count < n:
                chosen.append('(')
                dfs(i + 1, open_count + 1)
                chosen.pop()
            if i - open_count < open_count:
                chosen.append(')')
                dfs(i + 1, open_count)
                chosen.pop()
        dfs(0, 0)
        return ans

    
    # ░░░░░░░░░░░ LeetCode 17 —— 电话号码的字母组合 ░░░░░░░░░░░
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        MAPPING = "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"
        ans: List[str] = []
        chosen: List[str] = []
        def dfs(i: int) -> None:
            if i == len(digits):
                ans.append(''.join(chosen))
                return 
            idx = ord(digits[i]) - ord('0')
            for ch in MAPPING[idx]:  # 尝试该数字对应的所有字母
                chosen.append(ch)
                dfs(i + 1)
                chosen.pop()
        dfs(0)
        return ans


# ░░░░░░░░░░░ LeetCode 131 —— 分割回文串 ░░░░░░░░░░░
    @staticmethod
    def partition(s: str) -> List[List[str]]:
        """
        将字符串分割成若干回文子串
            1. 回溯框架：枚举每个分割位置
            2. 选择空间：从当前位置到字符串末尾的所有子串
            3. 剪枝条件：只有回文串才继续递归
            4. 终止条件：指针到达字符串末尾
            5. 回溯恢复：path.pop() 撤销选择
        """
        n = len(s)
        ans = []
        path = []
    
        def dfs(i: int) -> None:
            if i == n:                    # 分割完毕
                ans.append(path.copy())   # 必须复制！
                return
            
            for j in range(i, n):         # 枚举分割位置
                t = s[i:j+1]              # 候选子串
                if t == t[::-1]:          # 是回文串
                    path.append(t)        # 做出选择
                    dfs(j + 1)            # 递归剩余部分
                    path.pop()            # 撤销选择
        
        dfs(0)
        return ans

    # ░░░░░░░░░░░░░░ LeetCode 39 —— 组合总和 ░░░░░░░░░░░░░░
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
       candidates.sort()
       ans: List[List[int]] = []
       path: List[int] = []
       def dfs(u: int, left: int) -> None:
           if left == 0:
               ans.append(path.copy())
               return
           if u == len(candidates) or left < candidates[u]:
               return
           dfs(u + 1, left)
           path.append(candidates[u])
           dfs(u, left - candidates[u])
           path.pop()
       dfs(0, target)
       return ans

    
    # ░░░░░░░░░░░░░░ LeetCode 51 —— N 皇后 ░░░░░░░░░░░░░░
    @staticmethod
    def solveNQueens(n: int) -> List[List[str]]:
        """
        N 皇后问题 - 经典回溯算法
            1. 逐行放置：每行必须且只能放一个皇后
            2. 剪枝条件：检查列和两条对角线是否被占用
            3. 对角线规律：
               - 主对角线(↘)：r + c 相同
               - 副对角线(↙)：r - c 相同（加偏移避免负数）
            4. 状态记录：用布尔数组记录占用情况，避免重复计算
        """
        ans = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        col = [False] * n
        diag1 = [False] * (n * 2 - 1)
        diag2 = [False] * (n * 2 - 1)

        def dfs(r: int):
            if r == n:
                ans.append([''.join(row) for row in board])
                return
            
            # 在 (r,c) 放皇后
            for c, ok in enumerate(col):
                if not ok and not diag1[r + c] and not diag2[r - c]:   # 判断能否放皇后
                    board[r][c] = 'Q'
                    col[c] = diag1[r + c] = diag2[r - c] = True        # 皇后占用了 c 列和两条斜线
                    dfs(r + 1)
                    board[r][c] = '.'
                    col[c] = diag1[r + c] = diag2[r - c] = False       # 恢复现场
        
        dfs(0)
        return ans

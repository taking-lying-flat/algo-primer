class GeneralToolkit:
    # ░░░░░░░░░░░░░░░░░░░░░░ LeetCode 14 —— 最长公共前缀 ░░░░░░░░░░░░░░░░░░░░░░
    def longestCommonPrefix(
        self, strs: List[str]
    ) -> str:
        lcp = 0
        for col in zip(*strs):
            if len(set(col)) > 1:
                break
            lcp += 1
        return strs[0][:lcp]

    
    # ░░░░░░░░░░░░░░░░░░░░░░ LeetCode 169 —— 多数元素 ░░░░░░░░░░░░░░░░░░░░░░
    def majorityElement(
        self, nums: List[int]
    ) -> int:
        candidate = None
        cnt = 0
        for num in nums:
            if cnt == 0:
                candidate = num
            cnt += (1 if num == candidate else -1)
        return candidate

    
    # ░░░░░░░░░░░░░░░░░░░░░░ LeetCode 54 —— 螺旋矩阵 ░░░░░░░░░░░░░░░░░░░░░░
    def spiralOrder(
        self, matrix: List[List[int]]
    ) -> List[int]:
        DIRS = (0, 1), (1, 0), (0, -1), (-1, 0) 
        m, n = len(matrix), len(matrix[0])
        ans: List[int] = []
        i = j = di = 0
        for _ in range(m * n):
            ans.append(matrix[i][j])
            matrix[i][j] = None
            x, y = i + DIRS[di][0], j + DIRS[di][1]
            if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] is None:
                di = (di + 1) % 4
            i += DIRS[di][0]
            j += DIRS[di][1]
        return ans

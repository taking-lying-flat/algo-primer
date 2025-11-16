class MonoStackUtils:
    # ★★★★★ ░░░░░░░░░░░ HackerRank · Min Max Riddle（单调栈 · 每窗最小值的最大值） ░░░░░░░░░░░ ★★★★★
    def riddle(
        self, arr: List[int]
    ) -> List[int]:
        """
        找到每个窗口大小(1到n)中，所有窗口最小值的最大值
            1. 单调栈求边界：一次遍历同时找到每个元素的左右边界
               - left[i] ：左侧第一个 < arr[i] 的位置，默认 -1
               - right[i]：右侧第一个 < arr[i] 的位置，默认  n
               - 维护单调不降的索引栈；当前值更小则弹栈并写右边界；栈顶即为左边界
            2. 计算窗口长度：len = right[i] - left[i] - 1；更新 ans[len-1]
            3. 后向填充：ans[k] = max(ans[k], ans[k+1])
        """
        n = len(arr)
        left = [-1] * n
        right = [n] * n
        stack: List[int] = []

        for i in range(n):
            while stack and arr[i] < arr[stack[-1]]:
                prev = stack.pop()
                right[prev] = i
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        ans = [0] * n
        for i in range(n):
            length = right[i] - left[i] - 1
            ans[length - 1] = max(ans[length - 1], arr[i])

        for k in range(n - 2, -1, -1):
            ans[k] = max(ans[k], ans[k + 1])

        return ans


    # ★★★★★ ░░░░░░░░░░░ LeetCode 85 —— 最大矩形 ░░░░░░░░░░░ ★★★★★
    def maximalRectangle(
        self, matrix: List[List[str]]
    ) -> int:
        def largestRectangleArea(heights: List[int]) -> int:
            heights.append(-1)  # 哨兵: 强制清空栈中所有元素
            st = [-1]           # 哨兵: 作为左边界的起点（当栈中只有一个元素时的左边界）
            ans = 0
            for right, h in enumerate(heights):
                while len(st) > 1 and h <= heights[st[-1]]:
                    i = st.pop()   # 弹出的柱子作为矩形的高
                    left = st[-1]  # 栈顶元素是左边第一个更矮柱子的位置, 栈底 -> 栈顶递增
                    ans = max(ans, heights[i] * (right - left - 1))
                st.append(right)
            return ans
            
        n_cols = len(matrix[0])
        heights: List[int] = [0] * n_cols
        max_area = 0
        for row in matrix:
            for j, val in enumerate(row):
                heights[j] = heights[j] + 1 if val == '1' else 0
            max_area = max(max_area, largestRectangleArea(heights[:]))
        return max_area

    
    # ★★★★★ ░░░░░░░░░░░ LeetCode 221 —— 最大正方形 ░░░░░░░░░░░ ★★★★★
    def maximalSquare(
        self, matrix: List[List[str]]
    ) -> int:
        def largestSquareEdge(heights: List[int]) -> int:
            heights.append(0)  # 哨兵：强制清空栈
            stack: List[int] = [-1]  # 哨兵：左边界起点
            max_edge: int = 0
            for right, h in enumerate(heights):
                while len(stack) > 1 and h <= heights[stack[-1]]:
                    i = stack.pop()
                    left = stack[-1]
                    edge = min(heights[i], right - left - 1)  # 正方形边长 = min(高度, 宽度)
                    max_edge = max(max_edge, edge)
                stack.append(right)
            return max_edge
        
        n_cols: int = len(matrix[0])
        heights: List[int] = [0] * n_cols
        max_edge: int = 0
        for row in matrix:
            for j, val in enumerate(row):
                heights[j] = heights[j] + 1 if val == '1' else 0
            max_edge = max(max_edge, largestSquareEdge(heights[:]))
        return max_edge * max_edge

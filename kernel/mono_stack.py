class MonotonicStackTemplates:
    # ░░░░░░░░░░░ 找每个元素右边第一个更大的元素 ░░░░░░░░░░░
    @staticmethod
    def next_greater_element(nums: List[int]) -> List[int]:
        """
        维护单调递减栈: 栈底 → 栈顶递减
            - 栈内存储还没找到答案的元素下标
            - 当遇到更大元素时，栈内元素依次出栈并记录答案
            - 当前元素就是这些出栈元素右边第一个更大的值
        """
        n = len(nums)
        result = [-1] * n  # 初始化: 默认右边没有更大的元素
        stack = []         # 单调递减栈，存储还在等待答案的元素下标
        for i, num in enumerate(nums):
            # 当前元素比栈顶大 → 栈内元素找到了它们的答案, 就是当前元素
            while stack and num > nums[stack[-1]]:
                prev_idx = stack.pop()      # 弹出找到答案的元素
                result[prev_idx] = i        # 它的答案就是当前元素的位置
            stack.append(i)  # 当前元素入栈，等待找到它右边第一个更大的
        return result

    
    # ░░░░░░░░░░░ 找每个元素右边第一个更小的元素 ░░░░░░░░░░░
    @staticmethod
    def next_smaller_element(nums: List[int]) -> List[int]:
        """
        维护单调递增栈: 栈底 → 栈顶递增
            - 栈内存储还没找到答案的元素下标
            - 当遇到更小元素时，栈内元素依次出栈并记录答案
            - 当前元素就是这些出栈元素右边第一个更小的值
        """
        n = len(nums)
        result = [-1] * n  # 初始化: 默认右边没有更小的元素
        stack = []         # 单调递增栈，存储还在等待答案的元素下标
        for i, num in enumerate(nums):
            # 当前元素比栈顶小 → 栈内元素找到了它们的答案（就是当前元素）
            while stack and num < nums[stack[-1]]:
                prev_idx = stack.pop()      # 弹出找到答案的元素
                result[prev_idx] = i        # 它的答案就是当前元素的位置
            stack.append(i)  # 当前元素入栈，等待找到它右边第一个更小的
        return result

    
    # ░░░░░░░░░░░ 找每个元素左边第一个更大的元素 ░░░░░░░░░░░
    @staticmethod
    def prev_greater_element(nums: List[int]) -> List[int]:
        """
        维护单调递减栈（栈底 → 栈顶递减）
            - 栈内存储可能成为后续元素答案的"候选者"
            - 弹出所有不可能成为答案的元素（≤当前元素的）
            - 栈顶元素就是当前元素左边第一个更大的
        """
        n = len(nums)
        result = [-1] * n  # 初始化: 默认左边没有更大的元素
        stack = []         # 单调递减栈，存储可能成为答案的候选元素下标
        for i, num in enumerate(nums):
            # 弹出所有 ≤ 当前元素的栈顶, 它们不可能是后续元素的答案了
            while stack and num >= nums[stack[-1]]:
                stack.pop()  # 仅弹出，不记录
            # 经过弹出后，栈顶（如果存在）就是当前元素的答案
            if stack:
                result[i] = stack[-1]  # 当前元素的答案是栈顶
            stack.append(i)  # 当前元素入栈，可能成为后续元素的答案
        return result

    
    # ░░░░░░░░░░░ 找每个元素左边第一个更小的元素 ░░░░░░░░░░░
    @staticmethod
    def prev_smaller_element(nums: List[int]) -> List[int]:
        """
        维护单调递增栈: 栈底 → 栈顶递增
            - 栈内存储可能成为后续元素答案的"候选者"
            - 弹出所有不可能成为答案的元素（≥当前元素的）
            - 栈顶元素就是当前元素左边第一个更小的
        """
        n = len(nums)
        result = [-1] * n  # 初始化: 默认左边没有更小的元素
        stack = []         # 单调递增栈，存储可能成为答案的候选元素下标
        for i, num in enumerate(nums):
            # 弹出所有 ≥ 当前元素的栈顶, 它们不可能是后续元素的答案了
            while stack and num <= nums[stack[-1]]:
                stack.pop()  # 仅弹出，不记录
            # 经过弹出后，栈顶（如果存在）就是当前元素的答案
            if stack:
                result[i] = stack[-1]  # 当前元素的答案是栈顶
            stack.append(i)  # 当前元素入栈，可能成为后续元素的答案
        return result


 # ░░░░░░░░░░░░░░ HackerRank · Min Max Riddle ░░░░░░░░░░░░░░
    @staticmethod
    def riddle(arr: List[int]) -> List[int]:
        """
        找到每个窗口大小(1到n)中，所有窗口最小值的最大值
            1. 单调栈求边界: 一次遍历同时找到每个元素的左右边界
               - left[i]: 左边第一个比 arr[i] 小的元素位置，默认 -1
               - right[i]: 右边第一个比 arr[i] 小的元素位置，默认 n
               - 使用单调递增栈，当前元素比栈顶小时弹出并更新右边界
               - 栈顶元素即为当前元素的左边界
            2. 计算窗口长度: 对每个元素 arr[i]
               - 能作为最小值的最大窗口长度 = right[i] - left[i] - 1
               - 更新该长度窗口的最大最小值 ans[length-1]
            3. 后向传播: 从大窗口到小窗口填充答案
               - 若窗口大小 k 无答案，用 k+1 的答案填充
               - 因为大窗口的最小值也可作为小窗口的最小值
        """
        n = len(arr)
        left = [-1] * n
        right = [n] * n
        stack = []
    
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
    
        for i in range(n - 2, -1, -1):
            ans[i] = max(ans[i], ans[i + 1])
    
        return ans

    # ░░░░░░░░░░░ LeetCode 84 —— 柱状图中最大的矩形 ░░░░░░░░░░░
    @staticmethod
    def largestRectangleArea(heights: List[int]) -> int:
        """
        单调递增栈求最大矩形面积
             1. 对每个柱子，找左右两侧第一个更矮的柱子作为边界
             2. 维护单调递增栈，遍历时同时确定左右边界
             3. 当前柱子 ≤ 栈顶时，栈顶柱子的右边界确定（就是当前位置）
             4. 弹栈后，新栈顶是当前柱子的左边界
             5. 遍历结束后，计算每个柱子为高的最大矩形面积
        """
        n = len(heights)
        left_bound: List[int] = [-1] * n    # 每个柱子左侧第一个更矮柱子的下标
        right_bound: List[int] = [n]  * n   # 每个柱子右侧第一个更矮柱子的下标
        stack: List[int] = []               # 自栈底 → 栈顶, 对应的柱子高度严格递增, 存下标
        # 遍历 heights，维护右边界，同时填充左边界
        for idx, height in enumerate(heights):
            # 处理出栈: 当前高度 ≤ 栈顶对应高度 ⇒ 栈顶柱子的右边界确定为 idx
            # 当前高度 > 栈顶高度时，不淘汰（不出栈），直接将当前元素入栈
            while stack and height <= heights[stack[-1]]:
                prev_idx = stack.pop()
                right_bound[prev_idx] = idx
            if stack:     # 此时栈顶（若存在）就是 idx 的左侧第一个更矮柱子
                left_bound[idx] = stack[-1]
            stack.append(idx)

        max_area = 0
        for idx, height in enumerate(heights):
            width = right_bound[idx] - left_bound[idx] - 1
            max_area = max(max_area, height * width)
        return max_area

    # ░░░░░░░░░░░ LeetCode 85 —— 最大矩形 ░░░░░░░░░░░
    @staticmethod
    def maximalRectangle(matrix: List[List[str]]) -> int:
        """
        单调栈 + 柱状图求二维最大矩形
             1. 逐行将二维矩阵转化为柱状图问题
             2. heights[j] 表示第 j 列向上连续 '1' 的个数
             3. 对每一行，更新 heights 数组（遇 '0' 归零，遇 '1' 累加）
             4. 将每行的 heights 作为柱状图，求最大矩形面积
             5. 使用哨兵技巧简化边界处理
        """
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

    # ░░░░░░░░░░░ LeetCode 221 —— 最大正方形 ░░░░░░░░░░░
    @staticmethod
    def maximalSquare(matrix: List[List[str]]) -> int:
        """
        单调栈求二维最大正方形
             1. 类似最大矩形，逐行转化为柱状图问题
             2. 对每个可能的矩形，正方形边长 = min(高度, 宽度)
             3. 使用单调栈找到每个柱子能扩展的最大宽度
             4. 计算以每个柱子为高的最大正方形边长
             5. 返回最大边长的平方作为面积
        """
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

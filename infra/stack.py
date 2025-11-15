# ░░░░░░░░░░░ LeetCode 155 —— 最小栈 ░░░░░░░░░░░
class MinStack:
    """
    支持 O(1) 时间获取最小值的栈
        - 使用辅助栈同步维护每个状态对应的最小值
        - 初始化时加入哨兵 float('inf')，避免空栈判断
        - push 时：辅助栈压入 min(当前值, 栈顶最小值)
        - pop 时：两个栈同步弹出
    """
    def __init__(self):
        self.stack = []
        self.min_stack = [float('inf')]  # 哨兵：避免空栈判断
    
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_stack.append(min(val, self.min_stack[-1]))
    
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
    
    def top(self) -> int:
        return self.stack[-1]
    
    def getMin(self) -> int:
        return self.min_stack[-1]


class StackAlgoUtils:
    # ░░░░░░░░░░░░░░ LeetCode 20 —— 有效的括号 ░░░░░░░░░░░░░░
    @staticmethod
    def isValid(s: str) -> bool:
        """
        括号匹配验证
            1. 左括号入栈对应的右括号
            2. 遇到右括号时，栈顶应该匹配
            3. 最后栈应该为空
        """
        if len(s) % 2:
            return False
        pairs = {'(': ')', '[': ']', '{': '}'}
        stack: List[str] = []
        for c in s:
            if c in pairs:
                stack.append(pairs[c])
            elif not stack or stack.pop() != c:
                return False
        return not stack

    # ░░░░░░░░░░░ LeetCode 32 —— 最长有效括号 ░░░░░░░░░░░
    @staticmethod
    def longestValidParentheses(s: str) -> int:
        """
            1. 用栈存放索引，初始压入 -1 作为哨兵
            2. 遍历字符串：
               - 遇到 '('，将当前索引压入栈
               - 遇到 ')'，先 pop 栈顶：
                 • 若栈空：说明没有匹配的 '('，将当前索引 i 作为新的哨兵压入
                 • 否则：当前有效子串长度 = i - stack[-1]，更新 max_len
            3. 返回 max_len
        """
        max_len = 0
        stack: List[int] = [-1]  # 哨兵：有效子串起点前的位置
        
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:        # 遇到多余的 ')'，重置哨兵
                    stack.append(i)
                else:                # 以当前 ')' 为结尾的有效子串长度
                    max_len = max(max_len, i - stack[-1])
        
        return max_len

    # ░░░░░░░░░░░░░░ LeetCode 394 —— 字符串解码 ░░░░░░░░░░░░░░
    @staticmethod
    def decodeString(s: str) -> str:
        """
        使用栈解码编码字符串
        栈保存: (外层字符串, 重复次数) - 每次遇到 '[' 时保存当前状态
            1. 遇到数字: 累积重复次数
            2. 遇到 '[': 将当前状态压栈，重置变量处理内层
            3. 遇到 ']': 弹栈恢复外层状态，将内层结果重复后拼接
            4. 遇到字母: 直接添加到当前字符串
        """
        stack, multi, res = [], 0, ""
        for c in s:
            if c == '[':
                stack.append((res, multi))
                multi, res = 0, ""
            elif c == ']':
                last_res, cur_multi = stack.pop()
                res = last_res + res * cur_multi
            elif '0' <= c <= '9':
                multi = multi * 10 + int(c)
            else:
                res += c
        
        return res

    # ░░░░░░░░░░░ LeetCode 739 —— 每日温度 ░░░░░░░░░░░
    @staticmethod
    def dailyTemperatures(temperatures: List[int]) -> List[int]:
        """
        单调递减栈求等待天数
             1. 维护单调递减栈，存储还未找到更高温度的日期
             2. 遍历每天温度，如果比栈顶温度高，栈顶找到答案
             3. 答案是当前日期减去栈顶日期（等待的天数）
             4. 持续弹栈并记录答案，直到栈顶温度 ≥ 当前温度
             5. 当前日期入栈，等待找到更高温度
        """
        n = len(temperatures)
        ans: List[int] = [0] * n
        stack: List[int] = []  # 下标栈，自底→顶温度递减
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev = stack.pop()
                ans[prev] = i - prev
            stack.append(i)
        return ans

    # ░░░░░░░░░░░░░░ LeetCode 1249 · 移除无效的括号 ░░░░░░░░░░░░░░
    def minRemoveToMakeValid(s: str) -> str:
        index_to_move = set()
        stack = []
    
        for i, c in enumerate(s):
            if c not in "()":
                continue
            elif c == '(':
                stack.append(i)
            elif not stack:
                index_to_move.add(i)
            else:
                stack.pop()
        
        index_to_move = index_to_move.union(set(stack))
        string_builder = []
        for i, c in enumerate(s):
            if i not in index_to_move:
                string_builder.append(c)
        return "".join(string_builder)

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

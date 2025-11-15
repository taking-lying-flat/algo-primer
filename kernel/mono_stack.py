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

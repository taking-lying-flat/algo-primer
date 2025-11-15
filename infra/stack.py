# ░░░░░░░░░░░ LeetCode 155 —— 最小栈 ░░░░░░░░░░░
class MinStack:
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
    def isValid(
        self, s: str
    ) -> bool:
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
    def longestValidParentheses(
        self, s: str
    ) -> int:
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
    def decodeString(
        self, s: str
    ) -> str:
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

    
    # ░░░░░░░░░░░░░░ LeetCode 1249 · 移除无效的括号 ░░░░░░░░░░░░░░
    def minRemoveToMakeValid(
        self, s: str
    ) -> str:
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

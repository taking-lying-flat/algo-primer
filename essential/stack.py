class MonoStackUtils:
    # ★★★★★ HackerRank · Min Max Riddle（单调栈 · 每窗最小值的最大值） ★★★★★
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

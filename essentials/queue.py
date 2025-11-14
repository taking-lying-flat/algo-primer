class QueueAlgoUtils:
    # ░░░░░░░░░░░ LeetCode 239 —— 滑动窗口最大值 ░░░░░░░░░░░
    def maxSlidingWindow(
      self, nums: List[int], k: int
    ) -> List[int]:
        """
        单调队列: 返回每个长度为 k 的滑动窗口中的最大值
            1. 维护一个单调递减队列（存储索引）
            2. 队首始终是当前窗口的最大值
            3. 新元素入队时，移除队尾所有小于等于它的元素
            4. 队首元素超出窗口范围时出队
           
        单调队列特性:
            - 队列中的元素按值单调递减: 队首最大，队尾最小
            - 队首（左端）: 存储当前窗口最大值的索引
            - 队尾（右端）: 最近加入的元素
            - 保证了 O(1) 时间获取窗口最大值
        """
        ans: List[int] = []
        mono_q: Deque[int] = deque()
        for i, x in enumerate(nums):
            while mono_q and nums[mono_q[-1]] <= x:
                mono_q.pop()
            mono_q.append(i)
            if mono_q[0] <= i - k:
                mono_q.popleft()
            if i >= k - 1:
                ans.append(nums[mono_q[0]])
        return ans

    
    # ░░░░░░░░░░░ LeetCode 2762 —— 不间断子数组 ░░░░░░░░░░░
    def continuousSubarrays(
      self, nums: List[int]
    ) -> int:
        min_q = deque()
        max_q = deque()
        ans = left = 0

        for right, x in enumerate(nums):
            # 更新 min_q：维护递增
            while len(min_q) and x <= nums[min_q[-1]]:
                min_q.pop()
            min_q.append(right)
            
            # 更新 max_q：维护递减
            while len(max_q) and x >= nums[max_q[-1]]:
                max_q.pop()
            max_q.append(right)

            while nums[max_q[0]] - nums[min_q[0]] > 2:
                left += 1
                # 右移 left 后，原来在窗口最左侧之前的下标已经不在窗口中
                if min_q[0] < left:
                    min_q.popleft()
                if max_q[0] < left:
                    max_q.popleft()
            ans += right - left + 1
        return ans

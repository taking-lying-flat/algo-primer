class PointerParadigms:
    # ░░░░░░░░░░░ LeetCode 5 —— 最长回文子串 ░░░░░░░░░░░
    @staticmethod
    def longestPalindrome(s: str) -> str:
        """
        中心扩展法: 以每个字符 / 字符间隙为中心向两侧扩张, 找到最长回文
            1. 回文定义 → 左右字符对称相等
            2. 枚举两类中心:
               • 奇数中心: (i, i)
               • 偶数中心: (i, i+1)
            3. 扩张条件: 0 ≤ left < right < n 且 s[left] == s[right]
            4. 记录并更新最长区间 [start, end]
        """
        def expandAroundCenter(left: int, right: int) -> Tuple[int, int]:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left  -= 1
                right += 1
            return left + 1, right - 1      # 回到合法边界

        start, end = 0, 0
        for i in range(len(s)):
            odd_left,  odd_right  = expandAroundCenter(i, i)
            even_left, event_right = expandAroundCenter(i, i + 1)
            if odd_right - odd_left > end - start:
                start, end = odd_left, odd_right
            if event_right - even_left > end - start:
                start, end = even_left, event_right
        return s[start : end + 1]

    # ░░░░░░░░░░░ LeetCode 287 —— 寻找重复数 ░░░░░░░░░░░
    @staticmethod
    def findDuplicate(nums: List[int]) -> int:
        """
        Floyd 环检测算法（快慢指针）
            1. 将数组下标视为链表结点，下标 i 指向 nums[i]
            2. 由于存在重复数，链表必定形成环
            3. 使用快慢指针找到环中相遇点
            4. 从头结点和相遇点同步前进，相遇处即为环的入口（即重复数）
        """
        def next(i: int) -> int:
            """返回下一个结点，链表指针由 nums[i] 决定"""
            return nums[i]
    
        slow = fast = 0
        while True:
            slow = next(slow)
            fast = next(next(fast))
            if slow == fast:
                break
    
        head = 0
        while head != slow:
            slow = next(slow)
            head = next(head)
        return slow

    # ░░░░░░░░░░░ LeetCode 189 —— 轮转数组 ░░░░░░░░░░░
    @staticmethod
    def rotate(nums: List[int], k: int) -> None:
        """
        三次翻转法: 通过局部翻转实现整体轮转
            1. 轮转定义 → 右移 k 位等价于将后 k 个元素移到前面
            2. 双指针翻转: 从两端向中间交换
            3. 边界处理: k %= n 防止 k > n 的情况
        """
        def reverse(_from: int, _to: int) -> None:
            while _from < _to:
                nums[_from], nums[_to] = nums[_to], nums[_from]
                _from += 1
                _to -= 1
        
        n = len(nums)
        k %= n
        reverse(0, n - 1)    # 整体翻转
        reverse(0, k - 1)    # 前 k 个翻转
        reverse(k, n - 1)    # 后 n-k 个翻转

    # ░░░░░░░░░░░ LeetCode 11 —— 盛最多水的容器 ░░░░░░░░░░░
    @staticmethod
    def maxArea(height: List[int]) -> int:
        """
        相向双指针: 找两条线形成的最大面积
            1. 容器面积 = 宽度 × 高度 = (right-left) × min(h[left], h[right])
            2. 双指针从两端开始，初始宽度最大
            3. 每次移动较矮的那一端，因为：
               - 移动较高端：宽度减小，高度不增，面积必减小
               - 移动较矮端：宽度减小，但高度可能增加，面积可能增大
            4. 记录过程中的最大面积
        """
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            area = (right - left) * min(height[left], height[right])
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            max_area = max(max_area, area)
        return max_area

    # ░░░░░░░░░░░ LeetCode 15 —— 三数之和 ░░░░░░░░░░░
    @staticmethod
    def threeSum(nums: List[int]) -> List[List[int]]:
        """
        排序+相向双指针: 找所有和为 0 的三元组
            1. 先排序，方便去重和使用双指针
            2. 固定第一个数，用双指针在剩余部分找两数之和
            3. 去重技巧: 
               - 跳过重复的第一个数
               - 找到答案后跳过重复的第二、三个数
            4. 剪枝优化: 
               - 最小三数之和 > 0，后面不可能有解
               - 当前数与最大两数之和 < 0，跳过当前数
        """
        ans = []
        n = len(nums)
        nums.sort()

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] > 0:
                break
            if nums[i] + nums[-2] + nums[-1] < 0:
                continue
            
            left, right = i + 1, n - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif s < 0:
                    left += 1
                else:
                    right -= 1
        return ans

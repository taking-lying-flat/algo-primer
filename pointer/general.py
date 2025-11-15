class PointerParadigms:
    # ░░░░░░░░░░░░░░░░░░░░░░ LeetCode 5 —— 最长回文子串 ░░░░░░░░░░░░░░░░░░░░░░
    def longestPalindrome(
        self, s: str
    ) -> str:
        def expandAroundCenter(left: int, right: int) -> Tuple[int, int]:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        start, end = 0, 0
        for i in range(len(s)):
            odd_left,  odd_right  = expandAroundCenter(i, i)
            even_left, event_right = expandAroundCenter(i, i + 1)
            if odd_right - odd_left > end - start:
                start, end = odd_left, odd_right
            if event_right - even_left > end - start:
                start, end = even_left, event_right
        return s[start : end + 1]

  
    # ░░░░░░░░░░░░░░░░░░░░░░ LeetCode 287 —— 寻找重复数 ░░░░░░░░░░░░░░░░░░░░░░
    def findDuplicate(
        self, nums: List[int]
    ) -> int:
        def next(i: int) -> int:
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

    
    # ░░░░░░░░░░░░░░░░░░░░░░ LeetCode 189 —— 轮转数组 ░░░░░░░░░░░░░░░░░░░░░░
    def rotate(nums: List[int], k: int) -> None:
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

    
    # ░░░░░░░░░░░░░░░░░░░░░░ LeetCode 11 —— 盛最多水的容器 ░░░░░░░░░░░░░░░░░░░░░░
    def maxArea(
        self, height: List[int]
    ) -> int:
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

    
    # ░░░░░░░░░░░░░░░░░░░░░░ LeetCode 15 —— 三数之和 ░░░░░░░░░░░░░░░░░░░░░░
    def threeSum(
        self, nums: List[int]
    ) -> List[List[int]]:
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

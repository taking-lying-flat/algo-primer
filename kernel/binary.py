class BinarySearchTemplate:
    """
    1. rightmost_red — 适用于 True ... True | False ... False 模式
       - 序列前半部分都是 True（红区），后半部分都是 False（蓝区）
       - 返回最后一个 True 的位置
    
    2. leftmost_blue — 适用于 False ... False | True ... True 模式
       - 序列前半部分都是 False（红区），后半部分都是 True（蓝区）
       - 返回第一个 True 的位置
    核心思想：任何满足"单调性"的布尔函数都可以使用
    """
    def rightmost_red(
        self, left: int, right: int, is_red: Callable[[int], bool]
    ) -> int:
        """
        示例序列:  [T, T, T, T, F, F, F]
                            ↑
                        返回这个位置
        使用右中位数: (left + right + 1) // 2, 避免死循环
        case 1: mid 位置仍在红区, 更新 left = mid，保留 mid 作为候选答案
        case 2: mid 位置已经在蓝区, 更新 right = mid - 1，排除 mid
        """
        while left < right:
            mid = (left + right + 1) // 2
            if is_red(mid):
                left = mid
            else:
                right = mid - 1
        return left
    
    def leftmost_blue(
        self, left: int, right: int, is_blue: Callable[[int], bool]
    ) -> int:
        """
        示例序列:  [F, F, F, T, T, T, T]
                            ↑
                        返回这个位置
        # case 1: mid 位置已经在蓝区, 说明答案在 mid 或 mid 左边, 更新 right = mid，保留 mid 作为候选答案
        # case 2: mid 位置仍在红区, 说明答案一定在 mid 右边, 更新 left = mid + 1，排除 mid
        """
        while left < right:
            mid = (left + right) // 2
            if is_blue(mid):
                right = mid
            else:
                left = mid + 1
        return left

    def float_binary_search(
        self, left: float, right: float, check: Callable[[float], bool], eps: float = 1e-9
    ) -> float:
        """
        浮点数二分查找模板 - 寻找满足条件的最小值
        在连续区间 [left, right] 中找到满足 check(x) = True 的最小 x
        """
    while right - left > eps:
        mid = (left + right) / 2
        if check(mid):
            right = mid  # mid 满足条件，答案在 [left, mid]
        else:
            left = mid   # mid 不满足条件，答案在 [mid, right]
    return left  # 或 return right，差值小于 eps


class BinarySearchUtils:
    # ░░░░░░░░░░░░░░ LeetCode 34 —— 在排序数组中查找元素的第一个和最后一个位置 ░░░░░░░░░░░░░░
    def searchRange(
        self, nums: List[int], target: int
    ) -> List[int]:
        def find_last_red(left: int = 0, right: int = len(nums) - 1) -> int:
            while left < right:
                mid = (left + right + 1) // 2
                if nums[mid] <= target:
                    left = mid
                else:
                    right = mid - 1
            return left
        
        def find_first_blue(left: int = 0, right: int = len(nums) - 1) -> int:
            while left < right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            return left
        
        l1, l2 = find_last_red(0, len(nums) - 1), find_first_blue(0, len(nums) - 1)
        if not nums or nums[l1] != target:
            return [-1, -1]
        return [l2, l1]

    
    # ░░░░░░░░░░░ LeetCode 153 —— 寻找旋转排序数组中的最小值 ░░░░░░░░░░░
    def findMin(
        self, nums: List[int]
    ) -> int:
        """
        旋转排序数组中的最小值
             1. 旋转数组特点：存在一个断点，左边部分 > 右边部分
             2. 二分查找：比较 mid 和末尾元素
             3. 如果 nums[mid] <= nums[-1]，说明 mid 在右半部分，最小值在 mid 或左边
             4. 如果 nums[mid] > nums[-1]，说明 mid 在左半部分，最小值在右边
             5. 收缩区间直到找到最小值
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] <= nums[-1]:
                right = mid      # mid 可能是最小值，保留
            else:
                left = mid + 1   # mid 在左半部分，最小值在右边
        return nums[left]

    
    # ░░░░░░░░░░░ LeetCode 33 —— 搜索旋转排序数组 ░░░░░░░░░░░
    def search_rotated(
        self, nums: List[int], target: int
    ) -> int:
        """
        红 / 蓝 区划分由下式给出
            is_red(i) = (x <= target) ^ (x > pivot) ^ (target > pivot), 其中 pivot = nums[-1]
        · 若 target 在右段：
            红区 = 左段全部 + 右段中 x <= target
            蓝区 = 右段中 x > target
        · 若 target 在左段：
            红区 = 左段中 x <= target
            蓝区 = 其余元素
        """
        left, right = 0, len(nums) - 1
        pivot = nums[-1]
        def is_red(i: int) -> bool:
            x = nums[i]
            return (x <= target) ^ (x > pivot) ^ (target > pivot)
        while left < right:
            mid = (left + right + 1) // 2
            if is_red(mid):              # case 1: 红区→向右扩
                left = mid
            else:                        # case 2: 蓝区→向左收
                right = mid - 1
        return left if nums[left] == target else -1

    
    # ░░░░░░░░░░░ LeetCode 74 —— 搜索二维矩阵 ░░░░░░░░░░░
    def searchMatrix(
        self, matrix: List[List[int]], target: int
    ) -> bool:
        """
        搜索二维矩阵（每行递增，下一行首元素大于上一行末元素）
             1. 将二维矩阵视为一维有序数组
             2. 坐标转换：一维下标 i → 二维坐标 (i//n, i%n)
             3. 使用标准二分查找，找到最后一个 <= target 的位置
             4. 检查该位置的值是否等于 target
        """
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left < right:
            mid = (left + right + 1) // 2
            if matrix[mid // n][mid % n] <= target:
                left = mid
            else:
                right = mid - 1
        return matrix[left // n][left % n] == target

    
    # ░░░░░░░░░░░ LeetCode 240 —— 搜索二维矩阵 II ░░░░░░░░░░░
    def searchMatrixII(
        self, matrix: List[List[int]], target: int
    ) -> bool:
        """
        搜索二维矩阵 II（每行递增，每列递增）, 核心思想是Z字形搜索
             1. 从左下角或右上角开始（这里选择左下角）
             2. 当前元素比 target 小：只能向右移动（j++）
             3. 当前元素比 target 大：只能向上移动（i--）
             4. 每次比较可以排除一行或一列，类似 BST 的查找
        """
        m, n = len(matrix), len(matrix[0])
        i, j = m - 1, 0  # 从左下角开始
        while i >= 0 and j < n:
            x = matrix[i][j]
            if x < target:
                j += 1   # 当前值太小，向右移动
            elif x > target:
                i -= 1   # 当前值太大，向上移动
            else:
                return True
        return False


    # ░░░░░░░░░░░ LeetCode 2300 —— 咒语与药水的成功对数（排序 + 二分下界） ░░░░░░░░░░░
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        ans: List[int] = []
        potions.sort()
        for spell in spells:
            left, right = 0, len(potions)
            while left < right:
                mid = (left + right) // 2
                if spell * potions[mid] >= success:
                    right = mid
                else:
                    left = mid + 1
            ans.append(len(potions) - left)
        return ans


class BinaryAnswerUtils:
    # ░░░░░░░░░░░ LeetCode 274 —— H 指数 ░░░░░░░░░░░
    def hIndex(
        self, citations: List[int]
    ) -> int:
        """
        二分答案：最大 h 使得“引用次数 ≥ h”的论文数 ≥ h
        红区: cnt ≥ h  —— 当前 h 可行，尝试更大  
        蓝区: cnt < h  —— 当前 h 不可行，调小
        """
        left, right = 0, max(citations)
        def is_red(h: int) -> bool:
            cnt = sum(cite >= h for cite in citations)
            return cnt >= h              # case 1：红区
        while left < right:
            mid = (left + right + 1) // 2
            if is_red(mid):              # case 1：红区→向右扩
                left = mid
            else:                        # case 2：蓝区→向左收
                right = mid - 1
        return left


    # ░░░░░░░░░░░ LeetCode 275 —— H 指数 II（升序数组 · 二分答案 · 红蓝判定） ░░░░░░░░░░░
    def hIndex(
        self, citations: List[int]
    ) -> int:
        """
        已升序的 citations，二分答案 h：
          is_red(h)：数组中“≥ h”的论文数是否 ≥ h（可行 = 红区）
          外层：红区向右扩，蓝区向左收，收敛到最大可行 h
        说明：这里默认 citations 非空；若需要健壮性可在外层添加空数组判断。
        """
        def is_red(ans: int) -> int:
            # 在升序数组中二分找首个 >= ans 的下标（lower_bound）
            left, right = 0, len(citations) - 1
            while left < right:
                mid = (left + right) // 2
                if citations[mid] >= ans:
                    right = mid          # 保留满足的一侧，收缩右边界
                else:
                    left = mid + 1       # 不满足，左边界右移
            return len(citations) - left >= ans
    
        # 二分答案区间：[0, max(citations)]
        left, right = 0, max(citations)
        while left < right:
            pivot = (left + right + 1) // 2   # 取上中位，防止死循环
            if is_red(pivot):                 # 红区：可行 → 向右扩
                left = pivot
            else:                             # 蓝区：不可行 → 向左收
                right = pivot - 1
        return left


    # ░░░░░░░░░░░ LeetCode 410 —— 分割数组的最大值（答案二分） ░░░░░░░░░░░
    def splitArray(
        self, nums: List[int], k: int
    ) -> int:
        """
        二分答案：最小化“每段和的上界” mx
        蓝区：is_blue(mx)=True（可分 ≤k 段）→ 试着再小：right = mid
        红区：is_blue(mx)=False（需要 >k 段）→ 调大上界：left = mid + 1
        """
        def is_blue(mx: int) -> bool:
            parts = 1
            s = 0
            for x in nums:
                if s + x > mx:
                    parts += 1
                    s = x
                else:
                    s += x
            return parts <= k
    
        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if is_blue(mid):      # 蓝区：可行，收缩右边界
                right = mid
            else:                 # 红区：不可行，增大上界
                left = mid + 1
        return left

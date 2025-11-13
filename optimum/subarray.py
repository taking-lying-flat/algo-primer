class SubarrayDPToolkit:
    # ░░░░░░░░░░░ LeetCode 53 —— 最大子数组和 ░░░░░░░░░░░
    def maxSubArray(
      self, nums: List[int]
    ) -> int:
        """
        Kadane 算法求最大子数组和
             1. f[i] 表示以 nums[i] 结尾的最大子数组和
             2. 对每个位置，可以接续前面的子数组或重新开始
             3. f[i] = max(f[i-1], 0) + nums[i]
             4. 如果前面的和为负，不如重新开始
             5. 答案是所有 f[i] 的最大值
        """
        f = [0] * len(nums)
        f[0] = nums[0]
        for i in range(1, len(nums)):
            f[i] = max(f[i - 1], 0) + nums[i]
        return max(f)

  
    # ░░░░░░░░░░░ LeetCode 152 —— 乘积最大子数组 ░░░░░░░░░░░
    def maxProduct(
      self, nums: List[int]
    ) -> int:
        """
        最大子数组乘积（考虑负数的影响）
             1. f_max[i] 表示以 nums[i] 结尾的最大乘积
             2. f_min[i] 表示以 nums[i] 结尾的最小乘积
             3. 由于负数乘负数会变正，需要同时维护最大值和最小值
             4. f_max[i] = max(f_max[i-1] * nums[i], f_min[i-1] * nums[i], nums[i])
             5. f_min[i] = min(f_max[i-1] * nums[i], f_min[i-1] * nums[i], nums[i])
        """
        n = len(nums)
        f_max = [0] * n
        f_min = [0] * n
        f_max[0] = f_min[0] = nums[0]
        
        for i in range(1, n):
            x = nums[i]
            f_max[i] = max(f_max[i - 1] * x, f_min[i - 1] * x, x)
            f_min[i] = min(f_max[i - 1] * x, f_min[i - 1] * x, x)
            
        return max(f_max)

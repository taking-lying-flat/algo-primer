class FoundationToolKit:
    # ░░░░░░░░░░░░░░ LeetCode 198 —— 打家劫舍 ░░░░░░░░░░░░░░
    def rob(nums: List[int]) -> int:
        @cache
        def dfs(i: int) -> int:
            if i < 0:
                return 0
            return max(dfs(i - 2) + nums[i], dfs(i - 1))
        return dfs(len(nums) - 1)

    
    # ░░░░░░░░░░░░░░ LeetCode 3693 —— Climbing Stairs II（爬楼梯 II） ░░░░░░░░░░░░░░
    def climbStairs(
        self, n: int, costs: List[int]
    ) -> int:
        @cache
        def dfs(i: int) -> int:
            if i < 0:
                return 0
            return min(
                dfs(i - 3) + 9,
                dfs(i - 2) + 4,
                dfs(i - 1) + 1,
            ) + costs[i]
        return dfs(n - 1)


    # ░░░░░░░░░░░░░░ LeetCode 377 —— 组合总和 Ⅳ（排列数 · 完全背包） ░░░░░░░░░░░░░░
    def combinationSum4(
        self, nums: List[int], target: int
    ) -> int:
        # @cache
        # def dfs(i: int) -> int:
        #     if i == 0:
        #         return 1
        #     return sum(dfs(i - x) for x in nums if x <= i)
        # return dfs(target)

        # —— 外层循环枚举体积 i，内层循环枚举物品 x
        #    => 顺序敏感，计算的是排列数
        # 若要计算组合数（完全背包），则应「外层枚举物品，内层枚举体积」：
        f = [1] + [0] * target
        for i in range(1, target + 1):
            f[i] = sum(f[i - x] for x in nums if x <= i)
        return f[target]


    # ░░░░░░░░░░░░░░ LeetCode 2466 —— 统计构造好字符串的方案数（爬楼梯型 DP · 方案数） ░░░░░░░░░░░░░░
    def countGoodStrings(
        self, low: int, high: int, zero: int, one: int
    ) -> int:
        MOD = 1_000_000_007
        @cache
        def dfs(i: int) -> int:
            if i < 0:
                return 0
            if i == 0:
                return 1
            return (dfs(i - zero) + dfs(i - one)) % MOD 
        return sum(dfs(i) for i in range(low, high + 1)) % MOD


    # ░░░░░░░░░░░░░░ LeetCode 2266 —— 统计可被按下的文本数（分组 + DP 乘法） ░░░░░░░░░░░░░░
    def countTexts(
        self, pressedKeys: str
    ) -> int:
        MOD = 1_000_000_007
        f = [1, 1, 2, 4]
        g = [1, 1, 2, 4]
        for _ in range(10 ** 5 - 3):
            f.append((f[-1] + f[-2] + f[-3]) % MOD)
            g.append((g[-1] + g[-2] + g[-3] + g[-4]) % MOD)

        ans = 1
        for ch, s in groupby(pressedKeys):
            m = len(list(s))
            ans = ans * (g[m] if ch in "79" else f[m]) % MOD
        return ans

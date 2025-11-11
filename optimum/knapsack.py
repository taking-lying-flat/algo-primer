class KnapsackTemplates:
    # ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 0-1 背包 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    def knapsack_01(
        self, weights: List[int], values: List[int], capacity: int
    ) -> int:
        # n = len(weights)
        # @cache
        # def dfs(i: int, c: int) -> int:
        #     if i < 0 or c <= 0:
        #         return 0
        #     if c < weights[i]:  # 放不下当前物品，只能不选
        #         return dfs(i - 1, c)
        #     return max(
        #         dfs(i - 1, c),                           # 不选
        #         dfs(i - 1, c - weights[i]) + values[i]   # 选
        #     )
        # return dfs(n - 1, capacity)

        dp = [0] * (capacity + 1)
        for w, val in zip(weights, values):
            # 倒序枚举，保证每个物品只被用一次
            for j in range(capacity, w - 1, -1):
                dp[j] = max(dp[j], dp[j - w] + val)
        return dp[capacity]

    
    # ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 完全背包 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
        def knapsack_unbounded(
        self, weights: List[int], values: List[int], capacity: int
    ) -> int:
        # n = len(weights)
        # @cache
        # def dfs(i: int, c: int) -> int:
        #     if i < 0 or c <= 0:
        #         return 0
        #     if c < weights[i]:             # 放不下当前物品，只能不选
        #         return dfs(i - 1, c)
        #     # 可以选当前物品：选了之后 i 不变，允许重复选择
        #     return max(
        #         dfs(i - 1, c),                             # 不选
        #         dfs(i, c - weights[i]) + values[i]         # 选
        #     )
        # return dfs(n - 1, capacity)

        # 一维 DP 写法：容量正序枚举
        dp = [0] * (capacity + 1)
        for w, val in zip(weights, values):
            for c in range(w, capacity + 1):
                dp[c] = max(dp[c], dp[c - w] + val)
        return dp[capacity]

    
    # ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 二维约束 0-1 背包 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    def knapsack_2d(
        self,
        volumes: List[int],
        weights: List[int],
        values: List[int],
        max_volume: int,
        max_weight: int,
    ) -> int:
        # n = len(volumes)
        # @cache
        # def dfs(i: int, v_rem: int, w_rem: int) -> int:
        #     if i < 0 or v_rem <= 0 or w_rem <= 0:
        #         return 0
        #     if v_rem < volumes[i] or w_rem < weights[i]:
        #         return dfs(i - 1, v_rem, w_rem)  # 放不下当前物品，只能不选
        #     return max(
        #         dfs(i - 1, v_rem, w_rem),                                       # 不选
        #         dfs(i - 1, v_rem - volumes[i], w_rem - weights[i]) + values[i]  # 选
        #     )
        # return dfs(n - 1, max_volume, max_weight)

        dp = [[0] * (max_weight + 1) for _ in range(max_volume + 1)]
        for vol, wgt, val in zip(volumes, weights, values):
            for v in range(max_volume, vol - 1, -1):
                for w in range(max_weight, wgt - 1, -1):
                    dp[v][w] = max(dp[v][w], dp[v - vol][w - wgt] + val)
        return dp[max_volume][max_weight]

    
    # ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 多重背包 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    def knapsack_multiple(
        self,
        volumes: List[int],
        values: List[int],
        counts: List[int],
        capacity: int
    ) -> int:
        items: List[Tuple[int, int]] = []
        for v, w, s in zip(volumes, values, counts):
            k = 1
            while k <= s:
                items.append((v * k, w * k))
                s -= k
                k <<= 1
            if s:
                items.append((v * s, w * s))
        dp = [0] * (capacity + 1)
        for vol, val in items:
            for j in range(capacity, vol - 1, -1):
                dp[j] = max(dp[j], dp[j - vol] + val)
        return dp[capacity]

    def knapsack_multiple_queue(
        self,
        volumes: List[int],
        values: List[int],
        counts: List[int],
        capacity: int
    ) -> int:
        dp = [0] * (capacity + 1)
        for vol, val, cnt in zip(volumes, values, counts):
            for r in range(vol):
                q: deque[Tuple[int, int]] = deque()
                k = 0
                for j in range(r, capacity + 1, vol):
                    cur_val = dp[j] - k * val
                    while q and q[-1][1] <= cur_val:
                        q.pop()
                    q.append((k, cur_val))
                    while q[0][0] < k - cnt:
                        q.popleft()
                    dp[j] = q[0][1] + k * val
                    k += 1
        return dp[capacity]


class KnapsackApplications:
    # ░░░░░░░░░░░░░░ LeetCode 416 —— 分割等和子集（0-1 背包 · 可行性） ░░░░░░░░░░░░░░
    def canPartition(
        self, nums: List[int]
    ) -> bool:
        # @cache
        # def dfs(i: int, c: int) -> bool:
        #     if i < 0:
        #         return c == 0
        #     if c < nums[i]:
        #         return dfs(i - 1, c)
        #     return dfs(i - 1, c) or dfs(i - 1, c - nums[i])
        # s = sum(nums)
        # return s % 2 == 0 and dfs(len(nums) - 1, s // 2)

        s = sum(nums)
        if s % 2:
            return False
        s //= 2
        f = [True] + [False] * s
        for x in nums:
            for j in range(s, x - 1, -1):
                f[j] = f[j] or f[j - x]
        return f[s]

    
    # ░░░░░░░░░░░░░░ LeetCode 494 —— 目标和（0-1 背包 · 方案数） ░░░░░░░░░░░░░░
    def findTargetSumWays(self, 
        nums: List[int], target: int
    ) -> int:
        s = sum(nums) - abs(target)
        if s < 0 or s % 2 == 1:
            return 0

        # @cache
        # def dfs(i: int, j: int) -> int:
        #     if i < 0:
        #         return 1 if j == 0 else 0
        #     if j < nums[i]:
        #         return dfs(i - 1, j)
        #     return dfs(i - 1, j) + dfs(i - 1, j - nums[i])

        m = s // 2
        f = [1] + [0] * m
        for x in nums:
            for c in range(m, x - 1, -1):
                f[c] += f[c - x]
        return f[m]


    # ░░░░░░░░░░░░░░ LeetCode 2915 —— 和为目标值的最长子序列长度（0-1 背包 · 最值） ░░░░░░░░░░░░░░
    def lengthOfLongestSubsequence(
        self, nums: List[int], target: int
    ) -> int:
        # @cache
        # def dfs(i: int, c: int) -> int:
        #     if i < 0:
        #         return 0 if c == 0 else -inf
        #     if c < nums[i]:
        #         return dfs(i - 1, c)
        #     return max(
        #         dfs(i - 1, c),              # 不选
        #         dfs(i - 1, c - nums[i]) + 1 # 选
        #     )
        # ans = dfs(len(nums) - 1, target)
        # dfs.cache_clear()
        # return ans if ans > 0 else -1

        f = [0] + [-inf] * target
        for x in nums:
            for c in range(target, x - 1, -1):
                f[c] = max(f[c], f[c - x] + 1)
        return f[target] if f[target] > 0 else -1


    # ░░░░░░░░░░░░░░ LeetCode 2787 —— 按幂次方分解整数的方案数（0-1 背包 · 方案数） ░░░░░░░░░░░░░░
    def numberOfWays(
        self, n: int, x: int
    ) -> int:
        # 0-1 背包 · 方案数
        # f[c]：恰好凑出和为 c 的方案数
        # 转移：f[c] += f[c - j]，容量 c 必须倒序枚举（保证每个幂只用一次）

        # @cache
        # def dfs(i: int, c: int) -> int:
        #     if i == 0:
        #         return 1 if c == 0 else 0
        #     if c < i ** x:
        #         return dfs(i - 1, c)
        #     return dfs(i - 1, c) + dfs(i - 1, c - i ** x)
        # return dfs(n, n) % 1_000_000_007

        MOD = 1_000_000_007
        f = [1] + [0] * n
        for i in range(1, n + 1):
            j = i ** x
            for c in range(n, j - 1, -1):
                f[c] = (f[c] + f[c - j]) % MOD
        return f[n]


    # ░░░░░░░░░░░ LeetCode 3180 —— 执行操作可获得的最大总奖励（0-1 背包 · 可行性转最值） ░░░░░░░░░░░
    def maxTotalReward(
        self, rewardValues: List[int]
    ) -> int:
        rewardValues.sort()
        m = 2 * rewardValues[-1] - 1
        
        f = [True] + [False] * m
        for x in rewardValues:
            for j in range(2 * x - 1, x - 1, -1):
                f[j] |= f[j - x]
                
        return max(i for i, can in enumerate(f) if can)

    
    # ░░░░░░░░░░░░░░ LeetCode 322 —— 零钱兑换（完全背包 · 最少硬币数） ░░░░░░░░░░░░░░
    def coinChange(
        self, coins: List[int], amount: int
    ) -> int:
        # n = len(coins)
        # @cache
        # def dfs(i: int, c: int) -> int:
        #     if i < 0:
        #         return 0 if c == 0 else inf
        #     not_take = dfs(i - 1, c)
        #     if c >= coins[i]:
        #         take = dfs(i, c - coins[i]) + 1
        #         return min(take, not_take)
        #     return not_take

        f = [0] + [inf] * amount
        for coin in coins:
            for j in range(coin, amount + 1):
                f[j] = min(f[j], f[j - coin] + 1)
        return f[amount] if f[amount] < inf else -1


    # ░░░░░░░░░░░░░░ LeetCode 518 —— 零钱兑换 II（完全背包 · 方案数） ░░░░░░░░░░░░░░
    def change(
        self, amount: int, coins: List[int]
    ) -> int:
        # n = len(coins)
        # @cache
        # def dfs(i: int, c: int) -> int:
        #     if i < 0:
        #         return 1 if c == 0 else 0
        #     if c < coins[i]:  # 只能不选
        #         return dfs(i - 1, c)
        #     # 不选 + 继续选
        #     return dfs(i - 1, c) + dfs(i, c - coins[i])
        # return dfs(n - 1, amount)

        f = [1] + [0] * amount
        for coin in coins:
            for c in range(coin, amount + 1):
                f[c] += f[c - coin]
        return f[amount]


    # ░░░░░░░░░░░░░░ LeetCode 279 —— 完全平方数（完全背包 · 最少个数） ░░░░░░░░░░░░░░
    def numSquares(
        self, n: int
    ) -> int:
        # @cache
        # def dfs(i: int, j: int) -> int:
        #     if i == 0:
        #         return inf if j else 0
        #     if j < i * i:
        #         return dfs(i - 1, j)
        #     return min(dfs(i, j - i * i) + 1, dfs(i - 1, j))
        # ans = dfs(isqrt(n), n)
        # dfs.cache_clear()
        # return ans

        f = [0] + [inf] * n
        for x in range(1, isqrt(n) + 1):
            seq = x * x
            for j in range(seq, n + 1):
                f[j] = min(f[j], f[j - x * x] + 1)
        return f[n]

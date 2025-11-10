class KnapsackTemplates:
    # ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 0-1 背包 · 记忆化搜索 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
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
        #         dfs(i - 1, c - weights[i]) + values[i],  # 选
        #     )
        #
        # return dfs(n - 1, capacity)

        dp = [0] * (capacity + 1)
        for w, val in zip(weights, values):
            # 倒序枚举，保证每个物品只被用一次
            for j in range(capacity, w - 1, -1):
                dp[j] = max(dp[j], dp[j - w] + val)
        return dp[capacity]

    
    # ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 完全背包 · 记忆化搜索 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
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
        #         dfs(i, c - weights[i]) + values[i],        # 选
        #     )
        #
        # return dfs(n - 1, capacity)

        # 一维 DP 写法：容量正序枚举
        dp = [0] * (capacity + 1)
        for w, val in zip(weights, values):
            for c in range(w, capacity + 1):
                dp[c] = max(dp[c], dp[c - w] + val)
        return dp[capacity]

    
    # ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 二维约束 0-1 背包 · 记忆化搜索 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    def knapsack_2d_memo(
        self,
        weights: List[int],
        volumes: List[int],
        values: List[int],
        max_w: int,
        max_v: int
    ) -> int:
        n = len(weights)
        @cache
        def dfs(i: int, w_rem: int, v_rem: int) -> int:
            if i < 0 or w_rem <= 0 or v_rem <= 0:
                return 0
            not_take = dfs(i - 1, w_rem, v_rem)
            if w_rem >= weights[i] and v_rem >= volumes[i]:
                take = values[i] + dfs(
                    i - 1,
                    w_rem - weights[i],
                    v_rem - volumes[i],
                )
                return max(take, not_take)
            return not_take
        return dfs(n - 1, max_w, max_v)

    
    def knapsack_2d_dp(
        self,
        volumes: List[int],
        weights: List[int],
        values: List[int],
        max_volume: int,
        max_weight: int
    ) -> int:
        dp = [[0] * (max_weight + 1) for _ in range(max_volume + 1)]
        for vol, wgt, val in zip(volumes, weights, values):
            for v in range(max_volume, vol - 1, -1):
                for w in range(max_weight, wgt - 1, -1):
                    dp[v][w] = max(dp[v][w], dp[v - vol][w - wgt] + val)        
        return dp[max_volume][max_weight]

    
    # ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 多重背包 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    def knapsack_multiple_dp(
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


class KnapsackApplications:
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

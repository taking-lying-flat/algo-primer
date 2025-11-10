class KnapsackTemplates:
    # ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 0-1 背包 · 记忆化搜索 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    def knapsack_01_memo(
        self, weights: List[int], values: List[int], cap: int
    ) -> int:
        n = len(weights)
        @cache
        def dfs(i: int, c: int) -> int:
            if i < 0 or c <= 0:
                return 0
            not_take = dfs(i - 1, c)
            if c >= weights[i]:
                take = values[i] + dfs(i - 1, c - weights[i])
                return max(take, not_take)
            return not_take
        return dfs(n - 1, cap)

    
    def knapsack_01_dp(
        self, volumes: List[int], values: List[int], capacity: int
    ) -> int:
        dp = [0] * (capacity + 1)
        for vol, val in zip(volumes, values):
            for j in range(capacity, vol - 1, -1):
                dp[j] = max(dp[j], dp[j - vol] + val)
        return dp[capacity]

    
    # ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 完全背包 · 记忆化搜索 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    def knapsack_unbounded_memo(
        self, weights: List[int], values: List[int], cap: int
    ) -> int:
        n = len(weights)
        @cache
        def dfs(i: int, c: int) -> int:
            if i < 0 or c <= 0:
                return 0
            not_take = dfs(i - 1, c)
            if c >= weights[i]:
                take = values[i] + dfs(i, c - weights[i])  # 取当前物品后 i 不变，可再次选择
                return max(take, not_take)
            return not_take
        return dfs(n - 1, cap)

    
    def knapsack_unbounded_dp(
        self, volumes: List[int], values: List[int], capacity: int
    ) -> int:
        dp = [0] * (capacity + 1)
        for vol, val in zip(volumes, values):
            for j in range(vol, capacity + 1):
                dp[j] = max(dp[j], dp[j - vol] + val)    
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

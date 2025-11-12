class StateMachineToolkit:
    # ░░░░░░░░░░░░░░░ LeetCode 121 —— 买卖股票的最佳时机（状态机 DP · 一次交易） ░░░░░░░░░░░░░░░
    def maxProfit_121(
        self, prices: List[int]
    ) -> int:
        # f0：当前不持有股票的最大利润
        # f1：当前持有一股股票的最大利润
        f0 = 0        # 初始不持有，利润为 0
        f1 = -inf     # 初始不可能持有，用 -inf 打底
        for price in prices:
            f0 = max(f0, f1 + price)  # 不持有：要么本来就不持有，要么今天把手里的卖掉
            f1 = max(f1, -price)      # 持有：要么本来就持有，要么今天以 price 买入（只允许一次交易）
        return f0


    # ░░░░░░░░░░░░░░ LeetCode 122 —— 买卖股票的最佳时机 II（状态机 DP · 无限次交易） ░░░░░░░░░░░░░░
    def maxProfit_122(
        self, prices: List[int]
    ) -> int:
        # f[i][0]：前 i 天结束时「不持有」股票的最大利润
        # f[i][1]：前 i 天结束时「持有」一股股票的最大利润

        # @cache
        # def dfs(i: int, hold: bool) -> int:
        #     if i < 0:
        #         return -inf if hold else 0
        #     if hold:
        #         # 今天结束时持有：昨天就持有 / 昨天不持有今天买入
        #         return max(dfs(i - 1, True), dfs(i - 1, False) - prices[i])
        #     # 今天结束时不持有：昨天就不持有 / 昨天持有今天卖出
        #     return max(dfs(i - 1, False), dfs(i - 1, True) + prices[i])
        # return dfs(len(prices) - 1, False)

        n = len(prices)
        f = [[0] * 2 for _ in range(n + 1)]
        f[0][1] = -inf  # 第 0 天之前不可能持有股票，用 -inf 打底
        for i, p in enumerate(prices):
            # i 天（下标 0..i），转移到第 i+1 天结束时的状态
            f[i + 1][0] = max(
                f[i][0],        # 昨天就不持有，今天不操作
                f[i][1] + p,    # 昨天持有，今天卖出
            )
            f[i + 1][1] = max(
                f[i][1],        # 昨天就持有，今天不操作
                f[i][0] - p,    # 昨天不持有，今天买入
            )
        return f[n][0]

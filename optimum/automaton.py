class StateMachineToolkit:
    # ░░░░░░░░░░░░░░░ LeetCode 121 —— 买卖股票的最佳时机（状态机 DP · 一次交易） ░░░░░░░░░░░░░░░
    def maxProfit(
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
    def maxProfit(
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


    # ░░░░░░░░░░░░░░ LeetCode 123 —— 买卖股票的最佳时机 III（状态机 DP · 最多两次交易） ░░░░░░░░░░░░░░
    def maxProfit(
        self, prices: List[int]
    ) -> int:
        # 状态机 DP · 压缩版
        # buy1/buy2：第 1/2 次买入后的最大利润（手里有股票）
        # sell1/sell2：第 1/2 次卖出后的最大利润（手里没股票）

        # # 完整状态机写法
        # # f[k][0]：完成 k 笔交易、不持有 的最大利润
        # # f[k][1]：完成 k 笔交易、持有 的最大利润
        # k = 2
        # f = [[0, -inf] for _ in range(k + 1)]
        # for p in prices:
        #     for j in range(k, 0, -1):
        #         f[j][0] = max(f[j][0], f[j][1] + p)      # 卖出，完成第 j 笔
        #         f[j][1] = max(f[j][1], f[j - 1][0] - p)  # 从 j-1 笔买入
        # return f[2][0]

        buy1 = buy2 = -inf
        sell1 = sell2 = 0
        for p in prices:
            sell2 = max(sell2, buy2 + p)   # 第二次卖出
            buy2  = max(buy2,  sell1 - p)  # 第二次买入
            sell1 = max(sell1, buy1 + p)   # 第一次卖出
            buy1  = max(buy1,  -p)         # 第一次买入（从 0 开始）
        return sell2


    # ░░░░░░░░░░░░░░ LeetCode 188 —— 买卖股票的最佳时机 IV（状态机 DP · 最多 k 次交易） ░░░░░░░░░░░░░░
    def maxProfit(
        self, k: int, prices: List[int]
    ) -> int:
        # 状态机 DP + 交易次数维度
        # @cache
        # def dfs(i: int, j: int, hold: bool) -> int:
        #     if j < 0:  # 交易次数用完，非法状态
        #         return -inf
        #     if i < 0:  # 没有任何一天了
        #         return -inf if hold else 0  # 不能在开始前就持有股票
        #     if hold:
        #         # 现在持有：
        #         #   1）昨天就持有，今天不动
        #         #   2）昨天不持有，今天买入（消耗一次卖出机会 j-1）
        #         return max(
        #             dfs(i - 1, j, True),
        #             dfs(i - 1, j - 1, False) - prices[i]
        #         )
        #     # 现在不持有：
        #     #   1）昨天就不持有，今天不动
        #     #   2）昨天持有，今天卖出（不消耗 j）
        #     return max(
        #         dfs(i - 1, j, False),
        #         dfs(i - 1, j, True) + prices[i]
        #     )
        # return dfs(len(prices) - 1, k, False)

        f = [[-inf] * 2 for _ in range(k + 2)]
        for j in range(1, k + 2):
            f[j][0] = 0  # 不持有时的初始利润为 0，持有用 -inf 打底

        for p in prices:
            # j 从大到小遍历，避免本轮更新 f[j] 时用到已经更新过的 f[j-1]
            for j in range(k + 1, 0, -1):
                # 不持有：保持不持有 / 今天卖出
                f[j][0] = max(
                    f[j][0],      # 昨天就不持有，今天不操作
                    f[j][1] + p,  # 昨天持有，今天卖出
                )
                # 持有：保持持有 / 今天买入
                f[j][1] = max(
                    f[j][1],         # 昨天就持有，今天不操作
                    f[j - 1][0] - p  # 昨天不持有，且多“一个卖出机会”，今天买入
                )
        return f[-1][0]

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

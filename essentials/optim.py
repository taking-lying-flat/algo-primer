class OptimumToolKit:
    # ★★★★★ LeetCode 3181 —— 执行操作可获得的最大总奖励 II（状态压缩 DP · bitset 0-1 背包） ★★★★★
    def maxTotalReward(
        self, rewardValues: List[int]
    ) -> int:
        """
        状态压缩动态规划：用 bitset 实现带约束的 0-1 背包，求最大可达总奖励

        动态规划建模：
            - 用一个整数 f 表示「可达到的总奖励集合」 二进制第 s 位为 1 ⇔ 能取得总奖励 s
            - 初始状态：f = 1，只能取得和 0

        状态转移（0-1 背包 + 特殊约束）
            - 按升序遍历不同的奖励值 v（去重后）
                规则：要选择 v，之前的总和必须 < v
            - 因此只能从「和 < v」的状态转移
                  smaller = f & ((1 << v) - 1)   # 所有 s < v 的状态
                  smaller << v                   # 这些状态的和全部加上 v
            - 更新 DP 状态集合
                  f |= smaller << v
                  
        答案：所有奖励处理完后，f 中最高位的 1 的下标就是动态规划可达到的最大总奖励
        """
        f = 1
        for v in sorted(set(rewardValues)):
            f |= (f & ((1 << v) - 1)) << v
        return f.bit_length() - 1

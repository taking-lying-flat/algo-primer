class FoundationToolKit:
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

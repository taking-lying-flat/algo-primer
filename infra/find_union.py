class UnionFindSuite:
    # ░░░░░░░░░░░ LeetCode 2709 —— 最大公约数遍历 ░░░░░░░░░░░
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        """
        最大公约数遍历 —— 质因数分解 + 并查集
             1. 特判：长度为 1 必然可行；若存在 1 且长度 > 1，一定不连通。
             2. 预处理最小质因数 spf[i]，用于 O(logA) 分解 nums[i] 的质因数集合。
             3. 以“质因数”为中介建边：同一质因数出现过的位置用并查集 union 在一起。
             4. 遍历完成后，检查所有下标是否拥有同一个根节点，即整图是否连通。
        """
        if len(nums) == 1:
            return True
        
        if 1 in nums:
            return False
        
        max_val = max(nums)
        spf = list(range(max_val + 1))
        i = 2
        while i * i <= max_val:
            j = i * i
            while j <= max_val:
                if spf[j] == j:
                    spf[j] = i
                j += i
            i += 1
        
        def get_prime_factors(x: int) -> Set[int]:
            factors = set()
            while x > 1:
                p = spf[x]
                factors.add(p)
                while x % p == 0:
                    x //= p
            return factors
        
        parent = list(range(len(nums)))
        def find(x: int) -> int:
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(x: int, y: int) -> None:
            parent[find(x)] = parent[find(y)]
        
        indices = dict()
        for i, num in enumerate(nums):
            primes = get_prime_factors(num)
            for p in primes:
                if p in indices:
                    union(i, indices[p])
                else:
                    indices[p] = i
        
        root = find(0)
        return all(find(i) == root for i in range(len(nums)))

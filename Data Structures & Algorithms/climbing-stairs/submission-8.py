class Solution:
    def climbStairs(self, n: int) -> int:
        store = [-1] * n 
        def dfs(i):
            if i == n:
                return 1
            if i > n:
                return 0
            if store[i] != -1:
                return store[i]
            store[i] = dfs(i+1) + dfs(i+2)
            return store[i]
        return dfs(0)
        
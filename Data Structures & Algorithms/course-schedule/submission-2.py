class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            adj[a].append(b)

        visiting = set()
        visited  = set()

        def dfs(node):
            if node in visiting:
                return False
            if node in visited:
                return True

            visiting.add(node)

            for neighbor in adj[node]:
                if not dfs(neighbor):
                    return False

            visiting.remove(node)
            visited.add(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
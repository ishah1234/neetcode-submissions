class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n+1)]
        rank = [1] * (n+1)

        def find(node):
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        def union(a, b):
            rootA = find(a)
            rootB = find(b)

            if rootA == rootB:
                return False 

            if rank[rootA] < rank[rootB]:
                parent[rootA] = rootB
            elif rank[rootA] > rank[rootB]:
                parent[rootB] = rootA
            else: 
                parent[rootB] = rootA
                rank[rootA] += 1
            return True

        for a,b in edges:
            if not union(a,b):
                return [a,b]
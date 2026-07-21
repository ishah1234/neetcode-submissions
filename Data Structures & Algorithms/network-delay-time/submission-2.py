class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i : [] for i in range(1, n+1)}
        for u, v, t in times: 
            adj[u].append((t,v))
        heap = [(0,k)]
        visited = set()
        maxTime = 0
         
        while heap:
            time, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            maxTime = max(maxTime, time)

            for t, neighbor in adj[node]:
                if neighbor not in visited:
                    heapq.heappush(heap, (time+ t, neighbor))
        return maxTime if len(visited) == n else -1

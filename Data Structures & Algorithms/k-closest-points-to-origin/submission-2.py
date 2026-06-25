class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minH = []
        for x,y in points:
            distance = (x**2) + (y**2)
            minH.append([distance, x, y])

        heapq.heapify(minH)
        result = []
        while k>0:
            distance, x, y = heapq.heappop(minH)
            result.append([x,y])
            k -= 1
        
        return result

# so here we will first create a list for minHeap which will have the distance and the coordinates then we will heapify this and use a min heap so then we will pop the smallest one which will be the root and check if it matches k (like do we need to just pop 1 or more) if more then we will see the new root now and pop that as well and see if k has now been satisfied
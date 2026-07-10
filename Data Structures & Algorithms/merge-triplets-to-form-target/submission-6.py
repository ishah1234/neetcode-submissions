class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x,y,z = target
        max_a, max_b, max_c = 0, 0, 0
        for a, b, c in triplets:
            if a > x or b > y or c > z:
                continue
            max_a = max(a, max_a)
            max_b = max(b, max_b)
            max_c = max(c, max_c)
        return max_a == x and max_b == y and max_c == z
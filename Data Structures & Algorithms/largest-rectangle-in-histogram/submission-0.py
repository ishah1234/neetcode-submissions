class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxA = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                area = height * (i- index)
                maxA = max(maxA, area)
                start = index
            stack.append((start,h))

        for index, height in stack:
            area = height * (len(heights) - index)
            maxA= max(area, maxA)
        return maxA
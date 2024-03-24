class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        t = heights[:]
        t.sort()
        tot = 0
        for i in range(len(heights)):
            if heights[i] != t[i]:
                tot += 1
        return tot
        
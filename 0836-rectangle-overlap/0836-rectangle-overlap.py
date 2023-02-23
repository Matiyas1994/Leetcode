class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        width = max(min(rec1[2], rec2[2]) - max(rec1[0], rec2[0]), 0)
        height = max(min(rec1[3], rec2[3]) - max(rec1[1], rec2[1]), 0)
        return width * height > 0
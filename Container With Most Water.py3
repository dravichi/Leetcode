class Solution:
    def maxArea(self, height: List[int]) -> int:
        res, left, right = 0, 0, len(height)-1
        while left != right:
            temp = (right-left) * min(height[left], height[right])
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
            if temp > res:
                res = temp
        return res

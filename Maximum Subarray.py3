class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = temp = nums[0]
        for i in nums[1:]:
            if temp+i < i:
                temp = i
            else:
                temp += i
            if temp > m:
                m = temp
        return m

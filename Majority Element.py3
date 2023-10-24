class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = m = 0
        for i in nums:
            if m == 0:
                n = i
            if i == n:
                m += 1
            else:
                m -= 1
        return n

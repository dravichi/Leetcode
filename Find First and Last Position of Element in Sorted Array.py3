class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        def search(s, e):
            m = (s+e)//2
            if s <= e:
                if nums[m] <= target:
                    if nums[m] == target and m > res[1]:
                        res[1] = m
                    search(m+1, e)
                if nums[m] >= target:
                    if nums[m] == target:
                        res[0] = m
                    search(s, m-1)
        if nums:
            search(0, len(nums)-1)
        return res

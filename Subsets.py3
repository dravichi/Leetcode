class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        def backtrack(i, curr):
            if i == len(nums):
                return
            for j in range(i, len(nums)):
                curr.append(nums[j])
                res.append(curr[:])
                backtrack(j+1, curr)
                curr.pop()
        backtrack(0, [])
        
        return res

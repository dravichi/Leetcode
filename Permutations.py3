class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def bt(n):
            if len(nums) == len(n):
                res.append(n)
                return
            for i in nums:
                if i not in n:
                    bt(n+[i])
        bt([])
        return res

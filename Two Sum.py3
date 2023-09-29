class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ln = len(nums)
        d = dict()
        for i in range(ln):
            d[nums[i]] = i

        for i in range(ln):
            pair = target - nums[i]
            if pair in d and i != d[pair]:
                return [i, d[pair]]

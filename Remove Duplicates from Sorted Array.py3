class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # BEST MEMORY
      
        # k = 0
        # for i in range(len(nums)-1):
        #     if nums[i-k] == nums[i-k+1]:
        #         nums.pop(i-k)
        #         k += 1
        # return len(nums)

        # BEST PERFORMANCE
        
        k = 1
        for i in range(1, len(nums)):
             if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                k += 1
        return k
        

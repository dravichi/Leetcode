class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2): 
            return self.intersect(nums2, nums1)
        d = dict()
        a = []
        for i in nums1:
            d[i] = d.get(i, 0) + 1
        for i in nums2:
            if d.get(i, 0) != 0:
                a.append(i)
                d[i] -= 1
        return a

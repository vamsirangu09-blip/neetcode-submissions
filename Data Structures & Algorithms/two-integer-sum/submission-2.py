class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map1 = {}
        for i, n in enumerate(nums):
            k = target - n
            if k in map1:
                return [map1[k], i]
            else:
                map1[n] = i

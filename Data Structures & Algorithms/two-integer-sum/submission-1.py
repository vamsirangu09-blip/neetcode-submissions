class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevmap={}
        for i,n in enumerate(nums):
            k=target-n
            if k in prevmap:
                return [prevmap[k],i]
            else:
                prevmap[n]=i
        
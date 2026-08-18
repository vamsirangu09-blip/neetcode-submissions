class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [ []  for i in range(len(nums)+1) ]

        for n in nums:
            count[n]=1+count.get(n,0)
        for n, i in count.items():
            freq[i].append(n)
        res=[]
        for i in freq[::-1]:
            for j in range(len(i)):
                res.append(i[j])
                if len(res)==k:
                    return res



        




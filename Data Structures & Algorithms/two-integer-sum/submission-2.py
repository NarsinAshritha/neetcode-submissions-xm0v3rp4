class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
     hm={}
     for i,num in enumerate(nums):
        j=target-num

        if j in hm:
            return [hm[j],i]
        hm[num]=i
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
     lst=[]
     sublst=[]
     submax=0
     l=0

     for r in range(len(nums)):
        sublst.append(nums[r])
        while len(sublst)==k:
            lst.append(max(sublst))
            sublst.remove(nums[l])
            l+=1
     return lst

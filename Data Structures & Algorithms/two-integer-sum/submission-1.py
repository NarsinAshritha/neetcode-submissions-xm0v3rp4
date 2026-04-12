class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
     op=[]
     for i in range(0,len(nums)):
        j = target - nums[i]
        if (j in nums and nums.index(j) != i):
            op.append(min(i, nums.index(j)))
            op.append(max(i, nums.index(j)))
            return op
        else:
            continue
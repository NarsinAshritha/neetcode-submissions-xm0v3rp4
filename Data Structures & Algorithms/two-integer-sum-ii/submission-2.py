class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lst=[]
        for i,num in enumerate(numbers):
                if (target - num in numbers) and (i != numbers.index(target- num)):
                    lst.append(i+1)
                    lst.append(numbers.index(target- num)+1)
                if lst:
                    return lst
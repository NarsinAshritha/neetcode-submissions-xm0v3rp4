class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            # start of sequence
            if num - 1 not in num_set:
                current = num
                length = 1
                # checking the below condition only once we 
                #arrive at number thats the start of the sequence
                while current + 1 in num_set:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        highest_count = 0
        for num in nums:
            count = count + 1 if num else 0
            highest_count = max(highest_count, count)
        return highest_count
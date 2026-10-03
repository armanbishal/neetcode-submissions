class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2):
            for num in nums:
                ans.append(num)
        return ans

# Time Complexity: O(n); 2 for loops but iterating over a constant value thus, O(n)
# Space Complexity: O(n)
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for i in nums:
            if i in hashset: # O(1) for each lookup
                return True
            else:
                hashset.add(i)
        return False

# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            else:
                hashset.add(i)
        return False

# Time Complexity: O(1); Checking if an item exists takes O(1) average time complexity
# Space Complexity: O(n); Storing elements in the hashset
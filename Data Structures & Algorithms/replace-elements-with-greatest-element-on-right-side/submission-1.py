class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [0] * n
        rightMax = -1
        for i in range(n - 1, -1, -1):
            ans[i] = rightMax
            rightMax = max(arr[i], rightMax) # max between value of previous index of original array and the current rightMax (e.g: 1 vs -1)
        return ans

# Time Complexity: O(n)
# Space Complexity: O(n)
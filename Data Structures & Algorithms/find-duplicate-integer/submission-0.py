class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return -1
        
        seen = set()

        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        
        return -1
class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)-1

        while start<end:
            mid = (start+end)//2
            if nums[mid]<nums[end]:
                end = mid #min is on the left side
            
            else:
                start = mid+1 #min is on the right side
        
        return nums[start]
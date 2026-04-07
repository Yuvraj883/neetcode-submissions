class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # left = 0
        ans = []
        for i in range(len(numbers)):
            remaining = target - numbers[i]
            right = len(numbers)-1
            left = i+1
            
            while left<=right:
                mid = (left+right)//2
                print(left, mid, right)
                if numbers[mid] == remaining:
                    print(numbers[i], numbers[mid])
                    ans.append(i+1)
                    ans.append(mid+1)
                    return ans
                elif numbers[mid]<remaining:
                    left = mid+1
                elif numbers[mid]>remaining:
                    right = mid-1
        
        return ans

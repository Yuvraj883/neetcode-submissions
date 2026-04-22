class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def checkTime(k):
            hour = 0
            for pile in piles:
                hour+= math.ceil((pile/k))
            
            return hour
        
        piles.sort()
        start = 1
        end = max(piles)

        while start<end:
            mid = (start+end)//2

            temp = checkTime(mid)

            if temp>h:
                start=mid+1
            elif temp<h or temp==h:
                end=mid
            
        return start
        


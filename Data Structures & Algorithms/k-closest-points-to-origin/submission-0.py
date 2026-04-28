class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []
        heapq.heapify(heap)

        for point in points:
            x = point[0]
            y = point[1]

            distance = math.sqrt(((x-0)**2)+(y-0)**2)
            temp = (distance, [x,y])
            # print(temp)
            heapq.heappush(heap, temp)
        
        i = 0
        ans = []
        while i<k:
            temp = heapq.heappop(heap)
            ans.append(temp[1])
            i+=1


            
        print(heap)
        return ans
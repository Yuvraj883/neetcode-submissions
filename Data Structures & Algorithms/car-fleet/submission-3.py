class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pairs = [[p,s] for p,s in zip(position, speed)]

        stack = []
        count = 0
        for p,s in sorted(pairs) [::-1]:
            
            time = (target-p)/s

            if stack and stack[-1]>=time:
                continue
            
            stack.append(time)
            count+=1

            
        
        return count


        

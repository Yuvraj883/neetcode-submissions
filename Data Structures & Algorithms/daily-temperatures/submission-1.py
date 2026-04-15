class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        stack.append(len(temperatures) - 1)

        i = len(temperatures) - 2   
        while i >= 0:
            
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
                
            if stack:
                result[i] = stack[-1] - i
            
            stack.append(i)
            i -= 1
        
        return result
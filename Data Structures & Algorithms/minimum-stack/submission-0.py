class MinStack:

    def __init__(self):
        self.stack = []


    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val,val))
        else:
            mini = min(val, self.stack[-1][1])
            self.stack.append((val, mini))
        
    def pop(self) -> None:
        self.stack.pop()


    def top(self) -> int:
        return self.stack[-1][0]


    def getMin(self) -> int:
        top = self.stack[-1]
        return top[1]

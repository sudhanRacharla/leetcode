class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and self.isbadPair(stack[-1],c):
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)
    def isbadPair(self,a:str,b:str)->bool:
        if a.lower()==b.lower() and a!=b:
            return True
        else:
            return False
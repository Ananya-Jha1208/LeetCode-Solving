class Solution:
    def isValid(self, s: str) -> bool:

        paren = {'(':')','[':']','{':'}'}
        
        stack = []

        for x in s:
            if (x in '([{'):
                stack.append(x)
            elif (len(stack)==0 or x!=paren[stack.pop()]):
                return False
        return (len(stack)==0)        

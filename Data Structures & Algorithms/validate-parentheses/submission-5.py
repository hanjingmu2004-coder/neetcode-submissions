class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pairs={"(":")","{":"}","[":"]"}
        for i in s:
            if i in pairs:
                stack.append(i)
            else:
                if stack is not None and pairs[stack[-1]]==i:
                    stack.pop()
                else:
                    return False
        return False if stack else True
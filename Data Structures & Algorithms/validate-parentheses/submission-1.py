class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pairs={"(":")","{":"}","[":"]"}
        for i in s:
            if i in pairs:
                stack.append(i)
            else:
                if pairs[stack[-1]]==i:
                    stack.pop()
                else:
                    return False
        return True
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for s in tokens:
            if s in nums:
                stack.append(int(s))
            elif s=="+":
                stack.append(stack.pop()+stack.pop())
            elif s=="*":
                stack.append(stack.pop()*stack.pop())
            elif s=="/":
                a,b=stack.pop(),stack.pop()
                stack.append(b/a)
            elif s=="-":
                a,b=stack.pop(),stack.pop()
                stack.append(b-a)
        return stack[0]            
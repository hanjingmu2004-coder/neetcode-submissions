class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
        stack=[]
        for s in tokens:
            if s in nums:
                stack.append(nums[s])
            elif s=="+":
                stack.append(stack[-2]+stack[-1])
            elif s=="*":
                stack.append(stack[-2]*stack[-1])
            elif s=="/":
                stack.append(stack[-2]/stack[-1])
            else:
                stack.append(stack[-2]-stack[-1])
        return stack[-1]            
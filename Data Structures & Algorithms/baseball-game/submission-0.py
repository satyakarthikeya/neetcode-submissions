class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        res = 0
        for n in operations:
            if n == "+":
                res += stack[-1] + stack[-2]
                stack.append(stack[-1]+stack[-2])
            elif n == "D":
                res += 2 * stack[-1]
                stack.append(2 * stack[-1])
            elif n =="C":
                res -= stack[-1]
                stack.pop()
            else :
                res += int(n)
                stack.append(int(n))
        return res 
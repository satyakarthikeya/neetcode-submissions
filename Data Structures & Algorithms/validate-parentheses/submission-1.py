class Solution:
    def isValid(self, s: str) -> bool:
        braket = { ")" : "(", "]" : "[", "}" : "{" }

        stack = []
        for st in s:
            if st in braket:
                if stack and stack[-1]== braket[st]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(st)
        return True if not stack else False

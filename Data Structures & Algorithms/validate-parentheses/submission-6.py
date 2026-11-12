class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        cToOpen = {")" : "(", "]" : "[", "}" : "{"}
        for c in s:
            if c in cToOpen: # ([{}])
                if stack and stack[-1] == cToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c) #stack = [(, [, {, ]
        return True if not stack else False
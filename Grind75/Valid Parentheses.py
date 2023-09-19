class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            if s[i] in "({[":
                stack.append(s[i])
            elif s[i] in ")]}":
                if len(stack) == 0:
                    return False
                else:
                    pair = stack.pop()
                    if s[i] == ")" and not pair == "(":
                        return False
                    elif s[i] == "]" and not pair == "[":
                        return False
                    elif s[i] == "}" and not pair == "{":
                        return False
        if len(stack) > 0 :
            return False
        return True

print(Solution().isValid("))"))
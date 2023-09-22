class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""

        for i in range(len(s)):
            if s[i].isalpha() and s[i].isupper():
                result += s[i].lower()
            elif s[i].isalpha() and s[i].islower():
                result += s[i]
            elif s[i].isnumeric():
                result += s[i]
        
        index = 0
        index_back = len(result) - 1

        while index < len(result) // 2:
            if result[index] != result[index_back]:
                return False
            index += 1
            index_back -= 1
        
        return True
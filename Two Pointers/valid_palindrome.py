class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while right > left:
            while right > left and not self.is_alphaNum(s[right]):
                right -= 1
            while right > left and not self.is_alphaNum(s[left]):
                left += 1
            if s[left].lower() != s[right].lower():
                return False
            right -= 1
            left += 1
        return True


    def is_alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))

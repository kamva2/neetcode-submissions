class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        clean_s = "".join(i for i in s if i.isalnum())

        reversed_s = clean_s[::-1]

        return clean_s == reversed_s

        
class Solution(object):
    def isPalindrome(self, s):
        stri = ""
        s = s.lower()
        for i in s:
            if i.isalnum():
                stri = stri + i
        rev = stri[::-1]
        return stri == rev

        
class Solution:
    def reverseVowels(self, s) -> str:
        vowels = {"a","e","i","o","u","A","E","I","O","U"}
        l = 0
        word = list(s)
        n = len(s)
        r = n-1
        flagl = False
        flagr = False
        while l<r:
            if word[l] not in vowels: l+=1
            else: flagl = True 
            if word[r] not in vowels: r-=1
            else : flagr = True 
            if flagl == True and flagr == True:
                word[l], word[r] = word[r], word[l]
                l += 1
                r -= 1
                flagl = False
                flagr = False
        return "".join(word)
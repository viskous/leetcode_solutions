class Solution(object):
    def romanToInt(self, s):
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        sum = 0
        n = len(s)
        for r in range(n): 
            if r > 0 :
                if dic[s[r-1]] < dic[s[r]]:
                        sum = sum + dic[s[r]] - (2*dic[s[r-1]])
                else:
                    sum += dic[s[r]]
            else:
                    sum += dic[s[r]]
        return sum

class Solution:
    def compress(self, chars: List[str]) -> int:
        l = 0
        count = 0
        s = ""
        m = len(chars)
        for ch in range(m):
            if chars[l] == chars[ch]:
                count += 1
            else:
                s += chars[l]
                if count > 1:
                    s += str(count)
                count = 1
                l = ch
            if ch == m-1:
                s += chars[l]
                if count > 1:
                    s += str(count)
                count = 1
                l = ch
        chars_temp = list(s)
        t_count = len(chars_temp)
        for i in range(len(chars_temp)):
            chars[i] = chars_temp[i]
        return t_count


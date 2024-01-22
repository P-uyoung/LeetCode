class Solution:
    def compress(self, chars: [str]) -> int:
        s = chars[0]
        res, i = 1, 1
        cnt = 1
        while i < len(chars):
            if s == chars[i]:
                cnt += 1
            else:
                if cnt != 1:
                    chars[res:] = list(str(cnt)) + chars[i:]
                    if cnt >= 10:
                        i -= (cnt - len(str(cnt)) - 1)
                    else:
                        i -= cnt -2
                res = i + 1
                s = chars[i]
                cnt = 1
            i += 1
        if cnt > 1:
            chars[res:] = list(str(cnt))

        return len(chars)
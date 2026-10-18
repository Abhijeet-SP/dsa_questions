class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        tp = 0
        ct = 0
        for i in range(len(s)):
            while tp < len(t):
                if s[i] == t[tp]:
                    tp += 1
                    ct += 1
                    break
                else:
                    tp += 1

        if ct == len(s):
            return True
        return False
        
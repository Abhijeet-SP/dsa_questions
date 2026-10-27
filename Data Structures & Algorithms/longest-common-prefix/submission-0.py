class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = sorted(strs)
        f = s[0]
        l = s[-1]
        
        ans = ""
        for i in range(len(min(f, l, key=len))):
            if f[i] == l[i]:
                ans += f[i]
            else:
                break
        
        return ans
        
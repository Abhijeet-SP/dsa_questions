class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mpst = {}
        mpts = {}

        for i in range(len(s)):
            if s[i] in mpst and mpst[s[i]] != t[i]:
                return False 
            
            mpst[s[i]] = t[i]
        
        st = True

        for i in range(len(s)):
            if t[i] in mpts and mpts[t[i]] != s[i]:
                return False 
            
            mpts[t[i]] = s[i]
        
        ts = True
        return ts and st
                

        
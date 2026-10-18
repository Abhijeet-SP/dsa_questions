class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ct = 0 
        for i in details:
            if int(i[11:13]) > 60:
                ct += 1
        
        return ct

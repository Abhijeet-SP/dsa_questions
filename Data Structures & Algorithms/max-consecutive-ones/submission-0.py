class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ct = 0 
        cta = []
        for i in nums:
            if i == 1:
                ct += 1
            else:
                cta.append(ct)
                ct = 0 
        cta.append(ct)
        return max(cta)
            
        
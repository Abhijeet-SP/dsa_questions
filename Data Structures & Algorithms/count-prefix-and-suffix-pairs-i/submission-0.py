class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(str1, str2):
            l1 = len(str1)
            if str1 == str2[0:l1] and str1 == str2[-1*l1:]:
                return 1
            else:
                return 0
        sm = 0
        for i in range(len(words)):
            j = i+1
            while j < len(words):
                sm += isPrefixAndSuffix(words[i], words[j])
                j += 1
        
        return sm
        
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        marr = []
        ans = []
        for i in words:
            if i.startswith(('a', 'e', 'i', 'o', 'u')) and i.endswith(('a', 'e', 'i', 'o', 'u')):
                marr.append(1)
            else:
                marr.append(0)
        
        for i in queries:
            ans.append(sum(marr[i[0]:i[-1]+1]))
        
        return ans


        
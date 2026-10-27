class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in range(len(strs)):
            d["".join(sorted(strs[i]))] = d.get("".join(sorted(strs[i])), "") + strs[i] + ","

        ans = []
        for k, v in d.items():
            ans.append(v.split(','))
        for i in range(len(ans)):
            ans[i].pop()
        
        
        return ans
        
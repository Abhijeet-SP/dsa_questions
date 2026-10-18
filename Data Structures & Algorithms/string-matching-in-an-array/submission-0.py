class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        for i in range(len(words)):
            j = 0
            while j < len(words):
                if i == j:
                    j += 1
                elif words[i] in words[j]:
                    ans.append(words[i])
                    break
                else:
                    j += 1
        return ans

        
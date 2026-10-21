class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(numRows):
            lis_appen = []
            j = 0
            while j <= i:
                if j==0 or j == i:
                    lis_appen.append(1)
                    j += 1
                else:
                    if i == 0:
                        continue
                    else:
                        lis_appen.append(sum(ans[i-1][j-1: j+1]))
                        j += 1
            ans.append(lis_appen)
        return ans
        
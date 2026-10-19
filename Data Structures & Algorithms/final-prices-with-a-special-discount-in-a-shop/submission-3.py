class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        dp = []
        l = len(prices)
        for i in range(l):
            j = i
            while j < l:
                if j != l-1:
                    if prices[j+1] <= prices[i]:
                        dp.append(prices[i] - prices[j+1])
                        break
                    else:
                        j += 1
                else:
                    dp.append(prices[i])
                    break
        
        return dp


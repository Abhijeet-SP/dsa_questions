class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        fb = flowerbed.copy()
        if len(fb) == 1 and fb[0] == 0:
            return n == 1 or  n == 0
        if fb[0] == 0 and fb[1] == 0:
            n -= 1
            if n==0:
                return True
        if fb[len(fb)-1] == 0 and fb[len(fb) -2] == 0:
            n -= 1
            if n== 0:
                return True
        for i in range(1, len(fb)-1):
            if fb[i+1] == 0 and fb[i-1] == 0 and fb[i] != 1:
                n -= 1
                fb[i] = 1
                if n== 0:
                    return True
        return n == 0
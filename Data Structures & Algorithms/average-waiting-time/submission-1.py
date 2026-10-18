class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        sm = customers[0][-1]
        f = customers[0][0] + customers[0][-1]
        for i in range(1, len(customers)): 
            if f >= customers[i][0]:
                a = customers[i][0]
                f = f + customers[i][-1]
                sm += f - a
            else:
                f = customers[i][0] + customers[i][-1]
                sm += customers[i][-1]
        return sm/len(customers)

        
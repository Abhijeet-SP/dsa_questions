class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []
        for i in operations:
            if i == '+':
                records.append(sum(records.copy()[-2:]))
            elif i == 'C':
                records.pop()
            elif i == 'D':
                records.append(records.copy()[-1]*2)
            else:
                records.append(int(i))
        
        print(records)
        return sum(records)
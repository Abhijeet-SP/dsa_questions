class Solution:
    def minOperations(self, logs: List[str]) -> int:
        op = []
        for i in logs:
            if i == "../":
                if len(op) != 0:
                    op.pop()
            elif i != "./":
                op.append(i)
        print(op)
        return len(op)




        
        
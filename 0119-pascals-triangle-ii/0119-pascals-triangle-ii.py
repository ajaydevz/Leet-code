class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        results=[1]
        last=1
        for i in range(1,rowIndex+1):
            next_value=last * (rowIndex - i + 1) // i
            results.append(next_value)
            last=next_value
        return results
class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7  
        # Calculate the number of complete weeks.
        total = 0
        
        for i in range(weeks):
            total += (28 + 7 * i)  
        # Each week, the amount increases by 28 + 7 * i.
        
        for i in range(n % 7):
            total += (weeks + i + 1) 
        # For the remaining days, the amount increases by weeks + i + 1.
        
        return total

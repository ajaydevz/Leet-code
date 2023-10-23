class Solution:
    def isPowerOfFour(self, n):
        # Iterate through powers of 4 from 4^0 to 4^15
        for i in range(16):
            power_of_four = 4 ** i
            
            # If we find a power of four equal to 'n', return True
            if power_of_four == n:
                return True
            
            # If the current power of four is greater than 'n', there's no need to continue
            if power_of_four > n:
                return False
        
        # 'n' is not a power of four
        return False

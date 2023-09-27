class Solution(object):
    def decodeAtIndex(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        decoded_length = 0
        

        for char in s:
            if char.isdigit():
                decoded_length *= int(char)
            else:
                decoded_length += 1
        
        
        for char in reversed(s):
            k %= decoded_length  
            
            if k == 0 and char.isalpha():
                return char
            
            if char.isdigit():
                decoded_length //= int(char)
            else:
                decoded_length -= 1

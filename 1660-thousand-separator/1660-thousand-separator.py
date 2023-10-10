class Solution:
    def thousandSeparator(self, n: int) -> str:
        n = str(n)  # Convert the integer to a string
        length = len(n)  # Calculate the length of the string

        if length <= 3:
            return n  # If the number has 3 or fewer digits, no need for separators

        result = []
        for i in range(length):
            if i > 0 and (length - i) % 3 == 0:
                result.append('.')  # Add a separator before every group of 3 digits
            result.append(n[i])

        return ''.join(result)

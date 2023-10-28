class Solution:
    def countVowelPermutation(self, n: int) -> int:
        prevA, prevE, prevI, prevO, prevU = 1, 1, 1, 1, 1
        mod = 10**9 + 7  # Modulo value to handle large numbers

        for length in range(2, n + 1):
            # Calculate the next values for each vowel following the rules
            nextA = (prevE + prevU + prevI) % mod  # 'a' can be preceded by 'e', 'u', or 'i'
            nextE = (prevA + prevI) % mod  # 'e' can be preceded by 'a' or 'i'
            nextI = (prevE + prevO) % mod  # 'i' can be preceded by 'e' or 'o'
            nextO = prevI  # 'o' can only be preceded by 'i'
            nextU = (prevO + prevI) % mod  # 'u' can be preceded by 'o' or 'i'

            # Update the previous values for the next iteration
            prevA, prevE, prevI, prevO, prevU = nextA, nextE, nextI, nextO, nextU

        # Return the sum of all vowel counts modulo the defined value
        return (prevA + prevE + prevI + prevO + prevU) % mod
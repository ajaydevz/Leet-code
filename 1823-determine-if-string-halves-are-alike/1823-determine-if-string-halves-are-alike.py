class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        a = s[:n//2]
        b = s[n//2:]
        a_vowels = []
        b_vowels = []
        for i in a:
            if i in ('a','e','i','o','u','A','E','I','O','U'):
                a_vowels.append(i)
        for j in b:
            if j in ('a','e','i','o','u','A','E','I','O','U'):
                b_vowels.append(j)
        return (len(a_vowels)==len(b_vowels))

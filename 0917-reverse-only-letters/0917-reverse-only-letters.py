class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        alpha = []
        for i in s:
            if i.isalpha():
                alpha.append(i)

        alpha = alpha[::-1]
        ans = ''
        k = 0
        for i in s:
            if i.isalpha():
                ans += alpha[k]
                k+=1
            else:
                ans += i
        return ans

        



        
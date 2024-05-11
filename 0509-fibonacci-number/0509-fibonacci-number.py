class Solution:
    def fib(self, n: int) -> int:
        a,b = 0,1
        if n == 0:
            return 0
        for i in range(2,n+1):
            a,b = b,a+b
        return b

        
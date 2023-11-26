class Solution:
    def mySqrt(self, s: int) -> int:
        x=sqrt(s)
        if x%1<0.5:
            return round(x)
        else:
            return round(x-0.5)     
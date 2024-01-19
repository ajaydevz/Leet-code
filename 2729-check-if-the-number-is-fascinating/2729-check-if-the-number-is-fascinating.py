class Solution:
    def isFascinating(self, n: int) -> bool:
        s=str(n)+str(n*2)+str(n*3)
        k="123456789"
        return set(s)==set(k) and len(s)==9
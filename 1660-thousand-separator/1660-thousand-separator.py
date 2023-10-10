class Solution:
    def thousandSeparator(self, n: int) -> str:
        rep  = "{:,}".format(n)       
        return rep.replace(",", ".")   
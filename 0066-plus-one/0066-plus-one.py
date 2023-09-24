class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=''.join(map(str,digits))
        x=int(s)+1
        k=str(x)
        p=[int(i) for i in k]
        return p
                 
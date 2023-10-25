class Solution(object):
    def kthGrammar(self, n, k):
        if n == 1:
            return 0
        parent = self.kthGrammar(n - 1, (k + 1) // 2)
        if k % 2 == 0:
            return 0 if parent == 1 else 1
        else:
            return parent
        
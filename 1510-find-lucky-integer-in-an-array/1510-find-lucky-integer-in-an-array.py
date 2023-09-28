class Solution:
    def findLucky(self,arr):
        a=Counter(arr)
        l=[]
        for i in arr:
            if i==a[i]:
                l.append(i)
        if l:
            return max(l)
        return -1







        



        
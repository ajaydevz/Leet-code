class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def solve(s):
            ans=[]
            for i in s:
                if i!='#':
                    ans.append(i)
                elif ans:
                    ans.pop()
            return ans
        return solve(s) == solve(t)



class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count=Counter(nums)
        maximum=max(count.values())
        list1=list(count.elements())
        return [list1[i::maximum] for i in range(maximum)]
        
            
        
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people=list(zip(names,heights))
        people.sort(key=lambda x: x[1],reverse=True)
        names= [name for name,heights in people]
        return names

        

        
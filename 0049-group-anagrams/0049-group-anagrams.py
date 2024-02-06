class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
              
        anagram =  defaultdict(list)
        
        for i in strs:
            anagram[''.join(sorted(i))].append(i)

        return list(anagram.values())


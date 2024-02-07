class Solution:
    def frequencySort(self, s: str) -> str:
        charcount = Counter(s)
        sorted_char = sorted(charcount.items(), key = lambda x:x[1], reverse=True)
        sorted_string = ''.join(count*char for char,count in sorted_char)
        return sorted_string
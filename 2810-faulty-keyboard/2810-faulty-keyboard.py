class Solution:
    def finalString(self, s: str) -> str:
        
        list_s = list(s)
        return_list = []
        length = len(s)

        for i in range(length):
            if list_s[i] == "i":
                return_list.reverse()
            else:
                return_list.append(list_s[i])
                
        return ''.join(return_list)
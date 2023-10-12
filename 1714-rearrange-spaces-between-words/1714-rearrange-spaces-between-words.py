class Solution:
    def reorderSpaces(self, text: str) -> str:
        cnt = text.count(" ")
        text = text.split()
        if len(text) == 1:
            return text[0] + " " * cnt
        cnt_spaces, cnt_last = divmod(cnt, len(text) - 1)
        return (" " * cnt_spaces).join(text) + " " * cnt_last

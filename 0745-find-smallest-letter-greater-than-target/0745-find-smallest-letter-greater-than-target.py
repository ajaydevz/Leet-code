class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right, i = 0, len(letters), -1

        while left < right:
            mid = (left + right) // 2
            
            if mid + 1 < len(letters) and letters[mid] <= target and letters[mid + 1] > target:
                i = mid + 1
                break;
            elif letters[mid] > target:
                right = mid
            else:
                left = mid + 1

        return letters[0] if i == -1 else letters[i]

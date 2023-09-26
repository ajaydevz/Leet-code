class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        x = 0
        for i in arr1:
            count = 1
            for j in arr2:
                if abs(i-j) <= d:
                    count = 0
                    break
            if count:
                x += 1
        return x


        
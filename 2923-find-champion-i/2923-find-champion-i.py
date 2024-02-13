class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        arr = [0]*len(grid)
        for i in range(len(grid)):
            arr[i]=sum(grid[i])
        return arr.index(max(arr))


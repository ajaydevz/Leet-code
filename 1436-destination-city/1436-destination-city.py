class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start_city = set()
        for path in paths:
            start_city.add(path[0])
        for path in paths:
            if path[1] not in start_city:
                return path[1]

        
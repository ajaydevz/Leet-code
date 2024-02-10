class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        max_key = (releaseTimes[0], keysPressed[0])
        prev = 0
        for time,key in zip(releaseTimes,keysPressed):
            max_key = max(max_key, (time - prev, key))
            prev = time
        return max_key[1]
        


        

        
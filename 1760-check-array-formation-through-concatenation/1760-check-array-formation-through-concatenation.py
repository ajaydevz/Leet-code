class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        
        ## create a dictionary
        # key: head number of piece
        # value: all number of single piece
        mapping = { piece[0]: piece for piece in pieces }
        
        result = []
        
        # try to make array from pieces
        for number in arr:
            
            result += mapping.get( number, [] )
        
        # check they are the same or not
        return result == arr
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def max_from_rows(root):
    if not root:
        return
    
    queue = []
    queue.append(root)
    next_row = []
    max_ele_from_rows = []
    max_ele_from_rows.append(root.val)

    while queue:
        node = queue.pop(0)

        if node.left:
            next_row.append(node.left)

        if node.right:
            next_row.append(node.right)
        
        if not queue:
            queue, next_row = next_row, queue
            if queue:
                max_ele_from_rows.append(
                    max(
                        list(
                            map(lambda x: x.val, queue)
                        )
                    )
                )
    return max_ele_from_rows
        


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        return max_from_rows(root)      
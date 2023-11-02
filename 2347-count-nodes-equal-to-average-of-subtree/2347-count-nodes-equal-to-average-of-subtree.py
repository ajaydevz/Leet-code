class Solution:
    def __init__(self):
        self.matchingSubtreeCount = 0  # Initialize the count of subtrees with matching averages.

    # A Depth-First Search (DFS) function that returns a tuple of two values:
    # - The sum of values within the current subtree.
    # - The number of nodes within the current subtree.
    def calculateSubtreeValues(self, currentNode):
        if currentNode is None:
            return 0, 0  # Base case: Return 0 for both sum and number of nodes if the node is None.

        # Recursively calculate values for the left and right subtrees.
        leftSubtree  = self.calculateSubtreeValues(currentNode.left)
        rightSubtree = self.calculateSubtreeValues(currentNode.right)

        # Calculate the sum of values and the number of nodes in the current subtree.
        sumOfValues  = leftSubtree [0] + rightSubtree[0] + currentNode.val
        numberOfNodes  = leftSubtree [1] + rightSubtree[1] + 1

        # Check if the current node's value matches the average of its subtree.
        if numberOfNodes  != 0 and sumOfValues  // numberOfNodes  == currentNode.val:
            self.matchingSubtreeCount += 1

        return sumOfValues , numberOfNodes   # Return the calculated values for the current subtree.


    def averageOfSubtree(self, root):
        self.calculateSubtreeValues(root)  # Start the DFS from the root node.
        return self.matchingSubtreeCount 
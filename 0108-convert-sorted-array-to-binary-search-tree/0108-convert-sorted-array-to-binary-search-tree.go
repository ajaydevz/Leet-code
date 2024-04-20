/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func sortedArrayToBST(nums []int) *TreeNode {
    return sortedArrayToBSTRec(0, len(nums)-1, nums)
}

func sortedArrayToBSTRec(start int, end int, nums[]int) *TreeNode {
    if start > end {
        return nil
    }
    mid := (start+end)/2

    var root TreeNode
    root.Val = nums[mid]
    root.Left = sortedArrayToBSTRec(start, mid-1, nums)
    root.Right = sortedArrayToBSTRec(mid+1, end, nums)
    return &root
}

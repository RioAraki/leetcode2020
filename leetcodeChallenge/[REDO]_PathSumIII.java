/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

// there is duplicate when recursing and check sum, so it is not the best solution

class Solution {
    
    int paths = 0;
    
    public int pathSum(TreeNode root, int sum) {
        if (root == null) {
            return 0;
        }
        helper(root, sum);
        pathSum(root.left, sum);
        pathSum(root.right, sum);
        return paths;
    }
    
    private void helper (TreeNode node, int sum) {
        if (node != null && node.val == sum) {
            paths++;
        }
        if (node != null) {
            sum -= node.val;
            helper(node.left, sum);
            helper(node.right, sum);
        }
    }
}
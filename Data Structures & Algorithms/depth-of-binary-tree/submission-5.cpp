class Solution {
public:
    int maxDepth(TreeNode* root) {
        // Base case: If the node is null, the depth is 0
        if (!root) return 0;
        
        // Recursively find the depth of left and right subtrees
        // The depth of the current node is 1 + the maximum of its children
        return 1 + std::max(maxDepth(root->left), maxDepth(root->right));
    }
};
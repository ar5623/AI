#include <iostream>

// Definition for a binary tree node
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    void solve(TreeNode* root, int& low, int& high, int& sum) {
        // Base case
        if (root == nullptr) return;

        if (root->val >= low && root->val <= high) { // In the range
            sum += root->val;
            solve(root->left, low, high, sum);
            solve(root->right, low, high, sum);
        } else if (root->val < low) {
            solve(root->right, low, high, sum);
        } else if (root->val > high) {
            solve(root->left, low, high, sum);
        }
    }

    int rangeSumBST(TreeNode* root, int low, int high) {
        int sum = 0;
        solve(root, low, high, sum);
        return sum;
    }
};

int main() {
    // Example usage
    // Construct the binary search tree
    TreeNode* root = new TreeNode(10);
    root->left = new TreeNode(5);
    root->right = new TreeNode(15);
    root->left->left = new TreeNode(3);
    root->left->right = new TreeNode(7);
    root->right->right = new TreeNode(18);

    Solution solution;
    int low = 7, high = 15;
    int sum = solution.rangeSumBST(root, low, high);
    std::cout << "Sum of nodes in the range [" << low << ", " << high << "]: " << sum << std::endl;


    return 0;
}

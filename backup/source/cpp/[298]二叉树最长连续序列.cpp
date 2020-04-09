//给你一棵指定的二叉树，请你计算它最长连续序列路径的长度。 
//
// 该路径，可以是从某个初始结点到树中任意结点，通过「父 - 子」关系连接而产生的任意路径。 
//
// 这个最长连续的路径，必须从父结点到子结点，反过来是不可以的。 
//
// 示例 1： 
//
// 输入:
//
//   1
//    \
//     3
//    / \
//   2   4
//        \
//         5
//
//输出: 3
//
//解析: 当中，最长连续序列是 3-4-5，所以返回结果为 3 
//
// 示例 2： 
//
// 输入:
//
//   2
//    \
//     3
//    / 
//   2    
//  / 
// 1
//
//输出: 2 
//
//解析: 当中，最长连续序列是 2-3。注意，不是 3-2-1，所以返回 2。 
// Related Topics 树


//leetcode submit region begin(Prohibit modification and deletion)
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int longestConsecutive(TreeNode* root) {

    }
};
//leetcode submit region end(Prohibit modification and deletion)

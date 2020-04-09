//验证原始的序列 org 是否可以从序列集 seqs 中唯一地重建。序列 org 是 1 到 n 整数的排列，其中 1 ≤ n ≤ 104。重建是指在序列集 
//seqs 中构建最短的公共超序列。（即使得所有 seqs 中的序列都是该最短序列的子序列）。确定是否只可以从 seqs 重建唯一的序列，且该序列就是 org 。
// 
//
// 示例 1： 
//
// 输入：
//org: [1,2,3], seqs: [[1,2],[1,3]]
//
//输出：
//false
//
//解释：
//[1,2,3] 不是可以被重建的唯一的序列，因为 [1,3,2] 也是一个合法的序列。
// 
//
// 
//
// 示例 2： 
//
// 输入：
//org: [1,2,3], seqs: [[1,2]]
//
//输出：
//false
//
//解释：
//可以重建的序列只有 [1,2]。
// 
//
// 
//
// 示例 3： 
//
// 输入：
//org: [1,2,3], seqs: [[1,2],[1,3],[2,3]]
//
//输出：
//true
//
//解释：
//序列 [1,2], [1,3] 和 [2,3] 可以被唯一地重建为原始的序列 [1,2,3]。
// 
//
// 
//
// 示例 4： 
//
// 输入：
//org: [4,1,5,2,6,3], seqs: [[5,2,6,3],[4,1,5,2]]
//
//输出：
//true
// 
// Related Topics 图 拓扑排序


//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    bool sequenceReconstruction(vector<int>& org, vector<vector<int>>& seqs) {

    }
};
//leetcode submit region end(Prohibit modification and deletion)

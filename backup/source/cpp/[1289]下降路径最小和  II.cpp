//给你一个整数方阵 arr ，定义「非零偏移下降路径」为：从 arr 数组中的每一行选择一个数字，且按顺序选出来的数字中，相邻数字不在原数组的同一列。 
//
// 请你返回非零偏移下降路径数字和的最小值。 
//
// 
//
// 示例 1： 
//
// 
//输入：arr = [[1,2,3],[4,5,6],[7,8,9]]
//输出：13
//解释：
//所有非零偏移下降路径包括：
//[1,5,9], [1,5,7], [1,6,7], [1,6,8],
//[2,4,8], [2,4,9], [2,6,7], [2,6,8],
//[3,4,8], [3,4,9], [3,5,7], [3,5,9]
//下降路径中数字和最小的是 [1,5,7] ，所以答案是 13 。
// 
//
// 
//
// 提示： 
//
// 
// 1 <= arr.length == arr[i].length <= 200 
// -99 <= arr[i][j] <= 99 
// 
// Related Topics 动态规划


//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& arr) {

    }
};
//leetcode submit region end(Prohibit modification and deletion)

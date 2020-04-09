//已知有 N 门课程，它们以 1 到 N 进行编号。 
//
// 给你一份课程关系表 relations[i] = [X, Y]，用以表示课程 X 和课程 Y 之间的先修关系：课程 X 必须在课程 Y 之前修完。 
//
// 假设在一个学期里，你可以学习任何数量的课程，但前提是你已经学习了将要学习的这些课程的所有先修课程。 
//
// 请你返回学完全部课程所需的最少学期数。 
//
// 如果没有办法做到学完全部这些课程的话，就返回 -1。 
//
// 
//
// 示例 1： 
//
// 
//
// 输入：N = 3, relations = [[1,3],[2,3]]
//输出：2
//解释：
//在第一个学期学习课程 1 和 2，在第二个学期学习课程 3。
// 
//
// 示例 2： 
//
// 
//
// 输入：N = 3, relations = [[1,2],[2,3],[3,1]]
//输出：-1
//解释：
//没有课程可以学习，因为它们相互依赖。 
//
// 
//
// 提示： 
//
// 
// 1 <= N <= 5000 
// 1 <= relations.length <= 5000 
// relations[i][0] != relations[i][1] 
// 输入中没有重复的关系 
// 
// Related Topics 深度优先搜索 图 动态规划


//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    int minimumSemesters(int N, vector<vector<int>>& relations) {

    }
};
//leetcode submit region end(Prohibit modification and deletion)

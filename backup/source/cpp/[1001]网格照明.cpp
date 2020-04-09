//在 N x N 的网格上，每个单元格 (x, y) 上都有一盏灯，其中 0 <= x < N 且 0 <= y < N 。 
//
// 最初，一定数量的灯是亮着的。lamps[i] 告诉我们亮着的第 i 盏灯的位置。每盏灯都照亮其所在 x 轴、y 轴和两条对角线上的每个正方形（类似于国际象
//棋中的皇后）。 
//
// 对于第 i 次查询 queries[i] = (x, y)，如果单元格 (x, y) 是被照亮的，则查询结果为 1，否则为 0 。 
//
// 在每个查询 (x, y) 之后 [按照查询的顺序]，我们关闭位于单元格 (x, y) 上或其相邻 8 个方向上（与单元格 (x, y) 共享一个角或边）的
//任何灯。 
//
// 返回答案数组 answer。每个值 answer[i] 应等于第 i 次查询 queries[i] 的结果。 
//
// 
//
// 示例： 
//
// 输入：N = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,0]]
//输出：[1,0]
//解释： 
//在执行第一次查询之前，我们位于 [0, 0] 和 [4, 4] 灯是亮着的。
//表示哪些单元格亮起的网格如下所示，其中 [0, 0] 位于左上角：
//1 1 1 1 1
//1 1 0 0 1
//1 0 1 0 1
//1 0 0 1 1
//1 1 1 1 1
//然后，由于单元格 [1, 1] 亮着，第一次查询返回 1。在此查询后，位于 [0，0] 处的灯将关闭，网格现在如下所示：
//1 0 0 0 1
//0 1 0 0 1
//0 0 1 0 1
//0 0 0 1 1
//1 1 1 1 1
//在执行第二次查询之前，我们只有 [4, 4] 处的灯亮着。现在，[1, 0] 处的查询返回 0，因为该单元格不再亮着。
// 
//
// 
//
// 提示： 
//
// 
// 1 <= N <= 10^9 
// 0 <= lamps.length <= 20000 
// 0 <= queries.length <= 20000 
// lamps[i].length == queries[i].length == 2 
// 
// Related Topics 哈希表


//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    vector<int> gridIllumination(int N, vector<vector<int>>& lamps, vector<vector<int>>& queries) {

    }
};
//leetcode submit region end(Prohibit modification and deletion)

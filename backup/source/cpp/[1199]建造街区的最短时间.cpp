//你是个城市规划工作者，手里负责管辖一系列的街区。在这个街区列表中 blocks[i] = t 意味着第 i 个街区需要 t 个单位的时间来建造。 
//
// 由于一个街区只能由一个工人来完成建造。 
//
// 所以，一个工人要么需要再召唤一个工人（工人数增加 1）；要么建造完一个街区后回家。这两个决定都需要花费一定的时间。 
//
// 一个工人再召唤一个工人所花费的时间由整数 split 给出。 
//
// 注意：如果两个工人同时召唤别的工人，那么他们的行为是并行的，所以时间花费仍然是 split。 
//
// 最开始的时候只有 一个 工人，请你最后输出建造完所有街区所需要的最少时间。 
//
// 
//
// 示例 1： 
//
// 输入：blocks = [1], split = 1
//输出：1
//解释：我们使用 1 个工人在 1 个时间单位内来建完 1 个街区。
// 
//
// 示例 2： 
//
// 输入：blocks = [1,2], split = 5
//输出：7
//解释：我们用 5 个时间单位将这个工人分裂为 2 个工人，然后指派每个工人分别去建造街区，从而时间花费为 5 + max(1, 2) = 7
// 
//
// 示例 3： 
//
// 输入：blocks = [1,2,3], split = 1
//输出：4
//解释：
//将 1 个工人分裂为 2 个工人，然后指派第一个工人去建造最后一个街区，并将第二个工人分裂为 2 个工人。
//然后，用这两个未分派的工人分别去建造前两个街区。
//时间花费为 1 + max(3, 1 + max(1, 2)) = 4
// 
//
// 
//
// 提示： 
//
// 
// 1 <= blocks.length <= 1000 
// 1 <= blocks[i] <= 10^5 
// 1 <= split <= 100 
// 
// Related Topics 数学 动态规划


//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    int minBuildTime(vector<int>& blocks, int split) {

    }
};
//leetcode submit region end(Prohibit modification and deletion)

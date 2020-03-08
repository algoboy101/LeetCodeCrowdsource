//有 N 名工人。 第 i 名工人的工作质量为 quality[i] ，其最低期望工资为 wage[i] 。 
//
// 现在我们想雇佣 K 名工人组成一个工资组。在雇佣 一组 K 名工人时，我们必须按照下述规则向他们支付工资： 
//
// 
// 对工资组中的每名工人，应当按其工作质量与同组其他工人的工作质量的比例来支付工资。 
// 工资组中的每名工人至少应当得到他们的最低期望工资。 
// 
//
// 返回组成一个满足上述条件的工资组至少需要多少钱。 
//
// 
//
// 
// 
//
// 示例 1： 
//
// 输入： quality = [10,20,5], wage = [70,50,30], K = 2
//输出： 105.00000
//解释： 我们向 0 号工人支付 70，向 2 号工人支付 35。 
//
// 示例 2： 
//
// 输入： quality = [3,1,10,10,1], wage = [4,8,2,2,7], K = 3
//输出： 30.66667
//解释： 我们向 0 号工人支付 4，向 2 号和 3 号分别支付 13.33333。 
//
// 
//
// 提示： 
//
// 
// 1 <= K <= N <= 10000，其中 N = quality.length = wage.length 
// 1 <= quality[i] <= 10000 
// 1 <= wage[i] <= 10000 
// 与正确答案误差在 10^-5 之内的答案将被视为正确的。 
// 
// Related Topics 堆


//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    double mincostToHireWorkers(vector<int>& quality, vector<int>& wage, int K) {

    }
};
//leetcode submit region end(Prohibit modification and deletion)

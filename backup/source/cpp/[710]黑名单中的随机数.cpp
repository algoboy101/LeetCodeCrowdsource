//给定一个包含 [0，n ) 中独特的整数的黑名单 B，写一个函数从 [ 0，n ) 中返回一个不在 B 中的随机整数。 
//
// 对它进行优化使其尽量少调用系统方法 Math.random() 。 
//
// 提示: 
//
// 
// 1 <= N <= 1000000000 
// 0 <= B.length < min(100000, N) 
// [0, N) 不包含 N，详细参见 interval notation 。 
// 
//
// 示例 1: 
//
// 
//输入: 
//["Solution","pick","pick","pick"]
//[[1,[]],[],[],[]]
//输出: [null,0,0,0]
// 
//
// 示例 2: 
//
// 
//输入: 
//["Solution","pick","pick","pick"]
//[[2,[]],[],[],[]]
//输出: [null,1,1,1]
// 
//
// 示例 3: 
//
// 
//输入: 
//["Solution","pick","pick","pick"]
//[[3,[1]],[],[],[]]
//Output: [null,0,0,2]
// 
//
// 示例 4: 
//
// 
//输入: 
//["Solution","pick","pick","pick"]
//[[4,[2]],[],[],[]]
//输出: [null,1,3,1]
// 
//
// 输入语法说明： 
//
// 输入是两个列表：调用成员函数名和调用的参数。Solution的构造函数有两个参数，N 和黑名单 B。pick 没有参数，输入参数是一个列表，即使参数为空，
//也会输入一个 [] 空列表。 
// Related Topics 排序 哈希表 二分查找 Random


//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    Solution(int N, vector<int>& blacklist) {

    }
    
    int pick() {

    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(N, blacklist);
 * int param_1 = obj->pick();
 */
//leetcode submit region end(Prohibit modification and deletion)

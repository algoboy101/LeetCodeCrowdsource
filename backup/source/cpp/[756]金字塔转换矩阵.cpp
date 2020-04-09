//现在，我们用一些方块来堆砌一个金字塔。 每个方块用仅包含一个字母的字符串表示。 
//
// 使用三元组表示金字塔的堆砌规则如下： 
//
// 对于三元组(A, B, C) ，“C”为顶层方块，方块“A”、“B”分别作为方块“C”下一层的的左、右子块。当且仅当(A, B, C)是被允许的三元组，我
//们才可以将其堆砌上。 
//
// 初始时，给定金字塔的基层 bottom，用一个字符串表示。一个允许的三元组列表 allowed，每个三元组用一个长度为 3 的字符串表示。 
//
// 如果可以由基层一直堆到塔尖就返回 true，否则返回 false。 
//
// 
//
// 示例 1: 
//
// 输入: bottom = "BCD", allowed = ["BCG", "CDE", "GEA", "FFF"]
//输出: true
//解析:
//可以堆砌成这样的金字塔:
//    A
//   / \
//  G   E
// / \ / \
//B   C   D
//
//因为符合('B', 'C', 'G'), ('C', 'D', 'E') 和 ('G', 'E', 'A') 三种规则。
// 
//
// 示例 2: 
//
// 输入: bottom = "AABA", allowed = ["AAA", "AAB", "ABA", "ABB", "BAC"]
//输出: false
//解析:
//无法一直堆到塔尖。
//注意, 允许存在像 (A, B, C) 和 (A, B, D) 这样的三元组，其中 C != D。
// 
//
// 
//
// 注意： 
//
// 
// bottom 的长度范围在 [2, 8]。 
// allowed 的长度范围在[0, 200]。 
// 方块的标记字母范围为{'A', 'B', 'C', 'D', 'E', 'F', 'G'}。 
// 
// Related Topics 位运算 深度优先搜索


//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    bool pyramidTransition(string bottom, vector<string>& allowed) {

    }
};
//leetcode submit region end(Prohibit modification and deletion)

//给定一个 非空 字符串，将其编码为具有最短长度的字符串。 
//
// 编码规则是：k[encoded_string]，其中在方括号 encoded_string 中的内容重复 k 次。 
//
// 注： 
//
// 
// k 为正整数且编码后的字符串不能为空或有额外的空格。 
// 你可以假定输入的字符串只包含小写的英文字母。字符串长度不超过 160。 
// 如果编码的过程不能使字符串缩短，则不要对其进行编码。如果有多种编码方式，返回任意一种即可。 
// 
//
// 
//
// 示例 1： 
//
// 输入： "aaa"
//输出： "aaa"
//解释： 无法将其编码为更短的字符串，因此不进行编码。
// 
//
// 
//
// 示例 2： 
//
// 输入： "aaaaa"
//输出： "5[a]"
//解释： "5[a]" 比 "aaaaa" 短 1 个字符。
// 
//
// 
//
// 示例 3： 
//
// 输入： "aaaaaaaaaa"
//输出： "10[a]"
//解释： "a9[a]" 或 "9[a]a" 都是合法的编码，和 "10[a]" 一样长度都为 5。
// 
//
// 
//
// 示例 4： 
//
// 输入： "aabcaabcd"
//输出： "2[aabc]d"
//解释： "aabc" 出现两次，因此一种答案可以是 "2[aabc]d"。
// 
//
// 
//
// 示例 5： 
//
// 输入： "abbbabbbcabbbabbbc"
//输出： "2[2[abbb]c]"
//解释： "abbbabbbc" 出现两次，但是 "abbbabbbc" 可以编码为 "2[abbb]c"，因此一种答案可以是 "2[2[abbb]c]"。
// 
//
// 
// Related Topics 动态规划


//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    string encode(string s) {

    }
};
//leetcode submit region end(Prohibit modification and deletion)

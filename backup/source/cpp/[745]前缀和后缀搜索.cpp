//给定多个 words，words[i] 的权重为 i 。 
//
// 设计一个类 WordFilter 实现函数WordFilter.f(String prefix, String suffix)。这个函数将返回具有前缀 p
//refix 和后缀suffix 的词的最大权重。如果没有这样的词，返回 -1。 
//
// 例子: 
//
// 
//输入:
//WordFilter(["apple"])
//WordFilter.f("a", "e") // 返回 0
//WordFilter.f("b", "") // 返回 -1
// 
//
// 注意: 
//
// 
// words的长度在[1, 15000]之间。 
// 对于每个测试用例，最多会有words.length次对WordFilter.f的调用。 
// words[i]的长度在[1, 10]之间。 
// prefix, suffix的长度在[0, 10]之前。 
// words[i]和prefix, suffix只包含小写字母。 
// 
// Related Topics 字典树


//leetcode submit region begin(Prohibit modification and deletion)
class WordFilter {
public:
    WordFilter(vector<string>& words) {

    }
    
    int f(string prefix, string suffix) {

    }
};

/**
 * Your WordFilter object will be instantiated and called as such:
 * WordFilter* obj = new WordFilter(words);
 * int param_1 = obj->f(prefix,suffix);
 */
//leetcode submit region end(Prohibit modification and deletion)

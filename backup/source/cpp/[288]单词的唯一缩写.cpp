//一个单词的缩写需要遵循 <起始字母><中间字母数><结尾字母> 这样的格式。 
//
// 以下是一些单词缩写的范例： 
//
// a) it                      --> it    (没有缩写)
//
//     1
//     ↓
//b) d|o|g                   --> d1g
//
//              1    1  1
//     1---5----0----5--8
//     ↓   ↓    ↓    ↓  ↓    
//c) i|nternationalizatio|n  --> i18n
//
//              1
//     1---5----0
//     ↓   ↓    ↓
//d) l|ocalizatio|n          --> l10n
// 
//
// 假设你有一个字典和一个单词，请你判断该单词的缩写在这本字典中是否唯一。若单词的缩写在字典中没有任何 其他 单词与其缩写相同，则被称为单词的唯一缩写。 
//
// 示例： 
//
// 给定 dictionary = [ "deer", "door", "cake", "card" ]
//
//isUnique("dear") -> false
//isUnique("cart") -> true
//isUnique("cane") -> false
//isUnique("make") -> true
// 
// Related Topics 设计 哈希表


//leetcode submit region begin(Prohibit modification and deletion)
class ValidWordAbbr {
public:
    ValidWordAbbr(vector<string>& dictionary) {

    }
    
    bool isUnique(string word) {

    }
};

/**
 * Your ValidWordAbbr object will be instantiated and called as such:
 * ValidWordAbbr* obj = new ValidWordAbbr(dictionary);
 * bool param_1 = obj->isUnique(word);
 */
//leetcode submit region end(Prohibit modification and deletion)

//对于一个压缩字符串，设计一个数据结构，它支持如下两种操作： next 和 hasNext。 
//
// 给定的压缩字符串格式为：每个字母后面紧跟一个正整数，这个整数表示该字母在解压后的字符串里连续出现的次数。 
//
// next() - 如果压缩字符串仍然有字母未被解压，则返回下一个字母，否则返回一个空格。 
//hasNext() - 判断是否还有字母仍然没被解压。 
//
// 注意： 
//
// 请记得将你的类在 StringIterator 中 初始化 ，因为静态变量或类变量在多组测试数据中不会被自动清空。更多细节请访问 这里 。 
//
// 示例： 
//
// StringIterator iterator = new StringIterator("L1e2t1C1o1d1e1");
//
//iterator.next(); // 返回 'L'
//iterator.next(); // 返回 'e'
//iterator.next(); // 返回 'e'
//iterator.next(); // 返回 't'
//iterator.next(); // 返回 'C'
//iterator.next(); // 返回 'o'
//iterator.next(); // 返回 'd'
//iterator.hasNext(); // 返回 true
//iterator.next(); // 返回 'e'
//iterator.hasNext(); // 返回 false
//iterator.next(); // 返回 ' '
// 
//
// 
// Related Topics 设计


//leetcode submit region begin(Prohibit modification and deletion)
class StringIterator {
public:
    StringIterator(string compressedString) {

    }
    
    char next() {

    }
    
    bool hasNext() {

    }
};

/**
 * Your StringIterator object will be instantiated and called as such:
 * StringIterator* obj = new StringIterator(compressedString);
 * char param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */
//leetcode submit region end(Prohibit modification and deletion)

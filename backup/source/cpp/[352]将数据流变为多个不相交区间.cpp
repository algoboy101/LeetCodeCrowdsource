//给定一个非负整数的数据流输入 a1，a2，…，an，…，将到目前为止看到的数字总结为不相交的区间列表。 
//
// 例如，假设数据流中的整数为 1，3，7，2，6，…，每次的总结为： 
//
// [1, 1]
//[1, 1], [3, 3]
//[1, 1], [3, 3], [7, 7]
//[1, 3], [7, 7]
//[1, 3], [6, 7]
// 
//
// 
//
// 进阶： 
//如果有很多合并，并且与数据流的大小相比，不相交区间的数量很小，该怎么办? 
//
// 提示： 
//特别感谢 @yunhong 提供了本问题和其测试用例。 
// Related Topics 二分查找 Ordered Map


//leetcode submit region begin(Prohibit modification and deletion)
class SummaryRanges {
public:
    /** Initialize your data structure here. */
    SummaryRanges() {

    }
    
    void addNum(int val) {

    }
    
    vector<vector<int>> getIntervals() {

    }
};

/**
 * Your SummaryRanges object will be instantiated and called as such:
 * SummaryRanges* obj = new SummaryRanges();
 * obj->addNum(val);
 * vector<vector<int>> param_2 = obj->getIntervals();
 */
//leetcode submit region end(Prohibit modification and deletion)

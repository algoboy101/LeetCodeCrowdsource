//我们有 N 个与坐标轴对齐的矩形, 其中 N > 0, 判断它们是否能精确地覆盖一个矩形区域。 
//
// 每个矩形用左下角的点和右上角的点的坐标来表示。例如， 一个单位正方形可以表示为 [1,1,2,2]。 ( 左下角的点的坐标为 (1, 1) 以及右上角的点
//的坐标为 (2, 2) )。 
//
// 
//
// 示例 1: 
//
// rectangles = [
//  [1,1,3,3],
//  [3,1,4,2],
//  [3,2,4,4],
//  [1,3,2,4],
//  [2,3,3,4]
//]
//
//返回 true。5个矩形一起可以精确地覆盖一个矩形区域。
// 
//
// 
//
// 
//
// 示例 2: 
//
// rectangles = [
//  [1,1,2,3],
//  [1,3,2,4],
//  [3,1,4,2],
//  [3,2,4,4]
//]
//
//返回 false。两个矩形之间有间隔，无法覆盖成一个矩形。
// 
//
// 
//
// 
//
// 示例 3: 
//
// rectangles = [
//  [1,1,3,3],
//  [3,1,4,2],
//  [1,3,2,4],
//  [3,2,4,4]
//]
//
//返回 false。图形顶端留有间隔，无法覆盖成一个矩形。
// 
//
// 
//
// 
//
// 示例 4: 
//
// rectangles = [
//  [1,1,3,3],
//  [3,1,4,2],
//  [1,3,2,4],
//  [2,2,4,4]
//]
//
//返回 false。因为中间有相交区域，虽然形成了矩形，但不是精确覆盖。
// 
// Related Topics Line Sweep


//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    bool isRectangleCover(vector<vector<int>>& rectangles) {

    }
};
//leetcode submit region end(Prohibit modification and deletion)

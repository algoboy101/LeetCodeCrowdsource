//为了评估某网站的用户转化率，我们需要对用户的访问行为进行分析，并建立用户行为模型。日志文件中已经记录了用户名、访问时间 以及 页面路径。 
//
// 为了方便分析，日志文件中的 N 条记录已经被解析成三个长度相同且长度都为 N 的数组，分别是：用户名 username，访问时间 timestamp 和 
//页面路径 website。第 i 条记录意味着用户名是 username[i] 的用户在 timestamp[i] 的时候访问了路径为 website[i] 的
//页面。 
//
// 我们需要找到用户访问网站时的 『共性行为路径』，也就是有最多的用户都 至少按某种次序访问过一次 的三个页面路径。需要注意的是，用户 可能不是连续访问 这三
//个路径的。 
//
// 『共性行为路径』是一个 长度为 3 的页面路径列表，列表中的路径 不必不同，并且按照访问时间的先后升序排列。 
//
// 如果有多个满足要求的答案，那么就请返回按字典序排列最小的那个。（页面路径列表 X 按字典序小于 Y 的前提条件是：X[0] < Y[0] 或 X[0] =
//= Y[0] 且 (X[1] < Y[1] 或 X[1] == Y[1] 且 X[2] < Y[2])） 
//
// 题目保证一个用户会至少访问 3 个路径一致的页面，并且一个用户不会在同一时间访问两个路径不同的页面。 
//
// 
//
// 示例： 
//
// 输入：username = ["joe","joe","joe","james","james","james","james","mary","mary
//","mary"], timestamp = [1,2,3,4,5,6,7,8,9,10], website = ["home","about","career
//","home","cart","maps","home","home","about","career"]
//输出：["home","about","career"]
//解释：
//由示例输入得到的记录如下：
//["joe", 1, "home"]
//["joe", 2, "about"]
//["joe", 3, "career"]
//["james", 4, "home"]
//["james", 5, "cart"]
//["james", 6, "maps"]
//["james", 7, "home"]
//["mary", 8, "home"]
//["mary", 9, "about"]
//["mary", 10, "career"]
//有 2 个用户至少访问过一次 ("home", "about", "career")。
//有 1 个用户至少访问过一次 ("home", "cart", "maps")。
//有 1 个用户至少访问过一次 ("home", "cart", "home")。
//有 1 个用户至少访问过一次 ("home", "maps", "home")。
//有 1 个用户至少访问过一次 ("cart", "maps", "home")。
// 
//
// 
//
// 提示： 
//
// 
// 3 <= N = username.length = timestamp.length = website.length <= 50 
// 1 <= username[i].length <= 10 
// 0 <= timestamp[i] <= 10^9 
// 1 <= website[i].length <= 10 
// username[i] 和 website[i] 都只含小写字符 
// 
// Related Topics 排序 数组 哈希表


//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    vector<string> mostVisitedPattern(vector<string>& username, vector<int>& timestamp, vector<string>& website) {

    }
};
//leetcode submit region end(Prohibit modification and deletion)

//请你实现一个能够支持以下两种方法的推文计数类 TweetCounts： 
//
// 1. recordTweet(string tweetName, int time) 
//
// 
// 记录推文发布情况：用户 tweetName 在 time（以 秒 为单位）时刻发布了一条推文。 
// 
//
// 2. getTweetCountsPerFrequency(string freq, string tweetName, int startTime, i
//nt endTime) 
//
// 
// 返回从开始时间 startTime（以 秒 为单位）到结束时间 endTime（以 秒 为单位）内，每 分 minute，时 hour 或者 日 day 
//（取决于 freq）内指定用户 tweetName 发布的推文总数。 
// freq 的值始终为 分 minute，时 hour 或者 日 day 之一，表示获取指定用户 tweetName 发布推文次数的时间间隔。 
// 第一个时间间隔始终从 startTime 开始，因此时间间隔为 [startTime, startTime + delta*1>, [startTime 
//+ delta*1, startTime + delta*2>, [startTime + delta*2, startTime + delta*3>, ...
// , [startTime + delta*i, min(startTime + delta*(i+1), endTime + 1)>，其中 i 和 delta
//（取决于 freq）都是非负整数。 
// 
//
// 
//
// 示例： 
//
// 输入：
//["TweetCounts","recordTweet","recordTweet","recordTweet","getTweetCountsPerFre
//quency","getTweetCountsPerFrequency","recordTweet","getTweetCountsPerFrequency"]
//
//[[],["tweet3",0],["tweet3",60],["tweet3",10],["minute","tweet3",0,59],["minute
//","tweet3",0,60],["tweet3",120],["hour","tweet3",0,210]]
//
//输出：
//[null,null,null,null,[2],[2,1],null,[4]]
//
//解释：
//TweetCounts tweetCounts = new TweetCounts();
//tweetCounts.recordTweet("tweet3", 0);
//tweetCounts.recordTweet("tweet3", 60);
//tweetCounts.recordTweet("tweet3", 10);                             // "tweet3"
// 发布推文的时间分别是 0, 10 和 60 。
//tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 59); // 返回 [2]。统
//计频率是每分钟（60 秒），因此只有一个有效时间间隔 [0,60> - > 2 条推文。
//tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 60); // 返回 [2,1]
//。统计频率是每分钟（60 秒），因此有两个有效时间间隔 1) [0,60> - > 2 条推文，和 2) [60,61> - > 1 条推文。 
//tweetCounts.recordTweet("tweet3", 120);                            // "tweet3"
// 发布推文的时间分别是 0, 10, 60 和 120 。
//tweetCounts.getTweetCountsPerFrequency("hour", "tweet3", 0, 210);  // 返回 [4]。统
//计频率是每小时（3600 秒），因此只有一个有效时间间隔 [0,211> - > 4 条推文。
// 
//
// 
//
// 提示： 
//
// 
// 同时考虑 recordTweet 和 getTweetCountsPerFrequency，最多有 10000 次操作。 
// 0 <= time, startTime, endTime <= 10^9 
// 0 <= endTime - startTime <= 10^4 
// 
// Related Topics 设计


//leetcode submit region begin(Prohibit modification and deletion)
class TweetCounts {
public:
    TweetCounts() {

    }
    
    void recordTweet(string tweetName, int time) {

    }
    
    vector<int> getTweetCountsPerFrequency(string freq, string tweetName, int startTime, int endTime) {

    }
};

/**
 * Your TweetCounts object will be instantiated and called as such:
 * TweetCounts* obj = new TweetCounts();
 * obj->recordTweet(tweetName,time);
 * vector<int> param_2 = obj->getTweetCountsPerFrequency(freq,tweetName,startTime,endTime);
 */
//leetcode submit region end(Prohibit modification and deletion)

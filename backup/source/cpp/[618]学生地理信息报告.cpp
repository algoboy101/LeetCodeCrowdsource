//一所美国大学有来自亚洲、欧洲和美洲的学生，他们的地理信息存放在如下 student 表中。 
//
// 
//
// | name   | continent |
//|--------|-----------|
//| Jack   | America   |
//| Pascal | Europe    |
//| Xi     | Asia      |
//| Jane   | America   |
// 
//
// 
//
// 写一个查询语句实现对大洲（continent）列的 透视表 操作，使得每个学生按照姓名的字母顺序依次排列在对应的大洲下面。输出的标题应依次为美洲（Amer
//ica）、亚洲（Asia）和欧洲（Europe）。数据保证来自美洲的学生不少于来自亚洲或者欧洲的学生。 
//
// 
//
// 对于样例输入，它的对应输出是： 
//
// 
//
// | America | Asia | Europe |
//|---------|------|--------|
//| Jack    | Xi   | Pascal |
//| Jane    |      |        |
// 
//
// 
//
// 进阶：如果不能确定哪个大洲的学生数最多，你可以写出一个查询去生成上述学生报告吗？ 
//
// 
//


//There is no code of C++ type for this problem
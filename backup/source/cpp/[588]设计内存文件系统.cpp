//设计一个内存文件系统，模拟以下功能： 
//
// ls： 以字符串的格式输入一个路径。如果它是一个文件的路径，那么函数返回一个列表，仅包含这个文件的名字。如果它是一个文件夹的的路径，那么返回该 文件夹内 
//的所有文件和子文件夹的名字。你的返回结果（包括文件和子文件夹）应该按字典序排列。 
//
// mkdir：输入一个当前不存在的 文件夹路径 ，你需要根据路径名创建一个新的文件夹。如果有上层文件夹路径不存在，那么你也应该将它们全部创建。这个函数的返回
//类型为 void 。 
//
// addContentToFile： 输入字符串形式的 文件路径 和 文件内容 。如果文件不存在，你需要创建包含给定文件内容的文件。如果文件已经存在，那么你
//需要将给定的文件内容 追加 在原本内容的后面。这个函数的返回类型为 void 。 
//
// readContentFromFile： 输入 文件路径 ，以字符串形式返回该文件的 内容 。 
//
// 
//
// 示例: 
//
// 输入: 
//["FileSystem","ls","mkdir","addContentToFile","ls","readContentFromFile"]
//[[],["/"],["/a/b/c"],["/a/b/c/d","hello"],["/"],["/a/b/c/d"]]
//
//输出:
//[null,[],null,null,["a"],"hello"]
//
//解释:
//
// 
//
// 
//
// 注意: 
//
// 
// 你可以假定所有文件和文件夹的路径都是绝对路径，除非是根目录 / 自身，其他路径都是以 / 开头且 不 以 / 结束。 
// 你可以假定所有操作的参数都是有效的，即用户不会获取不存在文件的内容，或者获取不存在文件夹和文件的列表。 
// 你可以假定所有文件夹名字和文件名字都只包含小写字母，且同一文件夹下不会有相同名字的文件夹或文件。 
// 
// Related Topics 设计


//leetcode submit region begin(Prohibit modification and deletion)
class FileSystem {
public:
    FileSystem() {

    }
    
    vector<string> ls(string path) {

    }
    
    void mkdir(string path) {

    }
    
    void addContentToFile(string filePath, string content) {

    }
    
    string readContentFromFile(string filePath) {

    }
};

/**
 * Your FileSystem object will be instantiated and called as such:
 * FileSystem* obj = new FileSystem();
 * vector<string> param_1 = obj->ls(path);
 * obj->mkdir(path);
 * obj->addContentToFile(filePath,content);
 * string param_4 = obj->readContentFromFile(filePath);
 */
//leetcode submit region end(Prohibit modification and deletion)

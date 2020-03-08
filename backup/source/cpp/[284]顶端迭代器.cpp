//给定一个迭代器类的接口，接口包含两个方法： next() 和 hasNext()。设计并实现一个支持 peek() 操作的顶端迭代器 -- 其本质就是把原本
//应由 next() 方法返回的元素 peek() 出来。 
//
// 示例: 
//
// 假设迭代器被初始化为列表 [1,2,3]。
//
//调用 next() 返回 1，得到列表中的第一个元素。
//现在调用 peek() 返回 2，下一个元素。在此之后调用 next() 仍然返回 2。
//最后一次调用 next() 返回 3，末尾元素。在此之后调用 hasNext() 应该返回 false。
// 
//
// 进阶：你将如何拓展你的设计？使之变得通用化，从而适应所有的类型，而不只是整数型？ 
// Related Topics 设计


//leetcode submit region begin(Prohibit modification and deletion)
// Below is the interface for Iterator, which is already defined for you.
// **DO NOT** modify the interface for Iterator.

class Iterator {
    struct Data;
	Data* data;
public:
	Iterator(const vector<int>& nums);
	Iterator(const Iterator& iter);
	virtual ~Iterator();
	// Returns the next element in the iteration.
	int next();
	// Returns true if the iteration has more elements.
	bool hasNext() const;
};


class PeekingIterator : public Iterator {
public:
	PeekingIterator(const vector<int>& nums) : Iterator(nums) {
	    // Initialize any member here.
	    // **DO NOT** save a copy of nums and manipulate it directly.
	    // You should only use the Iterator interface methods.
	    
	}

    // Returns the next element in the iteration without advancing the iterator.
	int peek() {
        
	}

	// hasNext() and next() should behave the same as in the Iterator interface.
	// Override them if needed.
	int next() {
	    
	}

	bool hasNext() const {
	    
	}
};
//leetcode submit region end(Prohibit modification and deletion)

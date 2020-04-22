---
title: "[0028] 实现 strStr()"
tags:
  - leetcode
  - 题解
  - 双指针
  - 字符串
  - 精选TOP面试题
categories:
  - leetcode
  - 题解
author:
  - 黄宁
comments: true
updated: true
permalink:
mathjax: true
top: false
description: ...
date: 2020-04-22 15:27:28

---


# [0028] 实现 strStr()

* [GitHub](https://github.com/algoboy101/LeetCodeCrowdsource/tree/master/_posts/QA/%5B0028%5D%20%E5%AE%9E%E7%8E%B0%20strStr%28%29.md)
* http://leetcode.xuezhisd.top/post/e92fc7c8.html
* https://leetcode.com/problems/implement-strstr
* https://leetcode-cn.com/problems/implement-strstr


## 题目描述

<p>实现&nbsp;<a href="https://baike.baidu.com/item/strstr/811469" target="_blank">strStr()</a>&nbsp;函数。</p>
<p>给定一个&nbsp;haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回&nbsp; <strong>-1</strong>。</p>
<p><strong>示例 1:</strong></p>
<pre><strong>输入:</strong> haystack = &quot;hello&quot;, needle = &quot;ll&quot;
<strong>输出:</strong> 2
</pre>

<p><strong>示例 2:</strong></p>
<pre><strong>输入:</strong> haystack = &quot;aaaaa&quot;, needle = &quot;bba&quot;
<strong>输出:</strong> -1
</pre>

<p><strong>说明:</strong></p>
<p>当&nbsp;<code>needle</code>&nbsp;是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。</p>
<p>对于本题而言，当&nbsp;<code>needle</code>&nbsp;是空字符串时我们应当返回 0 。这与C语言的&nbsp;<a href="https://baike.baidu.com/item/strstr/811469" target="_blank">strstr()</a>&nbsp;以及 Java的&nbsp;<a href="https://docs.oracle.com/javase/7/docs/api/java/lang/String.html#indexOf(java.lang.String)" target="_blank">indexOf()</a>&nbsp;定义相符。</p>
<div><div>Related Topics</div><div><li>双指针</li><li>字符串</li></div></div>

## 题目解析

* 本题是一道模拟题

### 不确定性


### 方法一：双指针法

#### 分析

- 使用两个指针分别指向主串和模式串，当模式串的第一个字符与主串中的某个字符相匹配，则依次向后比较
- 若发现模式串中存在字符无法匹配的情况，则退回到前一次开始比较的下一个位置

#### 思路

- 定义i，j分别作为主串和模式串的下标
- 若haystack[i]与needle[j]相等，则下标都向后移
- 若出现不相等的情况，则利用变量len，退回到前一次开始比较的下一个位置

#### 注意

- int和string::size_type之间的比较

#### 知识点

- 字符串的遍历

#### 复杂度

- 时间复杂度 O(mn)，其中m为主串长度，n为模式串长度
- 空间复杂度 O(1)

#### 代码

```cpp
int strStr(string haystack, string needle) {
	if (!needle.size()){
		return 0;
	}
	int i = 0, j = 0;
	for (; i <= static_cast<int>(haystack.size()) - static_cast<int>(needle.size());){
		int len = 0;
		for (j = 0; j < needle.size();){
			if (haystack[i] == needle[j]){
				i++;
				j++;
				len++;
			}
			else{
				i = i - len + 1;
				break;
			}
		}
		if (len == needle.size()){
			return i - len;
		}
	}
	return -1;
}
```


### 方法二：KMP算法

#### 分析

- KMP算法为经典的字符串模式匹配算法

#### 思路

- 首先求出next数组，作为当比较时，主串与模式串中的某一字符不匹配后，模式串指针要跳转的位置
- 当模式串和主串中的字符匹配时，则依次向后比较，直到模式串所有字符比较完成

#### 注意

- next数组的初始化

- int和string::size_type之间的比较

#### 知识点

- next数组的生成

#### 复杂度

- 时间复杂度 O(m+n)，其中m为主串长度，n为模式串长度
- 空间复杂度 O(n)，其中n为模式串长度

#### 代码

```cpp
//https://www.cnblogs.com/dusf/p/kmp.html
//https://zhuanlan.zhihu.com/p/83334559

vector<int> getNext(string needle){
	vector<int> next(needle.size(), 0);
	next[0] = -1;
	int j = 0;
	int k = -1;
	while (j < needle.size() - 1){
		if (k == -1 || needle[j] == needle[k]){
			next[++j] = ++k;
		}
		else{
			k = next[k];
		}
	}
	return next;
}

int strStr(string haystack, string needle) {
	if (!needle.size()){
		return 0;
	}
	int i = 0, j = 0;
	vector<int> next = getNext(needle);
	while (i < static_cast<int>(haystack.size()) && j < static_cast<int>(needle.size())){
		if (j == -1 || haystack[i] == needle[j]){
			i++;
			j++;
		}
		else{
			j = next[j];
		}
	}
	if (j == needle.size()){
		return i - j;
	}
	else{
		return -1;
	}
}
```


## 相关题目

* https://leetcode-cn.com/problems/repeated-substring-pattern/
* https://leetcode-cn.com/problems/shortest-palindrome/

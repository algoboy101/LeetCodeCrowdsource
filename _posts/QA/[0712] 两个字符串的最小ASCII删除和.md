---
title: "[0712] 两个字符串的最小ASCII删除和"
tags:
  - leetcode
  - 题解
  - 动态规划
categories:
  - leetcode
  - 题解
author:
  - 张学志
  - 作者2
comments: true
updated: false
permalink:
mathjax: true
top: false
description: ...
date: 2020-03-07 00:11:52
---


# [0712] 两个字符串的最小ASCII删除和
* [GitHub](https://github.com/algoboy101/LeetCodeCrowdsource/tree/master/_posts/QA/%5B0712%5D%20%E4%B8%A4%E4%B8%AA%E5%AD%97%E7%AC%A6%E4%B8%B2%E7%9A%84%E6%9C%80%E5%B0%8FASCII%E5%88%A0%E9%99%A4%E5%92%8C.md)
* http://leetcode.xuezhisd.top/post/3d0b80dd.html
* https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings
* https://leetcode-cn.com/problems/minimum-ascii-delete-sum-for-two-strings


## 题目描述

<p>给定两个字符串<code>s1, s2</code>，找到使两个字符串相等所需删除字符的ASCII值的最小和。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> s1 = &quot;sea&quot;, s2 = &quot;eat&quot;
<strong>输出:</strong> 231
<strong>解释:</strong> 在 &quot;sea&quot; 中删除 &quot;s&quot; 并将 &quot;s&quot; 的值(115)加入总和。
在 &quot;eat&quot; 中删除 &quot;t&quot; 并将 116 加入总和。
结束时，两个字符串相等，115 + 116 = 231 就是符合条件的最小和。
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre>
<strong>输入:</strong> s1 = &quot;delete&quot;, s2 = &quot;leet&quot;
<strong>输出:</strong> 403
<strong>解释:</strong> 在 &quot;delete&quot; 中删除 &quot;dee&quot; 字符串变成 &quot;let&quot;，
将 100[d]+101[e]+101[e] 加入总和。在 &quot;leet&quot; 中删除 &quot;e&quot; 将 101[e] 加入总和。
结束时，两个字符串都等于 &quot;let&quot;，结果即为 100+101+101+101 = 403 。
如果改为将两个字符串转换为 &quot;lee&quot; 或 &quot;eet&quot;，我们会得到 433 或 417 的结果，比答案更大。
</pre>

<p><strong>注意:</strong></p>

<ul>
	<li><code>0 &lt; s1.length, s2.length &lt;= 1000</code>。</li>
	<li>所有字符串中的字符ASCII值在<code>[97, 122]</code>之间。</li>
</ul>
<div><div>Related Topics</div><div><li>动态规划</li></div></div>


## 题目解析
* [请一句话描述题目...]

### 不确定性


### 方法一：[算法名称]

#### 分析

#### 思路

#### 注意

#### 知识点

#### 复杂度

#### 代码

```cpp
//
```


### 方法二：[算法名称]

#### 分析

#### 思路

#### 注意

#### 知识点

#### 复杂度

#### 代码

```cpp
//
```


## 相关题目
* 

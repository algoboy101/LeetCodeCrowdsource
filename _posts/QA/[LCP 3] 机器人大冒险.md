---
title: "[LCP 3] 机器人大冒险"
tags:
  - leetcode
  - 题解
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
date: 2020-03-07 20:60:60
---


# [LCP 3] 机器人大冒险
* [GitHub](https://github.com/algoboy101/LeetCodeCrowdsource/tree/master/_posts/QA/%5BLCP%203%5D%20%E6%9C%BA%E5%99%A8%E4%BA%BA%E5%A4%A7%E5%86%92%E9%99%A9.md)
* http://leetcode.xuezhisd.top/post/74595290.html
* https://leetcode.com/problems/programmable-robot
* https://leetcode-cn.com/problems/programmable-robot


## 题目描述

<p>力扣团队买了一个可编程机器人，机器人初始位置在原点<code>(0, 0)</code>。小伙伴事先给机器人输入一串指令<code>command</code>，机器人就会<strong>无限循环</strong>这条指令的步骤进行移动。指令有两种：</p>

<ol>
	<li><code>U</code>: 向<code>y</code>轴正方向移动一格</li>
	<li><code>R</code>: 向<code>x</code>轴正方向移动一格。</li>
</ol>

<p>不幸的是，在 xy 平面上还有一些障碍物，他们的坐标用<code>obstacles</code>表示。机器人一旦碰到障碍物就会被<strong>损毁</strong>。</p>

<p>给定终点坐标<code>(x, y)</code>，返回机器人能否<strong>完好</strong>地到达终点。如果能，返回<code>true</code>；否则返回<code>false</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>command = &quot;URR&quot;, obstacles = [], x = 3, y = 2
<strong>输出：</strong>true
<strong>解释：</strong>U(0, 1) -&gt; R(1, 1) -&gt; R(2, 1) -&gt; U(2, 2) -&gt; R(3, 2)。</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>command = &quot;URR&quot;, obstacles = [[2, 2]], x = 3, y = 2
<strong>输出：</strong>false
<strong>解释：</strong>机器人在到达终点前会碰到(2, 2)的障碍物。</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>command = &quot;URR&quot;, obstacles = [[4, 2]], x = 3, y = 2
<strong>输出：</strong>true
<strong>解释：</strong>到达终点后，再碰到障碍物也不影响返回结果。</pre>

<p>&nbsp;</p>

<p><strong>限制：</strong></p>

<ol>
	<li><code>2 &lt;= command的长度 &lt;= 1000</code></li>
	<li><code>command</code>由<code>U，R</code>构成，且至少有一个<code>U</code>，至少有一个<code>R</code></li>
	<li><code>0 &lt;= x &lt;= 1e9, 0 &lt;= y &lt;= 1e9</code></li>
	<li><code>0 &lt;= obstacles的长度 &lt;= 1000</code></li>
	<li><code>obstacles[i]</code>不为原点或者终点</li>
</ol>



## 题目解析
* [请一句话描述题目...]

### 不确定性


### 方法一

#### 分析

#### 思路

#### 注意

#### 知识点

#### 复杂度

#### 参考

#### 答案

```cpp
//
```


### 方法二

#### 分析

#### 思路

#### 注意

#### 知识点

#### 复杂度

#### 参考

#### 答案

```cpp
//
```



---
title: "[1115] 交替打印FooBar"
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
date: 2020-03-07 00:18:35
---


# [1115] 交替打印FooBar
* https://leetcode.com/problems/print-foobar-alternately
* https://leetcode-cn.com/problems/print-foobar-alternately


## 题目描述

<p>我们提供一个类：</p>

<pre>
class FooBar {
  public void foo() {
&nbsp; &nbsp; for (int i = 0; i &lt; n; i++) {
&nbsp; &nbsp; &nbsp; print(&quot;foo&quot;);
&nbsp;   }
  }

  public void bar() {
&nbsp; &nbsp; for (int i = 0; i &lt; n; i++) {
&nbsp; &nbsp; &nbsp; print(&quot;bar&quot;);
&nbsp; &nbsp; }
  }
}
</pre>

<p>两个不同的线程将会共用一个 <code>FooBar</code>&nbsp;实例。其中一个线程将会调用&nbsp;<code>foo()</code>&nbsp;方法，另一个线程将会调用&nbsp;<code>bar()</code>&nbsp;方法。</p>

<p>请设计修改程序，以确保 &quot;foobar&quot; 被输出 n 次。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> n = 1
<strong>输出:</strong> &quot;foobar&quot;
<strong>解释:</strong> 这里有两个线程被异步启动。其中一个调用 foo() 方法, 另一个调用 bar() 方法，&quot;foobar&quot; 将被输出一次。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> n = 2
<strong>输出:</strong> &quot;foobarfoobar&quot;
<strong>解释:</strong> &quot;foobar&quot; 将被输出两次。
</pre>



## 题目代码

```cpp
class FooBar {
private:
    int n;

public:
    FooBar(int n) {
        this->n = n;
    }

    void foo(function<void()> printFoo) {
        
        for (int i = 0; i < n; i++) {
            
        	// printFoo() outputs "foo". Do not change or remove this line.
        	printFoo();
        }
    }

    void bar(function<void()> printBar) {
        
        for (int i = 0; i < n; i++) {
            
        	// printBar() outputs "bar". Do not change or remove this line.
        	printBar();
        }
    }
};
```


## 题目解析


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



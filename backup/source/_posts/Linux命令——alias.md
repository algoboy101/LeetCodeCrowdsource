---
title: Linux命令——alias
tags:
  - Linux
categories:
  - Linux
author: 张学志
abbrlink: '34e1'
date: 2015-11-04 13:47:00
description: ...
---





## alias
* **功能**：设置指令的别名
<!-- more -->
* **提示**：
	* 该命令可将一些较长的命令进行简化；
	* 使用alias时，用户必须使用单引号''将原来的命令引起来，防止特殊字符导致错误；
	* alias命令的作用只局限于该次登入的操作，若要每次登入都能够使用这些命令别名，则可将相应的alias命令存放到bash的初始化文件`/etc/.bashrc`中；
* **选项**： 
	* -p：打印已经设置的命令别名
* **示例**：
```bash
# 显示已定义的命令别名
alias
alias -p
# 显示某命令别名的信息
alias ll
# 定义命令xuezhisd,显示登录用户信息
alias xuezhisd='who am i'
```


## 参考网址
* [Linux命令查询网站](http://www.lx138.com/)
* [Linux命令大全](http://man.linuxde.net/)
* [baidu](http://baidu.com/)
* [Google](http://google.com.hk)

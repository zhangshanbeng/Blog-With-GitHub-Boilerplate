---
layout: post
title: Java课程学习记录
slug: javacourse
date: 2020-04-20 12:00
status: publish
author: Felix
categories: 
  - Java
tags:
  - Java
  
excerpt: Java学习过程的记录
---
###第一节课

1.**Error: A JNI error has occurred, please check your installation and try again**

原因：java -version与javac -version不一致

解决：卸载Java旧版本，[Java官方卸载工具地址](https://www.java.com/zh_CN/download/uninstalltool.jsp)

2.**Error:编码 GBK 的不可映射字符**

原因：java文件的编码格式不是ANSI编码格式

解决：`javac -encoding UTF-8`
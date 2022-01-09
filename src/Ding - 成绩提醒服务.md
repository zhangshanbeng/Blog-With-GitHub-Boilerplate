---
layout: post
title: Ding - 成绩提醒服务
slug: the first gift of 2022
date: 2022-01-9 12:00
status: publish
author: 张山崩
categories: 
  - Python
tags:
  - Crontab
  - Python
excerpt: 一个能帮助你消除成绩焦虑的服务
---

当有新成绩发布时，本服务将会发送一封邮件给你（延迟在10min左右）

本服务地址：http://jwjxnew.zhangshanbeng.cn/ （复制到浏览器中打开）

### 1. 使用说明

进入[Ding - 成绩提醒服务](http://jwjxnew.zhangshanbeng.cn/)后，点击[注册](http://jwjxnew.zhangshanbeng.cn/register/)按钮，进入注册界面，依次输入邮箱、学号、信息门户密码和邀请码，点击注册按钮即可

**注意：请确保你输入的信息是正确的，特别是学号和信息门户密码！**

如果记不清信息门户密码的，请务必去[->统一身份认证<-](https://authserver.casb4.njit.edu.cn:4443/authserver/login?service=http%3A%2F%2Fehall.njit.edu.cn%2Flogin%3Fservice%3Dhttps%3A%2F%2Fehall.casb4.njit.edu.cn%3A4443%2Fnew%2Findex.html)试一下你的密码

<img src=".\images\ding.jpg" alt="pic1" style="zoom:25%;" />

当出现”注册成功“字样时，说明已经注册成功，在接下来的10分钟内，系统将会进行第一次爬虫，你可能会收到一封初始化提醒邮件

**注意：请确保`zhangshanbeng@126.com`在白名单中！**

【可选】在未来的十分钟内，你可以返回首页，进入登录界面，依次输入学号和密码，即可登录详情页，详情页中你可以查看你的课程与成绩

如果详情页中没有出现成绩表格，可能有以下三种原因：

① 注册至登录查看详情页的间隔小于10分钟

② 你可能真的还没出成绩

③ 你的信息门户学号/密码错误

### 2. 项目原理

网页: Flask, MySQL

爬虫: [Licsber](https://github.com/Licsber/licsber-pypi)

定时执行: Crontab

项目实现很简单，没有任何技术含量可言，还是定时执行的老套路

### 3. 更多

本系统邀请码: dclG4dX6P（有效期至2022.1.10 0点）

如果在使用中遇到问题，欢迎加入我的交流群: [618177277](https://jq.qq.com/?_wv=1027&k=Ltbrj4e1) 与我取得联系，加群请备注学号

### 4. 写在最后

其实本项目在去年的7月5日开启了第一轮公测，用户达到了7人，运行1周有余，执行成功率在80%以上

但项目架构过于繁冗，于是在一周前，我对本项目进行了重构，大胆的采用了一些轻量级框架，提高了系统的运行效率，大大降低了部署的成本

项目中对我而言最困难的部分是网页部分，也是做的最烂的部分，今年我一定好好学习orz

最后的最后，在此特别感谢所有参与测试的同学！

Wish you a very happy new year 2022!



> 邀请码: dclG4dX6P
>
> 交流群: [618177277](https://jq.qq.com/?_wv=1027&k=Ltbrj4e1) 








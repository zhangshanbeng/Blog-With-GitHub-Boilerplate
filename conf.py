# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Galileo",
    "type": "local",
    "path": "../Galileo"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "zhangshanbeng/site-Blog@gh-pages"
}

# 站点设置
site_name = "Felix's site"
site_logo = "${static_prefix}logo.png"
site_build_date = "2020-01-11T11:11+08:00"
author = "张山崩"
email = "zhangshanbeng@gmail.com"
author_homepage = "https://www.zhangshanbeng.com/"
description = "光与影的交织 黑与白的渗透"
key_words = ['张山崩', 'zhangshanbeng', 'blog']
language = 'zh-CN'
external_links = [
    {
        "name": "Maverick",
        "url": "https://github.com/AlanDecode/Maverick",
        "brief": "🏄‍ Go My Own Way."
    },
    {
        "name": "三無計劃",
        "url": "https://www.imalan.cn",
        "brief": "熊猫小A的主页。"
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "GitHub",
        "url": "https://github.com/zhangshanbeng",
        "icon": "gi gi-github"
    },
    {
        "name": "Weibo",
        "url": "https://weibo.com/234277266/",
        "icon": "gi gi-weibo"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''

valine = {
    "enable": False,
    "el": '#vcomments',
    "appId": "tRknQHrs7qCKeKa4Yf58WWgD-gzGzoHsz",
    "appKey": "lGLjQ3Nm41o9Hfl45c5b6SOi",
}
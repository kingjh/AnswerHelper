#!/usr/bin/python
# -*- coding: utf-8 -*-
import webbrowser


# 直接用浏览器搜索问题
def open_wabpage(question):
    webbrowser.open('http://www.sogou.com/web?ie=utf8&interV=&query=' + question)

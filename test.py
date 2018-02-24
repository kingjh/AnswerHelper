#!/usr/bin/python
# -*- coding: utf-8 -*-

import img_utils
import json
import solve_utils
import config
import problem_utils
import re

question = "什么成语除自身外没有多余东西,形容贫"
p = re.compile("[不是|没有]")
# 排除引号内的否定词
p1 = re.compile("“.*[不是|没有].*”")
# 排除解释内的否定词
p2 = re.compile("[指|意思是].*[不是|没有]")
if (p.search(question) is not None) \
        & (p1.search(question) is None) \
        & (p2.search(question) is None):
    print(111)

question = "“日日思君不是君”的下一句是什么"
if (p.search(question) is not None) \
        & (p1.search(question) is None) \
        & (p2.search(question) is None):
    print(222)

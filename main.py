#!/usr/bin/python
# -*- coding: utf-8 -*-

import solve_utils
import problem_utils

result = problem_utils.get_result()
question = result[0]
answer = result[1]

# 直接用搜狗搜索问题
solve_utils.open_wabpage(question)

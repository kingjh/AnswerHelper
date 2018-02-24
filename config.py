#!/usr/bin/python
# -*- coding: utf-8 -*-

# 百度ocr app_id
APP_ID = ''
# 百度ocr api_key
API_KEY = ''
# 百度ocr secret_key
SECRET_KEY = ''

# 图片默认路径
# 若用img.jpg，MIUI会加一串数字变成如img_1519305705021.jpg，故用img_temp.jpg
IMAGE_PAGE = "img_temp.jpg"
# 上线请注释
# IMAGE_PAGE = "res/img/tiaozhandatiwang/1.jpg"
QUESTION_TEMP = "question.jpg"
ANSWER_TEMP = "answer.jpg"

# 获取题目方式
TYPE_IMG = 0

# API方式已经废弃，全部用图片方式获取
GET_TYPE = TYPE_IMG

# 区域的高度、间隔
# 适用于：知乎答题王、丰云榜、挑战答题王
WIDTH = 1080
QUESTION_AREA_START = 600
QUESTION_AREA_HEIGHT = 850

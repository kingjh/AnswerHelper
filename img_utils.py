#!/usr/bin/python
# -*- coding: utf-8 -*-

from aip import AipOcr
from PIL import ImageGrab
import config
import json
from PIL import Image
import matplotlib.pyplot as plt
import datetime
import os

client = AipOcr(config.APP_ID, config.API_KEY, config.SECRET_KEY)


# 通过adb获取android图像
def get_android_img():
    os.system('adb shell screencap -p /sdcard/' + config.IMAGE_PAGE)
    os.system('adb pull /sdcard/' + config.IMAGE_PAGE + ' .')


# 获取ios图像
# 暂时只实现android的
# def get_ios_img():
#     img = ImageGrab.grab()
#     # TODO 截取区域可以调整
#     box = (0, 300, 850, 1000)
#     img = img.crop(box)
#     img.save(config.IMAGE_PAGE_TEMP)


# 裁剪图像
def crop():
    img = Image.open(config.IMAGE_PAGE)
    plt.figure("beauty")
    plt.subplot(1, 2, 1), plt.title('origin')
    plt.imshow(img), plt.axis('off')
    # TODO 截取区域可以调整
    # 截取问题
    box = (0, config.QUESTION_AREA_START, config.WIDTH, config.QUESTION_AREA_HEIGHT)
    roi = img.crop(box)
    roi.save(config.QUESTION_TEMP)
    # 截取答案 (结束的y坐标 = 开始的y坐标 + ANSWER_AREA_HEIGHT)
    # box = (0, config.QUESTION_AREA_HEIGHT, 1080, config.QUESTION_AREA_HEIGHT + config.ANSWER_AREA_HEIGHT)
    # roi = img.crop(box)
    # roi.save(config.ANSWER_TEMP)


# 百度ocr获取图片位置
def get_file_content(file_path):
    with open(file_path, 'rb') as fp:
        return fp.read()


# 识别文字
def spot():
    # get_ios_img()
    get_android_img()
    crop()
    image = get_file_content(config.QUESTION_TEMP)
    question = client.basicGeneral(image)
    # 放弃识别答案，直接用问题在搜狗搜索
    # image = get_file_content(config.ANSWER_TEMP)
    # answer = client.basicGeneral(image)
    answer = ''
    result = {"question": question, "answer": answer}
    return result

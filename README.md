# 微信答题小程序辅助工具（适用于知乎答题王、丰云榜、挑战答题王等微信答题小程序、app）
## 思路
1.手机进入答题app

2.Android可以通过adb截屏并拉取图片
```shell
adb shell screencap -p /sdcard/autojump.png
adb pull /sdcard/autojump.png .
```
暂不支持iPhone

3.通过ocr将题目内容识别出来

4.打开浏览器用搜狗搜索题目

## 所需软件
* * Anaconda + ADB，在Windows运行

## 使用方法
暂不支持iPhone

1.请先安装Anaconda，把其中的python3可执行文件设为系统默认的python可执行文件；安装ADB

2.安装百度ocr库
```shell
pip install baidu-aip
```

3.在[百度云](https://cloud.baidu.com/product/ocr.html)中创建一个项目，获取相应的app id、api key以及secret_key，在config.py中进行替换

4.在img_utils中调整截图区域（WIDTH、QUESTION_AREA_START、QUESTION_AREA_HEIGHT）

5.手机进入开发者模式，用数据线连接到Windows，进入答题微信小程序或app

6.在Windows命令行执行
```shell
python main.py
```

7.浏览器会自动打开并用搜狗搜索题目，请自行判断正确答案

请注意连接手机后，第一次运行本程序时，打开网页会比较慢，故在答题前请先运行一次本程序

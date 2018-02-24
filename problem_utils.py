#!/usr/bin/python
# -*- coding: utf-8 -*-

import img_utils


def get_by_scan():
    # 识别文字
    result = img_utils.spot()
    question_words = result['question']['words_result']
    question = ''
    for i in range(0, len(question_words)):
        question += question_words[i]['words']
    # 放弃识别答案，直接用问题在搜狗搜索
    # answers = result['answer']['words_result']
    # answers = []
    answer = []
    # for i in range(0, len(answers)):
    #     answer.append(answers[i]['words'])

    question = question.replace("?", "")
    result = [question, answer]
    return result


def get_result():
    return get_by_scan()

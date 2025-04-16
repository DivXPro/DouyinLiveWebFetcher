#!/usr/bin/python
# coding:utf-8

# @FileName:    config.py
# @Time:        2024/1/2 22:27
# @Author:      bubu
# @Project:     douyinLiveWebFetcher

import os
from dotenv import load_dotenv

# 加载.env文件中的环境变量
load_dotenv()

# API配置
API_URL = os.getenv('API_URL', 'http://localhost:3000/douyin')

# 抖音配置
DOUYIN_COOKIE = os.getenv('DOUYIN_COOKIE', '')
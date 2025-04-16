#!/usr/bin/python
# coding:utf-8

# @FileName:    main.py
# @Time:        2024/1/2 22:27
# @Author:      bubu
# @Project:     douyinLiveWebFetcher

from liveMan import DouyinLiveWebFetcher
from config import API_URL

if __name__ == '__main__':
    live_id = '5168902178'
    room = DouyinLiveWebFetcher(live_id, API_URL)
    room.get_room_status()
    room.start()

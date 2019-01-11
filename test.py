#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random

import requests
from bs4 import BeautifulSoup
import time


class DownLoad(object):
    def __init__(self):
        self.base_url = 'http://140.143.163.99:805'
        self.chapter_url = (self.base_url+'/chapter/581825122ed01394526750b0'
                                          '?book_id=5816b415b06d1d32157790b1&page=0')
        self.names = []
        self.urls = []
        self.num = 0

    # 获取章节
    def get_chapter(self):
        chapters = requests.get(url=self.chapter_url)
        bs = BeautifulSoup(chapters.text, features='html.parser')
        divs = bs.select('body > div > p > a')
        for url in divs:
            self.urls.append(url.attrs['href'])
            self.names.append(url.text)
        return self.urls

    # 获取单章详情
    def get_detail(self, url):
        real_url = self.base_url+url
        res = requests.get(real_url)
        bs = BeautifulSoup(res.text, features='html.parser')
        div = bs.select('body > div')
        text = div[0].text
        # 写入文件
        with open('novel.txt', 'a', encoding='utf-8') as f:
            f.write(text)


if __name__ == '__main__':
    down_load = DownLoad()
    all_chapters = down_load.get_chapter()
    for index, short_url in enumerate(all_chapters):
        print('downloading %s' % down_load.names[index])
        # 随机睡1-4秒
        sleep_int = random.randint(1, 4)
        print('随机睡 %d 秒' % sleep_int)
        time.sleep(sleep_int)
        down_load.get_detail(short_url)
        if index == 10:
            break
    print('finished download,please open the novel.txt to see what happened')

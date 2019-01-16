#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import asyncio
import aiohttp
import logging
import base64
from contextlib import closing
import os

logging.basicConfig(level=logging.INFO)

target_url = 'http://jandan.net/ooxx/page-41'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
    'Host': 'jandan.net',
    'Referer': 'http://jandan.net/top'
}
req = requests.get(url=target_url, headers=headers)
if req.status_code == 200:
    html = req.text
    # print(html)
    # 'ol > li > div > div > div.text > p > span.img-hash'
    bs = BeautifulSoup(html, features='html.parser')
    span_ls = bs.select('div.text > p > span.img-hash')
    print(span_ls)
    logging.info(type(span_ls[0]))
    hash_ls = ['http:' + str(base64.b64decode(hash_img.string), encoding='utf-8') for hash_img in span_ls]
    print(hash_ls)
    logging.info(type(hash_ls[0]))
    logging.info(len(hash_ls[0]))
    # download images
    logging.info('starting to download the img')
    for img_url in hash_ls:
        # if exits
        if not os.path.exists(r'F:\spiderDownload\jianDan\%s' % img_url[-10:]):
            logging.info('download new img ……')
            with closing(requests.get(url=img_url, stream=True)) as res:
                with open(r'F:\spiderDownload\jianDan\%s' % img_url[-10:], 'wb') as f:
                    for chunk in res.iter_content(1024):
                        if chunk:
                            f.write(chunk)
        else:
            logging.info('already have it,do not download anymore')
    logging.info('download all the img')

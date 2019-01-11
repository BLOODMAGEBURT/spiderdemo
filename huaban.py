#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import json
from contextlib import closing


chapters = requests.get(url='https://unsplash.com/napi/collections/'
                            '1065976/photos?page=1&per_page=20&order_by=latest', verify=False)

# print(chapters.text)
json_res = json.loads(chapters.text)
print('开始下载了……')
for url in json_res:
    src_id = url['id']
    download_url = url['links']['download']+'?force=true'
    with closing(requests.get(url=download_url, verify=False, stream=True)) as res:
        with open('%s.jpg' % src_id, 'wb') as fd:
            print('下载新的……')
            for chunk in res.iter_content(chunk_size=1024):
                if chunk:
                    fd.write(chunk)
print('下载完了……')

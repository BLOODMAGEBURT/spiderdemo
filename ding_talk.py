import requests

headers = {
    'Host': 'aflow.dingtalk.com',
    'Origin': 'https://aflow.dingtalk.com',
    'x-client-corpId': 'dinge50c12a650b5717435c2f4657eb6378f',
    'User-Agent': '(Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36 '
                  'dingtalk-win/1.0.0 nw(0.14.7) DingTalk(4.6.8-Release.282) Mojo/1.0.0 Native AppType(release))',
    'Referer': '(https://aflow.dingtalk.com/dingtalk/pc/query/'
               'pchomepage.htm?corpid=dinge50c12a650b5717435c2f4657eb6378f)',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    '_csrf_token_': '1548067840250',
    'X-Requested-With': 'XMLHttpRequest',
    'client-corpid': 'dinge50c12a650b5717435c2f4657eb6378f'
}

cookies = {
    '_csrf_token_': '1548073898825',
    'up_ab': 'y',
    'preview_ab': 'y',
    'dt_s': 'u-4cd8944-6870064c99-bb850bc-336f6b-7cac6ac2-88c9a801-99c2-4e4d-ac97-7268ad67d808',
    'dingtalk_token': 'B4EDA79A03BB547AB00F2B3D97EB95D3',
    'dd_sid': 'k0_71c10b0b25b4455c996f_0b0b71c15c45b42577691e3331d178605581cc6c6286',
    'cna': 'ezGZFLswlwYCAd6AdXyEqUVh',
    'weiflow_token': 'P1B76D3B240CA1236F0416F9F9FE691AB3B841EFF841694E2B74E0CF40F1'
                     '115CC9E93F712BEEBE1DC918C4DBD88BCAB62197C8DA087'
                     '30A8D8CB2FF0F3940464DEEBB8ED1501F6E8CD367483A723C1D355D946A19'
                     '1DBBAA818E83538DED1479383CB2820C022801FBDA29F15210B64F763028F'
                     '797ABF854DF57C0464B7668CED8FD2B2FFA838514429D6FDA6E9070608563'
                     'FBD1FB5981736E19D5FD0CDB364A504AA243C35154FEAB9F283768F5E2C094C',
    'dingtalk_corpid': 'dinge50c12a650b5717435c2f4657eb6378f'
}

url = 'https://aflow.dingtalk.com/dingtalk/pc/query/task/getTodoTasksForSenior.json'
data = {
    'page': 1,
    'limit': 20,
    'corpid': 'dinge50c12a650b5717435c2f4657eb6378f',
    '__asp': 'dingtalk'
}
res = requests.post(url=url, headers=headers, cookies=cookies, data=data, verify=False)
print(res.json())
json = res.json()
print(type(json))
print(json['data']['taskVoPageList']['values'])

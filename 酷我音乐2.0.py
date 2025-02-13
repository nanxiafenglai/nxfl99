'''
Description: 酷我音乐签到脚本
Author: 南下风来
Date: 2025-02-10 18:00:22
LastEditTime: 2025-02-14 00:30:35
LastEditors: 南下风来
'''
'''
酷我音乐签到脚本
抓包url:https://integralapi.kuwo.cn/api/v1/online/sign/v1/earningSignIn/newDoListen
的loginUid, loginSid, appUid的值
变量：kwyy = appUid#devId#q#phone
'''

import os
import requests
import datetime
import random
import time
import re
import logging
import concurrent.futures

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 常量
LOGIN_URL = "http://ar.i.kuwo.cn/US_NEW/kuwo/login_kw"
BASE_URL = "https://integralapi.kuwo.cn/api/v1/online/sign/v1/earningSignIn/newDoListen"
WITHDRAW_URL = "https://integralapi.kuwo.cn/api/v1/online/sign/v1/getWithdraw"

HEADERS = {
    "Accept": "*/*",
    "Host": "ar.i.kuwo.cn",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
}

def make_request(url, params=None, headers=None):
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"请求失败: {e}")
        return None

def login(q):
    params = {
        'f': 'ar',
        'q': q
    }
    
    response = requests.get(LOGIN_URL, headers=HEADERS, params=params)
    try:
        username = re.search(r'uname3=([^;]+)', response.headers['Set-Cookie']).group(1)
        loginSid = re.search(r'websid=([^;]+)', response.headers['Set-Cookie']).group(1)
        loginUid = re.search(r'userid=([^;]+)', response.headers['Set-Cookie']).group(1)
        return username, loginSid, loginUid
    except Exception as e:
        logging.error(f"登录解析失败: {e}")
        return None, None, None


def signvideo(loginUid, loginSid, appUid):
    params = {
        'loginUid': loginUid,
        'loginSid': loginSid,
        'appUid': appUid,
        'terminal': 'ar',
        'from': 'sign',
        'adverId': '20130802-14795506463',
        'token': '',
        'extraGoldNum': '100',
        'clickExtraGoldNum': '0',
        'surpriseType': '',
        'verificationId': 'BiXdGRsLjE%252B80I0ekQ6PIxbE2c%252FKyDCJSZQ7KxXsKHE1vO6SDz%252FKJIoDdVbBBzzmi76q7NTHX6vcx1PrX38%252F7xA%253D%253D',
        'mobile': ''
    }
    
    response = make_request(BASE_URL, params=params, headers=HEADERS)
    if response and '成功' in response.text:
        logging.info(f"签到广告获得 {response['data']['obtain']} 金币")
    else:
        logging.info(f"签到广告: {response['data'].get('description', '未知错误')}")

def randomtime():
    random_number = random.randint(5, 15)
    time.sleep(random_number)
    return

def signvideo(loginUid, loginSid, appUid):  # 签到广告奖励
    url = 'https://integralapi.kuwo.cn/api/v1/online/sign/v1/earningSignIn/newDoListen'
    params = {
        'loginUid': loginUid,
        'loginSid': loginSid,
        'appUid': appUid,
        'terminal': 'ar',
        'from': 'sign',
        'adverId': '20130802-14795506463',
        'token': '',
        'extraGoldNum': '100',
        'clickExtraGoldNum': '0',
        'surpriseType': '',
        'verificationId': 'BiXdGRsLjE%252B80I0ekQ6PIxbE2c%252FKyDCJSZQ7KxXsKHE1vO6SDz%252FKJIoDdVbBBzzmi76q7NTHX6vcx1PrX38%252F7xA%253D%253D',
        'mobile': ''
    }

    headers = {
        'Host': 'integralapi.kuwo.cn',
        'Connection': 'keep-alive',
        'sec-ch-ua': '"Not A(Brand";v="99", "Android WebView";v="121", "Chromium";v="121"',
        'Accept': 'application/json, text/plain, */*',
        'sec-ch-ua-mobile': '?1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 14; POCO F2 Pro Build/UQ1A.240105.004; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/121.0.6167.101 Mobile Safari/537.36/ kuwopage',
        'sec-ch-ua-platform': '"Android"',
        'Origin': 'https://h5app.kuwo.cn',
        'X-Requested-With': 'cn.kuwo.player',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        #'Referer': 'https://h5app.kuwo.cn/apps/earning-sign/index.html?FULLHASARROW=1&showtab=0&kwflag=2642624794_1710263536072',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }

    response = requests.get(url, params=params, headers=headers)
    r_json = response.json()
    if '成功' in response.text:
        adtype = r_json['data']['obtain']
        print(f'签到广告——>{adtype}金币')
    else:
        description = r_json['data']['description']
        print(f'签到广告——>{description}')


def Homepage(loginUid, loginSid, appUid):  # 主页的广告

    url = "https://integralapi.kuwo.cn/api/v1/online/sign/v1/earningSignIn/newDoListen"
    params = {
        'loginUid': loginUid,
        'loginSid': loginSid,
        'appUid': appUid,
        'terminal': 'ar',
        'from': 'surprise',
        'goldNum': '70',
        'adverId': '20130702-14823094126',
        'token': '',
        'clickExtraGoldNum': '0',
        'surpriseType': '',
        'verificationId': '',
        'mobile': ''
    }

    headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '"Not A(Brand";v="99", "Android WebView";v="121", "Chromium";v="121"',
        'Accept': 'application/json, text/plain, */*',
        'sec-ch-ua-mobile': '?1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 14; POCO F2 Pro Build/UQ1A.240105.004; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/121.0.6167.101 Mobile Safari/537.36/ kuwopage',
        'sec-ch-ua-platform': '"Android"',
        'Origin': 'https://h5app.kuwo.cn',
        'X-Requested-With': 'cn.kuwo.player',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        #'Referer': 'https://h5app.kuwo.cn/apps/earning-sign/index.html?FULLHASARROW=1&showtab=0&kwflag=2642624794_1710349908737',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }

    response = requests.get(url, params=params, headers=headers)
    r_json = response.json()
    if '成功' in response.text:
        adtype = r_json['data']['obtain']
        print(f'主页广告——>{adtype}金币')
    else:
        description = r_json['data']['description']
        print(f'主页广告——>{description}')


def openbox(loginUid, loginSid, devId, appUid):
    current_hour = datetime.datetime.now().time().hour

    time_ranges = {
        0: "00-08",
        8: "08-10",
        10: "10-12",
        12: "12-14",
        14: "14-16",
        16: "16-18",
        18: "18-20",
        20: "20-24"
    }

    for start_hour, time_range in time_ranges.items():
        if start_hour <= current_hour < start_hour + 2:
            print(f"当前时间处于 {time_range} 时间段")
            break
    url = "https://integralapi.kuwo.cn/api/v1/online/sign/new/newBoxFinish"
    params = {
        'loginUid': loginUid,
        'loginSid': loginSid,
        'devId': devId,
        'appUid': appUid,
        'source': 'kwplayer_ar_10.7.6.2_qq.apk',
        'version': 'kwplayer_ar_10.7.6.2',
        'r': '0.6345674327264215',
        'action': 'new',
        'time': f'{time_range}',
        'goldNum': '23',
        'extraGoldnum': '0',
        'clickExtraGoldNum': '0'
    }

    headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '"Not A(Brand";v="99", "Android WebView";v="121", "Chromium";v="121"',
        'Accept': 'application/json, text/plain, */*',
        'sec-ch-ua-mobile': '?1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 14; POCO F2 Pro Build/UQ1A.240105.004; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/121.0.6167.101 Mobile Safari/537.36/ kuwopage',
        'sec-ch-ua-platform': '"Android"',
        'Origin': 'https://h5app.kuwo.cn',
        'X-Requested-With': 'cn.kuwo.player',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        #'Referer': 'https://h5app.kuwo.cn/apps/earning-sign/index.html?FULLHASARROW=1&showtab=0&kwflag=2642624794_1710342600688',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }

    response = requests.get(url, params=params, headers=headers)
    r_json = response.json()
    if '成功' in response.text:
        adtype = r_json['data']['obtain']
        print(f'时间段开宝箱——>{adtype}金币')
    else:
        description = r_json['data']['description']
        print(f'时间段开宝箱——>{description}')
    # 开宝箱的弹窗视频

    url = "https://integralapi.kuwo.cn/api/v1/online/sign/v1/earningSignIn/newDoListen"
    params = {
        "loginUid": loginUid,
        "loginSid": loginSid,
        "appUid": appUid,
        "terminal": "ar",
        "from": "sign",
        "adverId": "20130802-13379713291",
        "token": "",
        "extraGoldNum": "88",
        "clickExtraGoldNum": "0",
        "surpriseType": "",
        "verificationId": "",
        "mobile": ""
    }

    headers = {
        "Connection": "keep-alive",
        "sec-ch-ua": '"Not A(Brand";v="99", "Android WebView";v="121", "Chromium";v="121"',
        "Accept": "application/json, text/plain, */*",
        "sec-ch-ua-mobile": "?1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 14; POCO F2 Pro Build/UQ1A.240105.004; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/121.0.6167.101 Mobile Safari/537.36/ kuwopage",
        "sec-ch-ua-platform": '"Android"',
        "Origin": "https://h5app.kuwo.cn",
        "X-Requested-With": "cn.kuwo.player",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        #"Referer": "https://h5app.kuwo.cn/apps/earning-sign/index.html?FULLHASARROW=1&showtab=0&kwflag=2642624794_1710342600688",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    response = requests.get(url, params=params, headers=headers)
    r_json = response.json()
    if '成功' in response.text:
        adtype = r_json['data']['obtain']
        print(f'开宝箱弹窗——>{adtype}金币')
    else:
        description = r_json['data']['description']
        print(f'开宝箱弹窗——>{description}')


def sign(loginUid, loginSid, appUid):  # 签到
    # 签到没抓到
    # 签到弹窗

    url = "https://integralapi.kuwo.cn/api/v1/online/sign/v1/earningSignIn/newDoListen"
    params = {
        'loginUid': loginUid,
        'loginSid': loginSid,
        'appUid': appUid,
        'terminal': 'ar',
        'from': 'sign',
        'adverId': '20130802-13379713291',
        'token': '',
        'extraGoldNum': '88',
        'clickExtraGoldNum': '0',
        'surpriseType': '',
        'verificationId': '',
        'mobile': ''
    }

    headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '"Not A(Brand";v="99", "Android WebView";v="121", "Chromium";v="121"',
        'Accept': 'application/json, text/plain, */*',
        'sec-ch-ua-mobile': '?1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 14; POCO F2 Pro Build/UQ1A.240105.004; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/121.0.6167.101 Mobile Safari/537.36/ kuwopage',
        'sec-ch-ua-platform': '"Android"',
        'Origin': 'https://h5app.kuwo.cn',
        'X-Requested-With': 'cn.kuwo.player',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        #'Referer': 'https://h5app.kuwo.cn/apps/earning-sign/index.html?FULLHASARROW=1&showtab=0&kwflag=2642624794_1710342600688',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }

    response = requests.get(url, params=params, headers=headers)




def draw(loginUid, loginSid, appUid):  # 抽奖
    # 首次免费抽
    url = "https://integralapi.kuwo.cn/api/v1/online/sign/loterry/getLucky"
    params = {
        "loginUid": loginUid,
        "loginSid": loginSid,
        "appUid": appUid,
        'source': 'kwplayer_ar_10.7.6.2_qq.apk',
        'type': 'free'
    }

    headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '"Not A(Brand";v="99", "Android WebView";v="121", "Chromium";v="121"',
        'Accept': 'application/json, text/plain, */*',
        'sec-ch-ua-mobile': '?1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 14; POCO F2 Pro Build/UQ1A.240105.004; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/121.0.6167.101 Mobile Safari/537.36/ kuwopage',
        'sec-ch-ua-platform': '"Android"',
        'Origin': 'https://h5app.kuwo.cn',
        'X-Requested-With': 'cn.kuwo.player',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://h5app.kuwo.cn/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }

    response = requests.get(url, params=params, headers=headers)
    r_json = response.json()
    if '金币' in response.text:
        adtype = r_json['data']['loterryname']
        print(f'广告抽奖——>{adtype}')
    else:
        description = r_json['msg']
        print(f'免广告抽奖——>{description}')
    #  看视频抽
    randomtime()
    url = "https://integralapi.kuwo.cn/api/v1/online/sign/loterry/getLucky"
    params = {
        "loginUid": loginUid,
        "loginSid": loginSid,
        "appUid": appUid,
        'source': 'kwplayer_ar_10.7.6.2_qq.apk',
        'type': 'video'
    }

    headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '"Not A(Brand";v="99", "Android WebView";v="121", "Chromium";v="121"',
        'Accept': 'application/json, text/plain, */*',
        'sec-ch-ua-mobile': '?1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 14; POCO F2 Pro Build/UQ1A.240105.004; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/121.0.6167.101 Mobile Safari/537.36/ kuwopage',
        'sec-ch-ua-platform': '"Android"',
        'Origin': 'https://h5app.kuwo.cn',
        'X-Requested-With': 'cn.kuwo.player',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://h5app.kuwo.cn/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }

    response = requests.get(url, params=params, headers=headers)
    r_json = response.json()
    if '金币' in response.text:
        adtype = r_json['data']['loterryname']
        print(f'广告抽奖——>{adtype}')
    else:
        description = r_json['msg']
        print(f'广告抽奖——>{description}')


def video(loginUid, loginSid, appUid):  # 看视频

    url = "https://integralapi.kuwo.cn/api/v1/online/sign/v1/earningSignIn/newDoListen"
    params = {
        'loginUid': loginUid,
        'loginSid': loginSid,
        'appUid': appUid,
        'terminal': 'ar',
        'from': 'videoadver',
        'goldNum': '58',
        'adverId': '',
        'token': '',
        'extraGoldNum': '0',
        'clickExtraGoldNum': '0',
        'surpriseType': '',
        'verificationId': '',
        'mobile': ''
    }

    headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '"Not A(Brand";v="99", "Android WebView";v="121", "Chromium";v="121"',
        'Accept': 'application/json, text/plain, */*',
        'sec-ch-ua-mobile': '?1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 14; POCO F2 Pro Build/UQ1A.240105.004; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/121.0.6167.101 Mobile Safari/537.36/ kuwopage',
        'sec-ch-ua-platform': '"Android"',
        'Origin': 'https://h5app.kuwo.cn',
        'X-Requested-With': 'cn.kuwo.player',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        #'Referer': 'https://h5app.kuwo.cn/apps/earning-sign/index.html?FULLHASARROW=1&showtab=0&kwflag=2642624794_1710342600688',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }

    response = requests.get(url, params=params, headers=headers)
    r_json = response.json()
    if '成功' in response.text:
        adtype = r_json['data']['obtain']
        print(f'创意视频——>{adtype}金币')
    else:
        description = r_json['data']['description']
        print(f'创意视频——>{description}')
    randomtime()
    # 看广告后的弹窗

    url = "https://integralapi.kuwo.cn/api/v1/online/sign/v1/earningSignIn/newDoListen"
    params = {
        'loginUid': loginUid,
        'loginSid': loginSid,
        'appUid': appUid,
        'terminal': 'ar',
        'from': 'videoadver',
        'adverId': '20130802-14824211622',
        'token': '',
        'extraGoldNum': '110',
        'clickExtraGoldNum': '0',
        'surpriseType': '',
        'verificationId': '',
        'mobile': '',
        'listenTime': '0'
    }
    headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '"Not A(Brand";v="99", "Android WebView";v="121", "Chromium";v="121"',
        'Accept': 'application/json, text/plain, */*',
        'sec-ch-ua-mobile': '?1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 14; POCO F2 Pro Build/UQ1A.240105.004; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/121.0.6167.101 Mobile Safari/537.36/ kuwopage',
        'sec-ch-ua-platform': '"Android"',
        'Origin': 'https://h5app.kuwo.cn',
        'X-Requested-With': 'cn.kuwo.player',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        #'Referer': 'https://h5app.kuwo.cn/apps/earning-sign/index.html?FULLHASARROW=1&showtab=0&kwflag=2642624794_1710342600688',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }

    response = requests.get(url, params=params, headers=headers)
    r_json = response.json()
    if '成功' in response.text:
        adtype = r_json['data']['obtain']
        print(f'创意视频弹窗——>{adtype}金币')
    else:
        description = r_json['data']['description']
        print(f'创意视频弹窗——>{description}')


def collect(loginUid, loginSid, appUid):  # 收藏歌曲

    url = "https://integralapi.kuwo.cn/api/v1/online/sign/v1/earningSignIn/newDoListen"
    params = {
        'loginUid': loginUid,
        'loginSid': loginSid,
        'appUid': appUid,
        'terminal': 'ar',
        'from': 'collect',
        'goldNum': '18',
        'adverId': '',
        'token': '',
        'clickExtraGoldNum': '0',
        'surpriseType': '',
        'verificationId': '',
        'mobile': ''
    }

    headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '"Not A(Brand";v="99", "Android WebView";v="121", "Chromium";v="121"',
        'Accept': 'application/json, text/plain, */*',
        'sec-ch-ua-mobile': '?1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 14; POCO F2 Pro Build/UQ1A.240105.004; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/121.0.6167.101 Mobile Safari/537.36/ kuwopage',
        'sec-ch-ua-platform': '"Android"',
        'Origin': 'https://h5app.kuwo.cn',
        'X-Requested-With': 'cn.kuwo.player',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        #'Referer': 'https://h5app.kuwo.cn/apps/earning-sign/index.html?FULLHASARROW=1&showtab=0&kwflag=2642624794_1710342600688',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }

    response = requests.get(url, params=params, headers=headers)
    r_json = response.json()
    if '成功' in response.text:
        adtype = r_json['data']['obtain']
        print(f'收藏歌曲——>{adtype}金币')
    else:
        description = r_json['data']['description']
        print(f'收藏歌曲——>{description}')

    # 收藏弹窗

    url = "https://integralapi.kuwo.cn/api/v1/online/sign/v1/earningSignIn/newDoListen"
    params = {
        'loginUid': loginUid,
        'loginSid': loginSid,
        'appUid': appUid,
        'terminal': 'ar',
        'from': 'collect',
        'goldNum': '0',
        'adverId': '',
        'token': '',
        'extraGoldNum': '60',
        'clickExtraGoldNum': '0',
        'surpriseType': '',
        'verificationId': '',
        'mobile': '',
        'listenTime': '0'
    }
    randomtime()
    headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '"Not A(Brand";v="99", "Android WebView";v="121", "Chromium";v="121"',
        'Accept': 'application/json, text/plain, */*',
        'sec-ch-ua-mobile': '?1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 14; POCO F2 Pro Build/UQ1A.240105.004; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/121.0.6167.101 Mobile Safari/537.36/ kuwopage',
        'sec-ch-ua-platform': '"Android"',
        'Origin': 'https://h5app.kuwo.cn',
        'X-Requested-With': 'cn.kuwo.player',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        #'Referer': 'https://h5app.kuwo.cn/apps/earning-sign/index.html?FULLHASARROW=1&showtab=0&kwflag=2642624794_1710342600688',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }

    response = requests.get(url, params=params, headers=headers)
    r_json = response.json()
    if '成功' in response.text:
        adtype = r_json['data']['obtain']
        print(f'收藏歌曲弹窗——>{adtype}金币')
    else:
        description = r_json['data']['description']
        print(f'收藏歌曲弹窗——>{description}')

def listentomusic(loginUid, loginSid, appUid):
    times = ['5', '10', '20', '30']
    goldNums = ['43', '57', '60', '99']
    extraGoldNum = ['68', '68', '68', '68']
    url2 = "https://integralapi.kuwo.cn/api/v1/online/sign/v1/earningSignIn/newDoListen"
    url = "https://integralapi.kuwo.cn/api/v1/online/sign/v1/earningSignIn/newDoListen"
    headers = {
        "Host": "integralapi.kuwo.cn",
        "Connection": "keep-alive",
        "sec-ch-ua": '"Not A(Brand";v="99", "Android WebView";v="121", "Chromium";v="121"',
        "Accept": "application/json, text/plain, */*",
        "sec-ch-ua-mobile": "?1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 14; POCO F2 Pro Build/UQ1A.240105.004; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/121.0.6167.101 Mobile Safari/537.36/ kuwopage",
        "sec-ch-ua-platform": '"Android"',
        "Origin": "https://h5app.kuwo.cn",
        "X-Requested-With": "cn.kuwo.player",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        #"Referer": "https://h5app.kuwo.cn/apps/earning-sign/index.html?FULLHASARROW=1&showtab=0&kwflag=2642626091_1711184117441",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    goldNum = 0
    for time in times:
        goldNumcoin = goldNums[goldNum]
        extraGoldNumcoin = extraGoldNum[goldNum]
        params = {
            'loginUid': loginUid,
            'loginSid': loginSid,
            'appUid': appUid,
            "terminal": "ar",
            "from": "listen",
            "goldNum": goldNumcoin,
            "adverId": "",
            "token": "",
            "clickExtraGoldNum": "0",
            "surpriseType": "",
            "verificationId": "",
            "mobile": "",
            "listenTime": time
        }
        params2 = {
            'loginUid': loginUid,
            'loginSid': loginSid,
            'appUid': appUid,
            "terminal": "ar",
            "from": "listen",
            "adverId": "20130802-15030283408",
            "token": "",
            "extraGoldNum": extraGoldNumcoin,
            "clickExtraGoldNum": "0",
            "surpriseType": "",
            "verificationId": "",
            "mobile": "",
            "listenTime": time
        }
        goldNum = goldNum + 1
        response = requests.get(url, params=params, headers=headers)
        r_json = response.json()
        if '成功' in response.text:
            adtype = r_json['data']['obtain']
            print(f'听音乐弹窗——>{adtype}金币')
        else:
            description = r_json['data']['description']
            print(f'听音乐弹窗——>{description}')
        randomtime()
        response2 = requests.get(url2, params=params2, headers=headers)
        r_json = response2.json()
        if '成功' in response2.text:
            adtype = r_json['data']['obtain']
            print(f'听音乐——>{adtype}金币')
        else:
            description = r_json['data']['description']
            print(f'听音乐——>{description}')
        randomtime()

def tx(loginUid, loginSid, appUid, phone):
    if phone is None:
        return
    url = "https://integralapi.kuwo.cn/api/v1/online/sign/v1/getWithdraw"
    params = {
        "quotaId": "30002",
        'loginUid': loginUid,
        'loginSid': loginSid,
        'appUid': appUid,
        "source": "kwplayer_ar_10.7.6.2_qq.apk",
        "version": "1",
        "phone": phone
    }
    headers = {
        "Host": "integralapi.kuwo.cn",
        "Connection": "keep-alive",
        "sec-ch-ua": '"Not A(Brand";v="99", "Android WebView";v="121", "Chromium";v="121"',
        "Accept": "application/json, text/plain, */*",
        "sec-ch-ua-mobile": "?1",
        #"User-Agent": "Mozilla/5.0 (Linux; Android 14; POCO F2 Pro Build/UQ1A.240105.004; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/121.0.6167.101 Mobile Safari/537.36/ kuwopage",
        "sec-ch-ua-platform": '"Android"',
        "Origin": "https://h5app.kuwo.cn",
        "X-Requested-With": "cn.kuwo.player",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        #"Referer": "https://h5app.kuwo.cn/apps/earning-sign/cash_out.html?transparentTitleView=1&defBack=black&endBgColor=white&random=1711186177362&kwflag=2642624794_1711186175255",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.."
                           "9,en-US;q=0.8,en;q=0.7"
    }

    response = requests.get(url, params=params, headers=headers).json()
    text = response['data']['text']
    print(f"提现2元——>>>{text}")

def task():
    username, loginSid, loginUid = login(q)
    randomtime()
    signvideo(loginUid, loginSid, appUid)
    randomtime()
    Homepage(loginUid, loginSid, appUid)
    randomtime()
    openbox(loginUid, loginSid, devId, appUid)  # 开宝箱
    randomtime()
    draw(loginUid, loginSid, appUid)  # 抽奖
    randomtime()
    video(loginUid, loginSid, appUid)  # 看视频
    randomtime()
    video(loginUid, loginSid, appUid)  # 看视频
    randomtime()
    collect(loginUid, loginSid, appUid)  # 收藏
    listentomusic(loginUid, loginSid, appUid)# 听音乐

def main():
    kwyy = os.getenv('kwyy')
    if not kwyy:
        logging.error("环境变量 'kwyy' 未设置")
        return
        
    if '&' not in kwyy:
        try:
            appUid, devId, q, phone, 备注 = kwyy.split('#')
            username, loginSid, loginUid = login(q)
            if not all([username, loginSid, loginUid]):
                logging.error("登录失败")
                return
                
            logging.info(f'账号：{loginUid},任务开始'.center(30, '_'))
            tasks = [
                (signvideo, (loginUid, loginSid, appUid)),
                (Homepage, (loginUid, loginSid, appUid)),
                (openbox, (loginUid, loginSid, devId, appUid)),
                (draw, (loginUid, loginSid, appUid)),
                (video, (loginUid, loginSid, appUid)),
                (collect, (loginUid, loginSid, appUid)),
                (listentomusic, (loginUid, loginSid, appUid))
            ]
            
            for task in tasks:
                func, args = task
                func(*args)
                time.sleep(3)
            logging.info(f"账号：{loginUid},本次任务完成！".center(30, "_"))
            
        except Exception as e:
            logging.error(f"执行失败: {e}")
    else:
        for i, account in enumerate(kwyy.split('&')):
            logging.info(f'=====第{i+1}个账号=====')
            try:
                appUid, devId, q, phone, 备注 = account.split('#')
                username, loginSid, loginUid = login(q)
                if not all([username, loginSid, loginUid]):
                    continue
                    
                #logging.info(f'账号：{loginUid},任务开始'.center(30, '_'))
                tasks = [
                    (signvideo, (loginUid, loginSid, appUid)),
                    (Homepage, (loginUid, loginSid, appUid)),
                    (openbox, (loginUid, loginSid, devId, appUid)),
                    (draw, (loginUid, loginSid, appUid)),
                    (video, (loginUid, loginSid, appUid)),
                    (collect, (loginUid, loginSid, appUid)),
                    (listentomusic, (loginUid, loginSid, appUid))
                ]
                
                for task in tasks:
                    func, args = task
                    func(*args)
                    time.sleep(3)
                logging.info(f"账号：{loginUid},本次任务完成！".center(30, "_"))
                
                
            except Exception as e:
                logging.error(f"账号{i+1}执行失败: {e}")
                continue

if __name__ == '__main__':
    main()
import whois
import os
import requests
import random
import json
import pytesseract
from PIL import Image
from bs4 import BeautifulSoup


requests_session = requests.session()


def get_verify_code():

    url = "http://www.miitbeian.gov.cn/getDetailVerifyCode?26"

    headers = {
        'Accept': "*/*",
        'Accept-Encoding': "gzip, deflate",
        'Accept-Language': "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        'Cache-Control': "no-cache",
        'Connection': "keep-alive",
        'Host': "www.miitbeian.gov.cn",
        'Referer': "http://www.miitbeian.gov.cn/icp/publish/query/icpMemoInfo_searchExecute.action",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0",
        'Upgrade-Insecure-Requests': "1",
        'Cookie' : "__jsluid=c4601189393cf1eb89ec4acfc580b322; JSESSIONID=GyGBZcrqzFExD4EgNCNbsYtwxG4x4CLHTD4D9xpX1ztJDREmeQPD!-736616813; __jsl_clearance=1544070858.513|0|j8pkp7b2ejNmHKeD%2BVuwSdxUsYw%3D"
    }

    response = requests_session.get(url, headers=headers)
    print(response.status_code)
    if response.status_code == 200:
        with open('./code.jpg', 'wb') as file:
            file.write(response.content)
        img = Image.open('./code.jpg')
        return_code = pytesseract.image_to_string(img)
        print(len(return_code))
    else:
        print('false')


def IPC(verifyCode, domain):
    url = 'http://www.miitbeian.gov.cn/icp/publish/query/icpMemoInfo_login.action'
    payload = "verifyCode=" + verifyCode + "&id=97872191&siteName=&siteDomain="+ domain +\
              "baidu.com&siteUrl=&mainLicense=&siteIp=&unitName=&mainUnitNature=-1&certType=-1&mainUnitCertNo=&bindFlag=0"

    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'Accept-Encoding': "gzip, deflate",
        'Accept-Language': "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        'Cache-Control': "no-cache",
        'Connection': "keep-alive",
        'Content-Length': "144",
        'Content-Type': "application/x-www-form-urlencoded",
        'DNT': "1",
        'Host': "www.miitbeian.gov.cn",
        'Origin': "http://www.miitbeian.gov.cn",
        'Pragma': "no-cache",
        'Referer': "http://www.miitbeian.gov.cn/icp/publish/query/icpMemoInfo_searchExecute.action",
        'Upgrade-Insecure-Requests': "1",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0",
        'Cookie': "__jsluid=c4601189393cf1eb89ec4acfc580b322; JSESSIONID=GyGBZcrqzFExD4EgNCNbsYtwxG4x4CLHTD4D9xpX1ztJDREmeQPD!-736616813; __jsl_clearance=1544064356.174|0|GGBfXcYymOQ2BFbJ9AYXu24jIFk%3D"
    }

    response = requests_session.post(url, data=payload, headers=headers)
    if response.status_code != 200:
        return
    html_context = response.text

    soup = BeautifulSoup(html_context, "html.parser")
    soup_msg = soup.find_all(name='td', attrs={'class': "bxy"})
    soup.prettify()
    icp_list = []
    for content in soup_msg:
        content = content.get_text()
        content_out = "".join(content.split())
        icp_list.append(content_out)
    icp_info = {"name": icp_list[0], "nature": icp_list[1], "icp_number": icp_list[2],
                "web_name": icp_list[3], "domain": icp_list[4], "check_data": icp_list[-2]}
    return icp_info

if __name__ == '__main__':
    get_verify_code()
import os
import sys
import requests 
from bs4 import BeautifulSoup


print('Loading iii_settings.txt file...')
if os.path.isfile('./iii_settings.txt') is False:
    print('iii_settings.txt file is not found.')
    sys.exit(1)

handler = open('iii_settings.txt', 'r')
settings = ''.join(handler.readlines()).split('\n')[0:-1]
handler.close()
if len(settings) != 5:
    print('It seems that setting contents are not correct.')
    sys.exit(1)


url = 'https://keyauth.iii.org.tw/SSO/Login/GetTempPwd'
post_url = 'https://keyauth.iii.org.tw/SSO/Login/GetTempPwdAsync'
resp = requests.get(url)
html_doc = resp.text

soup = BeautifulSoup(html_doc, 'html.parser')
verification_token = soup.select_one('input[name="__RequestVerificationToken"]')

verification_token = verification_token.get('value')
payload = {
    '__RequestVerificationToken': verification_token,
    'EmpNo': settings[0],
    'IDNO': settings[1],
    'BirthdayYear': settings[2],
    'BirthdayMonth': settings[3],
    'BirthdayDay': settings[4],
}

tmp_passwd_resp = requests.post(post_url, data=payload, cookies=resp.cookies)

if '已成功申請臨時密碼，請至聯絡信箱檢視資訊' in tmp_passwd_resp.text:
    print('Sending getting tmp password request is successful.')
    sys.exit(0)


print('Sending getting tmp password request is failed.')
sys.exit(1)

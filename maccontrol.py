import requests
import cookielib
from requests.auth import HTTPBasicAuth
import sys

url_base = 'http://192.168.254.254/'
username = "username"
password = "password"
jar = cookielib.CookieJar()
headers = {'User-Agent': 'Mozilla/5.0', 'referer': 'http://192.168.254.254/tcpiplan_with_mac_addr_ctrl_linkmode.htm'}
submit = 'submit.htm?tcpiplan_with_mac_addr_ctrl_linkmode.htm'
s = requests.session()

def add_mac(self):
    payload = [
        ('newmac', mac),
        (submit, 'Send')
    ]
    s.post(url_base + "form2macacadd.cgi", auth=HTTPBasicAuth(username, password), cookies=jar, headers=headers, data=payload)
    print(mac + ' added!')

def enable_maccontrol():
    payload = [
        ('wlan', '1'),
        (submit, 'Send')
    ]
    s.post(url_base + "form2macac.cgi", auth=HTTPBasicAuth(username, password), cookies=jar, headers=headers, data=payload)
    print("MacControl Enabled!")

def disable_maccontrol():
    payload = [
        (submit, 'Send')
    ]
    s.post(url_base + "form2macac.cgi", auth=HTTPBasicAuth(username, password), cookies=jar, headers=headers, data=payload)
    print("MacControl Disabled!")

if __name__ == '__main__':
    if str(sys.argv[1]) == 'add':
        mac = str(sys.argv[2])
        add_mac(mac)

    elif str(sys.argv[1]) == 'enable':
        enable_maccontrol()

    elif str(sys.argv[1]) == 'disable':
        disable_maccontrol()

    else:
        print('USAGE: maccontrol.py [enable]')
        print('       maccontrol.py [disable]')
        print('       maccontrol.py [add] [MACADDRESS]')
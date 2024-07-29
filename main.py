# proxy6.net
import dotenv  #pip install python-dotenv
from os import environ
import urllib.request,json


dotenv.load_dotenv('.env')

api_key  = environ['proxy6_api_key']
url = f"https://proxy6.net/api/{api_key}/getproxy"
data = "" # Все данные по этому API_KEY
proxy_list = list() # инфо о прокси
selected_idx = 0 # Выбранный номер Прокси из списка
command = 'nodeta' # комманда, какое действие выполнить с прокси

# считать все данные данные
with urllib.request.urlopen(url) as u:
    data = dict(json.load(u))

# получаем  данные только для Прокси, записываем в список
for proxy in data["list"]:
    proxy_list.append(data["list"][proxy])


#Обновить список прокси
def update_proxy_list():
    data = dict();
    proxy_list.clear()
    # считать все данные данные
    with urllib.request.urlopen(url) as u:
        data = dict(json.load(u))
    # получаем  данные только для Прокси, записываем в список
    for proxy in data["list"]:
        proxy_list.append(data["list"][proxy])

def show_proxy_list(proxylist):
    print("Список доступных Прокси:")
    idx = 1
    for prx in proxylist:
        print(f"{idx}: IP:{prx['ip']}  HOST:{prx['host']} PORT:{prx['port']} USER:{prx['user']} PASS:{prx['pass']} ТИП:{prx['type']} IPv:{prx['version']} ДЕЙСТВУЕТ_ДО:{prx['date_end']}")
        idx = idx + 1


def select_proxy(proxylist):
    print("Выберите Прокси")
    idx = 1
    for prx in proxylist:
        print(
            f"{idx}: IP:{prx['ip']} HOST:{prx['host']} PORT:{prx['port']} USER:{prx['user']} PASS:{prx['pass']} ТИП:{prx['type']} IPv:{prx['version']} ДЕЙСТВУЕТ_ДО:{prx['date_end']}")
        idx = idx + 1
    print("Назад: 0")
    return int(input("Введите номер:> "))

def change_type(api_key, ids, proxy_type="https"):
    # запрос на изменение Типа Прокси Socks/HTTPS
    # proxy_type = "https" # "https" / "socks"
    req = f"https://proxy6.net/api/{api_key}/settype?ids={ids}&type={proxy_type}"
    with urllib.request.urlopen(req) as u:
        d = json.load(u)
        # print(d)
    update_proxy_list()


while command != "e":
    print(f"\nproxy6.net\n1: Показать список доступных Прокси.\n2: Изменить тип Прокси\ne: Выход.")
    command = input("введите команду :>")
    if command == "1":
        show_proxy_list(proxy_list)
    if command == "2":
        numb = int(input("введите номер Прокси :>"))
        if numb > len(proxy_list):
            print("[!]_WARNING: Некорректный номер Прокси!")
        else:
            if(proxy_list[numb-1]['type'] == "http"):
                change_type(api_key, proxy_list[numb-1]['id'], "socks")
            elif(proxy_list[numb-1]['type'] == "socks"):
                change_type(api_key, proxy_list[numb - 1]['id'], "http1")
            else:
                change_type(api_key, proxy_list[numb - 1]['id'], "http")
            print("[INFO]: Тип Проксти успешно изменён.")





# Практика: написать запрос для получения данных
# с api любой криптобиржи,
# данные выводить в консоль и обновлять файл, каждые 3 секунды.

import requests
import time
import datetime

def get_data():
    url = "https://api.binance.com/api/v3/ticker/price"
    data_raw = requests.get(url=url)


    if int(data_raw).status_code == 200:
        valutes = data_raw.json()
        print(valutes)
        data_clear = []
        for valute in valutes:
            if float(valutes["price"]) > 1.0:
                data_clear.append(valute)
        print(data_clear)


        data_asc = sorted(data_clear, key=lambda x: x["price"], reverse=True)


        with open("data.txt", "w") as file:
            for i in data_asc:
                print(f"{i['symbol']} | {i['price']}")
                file.writelines(data_asc)


    else:
        print(data_raw.status_code)
    except Exception as error:
    print(error)
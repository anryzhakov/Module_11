# Слушатель курса Junior Python-разработчик
# Рыжаков Андрей Николаевич, anryzhakov@yandex.ru
# Домашнее задание по теме "Обзор сторонних библиотек Python"

"""
    Материалы:
        https://habr.com/ru/articles/759922/
        https://skillbox.ru/media/code/biblioteka-requests-dlya-python-kod-i-praktika/
        https://stackoverflow.com/questions/56308427/python-import-matplotlib-fails-after-successful-install-using-pip-on-windows
"""

import pandas as pd             # https://pandas.pydata.org/docs/user_guide/index.html
import requests as rq           # https://requests.readthedocs.io/en/latest/index.html
import matplotlib.pyplot as pl  # https://matplotlib.org/stable/users/index.html

# j = rq.get('https://iss.moex.com/iss/securities.json?q=Yandex').json()
# data = [{k: r[i] for i, k in enumerate(j['securities']['columns'])} for r in j['securities']['data']]
# print(pd.DataFrame(data))

# j = rq.get('https://iss.moex.com/iss/securities/YNDX/aggregates.json?date=2022-09-21').json()
# data = [{k : r[i] for i, k in enumerate(j['aggregates']['columns'])} for r in j['aggregates']['data']]
# print(pd.DataFrame(data))

j = rq.get('http://iss.moex.com/iss/engines/stock/markets/shares/securities/YNDX/candles.json?from=2024-01-01&till=2024-06-30&interval=24').json()
data = [{k : r[i] for i, k in enumerate(j['candles']['columns'])} for r in j['candles']['data']]
frame = pd.DataFrame(data)
print(frame)
pl.plot(list(frame['close']))
pl.savefig("shares.png")
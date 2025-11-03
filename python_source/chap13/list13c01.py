# 이전에 실행한 날짜와 시간 출력하기

import os.path
import pickle
import datetime

CONFIG_FILE = 'config.dat'

previous = None

if os.path.exists(CONFIG_FILE):
    with open(CONFIG_FILE, 'rb') as f:
        previous = pickle.load(f)
        print('방문 일시 : ', previous)
        pass
else:
    print('처음 실행하셨군요!')

# 다양한 처리

current = datetime.datetime.now()

with open(CONFIG_FILE, 'wb') as f:
    pickle.dump(current, f)

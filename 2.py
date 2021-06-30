#!/usr/bin/env python3

#  опрашиваем веб-сервисы, получаем их IP, выводим информацию в стандартный вывод в виде: <URL сервиса> - <его IP>

import socket as s
import time as t
import datetime as dt
import json
import yaml


# установим переменные
i = 1
wait = 3 # интервал проверок в секундах
server = {'drive.google.com':'0.0.0.0', 'mail.google.com':'0.0.0.0', 'google.com':'0.0.0.0'}
init=0

fpath = "/home/user/netology/4.3/temp" # конфиг.файлы
flog  = "/home/user/netology/4.3/error.log" # файлы протоколов


print('Start check web services')

while 1==1 : # 
  for host in server:
    ip = s.gethostbyname(host)
    if ip != server[host]:
      if i==1 and init !=1:
          is_error=True
          with open(flog,'a') as fl:
            print(str(dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + '[error]' +str(host) +'IP '+server[host]+''+ip,file=fl)

# JSON
  with open(fpath+host+".json",'w') as jsnf:
    json_data= json.dumps({host:ip})
        jsnf.write(json_data)

# YAML
  with open(fpath+host+".yaml",'w') as ymlf:
    yaml_data=yaml.dumps({host: ip})
        ymlf.write(yaml_data)

      
 server[host]=ip

 
  t.sleep(wait)

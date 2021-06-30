## Домашнее задание к занятию "4.3. Языки разметки JSON и YAML"

### Задание 1

Мы выгрузили JSON, который получили через API запрос к нашему сервису:

```
{ "info" : "Sample JSON output from our service\t",
    "elements" :[
        { "name" : "first",
        "type" : "server",
        "ip" : 7175 
        },
        { "name" : "second",
        "type" : "proxy",
        "ip : 71.78.22.43
        }
    ]
}
```

Нужно найти и исправить все ошибки, которые допускает наш сервис

***Ответ:***

Ошибка:
```
 "ip : 71.78.22.43
```
должно быть
```
 "ip" : "71.78.22.43"
```

---
### Задание 2

В прошлый рабочий день мы создавали скрипт, позволяющий опрашивать веб-сервисы и получать их IP. К уже реализованному функционалу нам нужно добавить возможность записи JSON и YAML файлов, описывающих наши сервисы. Формат записи JSON по одному сервису: { "имя сервиса" : "его IP"}. Формат записи YAML по одному сервису: - имя сервиса: его IP. Если в момент исполнения скрипта меняется IP у сервиса - он должен так же поменяться в yml и json файле.



***Ответ:***

```
#!/usr/bin/env python3

#  опрашиваем веб-сервисы, получаем их IP, 
#  выводим информацию в стандартный вывод в виде: <URL сервиса> - <его IP>

import socket as s
import time as t
import datetime as dt
import json
import yaml


# установим переменные
i = 1
wait = 5 # интервал проверок в секундах
server = {'drive.google.com':'0.0.0.0', 'mail.google.com':'0.0.0.0', 'google.com':'0.0.0.0'}
init=0

fpath = "/home/user/netology/4.3/temp" # конфиг.файлы
flog  = "/home/user/netology/4.3/error.log" # файлы протоколов

print('Start check web services')

while 1==1 : 
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
```

---

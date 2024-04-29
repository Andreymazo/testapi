# Testrestapi
![](/media/Screenshot%20from%202024-04-27%2018-02-07.png)

![](/media/Screenshot%20from%202024-04-27%2014-50-17.png)

![](/media/Screenshot%20from%202024-04-27%2014-50-21.png)


##
        git clone https://github.com/Andreymazo/testapi.git

Hints:
free port:

- lsof -i :8000
- fuser -k 8000/tcp

Stop and remove containers:

- docker stop $(docker ps -a -q)
- docker rm $(docker ps -a -q)

to free 5432:
- systemctl stop postgresql


```cmd
sudo docker-compose up
```

if you wish to run without docker, 93 str in config.settings.py:
-       'HOST': 'db',#os.getenv('DB_HOST'), change to 
-       'HOST': os.getenv('DB_HOST')

```cmd
pip install -r requirements.txt
```
```cmd
python manage.py runserver
```


Django forms. 
1. Query - endpoint. here we fill in form and send it to 
Здесь нельзя редиректом, надо апи реквестом запрашивать, на выходных допилю, это канешна не по заданию.

![](/media/Screenshot%20from%202024-04-27%2015-12-28.png)

2. Result - endpoin. here we check if there such realestateobject
![](/media/Screenshot%20from%202024-04-27%2015-12-23.png)

3. Ping  - endpoint. Cheks sttus code
![](/media/Screenshot%20from%202024-04-27%2015-12-37.png)

4. Histori - endpoint - show list of all requests.
![](/media/Screenshot%20from%202024-04-27%2015-12-48.png)

5. emulate_server - endpoint - doesnt do anything, but giving back data

First i desided to run cmd files: testrestapi/cmd_history.sh, testrestapi/cmd_ping.sh, testrestapi/cmd_query.sh, testrestapi/cmd_result.sh
but there were inconviniences with csrf. For client better to put {csrftoken} in template and that it. intead of making additional request only to gain token.

На проверке работа была 30 сек. Сказали: - Учи мат часть. Конкретно по работе не объяснили, что не подошло.
Похоже формы не зашли, ну или моя "эмуляция" на 5 эндпоинте не впечатлила.

Подумал. На эндпоинте result надо аgи запрос сделать к эндпоинту emulate_server, а не просто обращаться к базе. Тут у меня ошибка
 моя "эмуляция" на 5 эндпоинте -  не пойдет. Here we must create new project with base and model RealEstateObject and run server in background mode. Daphne will do, i guess. daphne -b 0.0.0.0 -p 8002 config.asgi:application
or just python manage.py runserver 8002
we must see:

![](/media/Screenshot%20from%202024-04-29%2010-20-53.png)


+79219507391 Andrey Mazo
https://t.me/AndreyMazo
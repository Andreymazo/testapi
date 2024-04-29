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

port 8002 In repo https://github.com/Andreymazo/testbase

2. daphne -b 0.0.0.0 -p 8002 config.asgi:application

or just python manage.py runserver 8002 (if without daphne)

we must see:

![](/media/Screenshot%20from%202024-04-29%2010-20-53.png)

3. Check if our form query in testbase (RealEstateObject) and send back at 8000/qury and finish creating our HistoryQuery object with result true or false

1min video:
[Screencast from 29.04.2024 23:03:48.webm](https://github.com/Andreymazo/testapi/assets/116811819/d91c788b-ba92-4b79-ad6c-5d03bb84ba22)


+79219507391 Andrey Mazo
https://t.me/AndreyMazo

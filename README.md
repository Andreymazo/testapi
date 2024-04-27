# Testrestapi

![](/media/Screenshot%20from%202024-04-27%2014-50-17.png)

![](/media/Screenshot%20from%202024-04-27%2014-50-21.png)


##
        git clone 

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
2. Result - endpoin. here we check if there such realestateobject
3. Ping  - endpoint. Cheks sttus code
4. Histori - endpoint - show list of all requests.
5. emulate_server - endpoint - doesnt do anything, but giving back data

+79219507391 Andrey Mazo
https://t.me/AndreyMazo
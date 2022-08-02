This page provides example code for HTTP web server implemented in Python to test web_hook capability in FastNetMon and return all data received from FastNetMon.

Please put following code to file fastnetmon_webhook_receiver_server.py:
```
wget https://raw.githubusercontent.com/FastNetMon/webhook_receiver_python/main/fastnetmon_webhook_receiver_server.py
```


And run it this way:
```
python fastnetmon_webhook_receiver_server.py 8080
```

And enable FastNetMon’s feature:
```
sudo fcli set main web_callback_enabled enable
sudo fcli set main web_callback_url http://127.0.0.1:8080/attack/notify
sudo fcli commit
```

Starting from FastNetMon 2.0.320 you will be able to use IPv6 addresses for callbacks this way:
```
sudo fcli set main web_callback_enabled enable
sudo fcli set main web_callback_url http://[::1]:8080/attack/notify
sudo fcli commit
```

网站只能运行在本地端口上，没有进行服务器部署。因为超算不允许开放相关网页端口，无法使用uwsgi之类的工具。

打开Django服务：

先进入/home/Website目录，然后运行python3 manage.py runserver 0.0.0.0:8000


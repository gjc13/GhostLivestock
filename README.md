# GhostLivestock
Online GhostLivestock Generator

## Demo
[Hosted by DigitalOcean](http://ha.yaoht.cn/)

## Introduction
The website is based on

Django: https://www.djangoproject.com/

Django-bootstrap3: https://github.com/dyve/django-bootstrap3/

Bootstrap: http://getbootstrap.com/

## Deployment
### Development Env
```shell
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:80
```
### Production Env
You'd better deploy it with WSGI.
 
[How to deploy with WSGI](https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/)
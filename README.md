# Websime from the company [Simetric](https://www.simetric.com.br)
> Just a normal website to shows what the company does and what products and
services it sells. 

![PyPi][python-image]
![PyPi][status-image]
![Dockbit][deploy-image]
![Wercker][build-image]

The website itself is very simple and objective. As normally we have a public area and a private area
so I used Django to help me to manage it. Besides on private area I'm also using DjangoAdminLTE2 to
improve the look and fell.

## Technologies utilized
* Python 3.5+
* Django 1.11
* PostgreSQL 9.5+

## Public area
![](public.png)

## Private area
![](admin.png)

## Installation

Any Operating System:

```sh
mkvirtualenv simetric -p python3

pip install -r requeriments.txt

python makemigrations

python migrate

python manage.py createsuperuser

python manage.py runserver

access http://localhost:8000
```

## Release History

* 0.2.1
    * CHANGE: Update README
* 0.2.0
    * The first proper release
* 0.1.1
    * ADD: Create the app `acesso`
* 0.1.0
    * ADD: Create the app `core` 
* 0.0.1
    * Work in progress

## Meta

Diemesleno Souza Carvalho – [@diemesleno](https://twitter.com/diemesleno) – diemesleno@gmail.com

Distributed under the ![AUR][gpl-image] license. 

[https://github.com/diemeslen0/simetric](https://github.com/diemeslen0/)

[python-image]: https://img.shields.io/pypi/pyversions/Django.svg?style=flat-square
[gpl-image]: https://img.shields.io/aur/license/yaourt.svg?style=flat-square
[status-image]: https://img.shields.io/pypi/status/Django.svg?style=flat-square
[build-image]: https://img.shields.io/wercker/ci/wercker/docs.svg
[deploy-image]: https://img.shields.io/dockbit/DockbitStatus/health.svg?token=TvavttxFHJ4qhnKstDxrvBXM&style=flat-square

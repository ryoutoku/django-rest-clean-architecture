# django_rest_clean_architecture

## 概略

以下をベースとして、Django Rest Framework とクリーンアーキテクチャを考慮したサンプル実装

https://docs.djangoproject.com/ja/3.0/intro/tutorial01/

## 目的

Django Rest Framework で提供されているフレームワークにおいて、以下点を考察するためにサンプル実装を行う。

- どこにどのような機能を実装することを想定したものになっているのか
- その実装を行うことでどのような問題が発生しうるか

## フォルダ構成

```bash
.
├── domains
│   ├── __init__.py
│   ├── application_services.py     # Application Service実装
│   ├── apps.py
│   ├── objects.py                  # Aggregate, DomainObject実装
│   └── repositories.py             # repositoryのinterface定義
├── manage.py
├── mysite
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── polls
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── repositories.py             # domains.repositoriesのinterfaceの実装
    ├── serializers.py
    ├── tests.py
    ├── urls.py
    └── views.py
```

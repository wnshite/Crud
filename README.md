# CRUD

## 0. setting

- 가상환경 생성
- 가상환경 활성화
- `.gitignore` 설정(python, window, masos, django)

## 1. django

- `pip install django`
- 현재 우리가 다루고 있는 폴더의 프로젝트 생성
```shell
django-admin startproject crud.
```

- 앱 생성 /  등록
```shell
django-admin startapp posts
```

## 2. CRUD

- modeling (`models.py`)

```python
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
```

- migration
```shell
# 번역본 생성
python manage.py makemigrations
```

```shell
# DB에 반영
python manage.py migrate
```

- create super user
```shell
python manage.py createsuperuser
```

- admin 페이지 모델 등록(`admin.py`)
```python
from django.contrib import admin
from .models import Post

# Register your models here.
admin.site.register(Post)
```
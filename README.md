# Hello world
1. startproject hello world
   1. python -m pip install django~=3.2
   2. django-admin startproject hello world .
   3. python manage.py runserver
2. startapp
   1. python manage.py startapp playground
   2. setting.py > INSTALLED_APPS 'playground', 추가
3. playground/views
   1. say_hello()
4. urls
   1. playground/hello/ -> say_hello()
5. urls, playground/ urls
   1. playground / -> hello/ -> say_hello()
6. templates/playground/hello.html
   1. playground / -> hello/ -> say_hello() -> html
7. 프로젝트/urls.py -> 앱/urls.py -> 앱/templates/앱/index.html
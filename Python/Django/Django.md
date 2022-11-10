# DJANGO
## Install virtualenv
```bash
virtualenv -p <python_interpreter_executable> <virtualenv_name>
```


## Create a virtualenv environment
```bash
virtualenv -p <python_interpreter_path> <virtualenv_name>
```

## Activate it
```bash
cd <virtualenv_directory>
Scripts\\activate
```

## Install Django
```bash
pip install Django
```

```bash
(pip install Django==1.8.1) for a specific version
```


## Create Django project
```bash
django-admin.py startproject [project_label]
```

> Example:
> 
> ```python manage.py startapp boardgames```
> 
```
├── boardgames
│   ├── __init__.py
│   ├── settings.py     :   general settings
│   ├── urls.py         :   configure url in the project
│   └── wsgi.py         :   deploy your project 
├── db.sqlite3
└── manage.py           :   run the server
```


## Run Django project Server
```shell
cd [project_label]
python manage.py runserver
```


## Create app Django
```bash
python manage.py startapp [app_label]
```


> Example:
> 
> ```python manage.py startapp main```
> 


```
main
├── admin.py
├── apps.py
├── __init__.py
├── migrations
│   └── __init__.py
├── models.py
├── tests.py
└── views.py
```


1. Add [app_label] to **INSTALLED_APPS** in ```boardgames\\boardgames\\settings.py```
    ```python 
    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    main
    ]
    ```
    
1. Edit ```\\[Django_project]\\[app]\\views.py```
    ```python
    from django.http import HttpResponse
    # Create your views here.
    
    def home(request):
        return HttpResponse("Hello")
    ```
    
1. Edit ````\\[Django_project]\\[Django_project]\\urls.py````
    ```python
    from django.conf.urls import url
    from django.contrib import admin
    from main.views import home
    
    urlpatterns = [
        url(r'^admin/', admin.site.urls),
        url(r'', home),
    ]
    ```






> From Django 2.0: ```url``` has been replaced by ```path``` and ```re_path``` 
>
> ```python
> from django.urls import path, re_path
>
> urlpatterns = [
>     url('admin/', admin.site.urls),
>     url(r'^$', home, name='home')
>
> ]
> ```
>
> becomes
>
> ```python
> from django.urls import path, re_path
>
> urlpatterns = [
>     path('admin/', admin.site.urls),
>     re_path(r'^$', home, name='home'),
>
> ]
> ```


## Render a web page


1. Create directory ```\\[Django_project]\\[app]\\templates\\[app]```    
    > Note: the structure *template\\[app]* is useful for keeping the content portable


1. Create **home.html** in ```\\[Django_project]\\[app]\\templates\\[app]``` with the following content
    ```html
    <html>
        <head>
            <title>Hello, World!</title>
        </head>
        <body>
            <h1>Hello, World!</h1>
        </body>
    </html>
    ```


1. In order to render the **home.html** file, edit ```\\[Django_project]\\[app]\\views.py```
    ```python
    from django.shortcuts import render
    from django.http import HttpResponse
    # Create your views here.
    
    def home(request):
        return render(request, "main/home.html")
    ```




## Render a web page with variables


1. Edit **home.html** in ```\\[Django_project]\\[app]\\templates\\[app]``` with the following content
    ```html
    <html>
        <head>
            <title>Hello, World!</title>
        </head>
        <body>
            <h1>{{ message }}</h1>
        </body>
    </html>
    ```
    
    > Note: **message** is a variable
    
1. Edit ```\\[Django_project]\\[app]\\views.py```
    ```python
    from django.shortcuts import render
    from django.http import HttpResponse
    # Create your views here.


    def home(request):
        return render(request, 'main/home.html', {'message': 'Hello from Dario :)'})
    ```
    
## Using settings in Python code
In your Django apps, use settings by importing the object django.conf.settings. **Example:**
```python
from django.conf import settings


if settings.DEBUG:
    # Do something    
```




## **```views.py```** functions 
Called by urls.py


```python
def function(request):
    if request.method == 'POST':
        info_dict = request.POST.copy()  # .copy() allows to add items in next steps
        info_dict = info_dict.dict()
        # remove token key, since I don't need it
        del info_dict['csrfmiddlewaretoken']
        
    if request.method == 'GET':
        ...
```

### Submit a list of values
#### front-end code
attribute ```name``` must be an array 
```html
<div class="col-xs-3">  
    <select name="to[]" id="manangers_selection_to" class="form-control" size="13" multiple="multiple"></select>  
</div>
```

#### back-end code
```python
request.POST.getlist('to[]')
```

# notes
>
The ```render``` function Combines a given template with a given context dictionary and returns an HttpResponse object with that rendered text.


You request a page and the render function returns it.

The ```redirect``` function sends another request to the given url.
>


# Others:

## Get port the server is running on
```python
request.META['SERVER_PORT']
t.

You request a page and the render function returns it.


The ```redirect``` function sends another request to the given url.
>




# Others:


## Get port the server is running on
```python
request.META['SERVER_PORT']
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTkwNjg0MDM4MCwtMTI3MjYyNjc0OV19
-->

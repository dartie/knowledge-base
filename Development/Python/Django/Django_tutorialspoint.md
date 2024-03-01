# Django (Tutorialspoint)

## Create virtual environment
````
virtualenv -p <python_executable> <virtual_environment_name>
````

  > ````
  > virtualenv -p c:\\python36\\python.exe tutorialspoint_Django
  > ````
  
### Activate it
````
cd <virtual_environment_name>
\\Scripts\\activate
````

  > ````
  > cd tutorialspoint_Django
  > \\Scripts\\activate
  > ````

  
## Install Django
````
pip install Django
````


## Create Django Project
````
django-admin startproject <django_projectname>
````

  > ````
  > django-admin startproject myproject
  > ````

## Move to the project
````
cd <django_projectname>
````

  > ````
  > cd myproject
  > ````

 
## Run Django server
````
python manage.py runserver
````

    > Note:
    > for specifying the port, use ````0.0.0.0:<your_port>````
    > Example: ````
    > python manage.py runserver 0.0.0.0:9000
    > ````

    
## Create app in Django project
````
python manage.py startapp <app_name>
````

    > Example:
    > ````
    > python manage.py startapp myapp
    > ````




## Add app to Django project
1. Open file ```` \\<django_projectname>\\<django_projectname>\\settings.py ````
    > ```` \\myproject\\myproject\\settings.py ````

1. Add '<app_name>' in **INSTALLED_APPS** tuple

    > Example:
    > ````python    
    > INSTALLED_APPS = (
    >    'django.contrib.admin',
    >    'django.contrib.auth',
    >    'django.contrib.contenttypes',
    >    'django.contrib.sessions',
    >    'django.contrib.messages',
    >    'django.contrib.staticfiles',
    >    'myapp',
    > )
    > ```` 

    
## Create superuser
````
python manage.py createsuperuser
````

## Project migration
````
python manage.py migrate
````

## Handle a http request
### Define function to call at a specific url - Edit python ````<django_projectname>\\<app_name>\\views.py````
> Note: a 'view' is a Python function that takes a web request and returns a web response
1. Add import needed:
    ````python
    from django.shortcuts import render
    from django.http import HttpResponse
    ````
    
1. Create a function for handling a http request
  * Returning a html content:
    ````python
    def hello(request):
        text = """<h1>welcome to my app !</h1>"""
        return HttpResponse(text)
    ````
    
    or 
    
    ````
    def hello(request, number):
        text = "<h1>welcome to my app number %s!</h1>"% number
        return HttpResponse(text)
    ````

  * Rendering a html page:
    ````python
    def hello(request):
        return render(request, "hello.html", {})
    ````
    
    > Note: the html file specified as secondo parameter of render function, will be searched in ````<app_name>/templates```` directory 
    
  * Redirect to web page
    ````python
    from django.shortcuts import render, redirect
    from django.http import HttpResponse
    import datetime

    # Create your views here.
    def hello(request):
       today = datetime.datetime.now().date()
       daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
       return redirect("https://www.djangoproject.com")  # external url
        
    def viewArticle(request, articleId):
       """ A view that display an article based on his ID"""
       text = "Displaying article Number : %s" %articleId
       return redirect(viewArticles, year = "2045", month = "02")  # "viewArticles" is the name of the below function. It can also be used the name of the url (variable "name" specified in urls.py - value = articles) 
       
    def viewArticles(request, year, month):
       text = "Displaying articles of : %s/%s"%(year, month)
       return HttpResponse(text)       
    ````


### Handle url request - Edit python ````<django_projectname>\\urls.py````
> Note: in 'url.py', **urlpatterns** tuple define the mapping between URLs and views
````python
from myapp.views import hello, viewArticle, viewArticles, hello_date

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/', hello, name = 'hello'),
    url(r'^$', hello, name = 'hello'),
    url(r'^template/', hello_date, name = 'hello'),
    url(r'^article/(\\d+)/', viewArticle, name = 'article'),
    url(r'^articles/(\\d{2})/(\\d{4})', viewArticles, name = 'articles'),
    
]

````

## Templates
* <django_projectname>\\<app_name>\\templates\\main_template.html
    ````html
    <html>
       <body>
          
          Hello World!!!<p>Today is {{today}}</p>
          We are
          {% if today.day == 1 %}
          
          the first day of month.
          {% elif today == 30 %}
          
          the last day of month.
          {% else %}
          
          I don't know.
          {%endif%}
          
          <p>
             {% for day in days_of_week %}
             {{day}}
          </p>
    		
          {% endfor %}
          
       </body>
    </html>
    ````

* <django_projectname>\\<app_name>\\templates\\hello.html
    ````html
    {% extends "main_template.html" %}
    {% block title %}My Hello Page{% endblock %}
    {% block content %}
    
    Hello World!!!<p>Today is {{today}}</p>
    We are
    {% if today.day == 1 %}
    
    the first day of month.
    {% elif today == 30 %}
    
    the last day of month.
    {% else %}
    
    I don't know.
    {%endif%}
    
    <p>
    {% for day in days_of_week %}
    {{day}}
    </p>
    
    {% endfor %}
    {% endblock %}
    ````
    
## Add table and fields in database - ````\\<django_projectname>\\<app_name>\\models.py````
````python
from django.db import models

# Create your models here.
class Dreamreal(models.Model):

   website = models.CharField(max_length = 50)
   mail = models.CharField(max_length = 50)
   name = models.CharField(max_length = 50)
   phonenumber = models.IntegerField()

   class Meta:
      db_table = "dreamreal"  # optional - it forces the table name
````

### Apply modification made in the the **models.py**
````
python manage.py makemigrations
python manage.py migrate
````


# Send an email in python
1. import of smtplib
    ````python
    import of smtplib
    
    ````
1. Modify ````settings.py````:
    > **EMAIL_HOST** − smtp server.

    > **EMAIL_HOST_USER** − Login credential for the smtp server.

    > **EMAIL_HOST_PASSWORD** − Password credential for the smtp server.

    > **EMAIL_PORT** − smtp server port.

    > **EMAIL_USE_TLS** or _SSL − True if secure connection.
    
1. Modify ```` ```` : 
    ````python
    from django.core.mail import send_mail
    from django.http import HttpResponse

    def sendSimpleEmail(request, emailto):
       res = send_mail("hello paul", "comment tu vas?", "paul@polo.com", [emailto])
       return HttpResponse('%s'%res)
    ````

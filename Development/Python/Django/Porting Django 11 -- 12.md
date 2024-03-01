# Porting Django 11 -> 12
<br>

## 'provide the namespace argument to include() instead.' % len(arg). Passing a 3-tuple to include() is not supported. Pass a 2-tuple containing the list of patterns and app_name, and provide the namespace argument to include() instead.

### Solution:
1. Open file **urls.py**
1. Replace ```url(r'^admin/', include(admin.site.urls)),``` with ```url(r'^admin/', admin.site.urls),```


<br><br><br>


## AttributeError: 'WSGIRequest' object has no attribute 'user'

### Solution
1. Open file **settings.py**
1. Replace ```MIDDLEWARE_CLASSES``` with ```MIDDLEWARE```


<br><br><br>

##

### Solution
Remove ```SessionAuthenticationMiddleware``` from ```MIDDLEWARE``` list in **settings.py**





## Resources
* https://eldarion.com/blog/2017/12/26/10-tips-upgrading-django-20/
* https://www.codingforentrepreneurs.com/blog/django-version-20-a-few-key-features/

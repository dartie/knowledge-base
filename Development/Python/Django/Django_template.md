# Django template
## Use different css for pages


* base.html
```jinja2
{% block styles %}
{% endblock %}
```


* page1/template-view.html
```jinja2
{% extends "base.html" %}
{% load staticfiles %}


{% block styles %}
    <link rel="stylesheet" href="{% static 'css/page1.css' %}">
{% endblock %}
```




## Submit data
### Usign jquery
```javascript
$.ajax({
    type: "POST",
    url: url,
    data:{
        'csrfmiddlewaretoken':$('input[name="csrfmiddlewaretoken"]').val(),
    },
    success: function(response){
    }
});
```


### Using html
```html
            <form action="/upgrade" method="post">
            {% csrf_token %}
                <input type="text" class="form-control " id="Recordid_info" placeholder="Recordid" value="{{ record_id }}" name="Recordid_info"> <!-- hidden -->
                <input type="text" class="form-control " id="Customer_info" placeholder="Customer" value="{{ Customer }}" name="Customer_info"> <!-- hidden -->
                <input type="text" class="form-control " id="Deal_info" placeholder="Deal" value="{{ Deal }}" name="Deal_info"> <!-- hidden -->
                <input type="text" class="form-control " id="license_signed_fullfilename_info" placeholder="license_signed_fullfilename_info" value="{{ license_signed_fullfilename }}" name="license_signed_fullfilename_info"> <!-- hidden -->
                <input type="text" class="form-control " id="license_filename_info" placeholder="license_filename_info" value="{{ license_filename }}" name="license_filename_info"> <!-- hidden -->
                <textarea type="text" class="form-control hidden" id="license_signed_info" placeholder="license_signed" name="license_signed_info"></textarea> <!-- hidden -->
                <button type="submit" class="btn btn-danger navbar-btn navbar-right" onclick='return upgrade("{{ csrf_token }}")'>Upgrade</button>
            </form>


```




## Custom template
### Resource: https://docs.djangoproject.com/en/dev/howto/custom-template-tags/


### Create custom template
1. Create "templatetag" in the django project as template directory where to store custom templates
````
polls/
    __init__.py
    models.py
    templatetags/
        __init__.py
        poll_extras.py
    views.py
````
1. Create a new file with the follow content:
````python
from django import template


register = template.Library()


@register.filter
def function_name(arg1, arg2):
    pass
````


> It is suggested to name the function and the file in the same, in order to recognize it immediately.




### use custom template
1. In the template file:
````jinja2
variable|function_name
````


or 


````jinja2
variable|function_name:arg2
````


> variable is the arg2 of the function



### My Custom templates

#### Serve any image as base64

* `template_tags/app_filters.py`
    ```python
    import base64
    from django.contrib.staticfiles.finders import find as find_static_file

    @register.simple_tag(name='encode_static')
    def encode_static(path, encodign='base64', file_type='image'):
    try:
        file_path = find_static_file(path)
        ext = file_path.split('.')[-1]
        file_str = _get_file_data(file_path).decode('utf-8')
        return "data:{0}/{1};{2}, {3}".format(file_type, ext, encodign, file_str)
    except IOError:
        return ''


    def _get_file_data(file_path):
    with open(file_path, 'rb') as f:
        data = base64.b64encode(f.read())
        f.close()
        return data
    ```


## declare a variable
* load on top ````{% load i18n %}````


```jinja2
{% trans "string" as my_var %}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjE0Mzk2NDc3OF19
-->



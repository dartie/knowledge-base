# Create User in Django

## GUI



## via code
```python
from django.contrib.auth.models import User

create_user_obj = User.objects.create_user(username=new_user, password=new_user_pwd, email=new_user_email)
create_user_obj.first_name = new_user_firstname
create_user_obj.last_name = new_user_lastname
create_user_obj.save()
```

>>>
**Note:**
Don't use ```create``` because it does not save the password hashed.
Use ```create_user``` instead.
>>>


* Reference: http://cheng.logdown.com/posts/2016/01/06/django-create-and-login-user-manually


## Get all users in Django
```python
from django.contrib.auth.models import User

users = User.objects.all()
```

user will be a querySet. For turn it into a list, use:
```python
def QuerydictToList(querydict):
    """
    QuerydictToList turns a querydict to a list.
    :param querydict:
    :return: querydict_list
    """
    querydict_list = []
    for field_value in querydict:
        field_value = str(field_value)

        querydict_list.append(field_value)

    return querydict_list
```

## Get user id from username
```python
User.objects.get(username=the_username).pk
```

## Add user to the group
```python
user_id = 1
user_group = group_name

my_group = Group.objects.get(name=user_group)
my_group.user_set.add(user_id)
```

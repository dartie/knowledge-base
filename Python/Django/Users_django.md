# Edit user's password
* Link: https://www.laurivan.com/change-a-django-password-manually/


1. ```python manage.py shell```
1. Paste the code below:
   ```python
    from django.contrib.auth.models import User
    users = User.objects.all()
    print(users)
   ```


1. Get the id user from the list printed with the above command


1. Select a specific user
    ```python
    user = users[0]
    ```


1. Set the new password
    ```python
    user.set_password('_new_password_')
    ```


1. Save it
    ```python
    user.save()
    ```


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIwMDI1OTY3OThdfQ==
-->

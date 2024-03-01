# WRITE TO DB:


## References:
* https://docs.djangoproject.com/en/1.11/topics/db/models/




## Create table
1. Edit **models.py** 
  ````python
  class TABLE(models.Model):
  id = models.AutoField(primary_key=True)
  field_char = models.CharField(max_length=255)
  int_char = models.IntegerField()
  field_date = models.DateField()
  ````




## Add app to django
1. Detect *appname* and *configname* from **apps.py**
  ````python
  class LogConfig(AppConfig):
  name = 'log'
  ````


  > appname = log
  > configname = LogConfig




1. Edit **settings.py**, adding your app to ````INSTALLED_APPS````
  ````python
  'appname.apps.configname',
  ````


  > Example:
  > 'log.apps.LogConfig',




## Apply modifications
1. Run the command 
  ````bash
  python manage.py makemigrations
  ````


  Files have been generated in <appname>\\migrations


1. Run the following command if you want to generate the SQL command:
  ````bash
  python manage.py sqlmigrate
  ````


1. Run the command
  ````bash
  python manage.py migrate
  ````


> python manage.py makemigrations && python manage.py migrate




> Enter in Django interactive shell:
> python manage.py shell
>
> from APPNAME.models import TABLE
> object = TABLE(field=value)
> object.save()




## Execute queries:
1. Run
  ````python
  all_entries = TABLE.objects.all()
  ````


1. Print query for getting all elements:
  ````python
  print(all_entries.query)
  ````


1. Get count of elements:
  ````python
  TABLE.objects.count()
  ````


1. Queries on database:
  * All elements:
    ````python
    TABLE.objects.values()
    ````


    or 


    ````python
    TABLE.objects.all()
    ````




  * Specific columns:
    ````python
    TABLE.objects.values('column_name')
    ````


  * List of values:
    ````python
    TABLE.objects.values_list('column_name', flat=True)
    ````


  * List of values with filters:
    ````python
    TABLE.objects.filter(**criteria to include**).exclude(** criteria to exclude **).values_list('column_name', flat=True)
    ````


    > NOTE:
    > for exclude it could be used the the "Q" object
    > from myapp.models import Entry
    > from django.db.models import Q


    > Entry.objects.filter(~Q(id = 3))




  * Print a specific 
    ```python
    import pprint
    pprint.pprint(TABLE.objects.values()[N])
    ```




  * Query with filter
    ```python
    records = TABLE.objects.filter(id=101).exclude().values_list([FIELD1, FIELD2, FIELD3])
    ```


  * Query with dynamic filter
    * link: https://yuji.wordpress.com/2009/09/12/django-python-dynamically-create-queries-from-a-string-and-the-or-operator/
    * link: https://stackoverflow.com/questions/310732/in-django-how-does-one-filter-a-queryset-with-dynamic-field-lookups


    The key was how to use keyword arguments as strings.


    ```python
    Person.objects.filter(first_name__icontains='Yuji')
    ```
    
    is equal to:
    
    ```python
    Person.objects.filter( **{'first_name__icontains':'Yuji'})
    ```




```python
kwargs = {
    '{0}__{1}'.format('name', 'startswith'): 'A',
    '{0}__{1}'.format('name', 'endswith'): 'Z'
}


Person.objects.filter(**kwargs)




for info in info_dict:
    info_field_ = info.replace('_search', '').replace('__', ' ')
    info_field = settings.search_fields_to_select_dict[info_field_]
    info_value = info_dict[info]
    filter_dict[info_field + '__icontains'] = info_value


records = TABLE.objects.filter(**filter_dict).exclude().values_list([FIELD1, FIELD2, FIELD3])
```


## Tip:
* If you use values(), You'll end up with a list of dictionaries (technically a ValuesQuerySet)


```python
instance = MyModel.objects.values('description')[0]
description = instance['description']
```


* If you use **values_list()**, you'll end up with a list of tuples
```python
instance = MyModel.objects.values_list('description')[0]
description = instance[0]
```


* Or if you're just getting one value like in this case, you can use the flat=True kwarg with values_list to get a simple list of values
```python
description = MyModel.objects.values_list('description', flat=True)[0]
```

* The values() method returns a list of dictionaries:
```python
[{'comment_id': 1}, {'comment_id': 2}]
```


* The **values_list()** method returns a list of tuples:
```python
[(1,), (2,)]
```


* If you are using values_list() with a single field, you can use flat=True to return a list rather than a list of tuples.
```python
[1, 2]
```

## Filters

### Select date for a month

```python
.filter(date__year='2020', date__month='01')
```


### Select date for a range

```python
.filter(creation_date__range=[post_data["date_start"], post_data["date_end"]])
```

-------

# Get list of of table's columns 
```python
table._meta.get_fields()
```


## CREATE record with python code
```python
add_to_db = TABLE.objects.create(
field = value
)

add_to_db.save()
```


## UPDATE record with python code
```python
update = TABLE.objects.get(pk=id)
update.field = value
update.save()
```

***OR***

```python
Requests.objects.filter(id=int(info_dict['request_to_decline'])).update(status=1)  # update to status 2 = declined
```
## Drop table
### python code
```python
from django.db import connection

cursor = connection.cursor()
cursor.execute('show tables;')
parts = ('DROP TABLE IF EXISTS %s;' % table for (table,) in cursor.fetchall())
sql = 'SET FOREIGN_KEY_CHECKS = 0;\\n' + '\\n'.join(parts) + 'SET FOREIGN_KEY_CHECKS = 1;\\n'
connection.cursor().execute(sql)
```


## pass variable across views's functions
  ```python
  #view 1:


  request.session['list'] = list_to_process
  ```


  ```python
  #view 2:


  list_to_process = request.session['list']
  ```




### Bash script
```bash
#!/bin/sh

drop() {
    echo "Droping all tables prefixed with $1_."
    echo
    echo "show tables" | ./manage.py dbshell |
    egrep "^$1_" | xargs -I "@@" echo "DROP TABLE @@;" |
    ./manage.py dbshell
    echo "Tables dropped."
    echo
}

cancel() {
    echo "Cancelling Table Drop."
    echo
}

if [ -z "$1" ]; then
    echo "Please specify a table prefix to drop."
else
    echo "Drop all tables with $1_ prefix?"
    select choice in drop cancel;do
        $choice $1
        break
    done
fi
```


## Drop and recreate table
  ```bash
  python manage.py reset app_name
  ```


## Reset counter db
* If you really want to reset the counter, you can drop and recreate the table:
```bash
python manage.py sqlclear <app_name> > python manage.py dbshell
```


* Or, if you need to keep the data from other tables in the app, you can manually reset the counter:
```
python manage.py dbshell
mysql> UPDATE sqlite_sequence SET seq = (SELECT MAX(col) FROM TABLE) WHERE name="TABLE"
```
Example:
```sql
UPDATE sqlite_sequence SET seq = (SELECT MAX(id) FROM GeneratedLicenses) WHERE name="GeneratedLicenses";
```


or 


```sql
"DELETE FROM SQLITE_SEQUENCE WHERE NAME = '" + TABLE + "'"
```




# Reload static files in Pycharm 
````
python manage.py collectstatic --noinput --clear
````


````
Clear the browser cache (Ctrl+Shift+Canc)
````




# Troubleshooting:
## "django.db.utils.DatabaseError: table "myapp_tablename" already exists"
**Issue**:
the message appears after run "python manage.py migrate"


**FIX:** 
````
python manage.py migrate myapp --fake
````


## Conflicts
**FIX:**
To answer your question, with the new migration introduced in Django 1.7, in order to add a new field to a model you can simply add that field to your model and initialize migrations with ./manage.py makemigrations and then run ./manage.py migrate and the new field will be added to your db. To avoid dealing with errors for your existing models however, you can use the --fake:


1. Initialize migrations for your existing models:
```
./manage.py makemigrations myapp
```


1. Fake migrations for existing models:
```
./manage.py migrate --fake myapp
```


1. Add the new field to myapp.models:
```python
from django.db import models


class MyModel(models.Model):
... #existing fields
newfield = models.CharField(max_length=100) #new field
```


1. Run makemigrations again (this will add a new migration file in migrations folder that add the newfield to db):
```
./manage.py makemigrations myapp
```


1. Run migrate again:
```
./manage.py migrate myapp
```


```


# python manage.py commands
http://django-extensions.readthedocs.io/en/latest/command_extensions.html


* update
ngth=100) #new field
```

1. Run makemigrations again (this will add a new migration file in migrations folder that add the newfield to db):
```
./manage.py makemigrations myapp
```

1. Run migrate again:
```
./manage.py migrate myapp
```


# python manage.py commands
http://django-extensions.readthedocs.io/en/latest/command_extensions.html




* update
* date format
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTE4MTE0ODUyLC04NTU2MzYyMzksMTYxMT
E0NDgzNV19
-->

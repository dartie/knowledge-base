# SQLAlchemy

## Installation
```bash
pip install flask_sqlalchemy
```


## Import
```
from flask_sqlalchemy import SQLAlchemy
```

## Init
```python
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)


class Table(db.Model):
  __tablename__ = 'Table_name'
  __table_args__ = {'extend_existing': True}
  id = db.Column(db.Integer, primary_key=True)
  customer_name = db.Column(db.Text)
  project_name = db.Column(db.Text, nullable=True)
  standard_name = db.Column(db.Text)
  product = db.Column(db.Text)
  version = db.Column(db.Text)
  issue_date = db.Column(db.Date)
  registered_site_license = db.Column(db.Text, unique=True)
  generator = db.Column(db.Text)
```


## Select
```python
duplicates = Table.query.filter_by(field=field_value).all()
```


### Select Inner Join
Supposing a Table with `device_id` foreign-key of id in `Devices` Table
```python
records = db.session.query(Devices.description, Devices.ip, Devices.hostname, Results.status, Results.last_response).join(Devices)
records = [x for x in records]  # returns a tuple for each record
```

### Convert query to dictionary

```python
query.__dict__
```

```python
for u in session.query(User).all():
  print u.__dict__
```

or 

```python
query = session.query(User.name, User.birthday)
for row in query:
  print(row._asdict())
```


## Insert

```python
new_record = Table(
id=None,
field=field_value
)

db.session.add(new_record)
db.session.commit()
db.session.flush()
```

## Update

### 1 
```python
record = Table.query.filter_by(id=id)  # update_doc_versions = Table.query.get(id)
update_cmd = "UPDATE Table SET field = {} WHERE id={}".format(field_value, id)
db.engine.execute(update_cmd)
db.session.commit()
```


### 2 (it doesn't work, needs research)
```python
record = Table.query.filter_by(id=id)  # update_doc_versions = Table.query.get(id)
record.field = new_value
db.session.commit()
```

## Difference between commit and flush
When `session.flush()` is called, the transactions are taking place but, however, are not written to disk. Writing to disk only happens once `session.commit()` is called. Consequently, it is defined such that if `session.commit()` is called, then `session.flush()` is called automatically, anyhow.

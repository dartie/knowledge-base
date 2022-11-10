# Pandas

* https://towardsdatascience.com/pandas-index-explained-b131beaf6f7b
* https://www.ritchieng.com/pandas-multi-criteria-filtering/
* https://kanoki.org/2020/01/21/pandas-dataframe-filter-with-multiple-conditions/
* https://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/
* https://realpython.com/pandas-groupby/

* https://www.youtube.com/watch?v=dcqPhpY7tWk&t=5s
* https://www.youtube.com/watch?v=rUl-rkN7Z3c

## OrderedDict to Dataframe
```python
df = pd.DataFrame(OrderedDict_element)
```

## Load data from csv
```python
pd.read_csv("filename.csv") 
```

## Select specific columns
```python
df.filter(["Name", "College", "Salary"])
```

## Apply a filter
```python
df.filter(df.Name == "Dario")
```

## Apply multiple filters
```python
df.query('col1 <= 1 & 1 <= col1')
```

## Sum all columns
```python
df_sum = df.sum()
```

## Sort values
```python
df[ [*fields_to_select] ].sort_values(by="field_to_sort_by", ascending=True)
```

## Select with sql
In recent pandas the index will be saved in the database (you used to have to reset_index first).

Following the docs (setting a SQLite connection in memory):

```python
import sqlite3
# Create your connection.
cnx = sqlite3.connect(':memory:')
```

> Note: You can also pass a SQLAlchemy engine here (see end of answer).

We can save price2 to cnx:

```python
price2.to_sql(name='price2', con=cnx)
```

We can retrieve via read_sql:

```python
p2 = pd.read_sql('select * from price2', cnx)
```

However, when stored (and retrieved) dates are unicode rather than Timestamp. To convert back to what we started with we can use pd.to_datetime:

```python
p2.Date = pd.to_datetime(p2.Date)
p = p2.set_index('Date')
```

We get back the same DataFrame as prices:

```python
In [11]: p2
Out[11]: 
<class 'pandas.core.frame.DataFrame'>
DatetimeIndex: 1006 entries, 2009-01-02 00:00:00 to 2012-12-31 00:00:00
Data columns:
AAPL    1006  non-null values
GE      1006  non-null values
dtypes: float64(2)
```

You can also use a SQLAlchemy engine:

```python
from sqlalchemy import create_engine
e = create_engine('sqlite://')  # pass your db url

price2.to_sql(name='price2', con=cnx)
```

This allows you to use read_sql_table (which can only be used with SQLAlchemy):

```python
pd.read_sql_table(table_name='price2', con=e)
#         Date   AAPL     GE
# 0 2009-01-02  89.95  14.76
# 1 2009-01-05  93.75  14.38
# 2 2009-01-06  92.20  14.58
# 3 2009-01-07  90.21  13.93
# 4 2009-01-08  91.88  13.95
```

### list tables 
```sql
SELECT name from sqlite_master where type= "table"
```
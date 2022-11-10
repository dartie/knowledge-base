# Flask

## Resources
* [4 Connecting Flask to SQLite \\| Building Python-based, database-driven web applications (with maps!) using Flask, SQLite, SQLAlchemy and MapBox](http://jonathansoma.com/tutorials/flask-sqlalchemy-mapbox/connecting-flask-to-sqlite.html)

## Troubleshooting
* FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.   'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and
```python
SQLALCHEMY_TRACK_MODIFICATIONS = False
```
or
```python
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
```
before
```
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///SM.sqlite3'
db = SQLAlchemy(app)
```

* The session is unavailable because no secret
```python
app = Flask(__name__)
app.secret_key = 'asdasda'
```

* `Flask Error: “Method Not Allowed The method is not allowed for the requested URL”`
In 
```python
@app.route('/entry', methods=['GET', 'POST'])
```
`methods` does not contain the method used

## route


### route link with regex
```python
from flask import Flask
from werkzeug.routing import BaseConverter

app = Flask(__name__)

class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


app.url_map.converters['regex'] = RegexConverter

@app.route('/<regex("[abcABC0-9]{4,6}"):uid>-<slug>/')
def example(uid, slug):
    return "uid: %s, slug: %s" % (uid, slug)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

## Static files
You have by default the  [`static`  endpoint](http://flask.pocoo.org/docs/quickstart/#static-files)  for static files. Also  [`Flask`](http://flask.pocoo.org/docs/api/#flask.Flask)  application has the following arguments:

`static_url_path`: can be used to specify a different path for the static files on the web. Defaults to the name of the  `static_folder`  folder.

`static_folder`: the folder with static files that should be served at  `static_url_path`. Defaults to the 'static' folder in the root path of the application.

It means that the  `filename`  argument will take a relative path to your file in  `static_folder`  and convert it to a relative path combined with  `static_url_default`:

```python
url_for('static', filename='path/to/file')
```

will convert the file path from  `static_folder/path/to/file`  to the url path  `static_url_default/path/to/file`.

So if you want to get files from the  `static/bootstrap`  folder you use this code:

```html
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='bootstrap/bootstrap.min.css') }}">
```

Which will be converted to (using default settings):

```html
<link rel="stylesheet" type="text/css" href="static/bootstrap/bootstrap.min.css">
```

### avoid cache static files
```html
<script type="text/javascript" src=" {{ url_for('static', filename='js/main.js', version='9') }}">  </script>
```

## Custom templates
```python
@app.template_filter('make_caps')
def caps(text):
    """Convert a string to all caps."""
    return text.uppercase()
```
or

```python
@app.template_filter()
def make_caps(text):
    """Convert a string to all caps."""
    return text.uppercase()
```
Call it in jinja2 template with:
```jinja2
{{ "hello world!"|make_caps }}
```


## Template
```python
from flask import Flask, render_template, request
import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

# import Namespace
try:
    from types import SimpleNamespace as Namespace  # available from Python 3.3
except ImportError:
    class Namespace:
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def home():
	return render_template('index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0")
```

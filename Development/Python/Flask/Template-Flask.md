# Template Flask

## app.py
```python
from flask import Flask, render_template, request, jsonify, send_from_directory
from werkzeug.routing import BaseConverter
import os
import sys
import time
import inspect
from flask_sqlalchemy import SQLAlchemy
import datetime
import time
import threading
import json
import unidecode
import traceback

# import Namespace
try:
  from types import SimpleNamespace as Namespace  # available from Python 3.3
except ImportError:
  class Namespace:
      def __init__(self, **kwargs):
          self.__dict__.update(kwargs)


class RegexConverter(BaseConverter):
  def __init__(self, url_map, *items):
      super(RegexConverter, self).__init__(url_map)
      self.regex = items[0]


currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

op_system = sys.platform

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Network.sqlite3'
db = SQLAlchemy(app)
app.url_map.converters['regex'] = RegexConverter


@app.route(r'/<regex(".*\.(png|ico)"):file>')
def favicon(file):
  file = os.path.basename(file)
  return send_from_directory(os.path.join(app.root_path, 'static', 'icons'), file, mimetype='image/vnd.microsoft.icon')


@app.template_filter()
def format_table_fields(field):
  # adjust timestamp to show in the table
  time_format = "%m-%d-%Y, %H:%M:%S"
  formatted_field = field.strftime(time_format) if isinstance(field, datetime.datetime) else field

  return formatted_field


def log(text):
  datetimenow = datetime.datetime.now()
  datetimenow_str = format_table_fields(datetimenow)

  return datetimenow_str + ' - ' + text


@app.route('/', methods=['POST', 'GET'])
def index():
  # some code
  
  return render_template('index.html', jinja2_variable=flask_variable)


if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)
```

## template/base.html
```html
<!DOCTYPE html>
<body lang="en">
<head>
  <meta charset="UTF-8">
  <link rel="icon" type="image/x-icon" href="{{ url_for('static', filename='favicon.ico') }}">
  <link rel="stylesheet" type= "text/css" href="{{ url_for('static', filename='css/icons.css') }}">
  <link rel="stylesheet" type= "text/css" href="{{ url_for('static', filename='css/navigation-top.css') }}">
  <link rel="stylesheet" type= "text/css" href="{{ url_for('static', filename='css/style.css') }}">
  <link rel="stylesheet" type= "text/css" href="{{ url_for('static', filename='css/table_filter.css') }}">
  <link rel="stylesheet" type= "text/css" href="{{ url_for('static', filename='css/table_sort.css') }}">
  <link rel="stylesheet" type= "text/css" href="{{ url_for('static', filename='css/multiselect-dropdown.css') }}">
  <title>Network Monitor</title>
</head>
  <body>

      <div id="sticky" class="sticky">
          <div class="navbar sticky">
            <a href="/">Dashboard</a>
  <!--          <a href="/" rel="home">&nbsp;&nbsp;<img src="/static/icons/home.png" alt="Home" width="4%" height="4%">Home</a>-->
          </div>

      </div>

      <div class="main">

{% block content %}
{% endblock %}

      </div>

  <script src="{{ url_for('static', filename='js/common.js') }}" type="text/javascript"></script>

  <script>
      function init() {
          ;  // nothing yet
      }

      window.onload = init;
  </script>
  </body>
</html>
```

## templates/index.html
```html
{% extends 'base.html' %}
{% block content %}

{# Body content without "body" tags, as they are already in the base.html #}

{% endblock %}
```


## static/css/style.css
```css
.material-icons.ko { color: #FF3855; }
.material-icons.ok { color: #77E5B3; }

table {
  width: 100%;
  margin-bottom: 1rem;
  border-radius: 0;
  border-collapse: collapse;
  border-spacing: 0;
  font-family: Verdana, Geneva, sans-serif;
  border-color: grey;
  text-align: center;
}

body {
  margin: 0;
  padding: 0;
  background: #fff;
  /* font-family: canada-type-gibson,"Helvetica Neue",Helvetica,Arial,sans-serif; */
  font-family: Verdana, Geneva, sans-serif;
  font-weight: 400;
  line-height: 1.5;
  color: #666;
  -webkit-font-smoothing: antialiased;
}

/* margin first element */
.first {
  margin-left: 10px;
}

/* disallow to select text */
.noselect {
-webkit-touch-callout: none; /* iOS Safari */
  -webkit-user-select: none; /* Safari */
   -khtml-user-select: none; /* Konqueror HTML */
     -moz-user-select: none; /* Old versions of Firefox */
      -ms-user-select: none; /* Internet Explorer/Edge */
          user-select: none; /* Non-prefixed version, currently
                                supported by Chrome, Opera and Firefox */
}

/* sticky */
.sticky {
position: -webkit-sticky; /* Safari */
position: sticky;
top: 0;
}

/* general buttons */
.button {
  box-shadow:inset 0px 1px 0px 0px #bbdaf7;
  background:linear-gradient(to bottom, #79bbff 5%, #378de5 100%);
  background-color:#79bbff;
  border-radius:6px;
  border:1px solid #84bbf3;
  display:inline-block;
  cursor:pointer;
  color:#ffffff;
  font-family:Arial;
  font-size:15px;
  font-weight:bold;
  padding:6px 24px;
  text-decoration:none;
  text-shadow:0px 1px 0px #528ecc;
  width: 155px;
}

.button:hover {
  background:linear-gradient(to bottom, #378de5 5%, #79bbff 100%);
  background-color:#378de5;
}

.button:active {
  position:relative;
  top:1px;
}

/* add and remove buttons */
.circle-button {
  height: 30px;
  line-height: 30px;  /* sets the text in the center */
  width: 30px;
  font-size: 2em;
  /* font-weight: bold; */
  border-radius: 50%;
  color: white;
  text-align: center;
  cursor: pointer;
}

.red-btn{
  background-color: #ff3838;
  line-height: 25px;
}

.green-btn{
  background-color: #4CAF50;
}

/* hint style */
.hint__circle {
height: 30px;
width: 30px;
margin: 0 auto;
-webkit-border-radius: 100px;
color: black;
text-align: center;
line-height: 30px;
font-family: arial;
font-size: 20px;
border: 2px solid black;
opacity: .4;
}

.hint__circle:hover {
border: 2px solid #f37920;
color: #f37920;
cursor: pointer;
opacity: 1;
}

/* dropdown menu */
select {
padding: 5px;
}
```

### static/css/navigation-top.css
```css
/* The navigation bar */
.navbar {
overflow: hidden;
background-color: #333;
position: fixed; /* Set the navbar to fixed position */
top: 0; /* Position the navbar at the top of the page */
width: 100%; /* Full width */
}

/* Links inside the navbar */
.navbar a {
float: left;
display: block;
color: #f2f2f2;
text-align: center;
padding: 14px 16px;
text-decoration: none;
}

/* Change background on mouse-over */
.navbar a:hover {
background: #ddd;
color: black;
cursor: pointer;
}

/* Main content */
.main {
margin-top: 60px; /* Add a top margin to avoid content overlay */
}
```

## static/css/icons.css
```css
/* fallback */
@font-face {
font-family: 'Material Icons';
font-style: normal;
font-weight: 400;
src: url('fonts/flUhRq6tzZclQEJ-Vdg-IuiaDsNc.woff2') format('woff2');
}

.material-icons {
font-family: 'Material Icons';
font-weight: normal;
font-style: normal;
font-size: 24px;
line-height: 1;
letter-spacing: normal;
text-transform: none;
display: inline-block;
white-space: nowrap;
word-wrap: normal;
direction: ltr;
-webkit-font-feature-settings: 'liga';
-webkit-font-smoothing: antialiased;
}
```
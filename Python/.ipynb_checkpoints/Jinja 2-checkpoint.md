# Jinja 2
## Reference
http://jinja.pocoo.org/docs/2.10/templates/

## Import
```python
import jinja2
from custom_filters import *
```


## Python code
```python
template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(templates_dir, encoding='utf-8', followlinks=False), trim_blocks=True, lstrip_blocks=True, autoescape=True)  
template_env.filters['get_list_value'] = get_list_value  # add custom filter
loaded_template = template_env.get_template("rule_config-en_US.xml")  # template file to render  
result = loaded_template.render(CMname=CMname, check='', msg_dict=msg_dict)  # list of variable=value to pass to the template file to call
```

or (avoiding the template file)
```python
template_str = """string {{ }}

"""
template_env = jinja2.Environment(loader=jinja2.BaseLoader, trim_blocks=True, lstrip_blocks=True, autoescape=True).from_string(template_str)  
result = template_env.render(var=data)  # list of variable=value to pass to the template file to call
```

### Enable loop
add `extensions=['jinja2.ext.loopcontrols']` to `jinja2.Environment()` for enabling `break` and `continue`
```python
jinja2.Environment(extensions=['jinja2.ext.loopcontrols'])
```

## create a custom filter
**In python code:**
```python
def custom_filter(arg1, arg2):
    pass

template_env.filters['custom_filter'] = custom_filter  # add function "custom_filter" at the jinja2 filters
```

**In template code:**
```jinja2
{{ arg1|custom_filter(arg2) }}
```

## Declare a variable
```jinja2
{% set testing = 'it worked' %}
{% set another = testing %}
{{ another }}
```

## IF statement
```jinja2
{% if license_name != '' %}  
<license name="{{ license_name }}"/>  
{% endif %}
```

## FOR statement
```jinja2
{% for c in checks %}  
<check name="{{ c }}" xmsp_id="{{ c }}"/>  
{% endfor %}
```

| Variable           | Description                                                  |
| ------------------ | ------------------------------------------------------------ |
| loop.index         | The current iteration of the loop. (1 indexed)               |
| loop.index0        | The current iteration of the loop. (0 indexed)               |
| loop.revindex      | The number of iterations from the end of the loop (1 indexed) |
| loop.revindex0     | The number of iterations from the end of the loop (0 indexed) |
| loop.first         | True if first iteration.                                     |
| loop.last          | True if last iteration.                                      |
| loop.length        | The number of items in the sequence.                         |
| loop.cycle         | A helper function to cycle between a list of sequences. See the explanation below. |
| loop.depth         | Indicates how deep in a recursive loop the rendering currently is. Starts at level 1 |
| loop.depth0        | Indicates how deep in a recursive loop the rendering currently is. Starts at level 0 |
| loop.previtem      | The item from the previous iteration of the loop. Undefined during the first iteration. |
| loop.nextitem      | The item from the following iteration of the loop. Undefined during the last iteration. |
| loop.changed(*val) | True if previously called with a different value (or not called at all). |


### Iterate a dictionary
```jinja2
<ul>
  {% for key, value in _dict.items() %}
    <dt>{{ key }}</dt>
    <dd>{{ value }}</dd>
  {% endfor %}
</dl>
```

## Get template name
```jinja2
{{ self._TemplateReference__context.name }} 
```

## Python3 changes
Removed  `dict.iteritems()`,  `dict.iterkeys()`, and  `dict.itervalues()`.

Instead: use  `dict.items()`,  `dict.keys()`, and  `dict.values()`  respectively.
<!--stackedit_data:
eyJoaXN0b3J5IjpbODAxOTQyMTgwLC05MDczOTE2OTAsLTE2MD
Y2MTEyNCwzNjk5ODgyNzAsMTExNDc3NTAzMywtMTA3NzIxMzQ4
NSwzMDM4MjY3MDQsLTExMjk1NjY0MiwxMDcyODE0OTA2LC0yND
YwODcyMzgsLTEzMTEzNTIwNzYsNjAyNDk0Nzg1LDczMDk5ODEx
Nl19
-->

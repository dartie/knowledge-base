# Python

[[_TOC_]]


## Resources
* [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)
* [About — Python Notes (0.14.0)](http://thomas-cokelaer.info/tutorials/python/)


## Installation


### Windows

Download the package and follow the wizard


### Unix

```bash
sudo apt-get install python3-pip
```

#### To change Python 3.6.8 as the default in Ubuntu 18.04 to Python 3.7.

1. Install Python 3.7
    ```bash
    sudo apt-get install python3.7
    ```
    
1. Add Python3.6 & Python 3.7 to update-alternatives
    ```bash
    sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 1
    sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 2
    ```
    
1. Update Python 3 to point to Python 3.7   
    ```bash
    sudo update-alternatives --config python3 Enter 2 for Python 3.7
    ```
    
1. Test the version of python
    ```bash
    python3 --version
    Python 3.7.1 
    ```


## Export requirements


```shell
pip freeze > requirements.txt
```

## Load requirements


```pip install -r requirements.txt```


**requirementes.txt** looks like:


```
BeautifulSoup==3.2.0 
Django==1.3 
Fabric
```


> **Note:** if no version is specified, the latest release is downloaded










## Hide console window with GUI


### Unix


```bash
$ nohup mypythonprog &
```


### Windows


```shell
C:/> start pythonw mypythonprog
```



## Virtual environment - Virtualenv
* Separation of packages installations - you can use different package sets for each project.
* Separation of python versions - you can use different python versions for each project.






### Installation
```bash
sudo pip install virtualenv
```






### New env
```shell
cd ~/code/myproject/


virtualenv <env_name>


es: virtualenv env
```


> Note: for using a specific version of python, use -p


```shell
virtualenv -p /usr/bin/python2.6 <path/to/new/virtualenv/>
```






### Activate
```shell
cd ~/code/myproject/<env_name>/Scripts
run Activate.bat
```




## How to check python version at runtime


```python
>>>import sys
>>>sys.version_info
sys.version_info(major=2, minor=7, micro=11, releaselevel='final', serial=0)
>>> sys.version_info.major
2
```






## Add directory from which load modules


```python
>>> import sys 
>>> sys.path.append(’/ufs/guido/lib/python’) 


```


## Add parent directory to import paths
```python
import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
```




## Import modules dynamically


```python
moduleNames = ['sys', 'os', 're', 'unittest']
modules = map(__import__, moduleNames)
```

```python
import glob, importlib, os, pathlib, sys

# The directory containing your modules needs to be on the search path.
MODULE_DIR = '/path/to/modules'
sys.path.append(MODULE_DIR)

# Get the stem names (file name, without directory and '.py') of any 
# python files in your directory, load each module by name and run
# the required function.
py_files = glob.glob(os.path.join(MODULE_DIR, '*.py'))

for py_file in py_files:
  module_name = pathlib.Path(py_file).stem
  module = importlib.import_module(module_name)
  module.mikaj_laktom()
```

## Input from terminal
### Input function
```python
input_read = input('Message to display')
```


### Keyboard input with timeout
```python
import threading, msvcrt
import sys


def readInput(caption, default, timeout=5):
    class KeyboardThread(threading.Thread):
        def run(self):
            self.timedout = False
            self.input = b''
            while True:
                if msvcrt.kbhit():
                    chr = msvcrt.getche()
                    if ord(chr) == 13:
                        break
                    elif ord(chr) >= 32:
                        self.input += chr
                if len(self.input) == 0 and self.timedout:
                    break

    sys.stdout.write('%s: '%(caption))  # sys.stdout.write('%s(%s):'%(caption, default))
    result = default
    it = KeyboardThread()
    it.start()
    it.join(timeout)
    it.timedout = True
    if len(it.input) > 0:
        # wait for rest of input
        it.join()
        result = it.input
    print('')  # needed to move to next line
    return result
```



## Print
### Print removing previous text
**Python3**
```python
import time
for x in range (0,5):
    b = "Loading" + "." * x
    print (b, end="\\r")
    time.sleep(1)
```
**Python 2**
```python
import time
for x in range (0,5):
    b = "Loading" + "." * x
    print (b,)
    time.sleep(1)
```

**stdout**
```python
import os, sys, time

sys.stdout.write('### Excluding third part code files from analysis...\\r')
time.sleep(1)
sys.stdout.flush()
sys.stdout.write('### Excluding third part code files from analysis... done')
```


### Print removing previous text (x progressbar o loading)
```python
# here is the animation  
def animate(text):  
    for c in itertools.cycle(['|', '/', '-', '\\\\']):  
        if done:  
            break  
        sys.stdout.write('\\r' + text + ' ' + c)  
        sys.stdout.flush()  
        time.sleep(0.1)  
    sys.stdout.flush()  
    sys.stdout.write('\\rDone!')
```

### Print removing previous text (x progressbar o loading) - working with pyinstaller
```python
# here is the animation  
def animate(text):  
    CURSOR_UP_ONE = '\\x1b[1A' # Cursor up one line  
    ERASE_LINE = '\\x1b[2K' # Erase current line  
    print('')  # print a blank line  
    for c in itertools.cycle(['|', '/', '-', '\\\\']):  
        if done:  
            break  
        print(CURSOR_UP_ONE + ERASE_LINE + text + ' ' + c)  
        time.sleep(0.1)
    print(CURSOR_UP_ONE + ERASE_LINE + 'Done!')
```

### Print with custom color
```python
def print_colour(case, text, action='print', reset_style=Style.RESET_ALL):
    """

    :param case: specify the case ('new_project', 'ok', 'done', 'error', 'warning', 'debug', 'info' in order to apply
                 a specific style to the text)
    :param text: input text to which apply the style
    :param action: choose "print" for printing the text, or "return" for returning the value in case must be reused
                 (example: assign to a variable)
    :param reset_style: you can choose how to terminate the text. By default the style is reset, otherwise for enable
                        a style, you can leave it blank and the terminal will enable the style selected
    :return: if "action"==return, it return the input text with the style chosen
    """
    try:  # if colorama module is not loaded
        if case.lower() == 'new_project':
            style = Back.YELLOW + Fore.RED + Style.BRIGHT
        elif case.lower() == 'new_conf':
            style = Back.BLACK + Fore.CYAN
        elif case.lower() == 'analyse' or case.lower() == 'analyze':
            style = Back.BLACK + Fore.YELLOW
        elif case.lower() == 'debug':
            style = Back.CYAN + Fore.MAGENTA
        elif case.lower() == 'ok':
            style = Back.BLACK + Fore.GREEN + Style.BRIGHT
        elif case.lower() == 'done':
            style = Back.YELLOW + Fore.RED + Style.BRIGHT
        elif case.lower() == 'error':
            style = Style.BRIGHT + Back.BLACK + Fore.RED
        elif case.lower() == 'warning':
            style = Style.BRIGHT + Back.BLACK + Fore.YELLOW
        elif case.lower() == 'debug':
            style = Back.CYAN + Fore.MAGENTA
        elif case.lower() == 'info':
            style = Back.WHITE + Fore.BLUE
        elif case.lower().startswith('step'):
            style = Back.CYAN + Fore.MAGENTA
        elif case.lower().startswith('substep'):
            style = Back.BLACK + Fore.MAGENTA
        else:
            style = ''
    except:
        style = ''  # if colorama module is not loaded

    print_text = '{style}{text}{reset_style}'.format(style=style, text=str(text), reset_style=reset_style)

    # decide if the value must be printed or returned
    if action.lower() == 'print':
        print(print_text)
    elif action.lower() == 'return':
        return print_text
    else:
        print(print_text)
```

### Print in terminal as table
**1. tabulate**:  [https://pypi.python.org/pypi/tabulate](https://pypi.python.org/pypi/tabulate)

```
>>> from tabulate import tabulate
>>> print tabulate([['Alice', 24], ['Bob', 19]], headers=['Name', 'Age'])
Name      Age
------  -----
Alice      24
Bob        19
```

tabulate has many options to specify headers and table format.

```
>>> print tabulate([['Alice', 24], ['Bob', 19]], headers=['Name', 'Age'], tablefmt='orgtbl')
| Name   |   Age |
|--------+-------|
| Alice  |    24 |
| Bob    |    19 |
```

**2. PrettyTable**:  [https://pypi.python.org/pypi/PrettyTable](https://pypi.python.org/pypi/PrettyTable)

```
>>> from prettytable import PrettyTable
>>> t = PrettyTable(['Name', 'Age'])
>>> t.add_row(['Alice', 24])
>>> t.add_row(['Bob', 19])
>>> print t
+-------+-----+
|  Name | Age |
+-------+-----+
| Alice |  24 |
|  Bob  |  19 |
+-------+-----+
```

PrettyTable has options to read data from csv, html, sql database. Also you are able to select subset of data, sort table and change table styles.

**3. texttable**:  [https://pypi.python.org/pypi/texttable](https://pypi.python.org/pypi/texttable)

```
>>> from texttable import Texttable
>>> t = Texttable()
>>> t.add_rows([['Name', 'Age'], ['Alice', 24], ['Bob', 19]])
>>> print t.draw()
+-------+-----+
| Name  | Age |
+=======+=====+
| Alice | 24  |
+-------+-----+
| Bob   | 19  |
+-------+-----+
```

with texttable you can control horisontal/verical align, border style and data types.

Other options:

-   [terminaltables](https://github.com/Robpol86/terminaltables)  Easily draw tables in terminal/console applications from a list of lists of strings. Supports multi-line rows.
-   [asciitable](https://pypi.python.org/pypi/asciitable/0.8.0)  Asciitable can read and write a wide range of ASCII table formats via built-in Extension Reader Classes.


### Pretty print

#### pprint()
```python
import pprint

dct_arr = [
  {'Name': 'John', 'Age': '23', 'Country': 'USA'},
  {'Name': 'Jose', 'Age': '44', 'Country': 'Spain'},
  {'Name': 'Anne', 'Age': '29', 'Country': 'UK'},
  {'Name': 'Lee', 'Age': '35', 'Country': 'Japan'}
]

pprint.pprint(dct_arr)
```

Output:
```
[{'Age': '23', 'Country': 'USA', 'Name': 'John'},
 {'Age': '44', 'Country': 'Spain', 'Name': 'Jose'},
 {'Age': '29', 'Country': 'UK', 'Name': 'Anne'},
 {'Age': '35', 'Country': 'Japan', 'Name': 'Lee'}]
```
To compare, below is the output of a normal print() statement:

```python
[{'Name': 'John', 'Age': '23', 'Country': 'USA'}, {'Name': 'Jose', 'Age': '44', 'Country': 'Spain'}, {'Name': 'Anne', 'Age': '29', 'Country': 'UK'}, {'Name': 'Lee', 'Age': '35', 'Country': 'Japan'}]
```
The pprint() output is definitely more readable. What it does is to break each dictionary element in the array right after the commas while also sorting the dictionary’s values by key.

If you don’t want your key-value pairs sorted by key, then you should set the sort_dicts parameter to be False in the pprint() function.

#### json.dumps()
```python
import json

dct_arr = [
  {'Name': 'John', 'Age': '23', 'Country': 'USA'},
  {'Name': 'Jose', 'Age': '44', 'Country': 'Spain'},
  {'Name': 'Anne', 'Age': '29', 'Country': 'UK'},
  {'Name': 'Lee', 'Age': '35', 'Country': 'Japan'}
]

print(json.dumps(dct_arr, sort_keys=False, indent=4))
```

```python
[
    {
        "Age": "23",
        "Country": "USA",
        "Name": "John"
    },
    {
        "Age": "44",
        "Country": "Spain",
        "Name": "Jose"
    },
    {
        "Age": "29",
        "Country": "UK",
        "Name": "Anne"
    },
    {
        "Age": "35",
        "Country": "Japan",
        "Name": "Lee"
    }
]
```
Compared to the output of the pprint() function, this is much more readable, although it costs more lines since it’s in pretty JSON format.

#### yaml.dump()
```bash
pip3 install pyyaml
```

```python
import yaml

dct_arr = [
  {'Name': 'John', 'Age': '23', 'Residence': {'Country':'USA', 'City': 'New York'}},
  {'Name': 'Jose', 'Age': '44', 'Residence': {'Country':'Spain', 'City': 'Madrid'}},
  {'Name': 'Anne', 'Age': '29', 'Residence': {'Country':'UK', 'City': 'England'}},
  {'Name': 'Lee', 'Age': '35', 'Residence': {'Country':'Japan', 'City': 'Osaka'}}
]

print(yaml.dump(dct_arr, sort_keys=False, default_flow_style=False))
```

```
- Name: John
  Age: '23'
  Residence:
    Country: USA
    City: New York
- Name: Jose
  Age: '44'
  Residence:
    Country: Spain
    City: Madrid
- Name: Anne
  Age: '29'
  Residence:
    Country: UK
    City: England
- Name: Lee
  Age: '35'
  Residence:
    Country: Japan
    City: Osaka
```


## Switch in Python


```python
component_dir = []
        {
            'prqa-framework': lambda mod : component_dir.append (self.options['qaf_doc_dir']),
        }.get (self.options['module'],
               lambda mod : component_dir.append (os.path.join(self.options['ac_dir'], mod))) (self.options['module'])
```

## Platforms
```python
import sys

def get_platform():
    platforms = {
        'linux1' : 'Linux',
        'linux2' : 'Linux',
        'linux' : 'Linux',
        'darwin' : 'OS X',
        'win32' : 'Windows'
    }
    if sys.platform not in platforms:
        return sys.platform
    
    return platforms[sys.platform]
```

```python
import distro  
distro.linux_distribution()  
('Ubuntu', '19.04', 'Disco Dingo')  

import platform
platform.platform()
'Windows-7-6.1.7600'
```

```python
# only windows
sys.getwindowsversion()
sys.getwindowsversion(major=6, minor=1, build=7600, platform=2, service_pack=”)
```

## Strings
### Strip non ASCII characters

```python
import string
printable = set(string.printable)
text_filtered_func = filter(lambda x: x in printable, s)

text_filtered = ''.join(text_filtered_func)
```


### split keeping the delimiter


### split the carriage return
* https://docs.python.org/3/library/stdtypes.html#str.splitlines
```python
str.splitlines()

str.splitlines([keepends=True])  # Line breaks are not included in the resulting list unless `keepends` is given and true.
```


## Regex
source: [www.regexr.com](www.regexr.com)

`[]` : domain

`[A-Z]` : Matches a character having a character code between the two specified characters inclusive.
> **Example**
> `[g-s]`
> abcdef`ghijklmnopqrs`tuvwxyz

`[^A-Z]` : Match any character that is not in the set.
> **Example**
> `[^aeiou]`
> `gl`i`b j`o`cks v`e`x dw`a`rv`e`s!`

`\\w` : Matches any word character (alphanumeric & underscore). Only matches low-ascii characters (no accented or non-roman characters). 
Equivalent to `[A-Za-z0-9_]`
> **Example**
> `bonjour`, `mon` `fr`è`re`

`\\W` : Matches any character that is not a word character (alphanumeric & underscore). 
Equivalent to `[^A-Za-z0-9_]`
> **Example**
> bonjour`, `mon` `fr`è`re

`\\d` : Matches any digit character (0-9). 
Equivalent to `[0-9]`
> **Example**
> +`1`-(`444`)-`555`-`1234`

`\\D` : Matches any character that is not a digit character (0-9). Equivalent to `[^0-9]`.
> **Example**
> +`1`-(`444`)-`555`-`1234`

`\\s` : Matches any whitespace character (spaces, tabs, line breaks).
> **Example**
> glib` `jocks` `vex` `dwarves!

`\\S` : Matches any character that is not a whitespace character (spaces, tabs, line breaks).
> **Example**
> `glib` `jocks` `vex` `dwarves!`

`.` : Matches any character except line breaks. 
Equivalent to `[^\\n\\r]`.
> **Example**
> `glib jocks vex dwarves!`


### Anchors:
`^` : Matches the beginning of the string, or the beginning of a line if the multiline flag (m) is enabled. This matches a position, not a character.
> **Example**
> `^\\w+`
> `she` sells seashells

`$` : Matches the end of the string, or the end of a line if the multiline flag (m) is enabled. This matches a position, not a character.
> **Example**
> `\\w+$`
> she sells `seashells`

`\\b` : Matches a word boundary position such as whitespace, punctuation, or the start/end of the string. This matches a position, not a character.
> **Example**
> `s\\b`
> she sell`s` seashell`s`

`\\B` : Matches any position that is not a word boundary. This matches a position, not a character.
> **Example**
> `s\\B`
> `s`he `s`ells `s`ea`s`hells


### Quantifiers & Alternation:
`?` : optional. Matches 0 or 1 of the preceding token, effectively making it optional.
> **Example**
> `colou?r`
> `color` `colour`

`?` : lazy. Makes the preceding quantifier lazy, causing it to match as few characters as possible. By default, quantifiers are greedy, and will match as many characters as possible.
> **Example**
> `b\\w+?`
> b `be` `be`e `be`er `be`ers

`+` : Matches 1 or more of the preceding token.
> **Example**
> `b\\w+`
> b `be` `bee` `beer` `beers`

`*` : Matches 0 or more of the preceding token.
> **Example**
> `b\\w*`
> `b` `be` `bee` `beer` `beers`

`|` : Acts like a boolean OR. Matches the expression before or after the |.
It can operate within a group, or on a whole expression. The patterns will be tested in order.
> **Example**
> `b(a|e|i)d`
> `bad` bud bod `bed` `bid`


### Escaped Characters
```
\\.	\\\\	\\+	\\*	\\?	\\^	\\$	\\[	\\]	\\{	\\}	\\(	\\)	\\|	\\/	
```

#### Particular Cases:
```
\\[(.*?)\\]
```

**Explanation:**
* `\\[` : `[` is a meta char and needs to be escaped if you want to match it literally.
* `(.*?)` : match everything in a non-greedy way and capture it.
* `\\]` : `]` is a meta char and needs to be escaped if you want to match it literally.


### .search()
```python
txt = '<text>'
regex_var = re.compile(r'<pattern>')
search_var = regex_var.search('<text_in_which_to_search>')
print(search_var.group())

>>> phoneNumRegex = re.compile(r'(\\d\\d\\d)-(\\d\\d\\d-\\d\\d\\d\\d)')
>>> mo = phoneNumRegex.search('My number is 415-555-4242.')
>>> mo.group(1)
'415'
>>> mo.group(2)
'555-4242'
>>> mo.group(0)
'415-555-4242'
>>> mo.group()
'415-555-4242'
```


### .findall()
```python
txt = '<text>'
regex_var = re.compile(r'<pattern>')
search_var = regex_var.findall('<text_in_which_to_search>')
print(search_var)

>>> phoneNumRegex = re.compile(r'\\d\\d\\d-\\d\\d\\d-\\d\\d\\d\\d')
>>> mo = phoneNumRegex.search('My number is 415-555-4242.')
>>> print('Phone number found: ' + mo.group())
Phone number found: 415-555-4242


>>> phoneNumRegex = re.compile(r'\\d\\d\\d-\\d\\d\\d-\\d\\d\\d\\d') # has no groups
>>> phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
['415-555-9999', '212-555-0000']
```


### regex_search.start():regex_search.end()
```python
import re
txt = '<text_in_which_to_search>'
regex_search = re.search('-v[\\d]\\.[\\d]', txt)
if(regex_search):
  regex_result = txt[regex_search.start():regex_search.end()]
```


### re.sub()
**syntax**
```python
re.sub(r'<regex-pattern>', r'<replacement>', 'input_string')
```

```python
result = re.sub('abc',  '',    input)           # Delete pattern abc
result = re.sub('abc',  'def', input)           # Replace pattern abc -> def
result = re.sub(r'\\s+', ' ',   input)           # Eliminate duplicate whitespaces
result = re.sub('abc(def)ghi', r'\\1', input)    # Replace a string with a part of itself
```

#### Count Replacements
When you want to know how many replacements did happen use `re.subn()` instead:

```python
result = re.subn(pattern, replacement, input)
print ('Result: ', result[0])
print ('Replacements: ', result[1])
```

#### Using Backreferences
Numeric Backreferences
To use back reference define capture groups using `()` and reference to those using `\\1`, `\\2`, and so on. Do not forget the `r` prefix on the back reference string, otherwise `\\1` will be interpreted as a character.

```python
result = re.sub("(\\d+) (\\w+)", r"\\2 \\1")
```

```python
re.sub(r'(foo)', r'\\g<1>123', 'foobar')
'foo123bar'
```


#### Named Backreferences
For named backreferences define a named capture group `(?)` and reference using `\\g`. Again ensure to add the `r` prefix on the backreference string.

```python
result = re.sub("(?<number>\\d+) (?<word>\\w+)", r"\\g<word> \\g<number>")
```


### Split with regex expression python keeping delimiter
```python
# This keeps all separators  in result
##########################################################################
import re
#st="%%(c+dd+e+f-1523)%%7"
st='M3CM Rule-1.3,M2CM Rule-5.2'
sh=re.compile('M\\dCM')

def splitStringFull(sh, st):
  ls=sh.split(st)
  lo=[]
  start=0
  for l in ls:
    if not l : continue
    k=st.find(l)
    llen=len(l)
    if k> start:
      tmp= st[start:k]
      lo.append(tmp)
      lo.append(l)
      start = k + llen
    else:
      lo.append(l)
      start =llen
  return lo
 #############################


li= splitStringFull(sh , st)
print(li)
```


### Count words in a string
```python 
words_to_search = ['M2CM Rule', 'M3CM Rule']
count = 0
for word_to_search in words_to_search:
   count += sum(1 for _ in re.finditer(r'\\b%s\\b' % re.escape(word_to_search), output_diaglist_line))

if count > 1:  # count got more than 1 occurrence
```

## Lists
Collection of items (similar to C-language arrays).
Lists can contain mixed items such as numbers, strings, list.

```python
l1=[1, 'html.it'] # list with an int and a string
l2=[1, 1.2, 'ciao', [1,2] ] # list with: int, real, string and another list
>>> s=['html', 'it', 'html.it']
>>> s[0] # indexing
'html'
>>> s[-2] # index from right
'it'
>>> s[:2] # slicing
['html', 'it']
>>> s[2:]
['html.it']
>>> s[1:-1]
['it']
```

### Methods

#### append(item)
append item at bottom

```python
>>> stack.append(['e','f'])
>>> stack
['a', 'b', 'c', ['e', 'f']]
```

#### extend(list)
Connect 2 lists (at the tail)

```python
>>> a = [1, 2]
>>> b = ['a', 'b']
>>> a.extend(b)
>>> a
[1, 2, 'a', 'b']
>>>
```

#### .insert(index, item)
Add an item at the top of the list

#### .pop([index])
Returns the item with the index specified, then removes the item. "index" is optional, without it, pop removes it and returns the last list element

#### .remove(item)
Removes item from the list

#### del list[index]
Removes the item at index position

#### sort()
Sort the list in ascending order

```python
sort(reverse=True)	# returns the list ordered as descendent
```

#### sorted(list)
```python
Returns the list in ascending order
>>> l = [3, 2, 5 ,4, 7, 1]
>>> sorted(l)
[1, 2, 3, 4, 5, 7]
```
> Difference between **sort** and **sorted**:
> **sorted** function doesn't modify the original list. where as **sort** function updates the list with sorted version of the list.

>  `sorted()`  returns a  **new**  sorted list, leaving the original list unaffected.  `list.sort()`  sorts the list  **in-place**, mutating the list indices, and returns  `None`  (like all in-place operations).
>
> `sorted()`  works on any iterable, not just lists. Strings, tuples, dictionaries (you'll get the keys), generators, etc., returning a list containing all elements, sorted.
>
> -   Use  `list.sort()`  when you want to mutate the list,  `sorted()`  when you want a new sorted object back. Use  `sorted()`  when you want to sort something that is an iterable, not a list  _yet_.
>
> -   For lists,  `list.sort()`  is faster than  `sorted()`  because it doesn't have to create a copy. For any other iterable, you have no choice.


#### .index(item)
```python
Find the index of an item given a list containing it:
>>>>["foo", "bar", "baz"].index("bar")
1
```



### Get difference between two lists:
```python
temp1 = ['One', 'Two', 'Three', 'Four']
temp2 = ['One', 'Two']
In [5]: list(set(temp1) - set(temp2))
Out[5]: ['Four', 'Three']
```

OR:
```python
temp1 = ['One', 'Two', 'Three', 'Four']
temp2 = ['One', 'Two']

OR_List = set(temp1).symmetric_difference(temp2)
print(OR_List)
```

### Get common elements between two lists:
```python
temp1 = ['One', 'Two', 'Three', 'Four']
temp2 = ['One', 'Two']
In [5]: list(set(temp1).intersection(temp2))
```

### Get duplicated:
```pyon
a = [1,2,3,2,1,5,6,5,5,5] 
import collections 
print [item for item, count in collections.Counter(a).items() if count > 1] ## [1, 2, 5]
```

### list comprehension: List comprehensions provide a concise way to create lists
```python
# int to string
recovery_dataflow_messages = [str(x) for x in recovery_dataflow_messages] 
```

Alternative way:
```python
map(function_to_apply, list_of_inputs)
Use the map function(in py2):
results = map(int, results)
```

In py3:
```python
results = list(map(int, results))
```

```python
# list comprehensions
vals = [expression 
        for value in collection 
        if condition]

# This is equivalent to:

vals = []
for value in collection:
    if condition:
        vals.append(expression)
```
```python
# list comprehensions with if - else
vals = [ expression 
		if conditional 
		else other thing 
		for this many times ]
```


```python
new_content = ['"' + x.strip('\\n') + '"\\n' if x.startswith('-d ') else x for x in new_content]
```

**multiple if-else**
```python
>>> l = [1, 2, 3, 4, 5]
>>> ['yes' if v == 1 else 'no' if v == 2 else 'idle' for v in l]
['yes', 'no', 'idle', 'idle', 'idle']
```

**Nested list comprehensions**
```python
l = [ [' a', 'b '], [' c', 'd'] ]
newlist = [[y.strip() for y in x] for x in l]
> newlist = = [ ['a', 'b'], ['c', 'd'] ]
```
### Special built-in functions
[http://book.pythontips.com/en/latest/map_filter.html](http://book.pythontips.com/en/latest/map_filter.html)
#### zip between 2 lists
```python
>>> A = [3, 4, 6, 7]
>>> B = [1, 3, 6, 3]
>>> zip(A, B) # Just to demonstrate
[(3, 1), (4, 3), (6, 6), (7, 3)]

# remove any empty elements from the list
inc_got = [x for x in inc_got if x]
```

#### Map
applies a function to all the items in an input_list
```python
map(function_to_apply, list_of_inputs)
```

#### Get max length of a list
```python
le = max(len(x) for x in lis)   #find out the max length     
```

### Order elements naturally
```python
import re

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    \'''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    \'''
    return [ atoi(c) for c in re.split('(\\d+)', text) ]

alist=[
    "something1",
    "something12",
    "something17",
    "something2",
    "something25",
    "something29"]

alist.sort(key=natural_keys)
print(alist)
```


## Dictionary


### Custom functions
#### invert_dict1
```python
def invert_dict(dictionary):
    inv_dictionary = {}
    for k, v in dictionary.items():
        if v in inv_dictionary:
            value_stored = inv_dictionary[v]
            if isinstance(value_stored, list):
                inv_dictionary[v] = value_stored + [k]
            else:    
                inv_dictionary[v] = [value_stored, k]
        else:
            inv_dictionary[v] = k

    return inv_dictionary
```
#### invert_dict2
```python
def invert_dict(mydict, reverse=False):
    """
    Inverts keys and values.
    Values will be sorted (provided reverse=True if the order must be reversed)
    Since values of the original dictionary may be duplicated, the value of the new dictionary is always a list  
    :param mydict: 
    :param reverse: 
    :return: 
    """
    mydict_inverted = dict()
    for v in sorted(mydict.values(), reverse=reverse):
        k = list(mydict.keys())[list(mydict.values()).index(v)]
        # if v not in mydict_inverted:
        #     mydict_inverted[v] = k
        if v not in mydict_inverted:
            mydict_inverted[v] = []

        mydict_inverted[v].append(k)

    return mydict_inverted
```


### Dictionary comprehension
* https://www.datacamp.com/community/tutorials/python-dictionary-comprehension
* http://cmdlinetips.com/2018/01/5-examples-using-dict-comprehension/

```python
### If Condition
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5} 
# Check for items greater than 2 
dict1_cond = {k:v for (k,v) in dict1.items() if v>2} 
print(dict1_cond)
> {'e': 5, 'c': 3, 'd': 4}

### Multiple If Conditions
dict1_doubleCond = {k:v for (k,v) in dict1.items() if v>2  if v%2 == 0} 
print(dict1_doubleCond)
> {'d': 4}

### Nested Dictionary Comprehension
nested_dict = {'first':{'a':1}, 'second':{'b':2}} 
float_dict = {outer_k: {float(inner_v) for (inner_k, inner_v) in outer_v.items()} for (outer_k, outer_v) in nested_dict.items()} 
print(float_dict)

> {'first': {1.0}, 'second': {2.0}}
```

### Order dictionary by key (natural order)
```python
dict1 = dict(natsort.natsorted(dict1.items()))
```

### 
```python
import collections

def nested_dict():
    return collections.defaultdict(nested_dict)

product_to_add = collections.defaultdict(nested_dict)

product_to_add['a']['b']['c'] = 2
```

## Namespace
not built-in
```python
# import Namespace
try:
    from types import SimpleNamespace as Namespace  # available from Python 3.3
except ImportError:
    class Namespace:
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)
```
**Add elements** 
```python
# import Namespace
try:
    from types import SimpleNamespace as Namespace  # available from Python 3.3
except ImportError:
    class Namespace:
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)
            
namespace_test = Namespace(a='a')

setattr(namespace_test, 'b', 'b')  # <--- add more elements

>>> namespace_test
namespace(b='b', c='c')
```

## Versions
versions can be handled with version module
```python
>>> from packaging import version
>>> version.parse("2.3.1") < version.parse("10.1.2")
True
```

## Files
### Join Paths
```python
[os.path.join(path1[, path2[, ...]])]
```
Joins one or more path components intelligently.

strings shouldn't start with a slash. If they start with a slash, then they're considered an "absolute path" and everything before them is discarded.

### Iterate directory content (os.walk)
```python
os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])
```

**Parameters**

-   **top**  − Each directory rooted at directory, yields 3-tuples, i.e., (dirpath, dirnames, filenames)
    
-   **topdown**  − If optional argument topdown is True or not specified, directories are scanned from top-down. If topdown is set to False, directories are scanned from bottom-up.
    
-   **onerror**  − This can show error to continue with the walk, or raise the exception to abort the walk.
    
-   **followlinks**  − This visits directories pointed to by symlinks, if set to true.

```python
# !/usr/bin/python3
import os

os.chdir("d:\\\\tmp")
for root, dirs, files in os.walk(".", topdown = False):
   for name in files:
      print(os.path.join(root, name))
   for name in dirs:
      print(os.path.join(root, name))
```



### Check permissions
```python
>>> import os 
>>> os.access('my_folder', os.R_OK)  # Check for read access  
True  
>>> os.access('my_folder', os.W_OK)  # Check for write access  
True  
>>> os.access('my_folder', os.X_OK)  # Check for execution access  
True  
>>> os.access('my_folder', os.X_OK | ox.W_OK)  # Check if we can write file to the directory  
True
```


```python
import os

def all_files_under(path):
    """Iterates through all files that are under the given path."""
    for cur_path, dirnames, filenames in os.walk(path):
        for filename in filenames:
            yield os.path.join(cur_path, filename)

latest_file = max(all_files_under('root'), key=os.path.getmtime)
```

### Order files by size
```python
def sort_files_by_size(files, reverse_order=True):
    # Loop and add files to list.
    pairs = []
    for file in files:
        # Use join to get full file path.
        location = os.path.abspath(file)

        # Get size and add to list of tuples.
        size = os.path.getsize(location)
        pairs.append((size, file))

    # Sort list of tuples by the first element, size.
    pairs.sort(key=lambda s: s[0], reverse=reverse_order)

    return [x[1] for x in pairs]
```

### Get last modified time for a file
* https://thispointer.com/python-get-last-modification-date-time-of-a-file-os-stat-os-path-getmtime/

```python
modTimesinceEpoc  =  os.path.getmtime(filePath)
modificationTime  =  datetime.datetime.utcfromtimestamp(modTimesinceEpoc).strftime('%Y-%m-%d %H:%M:%S')
print("Last Modified Time : ",  modificationTime  ,  ' UTC')
```


```python
import os
import datetime
def modification_date(filename):
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t)
```

### Get creation datetime for a file
```python
import os
import platform

def creation_date(path_to_file):
    """
    Try to get the date that a file was created, falling back to when it was
    last modified if that isn't possible.
    See http://stackoverflow.com/a/39501288/1709587 for explanation.
    """
    if platform.system() == 'Windows':
        return os.path.getctime(path_to_file)
    else:
        stat = os.stat(path_to_file)
        try:
            return stat.st_birthtime
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            return stat.st_mtime
```

### Get io.reader from bytes

```python
import io

file_reader = io.BytesIO(file_bytes)
```


## Add custom method to built-in type
```python
class string(str):
    def sayHello(self):
        print(self, "is saying 'hello'")
```

Test:

```python
>>> x = string("test")
>>> x
'test'
>>> x.sayHello()
test is saying 'hello'
```

You could also overwrite the str-type with  `class str(str):`, but that doesn't mean you can use the literal  `"test"`, because it is linking to the builtin  `str`.

```python
>>> x = "hello"
>>> x.sayHello()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    x.sayHello()
AttributeError: 'str' object has no attribute 'sayHello'
>>> x = str("hello")
>>> x.sayHello()
hello is saying 'hello'
```

### create directory
* `os.mkdir` : creates a specific folder
* `os.makedirs` : creates the tree



## FTP
* install pyftpdlib
**Reference**
* https://media.readthedocs.org/pdf/pyftpdlib/latest/pyftpdlib.pdf
* https://pyftpdlib.readthedocs.io/en/latest/api.html

```python
import os
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

cwd = os.getcwd()

authorizer = DummyAuthorizer()
authorizer.add_user("dario", "12345", ".", perm="elradfmwMT")
authorizer.add_anonymous(cwd)

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(("0.0.0.0", 21), handler)
server.serve_forever()
```

**2**
```python
from pyftpdlib import servers
from pyftpdlib.handlers import FTPHandler
address = ("0.0.0.0", 21)  # listen on every IP on my machine on port 21
server = servers.FTPServer(address, FTPHandler)
server.serve_forever()
```

## Eval code from file (ast)
```python
import ast

dict = ast.literal_eval('file.txt')

```



## Work with configuration files

### configfile

```bash
pip install configfile
```

#### Read config file

```python
import configparser
config = configparser.ConfigParser()
config.read("settings.ini")
```

```python
def read_settings(file):
    # Parse configuration file
    config = configparser.ConfigParser()  # SafeConfigParser()
    config.read(file)

    # get sections
    config_sections = config.sections()

    # get OrderedDict with section : {settings} - it excludes the DEFAULT section
    settings_dict = config._sections
    #settings_dict.update(config["DEFAULT"])

    default_key = "DEFAULT"
    section_list = [x[0] for x in config.items()]
    if default_key in section_list:
        settings_dict.update(OrderedDict([(default_key, OrderedDict(config[default_key]))]))
        settings_dict.move_to_end(default_key, last=False)  # move DEFAULT key at beginning

    unique_settings = {}
    for section in config_sections:
        unique_settings.update(dict(config[section]))

    return settings_dict, unique_settings
```



#### Write config file

```python
import configparser

config = configparser.RawConfigParser()

# Please note that using RawConfigParser's set functions, you can assign
# non-string values to keys internally, but will receive an error when
# attempting to write to a file or when you get it in non-raw mode. Setting
# values using the mapping protocol or ConfigParser's set() does not allow
# such assignments to take place.
config.add_section('Section1')
config.set('Section1', 'an_int', '15')
config.set('Section1', 'a_bool', 'true')
config.set('Section1', 'a_float', '3.1415')
config.set('Section1', 'baz', 'fun')
config.set('Section1', 'bar', 'Python')
config.set('Section1', 'foo', '%(bar)s is %(baz)s!')

# Writing our configuration file to 'example.cfg'
with open('example.cfg', 'w') as configfile:
    config.write(configfile)
```





## Database Connections

### SQLlite3
```python
import sqlite3
conn = sqlite3.connect('omega.anag.db')
c = conn.cursor()
t = ('RHAT',)
c.execute('SELECT * FROM PLU')
#print(c.fetchall())
scrivi_risultato = open('risultato.txt', 'w')
for lines in c.fetchall():
    scrivi_risultato.write(';'.join(str(line) for line in lines))
    scrivi_risultato.write('\\n')
scrivi_risultato.close()
```

#### Init
```python
import sqlite3

conn = sqlite3.connect('<db file>')
cur = conn.cursor()
```

### Get
```python
cur.execute(‘Select * FROM ...’)
```

```python
all = cur.fetchall()  # get all rows selected in list of tuples (each tuple is a record)
```

```python
first = cur.fetchone()  # get the next record (tuple)
```

### Coursera course example
![](https://lh5.googleusercontent.com/6Sri-9oC51EQSf1E0juPp2N67t5ZCU_J1cvRbOqRFsiWfR1h7ybvIQbk73SZUnWK2GDJPZ4EK6KPDtBzLgQ4J62eRicLPn_2NPsGnuxe6Gjtobd0jP-COIUNBzUjfSE8n1bMfBuf)

![](https://lh4.googleusercontent.com/S2tkCeUXs7HwUHeOy-6J9b96U6DKRIVo4v0Hfb0Mqht4wzpTem47GSNtTFdzKCj7fHyHymJTvhNcAgw6D8Z7yLL4W84tN74L2RYfs5PKmfPZW901fIsYBRU6p_oPu4pL8L1av4ui)


```python
import sqlite3

  

conn = sqlite3.connect('trackdb.sqlite')

cur = conn.cursor()

  

# cursor.execute(‘’) executes the query passed as argument

# cursor.execute(‘’’ ‘’’) executes more queries separated by semicolon, passed as argument

  

cur.executescript(\'''

DROP TABLE IF EXISTS Artist;

  

CREATE TABLE Artist (

id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,

name TEXT UNIQUE

);

\''') # 1. Remove the table if exists - 2. Create the table

  

cur.execute(\'''INSERT OR IGNORE INTO Artist (name)

VALUES ( ? )\''', ( artist, ) ) # if the artist is not already in the table (INSERT OR IGNORE INTO), it will be added

cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, )) # get artist id

  

# cursor.fetchone() returns the next record (tuple)

# cursor.fetchall() returns a list of tuples (each tuple is a record)

artist_id = cur.fetchone()[0] # assign the first column got to a variable

  

# connection.commit() commits the current transaction. If you don.t call this method, anything you did since the last call to commit() is not visible from other database connections.  
  
# connection.rollback() rolls back any changes to the database since the last call to commit().

conn.commit()
```


## XML
eXtensible Markup Language is a markup language that defines a set of rules for encoding documents in a format that is both human-readable and machine-readable.
```python
<?xml version="1.0" encoding="UTF-8"?>
<!-- This is a comment -->
<users>
	<user age="16">
    	<name>Luca</name>
    	<surname>Cicci</surname>
    	<address>Milano</address>
	</user>
	<user age="54">
    	<name>Max</name>
 	   <surname>Rossi</surname>
    	<address>Roma</address>
	</user>
</users>
```


### Structure
-   Each tag is a Node (also called element)
  
-   Users: root tag
    
-   User: child node of Users
    
-   Name / surname / address : child nodes of user
    
-   Age: attribute
    
-   Luca / Cicci / Milano : node text content

<br>
Special characters must be replaced with xml entities:

| **Char** | **Entity** |
| -------- | ---------- |
| &        | &amp;      |
| <        | &lt;       |
| >        | &gt;       |
| "        | &quot;     |
| '        | &apos;     |


### LXML
* Fastest library for parsing xml files

**Reference:** [https://www.tutorialspoint.com/the-elementtree-xml-api-in-python](https://www.tutorialspoint.com/the-elementtree-xml-api-in-python)

```python
from lxml import etree
tree = etree.parse(xmspfile)  
root = tree.getroot()  
  
module_node = root.getchildren()[0]  
module_name = module_node.attrib['name']

for message_tag in module_node.getchildren():
    # get node's attribute
    check_name = message_tag.attrib['name']
    
    # get node by tag name
    sa_message_tag = message_tag.find('number')

    # get node by node text
    sa_message = sa_message_tag.text

	# get node string
	message_tag_string = etree.tostring(message_tag)  # decode('utf-8')
```

```python
from lxml import etree
root = etree.parse("fruits.xml").getroot()

item = root.find("item")
etree.dump(item)
```

```python
from lxml import etree
tree = etree.parse(xmspfile)  
root = tree.getroot()  
  
module_node = root.getchildren()[0]  
module_name = module_node.attrib['name']

for message_tag in module_node.getchildren():  
    check_name = message_tag.attrib['name']
    sa_message = message_tag.find('number').text
```

#### Get Parent node

The standard `xml.etree.ElementTree` lacks any decent method of selecting the parent node. We can work around this limitation by constructing a child-to-parent map for the entire tree

```python
parent_map = {c:p for p in root.iter() for c in p}
```

```python
import xml.etree.ElementTree as ET

root = ET.parse('yourfile.xml')

# https://stackoverflow.com/a/20132342/18771
parent_map = {c:p for p in root.iter() for c in p}

for child in root.iterfind('targetElement'):
    if(len(child.attrib) < 1 and len(child) < 1):
        parent_map[child].remove(child)
```

### Minidom
```python
from  xml.dom import  minidom
```

#### Parse
```python
# read xml file
doc = minidom.parse(xml_file)

# Get "Nodes" By Tag  --> list of objects
messages = doc.getElementsByTagName("message")

# Get "Node TagName"
Node.tagName

# print "Node attribute"
message_number = message.attributes['id'].value

## get "attribute info"
# keys
node.attributes.keys()
# values
node.attributes.values()
# items
node.attributes.items()

# get "parent Node"
rule_subgroup_node = message.parentNode

# get "Node text"
rule_subgroup_text_element[0].childNodes[0].data

# print any node as xml format
print(node.toxml())

# parse all children of a node
for component_tag in component_enabled_acf[0].childNodes:
   if component_tag.nodeType != component_tag.TEXT_NODE:
       print(component_tag.toxml())
```


#### Quick Parse
```python
node = Node(minidom.parse(os.path.join(project_dir, "prqaproject.xml")).documentElement)
node.child("configuration").child("rcf").attribute("name")
```

#### Get all children nodes
```python
node = Node(minidom.parse(os.path.join(options.prqa_project, "prqaproject.xml")).documentElement)
config_nodes = node.child("configurations").children("config")
    for conf_node in config_nodes:
        if conf_node.attribute("name") == options.prqaf_prj_configuration:
            return conf_node.child("messages").attribute("name")
```

### Get xml declaration
```	python
# read rcf file for  XML Declaration
read_xml_Declaration = open(rcf_input, 'r')
read_xml_Declaration_content = read_xml_Declaration.readlines()
read_xml_Declaration.close()

xml_Declaration = ''
for xml_line in read_xml_Declaration_content:
   xml_line = re.sub(r'\\s$', '', xml_line)
   if xml_line != '':
       xml_Declaration = read_xml_Declaration_content[0]
       break
```

### ElementTree module



#### parse rcf file
```python
tree = ElementTree.parse(args.xml_file)
root = tree.getroot()

rulegroup_tag = root.getchildren()[0]
category_nodes = rulegroup_tag.getchildren()

for cat_node in category_nodes:
    cat = cat_node.find('text').text

    if cat not in CM__dict:
        CM__dict[cat] = []  # init category in CM__dict

    print(cat)

    classification_nodes = cat_node.find('enforcement').findall('rule')

    for class_node in classification_nodes:
        rules_nodes = class_node.find('enforcement').findall('rule')
        for rule_node in rules_nodes:
            rulename = rule_node.attrib['id']
            rulename = rulename.replace('ule', '').replace('ir', '')  # turn "Rule-" in "R-"
            CM__dict[cat].append(rulename)
            rule_cat__dict[rulename] = cat

            print('{}{}'.format(indent, rulename))
```

### Write
* Elements must be created from the document      object (new_message_xml - considering the example below)
* Elements must be added in append to the parent      tag 

```python
#### create new message.xml file
new_message_xml = minidom.Document()

# user_messages TAG
user_messages_tag = new_message_xml.createElement('user_messages')
new_message_xml.appendChild(user_messages_tag)
```
**xml output**
```xml
<user_messages/>
```

```python
# messages TAG
messages_tag = new_message_xml.createElement('messages')
user_messages_tag.appendChild(messages_tag)
user_messages_tag.setAttribute('version', '9.2.0')
user_messages_tag.setAttribute('component', 'qac')
```

**xml output**
```xml
<user_messages component="qac" version="9.2.0">
   <messages/>
</user_messages>
```

```python
# message TAG  *** to repeat
message_tag = new_message_xml.createElement('message')
messages_tag.appendChild(message_tag)
message_tag.setAttribute('help', '')
message_tag.setAttribute('id', '8500')
message_tag.setAttribute('level', 'QA_USERMESSAGE')
```

```xml
<message help="" id="8500" level="QA_USERMESSAGE"/>
```

**Put into the existing document, it will be:**
```xml
<user_messages component="qac" version="9.2.0">
   <messages>
      <message help="" id="8500" level="QA_USERMESSAGE">
      </message>
   </messages>
</user_messages>
```

```python
# text TAG  *** to repeat
text_tag = new_message_xml.createElement('text')
message_tag.appendChild(text_tag)
```

```xml
<text></text>
```

```python
# message text *** to repeat
text_node = new_message_xml.createTextNode('textnode')
text_tag.appendChild(text_node)
```

```xml
<text>textnode</text>
```

**Put into the existing document, it will be:**
```xml
<user_messages component="qac" version="9.2.0">
   <messages>
      <message help="" id="8500" level="QA_USERMESSAGE">
         <text>textnode</text>
      </message>
   </messages>
</user_messages>
```

```python
#print(new_message_xml.toxml())
print(new_message_xml.toprettyxml(indent='   ', encoding="utf-8").decode('utf-8'))
```

```xml
<?xml version="1.0" ?>
<user_messages component="qac" version="9.2.0">
   <messages>
      <message help="" id="8500" level="QA_USERMESSAGE">
         <text>textnode</text>
      </message>
   </messages>
</user_messages>
```

### untangle
* [http://docs.python-guide.org/en/latest/scenarios/xml/](http://docs.python-guide.org/en/latest/scenarios/xml/)


### xmltodict
```xml
<mydocument has="an attribute">
 <and>
   <many>elements</many>
   <many>more elements</many>
 </and>
 <plus a="complex">
   element as well
 </plus>
</mydocument>
```

**Python code:**
```python
import xmltodict

with open('path/to/file.xml') as fd:
   doc = xmltodict.parse(fd.read())
```

**and then you can access elements, attributes and values like this:**

```python
doc['mydocument']['@has'] # == u'an attribute'
doc['mydocument']['and']['many'] # == [u'elements', u'more elements']
doc['mydocument']['plus']['@a'] # == u'complex'
doc['mydocument']['plus']['#text'] # == u'element as well'
```

### xml formatter
```python
import xmlformatter

formatter = xmlformatter.Formatter(indent="1", indent_char="\\t", encoding_output="ISO-8859-1", preserve=["literal"])
# formatter = xmlformatter.Formatter(indent="2", indent_char=" ", encoding_output="UTF-8", preserve=["literal"])

formatter.format_file("/home/pa/doc.xml")

formatter.format_string(xml_content)
```

## Urls

## urllib module
* [What is the urllib module in Python 3?](https://www.educative.io/edpresso/what-is-the-urllib-module-in-python-3)

urllib has been split up in Python 3.

* The `urllib.urlencode()` function is now `urllib.parse.urlencode()`
* The `urllib.urlopen()` function is now `urllib.request.urlopen()`

```python
from urllib import request, parse
data = parse.urlencode(<your data dict>).encode()
req =  request.Request(<your url>, data=data)    # this will make the method "POST"
resp = request.urlopen(req)
```


### Decode urls

* https://www.urldecoder.io/python/

```python
import urllib.parse
encodedStr = 'Hell%C3%B6%20W%C3%B6rld%40Python'
urllib.parse.unquote(encodedStr)
```

```
'Hellö Wörld@Python'
```

```python
urllib.parse.unquote('My+name+is+Rajeev')
```

```
'My+name+is+Rajeev'
```



**URL Decoding multiple query strings at once**
If you want to decode or parse multiple query strings of type application/x-www-form-urlencoded (e.g 'name=Rajeev+Singh&phone=%2B919999999999'), then you can use parse_qs or parse_qsl functions provided by urllib.parse package.

The `parse_qs` function returns a dictionary of key-value pairs whereas the `parse_qsl` function returns a list of (key, value) tuples.

**parse_qs**
```python
import urllib.parse
queryStr = 'name=Rajeev+Singh&phone=%2B919999999999&phone=%2B628888888888'
urllib.parse.parse_qs(queryStr)
```

```
{'name': ['Rajeev Singh'], 'phone': ['+919999999999', '+628888888888']}
```


**parse_qsl**
```python
import urllib.parse
queryStr = 'name=Rajeev+Singh&phone=%2B919999999999&phone=%2B628888888888'
urllib.parse.parse_qsl(queryStr)
```

```
[('name', 'Rajeev Singh'), ('phone', '+919999999999'), ('phone', '+628888888888')]
```

### Encode urls

* https://www.urlencoder.io/python/

```python
import urllib.parse
query = 'Hellö Wörld@Python'
urllib.parse.quote(query)
```

```
'Hell%C3%B6%20W%C3%B6rld%40Python'
```


> Note that, the `quote()` function considers `/` character safe by default. That means, It doesn’t encode `/` character -
> ```python
> urllib.parse.quote('/')
> ```
>
> ```
> '/'
> ```

The `quote()` function accepts a named parameter called safe whose default value is `/`. If you want to encode `/` character as well, then you can do so by supplying an empty string in the safe parameter like this-

> ```python
> urllib.parse.quote('/', safe='')
> ```
> 
> ```
> '%2F'
> ```

**Encoding space characters to plus sign (+) using quote_plus() function**
The `quote()` function encodes space characters to `%20`. If you want to encode space characters to plus sign (`+`), then you can use another function named `quote_plus` provided by `urllib.parse` package.

```python
>>> import urllib.parse
>>> query = 'Hellö Wörld@Python'
>>> urllib.parse.quote_plus(query)
```

```
'Hell%C3%B6+W%C3%B6rld%40Python'
```


**Encoding multiple parameters at once**
You can encode multiple parameters at once using `urllib.parse.urlencode()` function. This is a convenience function which takes a dictionary of key value pairs or a sequence of two-element tuples and uses the `quote_plus()` function to encode every value. The resulting string is a series of `key=value` pairs separated by `&` character.

```python
import urllib.parse
params = {'q': 'Python URL encoding', 'as_sitesearch': 'www.urlencoder.io'}
urllib.parse.urlencode(params)
```

```
'q=Python+URL+encoding&as_sitesearch=www.urlencoder.io'
```

If you want the `urlencode()` function to use the `quote()` function for encoding parameters, then you can do so like this:

```python
urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
```


**Encoding multiple parameters at once where one parameter can have multiple values**
The `urlencode()` function takes an optional argument called `doseq`. If your input can have multiple values for a single key, then you should set the `doseq` argument to `True` so that all the values are encoded properly:

```python
>>> import urllib.parse
>>> params = {'name': 'Rajeev Singh', 'phone': ['+919999999999', '+628888888888']}
>>> urllib.parse.urlencode(params, doseq=True)
```

```
'name=Rajeev+Singh&phone=%2B919999999999&phone=%2B628888888888'
```



## JSON

### Create json
```python
import json

data['metadata'] = {}
  data['metadata']['kernelspec'] = {}
  data['metadata']['kernelspec']['display_name'] = "Python 3"
  data['metadata']['kernelspec']['language'] = "python"
  data['metadata']['kernelspec']['name'] = "python3"

result = json.dumps(data, indent=2)
```

```python
# a Python object (dict):
x = {
"name": "John",
"age": 30,
"city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
```
```
{"name": "John", "age": 30, "city": "New York"}
```

**Additional arguments**
* `sort_keys` : if `True` sorts the keys
* `indent` : set the number of spaces indentation
* `separators` : sets the pairs separators and the key-value separator. For instance: `(". ", " = ")`

### Parse json

```python
import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
```

## API


## Web Scraping

### modules installation
```bash
pip3 install lxml
pip3 install beautifulsoup4
```

### import
```python
from bs4 import BeautifulSoup
from urllib import request
```

### parse
```python
File = request.urlopen(url)
FileHtml = File.read()
File.close()
soup = BeautifulSoup(FileHtml, features="lxml")

articles_nodes = soup.find_all('a',attrs={"class": "btn"})
```

in case of message `urllib.error.HTTPError: HTTP Error 403: Forbidden`

```python
req = request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
File = request.urlopen(req)
FileHtml = File.read()
File.close()
soup = BeautifulSoup(FileHtml, features="lxml")

articles_nodes = soup.find_all('a',attrs={"class": "btn"})
```

```python
try:  
    from BeautifulSoup import BeautifulSoup  
except ImportError:  
    import bs4  
    from bs4 import BeautifulSoup

with open(doc_file, 'r', encoding='utf-8', errors='ignore') as read_html:  
    html = read_html.read()  
parsed_html = BeautifulSoup(html, features="lxml")  
  
headers = parsed_html.find_all(['h1', 'h2', 'h3'])  
elements = parsed_html.find_all('div')

  
for div in elements:  
    div_contents = [x for x in div.contents if isinstance(x, bs4.element.Tag)]  
    for div_element in div_contents:  
        tag = div_element.name  
  
        div_text = div_element.text
```



## Excel

**References:**
* https://code.tutsplus.com/tutorials/how-to-read-and-write-csv-files-in-python--cms-29907
* https://realpython.com/python-csv/
* http://stackabuse.com/reading-and-writing-csv-files-in-python/
* [Use openpyxl - read and write Cell in Python - Sou-Nan-De-Gesu](https://www.soudegesu.com/en/post/python/cell-excel-with-openpyxl/)
* [Openpyxl tutorial - read, write Excel xlsx files in Python](http://zetcode.com/python/openpyxl/)

```python
import openpyxl

book = openpyxl.load_workbook('sample.xlsx')

sheet = book.active

a1 = sheet['A1']
a2 = sheet['A2']
a3 = sheet.cell(row=3, column=1)

print(a1.value)
print(a2.value) 
print(a3.value)
```

### write excel
```python
def write_spreadsheet(xls_file, record_list, overwrite=True):
    """
    
    :param xls_file: output filename
    :param record_list: [ [ 'r1f1', 'r1f2' ], [ 'r2f1', 'r2f2' ] ] 
    :param overwrite: Flag for overwriting the output file in case it exists, or appending records
    :return: 
    """
    if overwrite:
        add_record_xls_workbook = openpyxl.Workbook()
    else:
        if os.path.exists(xls_file):
            add_record_xls_workbook = openpyxl.load_workbook(xls_file)
        else:
            add_record_xls_workbook = openpyxl.Workbook()

    # grab the active worksheet
    active_sheet = add_record_xls_workbook.active

    # append row
    for row in record_list:
        active_sheet.append(row)

    # Save the file
    add_record_xls_workbook.save(xls_file)
```

### read excel
```python
wb = openpyxl.load_workbook(excel_file, data_only=True)

# get list of sheets
wbsheets = wb.sheetnames

# select worksheet
for sheet in wbsheets:
    sheet_name_adjusted = re.sub(r'\\s', '', sheet.lower())

    get_real_sheet_name[sheet_name_adjusted] = sheet  # populate "get_real_sheet_name"

for row in range(1, wbsheet.max_row + 1):
	category_cell = '{col}{row}'.format(col=col_cat, row=row)
    amount_cell = '{col}{row}'.format(col=col_amount, row=row)
    incoming_cell = '{col}{row}'.format(col=col_incoming, row=row)

    category_content = wbsheet[category_cell].value









CM_excel_sheets = ['AUTOSAR', 'MISRA']  #['AUTOSAR', 'MISRA']

for sheet in CM_excel_sheets:
    cm_excel_sheet = wb.get_sheet_by_name(sheet)

    for row in range(1, cm_excel_sheet.max_row):
        for col in range(1, cm_excel_sheet.max_column):
            col_n = col
            col = openpyxl.utils.get_column_letter(col)
            cell = '{col}{row}'.format(col=col, row=row)
            first_cell_content = cm_excel_sheet[cell].value
            #print(cell)
            if first_cell_content == 'None' or first_cell_content is None or type(first_cell_content) == 'NoneType':
                first_cell_content = '   '
```

### Append excel
```python
def logToxls(xls_file, record_list):
    # info_xls_list.append(info_dict['user_info'], info_dict['Deal_info'], info_dict['Customer_info'], info_dict['user_info'])  # add info from dict
    #info_xls_list.append(list(table.objects.filter(id=record_id).values_list('annsource', flat=True)))  # add info from db

    if os.path.exists(xls_file):
        add_record_xls_workbook = openpyxl.load_workbook(xls_file)
    else:
        add_record_xls_workbook = openpyxl.Workbook()

    # grab the active worksheet
    active_sheet = add_record_xls_workbook.active

    # append row
    active_sheet.append(record_list)

    # get next row available
    row = active_sheet.max_row

    # center columns
    columns_to_center = [4, 5, 6, 7, 8, 9, 10, 11]
    for col in columns_to_center:
        cell_obj = active_sheet.cell(row, col)
        cell_obj.alignment = Alignment(horizontal='center')

    # Save the file
    try:
        add_record_xls_workbook.save(xls_file)
    except:
        print('{}Error writing on file "{}". \\nRecord: "{}"{}'.format(Fore.RED + Style.BRIGHT, xls_file, record_list, Style.RESET_ALL))
        error_file = os.path.splitext(xls_file)[0] + '.txt'
        write_errors = open(error_file, 'a', encoding='utf-8', errors='ignore')# as write_errors:
        write_errors.write(', '.join([str(x) for x in record_list]) + '\\n')
        return

    print("Record %s saved to xls %s" %(record_list[0], xls_file))
```

### Stet style
```python
from openpyxl.styles import Alignment

currentCell = ws.cell('A1') #or currentCell = ws['A1']
currentCell.alignment = Alignment(horizontal='center')
```

## Google Spreadsheet
```python
def logToGspreadsheet(aka_id, record_list):
    json_secret_filepath = os.path.join(django_project_path, 'log', 'client_secret.json')
    scope = "https://spreadsheets.google.com/feeds"
    creds = ServiceAccountCredentials.from_json_keyfile_name(json_secret_filepath, scope)
    client = gspread.authorize(creds)

    gsheet = client.open_by_key(aka_id)  # open spreadsheet
    wsheet = gsheet.get_worksheet(0)  # Select a specific Sheet

    # append row after last filled
    def append_row_content(worksheet, value_list):
        if not isinstance(value_list, list):
            raise TypeError('"value_list" must be a list')

        # get number of lines used
        #record_row = len(worksheet.get_all_records()) + 2  # +2 because the first is not returned in the count, since is used by the header

        # detect first row available (check only first cell of the column)
        #record_row = len([x for x in worksheet.col_values(1) if not x.strip(' ') == '']) +  1 # +1 for selecting the next row
        record_row = get_first_row_spreadsheet(worksheet.col_values(1)) + 1
        #print(record_row)

        col = 0
        try:
            for v in value_list:
                col += 1
                worksheet.update_cell(record_row, col, v)
        except:
            worksheet.append_row(value_list)

    append_row_content(wsheet, record_list)
    #wsheet.append_row(record_list)

    print("Record %s saved to GoogleSpreadsheet" % record_list[0] )
```



## date - time
### Reference
* [https://www.programiz.com/python-programming/datetime/strftime](https://www.programiz.com/python-programming/datetime/strftime)
* https://pymotw.com/2/datetime/
* https://www.pythonforbeginners.com/basics/python-datetime-time-examples
* https://www.saltycrane.com/blog/2008/06/how-to-get-current-date-and-time-in/
* https://www.cyberciti.biz/faq/howto-get-current-date-time-in-python/
* https://www.guru99.com/date-time-and-datetime-classes-in-python.html
* https://www.idiotinside.com/2015/03/14/working-with-date-and-time-python-892/
* http://www.marinamele.com/2014/03/13-useful-tips-about-python-datetime.html


### import datetime
```python
import datetime
```
### Date Objects
```python
>>> x = datetime.datetime(2020, 5, 17)
2020-05-17 00:00:00
```

### current timestamp
```python
>>> datetime.datetime.now()
2018-07-25 15:12:59.187779

>>> print(x.year)
2018
>>> print(x.strftime("%A"))
Monday
```

```python
print("Current date and time using str method of datetime object:")
print(str(now))

print("Current date and time using instance attributes:")
print("Current year: %d" % now.year)
print("Current month: %d" % now.month)
print("Current day: %d" % now.day)
print("Current hour: %d" % now.hour)
print("Current minute: %d" % now.minute)
print("Current second: %d" % now.second)
print("Current microsecond: %d" % now.microsecond)

print("Current date and time using strftime:")
print(now.strftime("%Y-%m-%d %H:%M"))

print("Current date and time using isoformat:")
print(now.isoformat())
```

output:
```
Current date and time using str method of datetime object:
2014-09-26 16:34:40.278298

Current date and time using instance attributes:
Current year: 2014
Current month: 9
Current day: 26
Current hour: 16
Current minute: 34
Current second: 40
Current microsecond: 278298

Current date and time using strftime:
2014-09-26 16:34

Current date and time using isoformat:
2014-09-26T16:34:40.278298
```




#### strftime format 
| %a   | Weekday, short version                                      | Wed                      |
| ---- | ----------------------------------------------------------- | ------------------------ |
| %A   | Weekday, full version                                       | Wednesday                |
| %w   | Weekday as a number 0-6, 0 is Sunday                        | 3                        |
| %d   | Day of month 01-31                                          | 31                       |
| %b   | Month name, short version                                   | Dec                      |
| %B   | Month name, full version                                    | December                 |
| %m   | Month as a number 01-12                                     | 12                       |
| %y   | Year, short version, without century                        | 18                       |
| %Y   | Year, full version                                          | 2018                     |
| %H   | Hour 00-23                                                  | 17                       |
| %I   | Hour 00-12                                                  | 05                       |
| %p   | AM/PM                                                       | PM                       |
| %M   | Minute 00-59                                                | 41                       |
| %S   | Second 00-59                                                | 08                       |
| %f   | Microsecond 000000-999999                                   | 548513                   |
| %z   | UTC offset                                                  | +0100                    |
| %Z   | Timezone                                                    | CST                      |
| %j   | Day number of year 001-366                                  | 365                      |
| %U   | Week number of year, Sunday as the first day of week, 00-53 | 52                       |
| %W   | Week number of year, Monday as the first day of week, 00-53 | 52                       |
| %c   | Local version of date and time                              | Mon Dec 31 17:41:00 2018 |
| %x   | Local version of date                                       | 12/31/18                 |
| %X   | Local version of time                                       | 17:41:00                 |
| %%   | A % character                                               | %                        |


### Timezone
```python
from datetime import datetime
from pytz import timezone

fmt = "%Y-%m-%d %H:%M:%S %Z%z"

# Current time in UTC
now_utc = datetime.now(timezone('UTC'))
print(now_utc.strftime(fmt))

# Convert to US/Pacific time zone
now_pacific = now_utc.astimezone(timezone('US/Pacific'))
print(now_pacific.strftime(fmt))

# Convert to Europe/Berlin time zone
now_berlin = now_pacific.astimezone(timezone('Europe/Berlin'))
print(now_berlin.strftime(fmt))
```
output

```
2018-07-30 06:44:48 UTC+0000
2018-07-29 23:44:48 PDT-0700
2018-07-30 08:44:48 CEST+0200
```

#### Timezone list
```python
from pytz import all_timezones

print len(all_timezones)
for zone in all_timezones:
    print(zone)
```


### datetime format conversion

### time operations

### Find number of the microseconds since Epoch for given datetime
```python
from datetime import datetime, timedelta

epoch = datetime(1970, 1, 1)

def timestamp_microsecond(utc_time):
    td = utc_time - epoch
    assert td.resolution == timedelta(microseconds=1)
    return (td.days * 86400 + td.seconds) * 10**6 + td.microseconds

print(timestamp_microsecond(utc_time))
# -> 1394004146976637

utc_time = epoch + timedelta(microseconds=1394004146976637)
# -> datetime.datetime(2014, 3, 5, 7, 22, 26, 976637)
```


### other
```python
>>> from datetime import datetime
>>> datetime.fromisoformat('2014-03-05 07:22:26.976637+00:00').timestamp()
1394004146.976637
```

```python
def get_filetimestamp_now():
    date_time = datetime.datetime.now()  # get datatime info
    dated_text = '%s' % (date_time.day)  # get datatime day in dated
    datem_text = '%s' % (date_time.month)  # get datatime month in datem
    datey_text = '%s' % (date_time.year)  # get datatime year in datey
    date_text = dated_text.rjust(2, '0') + '-' + datem_text.rjust(2, '0') + '-' + datey_text.rjust(4, '0')  # I adjust the date string filling the data and having dd-mm-yyyy
    time_text = date_time.strftime("%X")  # I get the time hh:mm:ss
    file_timestamp = datey_text.rjust(4, '0') + datem_text.rjust(2, '0') + dated_text.rjust(2, '0') + time_text.replace(':', '')

    return file_timestamp
```

### time
```python
a = datetime.time(0, 2, 31)
a.strftime("%X")
'00:02:31'
```

### Get epoch datetime
```python
def convert_datestr_to_epoch(date_time):
    # date_time = '29.08.2011 11:05:02'
    pattern = '%d.%m.%Y %H:%M:%S'
    h, m, s = date_time.split(':')
    s, ms = s.split('.')
    date_time = '{DD}.{MM}.{YYYY} {HH}:{mm}:{SS}'.format(DD='01', MM='01', YYYY='1970', HH=h, mm=m, SS=s)
    epoch = int(time.mktime(time.strptime(date_time, pattern)))

    return epoch

```

### Convert time to seconds
```python
def convert_datestr_to_seconds(t):
    pattern = '%H:%M:%S'
    h, m, s = t.split(':')
    if '.' in s:
        s, ms = s.split('.')
    else:
        ms = '00'
    t = '{HH}:{mm}:{SS}'.format(HH=h, mm=m, SS=s)
    x = time.strptime(t, pattern)

    return datetime.timedelta(hours=x.tm_hour, minutes=x.tm_min, seconds=x.tm_sec).total_seconds()
```
OR

```python
timestr = '00:04:23'
ftr = [3600,60,1]
sum([a*b for a,b in zip(ftr, map(int,timestr.split(':')))])
```


### Get smallest value accepte by the platform
```python
import datetime
import platform
print(
    "Running on Python ver.{} on {} {}\\n" \\
    .format(
        platform.python_version(),
        platform.system(),
        platform.release()
        )
)
for timestamp in range(1, 100000000):
    try:
        dt = datetime.datetime.fromtimestamp(timestamp)
    except:
        pass
    else:
        break
print(
    "Smallest accepted Unix timestamp by {}: '{}' ({})" \\
    .format(platform.system(), timestamp, dt)
)
```

### Get delta object from timestamp
```python
from datetime import datetime, timedelta
# we specify the input and the format...
t = datetime.strptime("05:20:25","%H:%M:%S")
# ...and use datetime's hour, min and sec properties to build a timedelta
delta = timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
```

### How to get the date N days ago in Python
```python
import datetime 
tod = datetime.datetime.now()
d = datetime.timedelta(days = 50)
a = tod - d
print(a)
2014-12-13 22:45:01.743172
```
**OR**

```python
from datetime import datetime, timedelta

N = 2
date_N_days_ago = datetime.now() - timedelta(days=N)

print datetime.now()
print date_N_days_ago
```


### File timestamp
```python
def get_file_timestamp(sep="", format_string="%Y{0}%m{0}%d{0}{0}%H{0}%M{0}%S{0}%f"):
    now = datetime.datetime.now()

    return now.strftime(format_string.format(sep))
```

## Calendar in python

1. [holidays](https://pypi.org/project/holidays/)
1. [workalendar](https://pypi.org/project/workalendar/)

### Get holidays (holidays module)

```python
# Get holidays
# holidays module
import calendar
import holidays

it_year_holidays_dict = holidays.Italy(years=[year])
it_year_holidays_list = list(it_year_holidays_dict.keys())

holidays_current_month = [x.day for x in it_year_holidays_list if x.month == month]

# get weekends current month
weeks_current_month = calendar.monthcalendar(year, month)
weekend_days_groupedby_week = [x[-2:] for x in weeks_current_month]
weekend_days_current_month = [item for sublist in weekend_days_groupedby_week for item in sublist if item != 0]
```

### Get holidays (workalendar module)

```python
# Get holidays
# workalendar module
import calendar
from workalendar.europe import Italy

it_calendar = Italy()
it_year_holidays_dict = it_calendar.holidays(year)
it_year_holidays_list = [x[0] for x in it_year_holidays_dict]

holidays_current_month = [x.day for x in it_year_holidays_list if x.month == month]

# get weekends current month
weeks_current_month = calendar.monthcalendar(year, month)
weekend_days_groupedby_week = [x[-2:] for x in weeks_current_month]
weekend_days_current_month = [item for sublist in weekend_days_groupedby_week for item in sublist if item != 0]
```


--------

## Switch in Python


```python
component_dir = []
        {
            'prqa-framework': lambda mod : component_dir.append (self.options['qaf_doc_dir']),
        }.get (self.options['module'],
               lambda mod : component_dir.append (os.path.join(self.options['ac_dir'], mod))) (self.options['module'])
```


## Virtual environment - Virtualenv


* Separation of packages installations - you can use different package sets for each project.
* Separation of python versions - you can use different python versions for each project.






### Installation


```bash
sudo pip install virtualenv
```






### New env


```shell
cd ~/code/myproject/


virtualenv <env_name>


es: virtualenv env
```


> Note: for using a specific version of python, use -p


```shell
virtualenv -p /usr/bin/python2.6 <path/to/new/virtualenv/>
```






### Activate




```shell
cd ~/code/myproject/<env_name>/Scripts
run Activate.bat
```


## Argparse : parse input argumens
### reference
* [https://pymotw.com/2/argparse/](https://pymotw.com/2/argparse/)
* [https://docs.python.org/3/library/argparse.html](https://docs.python.org/3/library/argparse.html)
* [Stack Overflow : how-can-i-pass-a-list-as-a-command-line-argument-with-argparse](https://stackoverflow.com/questions/15753701/how-can-i-pass-a-list-as-a-command-line-argument-with-argparse)

a command looks like this:
```
qacli     analyze    -P     c:\\project
   ^         ^        ^        ^
command subcommand  option   parameter 
```
each one is an argument

-   positional Argument: parameter without option (“var”, help=”helptext”)
    
-   optional Argument: parameter with option (“-op”, “--option”, dest=”var”, help=”helptext”)

Every option has some values like:

-   [dest](http://docs.python.org/library/argparse.html#dest): You will access the value of option with this variable
    
-   [help](http://docs.python.org/library/argparse.html#help): This text gets displayed whey someone uses --help. Use `help=argparse.SUPPRESS` for hiding the argument from the help  
    % character needs to be escaped using an additional %. So 100% will be 100%%
    
-   [default](http://docs.python.org/library/argparse.html#default): If the command line argument was not specified, it will get this default value.
    
-   [action](http://docs.python.org/library/argparse.html#action): Actions tell optparse what to do when it encounters an option on the command line. actiondefaults to store. These actions are available:
    
-   **store**: take the next argument (or the remainder of the current argument), ensure that it is of the correct type, and store it to your chosen destination dest.
    
-   **store_true**: store True in dest if this flag was set.
    
-   **store_false**: store False in dest if this flag was set.
    
-   **store_const**: store a constant value
    
-   **append**: append this option’s argument to a list
    
-   **count**: increment a counter by one
    
-   **callback**: call a specified function
    
-   [nargs](http://docs.python.org/library/argparse.html#nargs): ArgumentParser objects usually associate a single command-line argument with a single action to be taken. The nargs keyword argument associates a different number of command-line arguments with a single action.
	nargs='+': appends all arguments to the list
	- `N`: The absolute number of arguments (e.g., 3).
	-  `?` : 0 or 1 arguments
	- `'*'`. All command-line arguments present are gathered into a list. 0 or all arguments
	- `'+'`. All, and at least one, argument. Just like `'*'`, all command-line args present are gathered into a list. Additionally, an error message will be generated if there wasn’t at least one command-line argument present.
	- `argparse.REMAINDER`: All the remaining command-line arguments are gathered into a list. This is commonly useful for command line utilities that dispatch to other command line utilities.


-   [required](http://docs.python.org/library/argparse.html#required): Mark a command line argument as non-optional (required).
    
-   [choices](http://docs.python.org/library/argparse.html#choices): Some command-line arguments should be selected from a restricted set of values. These can be handled by passing a container object as the choices keyword argument to add_argument(). When the command line is parsed, argument values will be checked, and an error message will be displayed if the argument was not one of the acceptable values.  
    Restricts values accepted
    
- [type](http://docs.python.org/library/argparse.html#type): Use this command, if the argument is of another type (e.g. int or float).
	- `type=argparse.FileType('r')` reads the file for you
			Argparse has some built in filetypes which makes it easier to open files specified on the command line. Here’s an example reading a file, you can do the same writing a file.

		```python
		parser = argparse.ArgumentParser()
		parser.add_argument('f', type=argparse.FileType('r'))
		args = parser.parse_args()
		
		for line in args.f:
		    print( line.strip() )
		```



argparse automatically generates a help text. So if you call python myScript.py --help you will get something like that:
```
usage: Multiplication.py [-h]  [-i FILE]  
  
Matrix multiplication  
  
optional arguments:  
-h, --help show this help message and exit  
-i FILE input file with two matrices
```

to see:
-   metavar   
-   nargs ? (maybe, positional argument optional) and *
-   const
-   parser.error


### subcommands
```python
from argparse import ArgumentParser, RawTextHelpFormatter, SUPPRESS

parser = ArgumentParser(formatter_class=RawTextHelpFormatter, description="""
Compilition script Custom Component. 
If run with mode "create" it will create the 
""")

subparsers = parser.add_subparsers(help='Functions')
parser_1 = subparsers.add_parser('cmd1', help='...')
parser_2 = subparsers.add_parser('cmd2', help='...')

     
# Options
parser_1.add_argument("-debug", dest="debug", action='store_true', help=SUPPRESS, default=False)

args = parser.parse_args()

print(args)
```

### Get dict of arguments
```python
def create_options_dict(parser):
    dest_options_dict = {}

    for action in parser._actions:
        options = action.option_strings
        dest = action.dest

        dest_options_dict[dest] = '/'.join(options)

    return dest_options_dict
```

### Ignore unrecognised arguments
Replace

```python
args = parser.parse_args()
```

with

```python
args, unknown = parser.parse_known_args()
```

For example,

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--foo')
args, unknown = parser.parse_known_args(['--foo', 'BAR', 'spam'])
print(args)
# Namespace(foo='BAR')
print(unknown)
# ['spam']
```

### Template
```python
# check args
parser = ArgumentParser(formatter_class=RawTextHelpFormatter, description="""
Description
 
""")
 
# Options
parser.add_argument("-op", "--output",  # optional argument (it has a flag)
                    dest="output_path",
                    help="Output Location",
                    required=False,
                    #nargs="+",
                    #nargs='?',  # optional argument
                    #default=""
                    #type=int
                    )

parser.add_argument("source_file",  # positional argument (it does not have any flag)
                     help="source file must be analyzed")

args = parser.parse_args()  # it returns args.output_path and args.source_file

# end check args

```


## Access to windows registry
### import winreg
```python
import winreg
```

### read key value
```python
def get_reg(name):
    try:
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, winreg.KEY_READ)
        value, regtype = winreg.QueryValueEx(registry_key, name)
        winreg.CloseKey(registry_key)
        return value
    except WindowsError:
        return None
```

```python
def getRegValue(keyName, valueName):  
    reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)  
    key = winreg.OpenKey(reg, keyName)  
    value = winreg.QueryValueEx(key, valueName)  
    winreg.CloseKey(key)  
    return value[0]  
  
  
def get_reg(name):  
    try:  
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, winreg.KEY_READ)  
        value, regtype = winreg.QueryValueEx(registry_key, name)  
        winreg.CloseKey(registry_key)  
        return value  
    except WindowsError:  
        return None
```

### iterate over keys
```python
try:  
    i = 0  
    while 1:  
        name, value, type = winreg.EnumValue(key, i)  
        print(name, value, i)  
        i += 1  
except WindowsError:  
    print()
```

### iterate subdirectory
```python
parent = winreg.OpenKey(reg, r'SOFTWARE\\PRQA\\prqa-framework')

i = 0  
while True:  
    try:  
        key = winreg.EnumKey(parent, i)  
        print(key)  
        i += 1  
  except WindowsError:  
        break
```

### write key value
```python
def set_reg(name, value):
    try:
        winreg.CreateKey(winreg.HKEY_CURRENT_USER, REG_PATH)
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, winreg.KEY_WRITE)
        winreg.SetValueEx(registry_key, name, 0, winreg.REG_SZ, value)
        winreg.CloseKey(registry_key)
        return True
    except WindowsError:
        return False
```


























## Networking


### Resources:


* https://pymotw.com/2/socket/tcp.html
* https://wiki.python.org/moin/TcpCommunication
* https://docs.python.org/3/howto/sockets.html




### Client


```python
import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()


print ("received data:", data)
```


* **```socket.send```** is a low-level method and basically just the C/syscall method [send(3)](http://linux.die.net/man/3/send) / [send(2)](http://linux.die.net/man/2/send). It can send less bytes than you requested, but returns the number of bytes sent.


* **```socket.sendall```** is a high-level Python-only method that sends the entire buffer you pass or throws an exception. It does that by calling `socket.send` until everything has been sent or an error occurs.


    


    **sendall** uses under the hood **send**


    ```python
    def sendall(sock, data, flags=0):
        ret = sock.send(data, flags)
        if ret > 0:
            return sendall(sock, data[ret:], flags)
        else:
            return None
    ```

If you're using TCP with blocking sockets and don't want to be bothered by internals (this is the case for most simple network applications), use sendall.






### Server

```python
import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)  # the argument of method .listen() is the number of requests can be handled at same time


conn, addr = s.accept()
print 'Connection address:', addr
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print "received data:", data
    conn.send(data)  # echo
conn.close()
```

be handled at same time

```python
conn, addr = s.accept()
print 'Connection address:', addr
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print "received data:", data
    conn.send(data)  # echo
conn.close()
```


## Files
### Copy / Move entire directories with all content
```python
def copy_dir(root_src_dir, root_target_dir):  
    operation = 'copy' # 'copy' or 'move'  
  
  for src_dir, dirs, files in os.walk(root_src_dir):  
        dst_dir = src_dir.replace(root_src_dir, root_target_dir)  
        if not os.path.exists(dst_dir):  
            os.mkdir(dst_dir)  
        for file_ in files:  
            src_file = os.path.join(src_dir, file_)  
            dst_file = os.path.join(dst_dir, file_)  
            if os.path.exists(dst_file):  
                os.remove(dst_file)  
            if operation is 'copy':  
                shutil.copy(src_file, dst_dir)  
            elif operation is 'move':  
                shutil.move(src_file, dst_dir)
```

## Run a process

### simple

```python
def run_process(cmd):
    shell = False
    if os.sep == "\\":
        shell = True
    p = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=shell, universal_newlines=True)
    p_out, p_err = p.communicate()
    p_rc = p.returncode

    return p_rc, p_out, p_err
```

### subprocess from Python 3.7
```python
import subprocess

subprocess.run('ls')

subprocess.run(['ls', '-al'])
subprocess.run('ls -al', shell=True)

p1 = subprocess.run(['ls', '-al'])
print(p1)
# CompletedProcess(args=['ls', '-al'], returncode=0)
p1.args
# ['ls', '-al']
p1.returncode
# 0
p1.stdout
# None
# None because the output is redirected to the screen

p1 = subprocess.run(['ls', '-al'], capture_output=True)
# b'total 0\\ndrwxrwxrwx 1 dartie dartie 512 Mar  2 09:46 .\\ndrwxrwxrwx 1 dartie dartie 512 Mar  2 09:46 ..\\n'

p1 = subprocess.run(['ls', '-al'], capture_output=True, text=True)
# 'total 0\\ndrwxrwxrwx 1 dartie dartie 512 Mar  2 09:46 .\\ndrwxrwxrwx 1 dartie dartie 512 Mar  2 09:46 ..\\n'

p1 = subprocess.run(['ls', '-al', 'blabla'], stderr=subprocess.DEVNULL)
# no issues and output are raised.
```

**Arguments**
* `shell=True` = runs the command in a new shell
  * Allows to not to raise an error in case of command error (for example, `ls` on windows would fail. `shell=True` doesn't interrupt the script)
  * Allows to pass a string as command argument, rather than a list (i.e.: `ls -al` - without `shell=True` would be `['ls', '-al']`)
* `capture_output=True` = allows to redirect the output to stdout (`process.stdout`) in binary format
* `text=True` = used with `capture_output=True`, allows to redirect the output to stdout (`process.stdout`) in text format (avoids `.decode()` method)
* `stdout` = address the output. `stdout=subprocess.PIPE` redirects it to the pipe. A file object can be specified for writing to a file.
* `stderr` = address the error output. `stderr=subprocess.DEVNULL` redirects it to null, `stderr=subprocess.PIPE` redirect it to the pipe. A file object can be specified for writing to a file.
* `input` = allows to pass the input to the command

**Methods**
* `process.returncode` = get process returncode
* `process.args` = get process arguments
* `process.stdout` = get process output
* `process.stderr` = get process error output



#### Input
Having **test.txt** 
```
This
is
a test
with
7
lines
```

```python
p1 = subprocess.run(['cat', 'test.txt'], capture_output=True, text=True)
p2 = subprocess.run(['grep', '-n', 'test'], capture_output=True, text=True, input=p1.stdout)
print(p2.stdout)
# 4:test

# equivalent to
p1 = subprocess.run('cat test.txt | grep -n test', capture_output=True, text=True, shell=True)
```


### Hide console in windows
```python
def get_subprocess_flags():
    if sys.platform.startswith("win"):
        # Don't display the Windows GPF dialog if the invoked program dies.
        # See comp.os.ms-windows.programmer.win32
        #  How to suppress crash notification dialog?, Jan 14,2004 -
        #     Raymond Chen's response [1]

        import ctypes
        SEM_NOGPFAULTERRORBOX = 0x0002  # From MSDN
        ctypes.windll.kernel32.SetErrorMode(SEM_NOGPFAULTERRORBOX);
        CREATE_NO_WINDOW = 0x08000000  # From Windows API
        subprocess_flags = CREATE_NO_WINDOW
    else:
        subprocess_flags = 0

    return subprocess_flags

p = Popen(cmd, cwd=exedir, stdout=PIPE, stderr=PIPE, creationflags=subprocess_flags, shell=True)
p_out, p_err = p.communicate()
p_rc = p.returncode

p_out.decode('utf-8')
```

### Display live output
```python
def myrun(cmd):
    """
    from http://blog.kagesenshi.org/2008/02/teeing-python-subprocesspopen-output.html
    """
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout = []
    while True:
        line = p.stdout.readline()
        line = line.strip().decode('utf-8')  # strip could be replaced by a remove suffix
        stdout.append(line)
        print(line)
        if line == '' and p.poll() != None:
            break
    return '\\n'.join(stdout)
```

### function template
```python
# TODO: add ENV
def run_command(cmd):
    """
    from http://blog.kagesenshi.org/2008/02/teeing-python-subprocesspopen-output.html
    """
    p = subprocess.Popen(cmd, creationflags=subprocess_flags, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout = []
    while True:
        line = p.stdout.readline()
        line = line.strip().decode('utf-8')  # strip could be replaced by a remove suffix
        stdout.append(line)
        print(line)
        if line == '' and p.poll() != None:
            break
    return '\\n'.join(stdout)
```

## Threads
* https://www.tutorialspoint.com/python/python_multithreading.htm
* [https://timber.io/blog/multiprocessing-vs-multithreading-in-python-what-you-need-to-know/](https://timber.io/blog/multiprocessing-vs-multithreading-in-python-what-you-need-to-know/)
* [https://nyu-cds.github.io/python-concurrency/03-threads/](https://nyu-cds.github.io/python-concurrency/03-threads/)
* [https://stackoverflow.com/questions/19233246/python-update-local-variable-in-a-parallel-process-from-parent-program](https://stackoverflow.com/questions/19233246/python-update-local-variable-in-a-parallel-process-from-parent-program)
* [https://kite.com/python/examples/500/threading-use-thread-local-variables](https://kite.com/python/examples/500/threading-use-thread-local-variables)
* [Python Multithreading Tutorial: Active threads & enumerate() - 2020](https://www.bogotobogo.com/python/Multithread/python_multithreading_Enumerating_Active_threads.php)
* [Python Multithreading Tutorial: Concurrency and Parallelism \\| Toptal](https://www.toptal.com/python/beginners-guide-to-concurrency-and-parallelism-in-python)
* [threading – Manage concurrent threads - Python Module of the Week](https://pymotw.com/2/threading/)


```python
import threading

t = threading.Thread(target=download_video, args=(l,))
t.start()

for t in thread_list:
    t.join()

```

### Update same variable

```python
lock = threading.Lock()
online_hosts = {}


def ping_host(host):
  host = host.strip()

  hostname, status = ping(host)

  with lock:
      online_hosts[host] = hostname, status

  return status


def main():
  ip_list = []

  thread_list = []
  for ip in ip_list:
      t = threading.Thread(target=ping_host, args=(ip,))
      thread_list.append(t)
      t.start()

  for t in thread_list:
      t.join()  # wait all threads to be completed
```

### Modify objects with Queue
```python
import queue
from threading import Thread


def foo(bar):
  print('hello {0}'.format(bar))
  return bar


que = queue.Queue()
threads_list = list()

strings = ['a', 'b', 'c', 'd']

for s in strings:
  t = Thread(target=lambda q, arg1: q.put(foo(arg1)), args=(que, s))
  t.start()
  threads_list.append(t)

# Join all the threads
for t in threads_list:
  t.join()

# Check thread's return value
while not que.empty():
  result = que.get()
  print(result)
```

## OpenCV
### Installation
1. Download packages for windows here:
2. Install them
	```bash
	pip install numpy-1.15.2+mkl-cp36-cp36m-win_amd64.whl & pip install opencv_python-3.4.3-cp36-cp36m-win_amd64.whl
	```
1. 


## Face recognition
### Installation
#### Unix
1. Install `face_recognition` module
    ```bash
    pip3 install face_recognition
    ```
> In case of error `ImportError: bad magic number in 'face_recognition': b'\\x03\\xf3\\r\\n'`:
    ```bash
    find . -name \\*.pyc -delete
    ```

### Run
* `fr.py`
```python
# import the libraries
import os
import face_recognition

# make a list of all the available images
images = os.listdir('images')

# load your image
image_to_be_matched = face_recognition.load_image_file('my_image.jpg')

# encoded the loaded image into a feature vector
image_to_be_matched_encoded = face_recognition.face_encodings(
    image_to_be_matched)[0]

# iterate over each image
for image in images:
    # load the image
    current_image = face_recognition.load_image_file("images/" + image)
    # encode the loaded image into a feature vector
    current_image_encoded = face_recognition.face_encodings(current_image)[0]
    # match your image with the image and check if it matches
    result = face_recognition.compare_faces(
        [image_to_be_matched_encoded], current_image_encoded)
    # check if it was a match
    if result[0] == True:
        print ("Matched: " + image)
    else:
        print ("Not matched: " + image)
```

```
-   fr.py
-   my_image.jpg
-   images/
    -   barack_obama.jpg
    -   bill_gates.jpg
    -   jeff_bezos.jpg
    -   mark_zuckerberg.jpg
    -   ray_dalio.jpg
    -   shah_rukh_khan.jpg
    -   warren_buffett.jpg
```

where `my_image.jpg` is the image to check.


## PDF Forms
* `ReportLab` installation `pip install reportlab`
* import 
```python
from reportlab.pdfgen import canvas  
from reportlab.pdfbase import pdfform  
from reportlab.lib.colors import magenta, pink, blue, green, lightyellow  
from reportlab.pdfbase import pdfmetrics  
from reportlab.pdfbase.ttfonts import TTFont  
from reportlab.lib.utils import ImageReader
```
### Draw Canvas
```python
c = canvas.Canvas('simple_form.pdf')
c.setFont("Courier", 20)
c.drawCentredString(300, 700, 'Employment Form')  
c.setFont("Courier", 14)  
form = c.acroForm
```

### Set Font
```python
c.setFont("Courier", 20)
```

#### Include custom font
```python
  
TTFSearchPath = (  
            'c:/winnt/fonts',  
            'c:/windows/fonts',  
            '/usr/lib/X11/fonts/TrueType/',  
            '/usr/share/fonts/truetype',  
            '/usr/share/fonts',             #Linux, Fedora  
		    '/usr/share/fonts/dejavu',      #Linux, Fedora  
            '%(REPORTLAB_DIR)s/fonts',      #special  
            '%(REPORTLAB_DIR)s/../fonts',   #special  
            '%(REPORTLAB_DIR)s/../../fonts',#special  
            '%(CWD)s/fonts',                #special  
            '~/fonts',  
            '~/.fonts',  
            '%(XDG_DATA_HOME)s/fonts',  
            '~/.local/share/fonts',  
            #mac os X - from  
			#http://developer.apple.com/technotes/tn/tn2024.html  '~/Library/Fonts',  
            '/Library/Fonts',  
            '/Network/Library/Fonts',  
            '/System/Library/Fonts',  
            )  
  
pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))  
pdfmetrics.registerFont(TTFont('VeraBd', 'VeraBd.ttf'))  
pdfmetrics.registerFont(TTFont('VeraIt', 'VeraIt.ttf'))  
pdfmetrics.registerFont(TTFont('VeraBI', 'VeraBI.ttf'))
```

### Textbox
```python
c.drawString(x, y, 'TEXT')
```


### listbox
```python
c.drawString(10, 650, 'Choose a letter:')  
options = [('A', 'Av'), 'B', ('C', 'Cv'), ('D', 'Dv'), 'E', ('F',), ('G', 'Gv')]  
form.listbox(name='listbox1', value='A',  
             x=165, y=590, width=72, height=72,  
             borderColor=magenta, fillColor=pink,  
             textColor=blue, forceBorder=True, options=options,  
             fieldFlags='multiSelect')
```

### radio button
```python
c.setFont("Courier", 16)  
c.drawString(10, 680, 'Fruits:')  
c.setFont("Courier", 12)  
c.drawString(10, 650, 'Apple:')  
form.radio(name='group1', tooltip='Apple',  
           value='apple', selected=False,  
           x=110, y=650, buttonStyle='check',  
           borderStyle='solid', shape='square',  
           borderColor=blue, fillColor=magenta,  
           textColor=blue, forceBorder=True)  
  
c.drawString(10, 600, 'Banana:')  
form.radio(name='group1', tooltip='Banana',  
           value='banana', selected=False,  
           x=110, y=600, buttonStyle='check',  
           borderStyle='solid', shape='square',  
           borderColor=blue, fillColor=yellow,  
           textColor=blue, forceBorder=True)
```

### choice (dropdown menu)
```python
c.drawString(10, 650, 'Choose a letter:')  
options = [('A', 'Av'), 'B', ('C', 'Cv'), ('D', 'Dv'), 'E', ('F',), ('G', 'Gv')]  
form.choice(name='choice1', tooltip='Field choice1',  
            value='A',  
            x=165, y=645, width=72, height=20,  
            borderColor=magenta, fillColor=pink,  
            textColor=blue, forceBorder=True, options=options)
```


### Canvas Template
```python
from reportlab.pdfgen import canvas  
from reportlab.pdfbase import pdfform  
from reportlab.lib.colors import magenta, pink, blue, green, lightyellow  
from reportlab.pdfbase import pdfmetrics  
from reportlab.pdfbase.ttfonts import TTFont  
from reportlab.lib.utils import ImageReader  
  
TTFSearchPath = (  
            'c:/winnt/fonts',  
            'c:/windows/fonts',  
            '/usr/lib/X11/fonts/TrueType/',  
            '/usr/share/fonts/truetype',  
            '/usr/share/fonts',             #Linux, Fedora  
  '/usr/share/fonts/dejavu',      #Linux, Fedora  
  '%(REPORTLAB_DIR)s/fonts',      #special  
  '%(REPORTLAB_DIR)s/../fonts',   #special  
  '%(REPORTLAB_DIR)s/../../fonts',#special  
  '%(CWD)s/fonts',                #special  
  '~/fonts',  
            '~/.fonts',  
            '%(XDG_DATA_HOME)s/fonts',  
            '~/.local/share/fonts',  
            #mac os X - from  
 #http://developer.apple.com/technotes/tn/tn2024.html  '~/Library/Fonts',  
            '/Library/Fonts',  
            '/Network/Library/Fonts',  
            '/System/Library/Fonts',  
            )  
  
pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))  
pdfmetrics.registerFont(TTFont('VeraBd', 'VeraBd.ttf'))  
pdfmetrics.registerFont(TTFont('VeraIt', 'VeraIt.ttf'))  
pdfmetrics.registerFont(TTFont('VeraBI', 'VeraBI.ttf'))

c = canvas.Canvas('Helix QAC License Request.pdf')  
  
#  
# LOGO  
#  
logo = ImageReader('logo.png')  
# c.drawImage(logo, 13, 670, mask='auto', preserveAspectRatio=True)  # 1  
c.drawImage(logo, 20, 785, mask='auto', preserveAspectRatio=True, width=200)  # 2  
  
c.setFont("Vera", 20)  
# c.drawCentredString(300, 800, 'Perforce - Helix QAC License Request')  
c.drawCentredString(410, 800, 'Helix QAC License Request')  
c.setFont("Vera", 14)  
form = c.acroForm

c.save()
```

### Parse Pdf form
```python
from PyPDF2 import PdfFileReader

def fields_extractor(path):  
    with open(path, 'rb') as f:  
        pdf = PdfFileReader(f)  
        return pdf.getFields()

pdf_file = 'Helix QAC License Request.pdf'
fields = fields_extractor(pdf_file )  
  
for f in fields:  
    v = fields[f]['/V']  
    print('{} : {}'.format(f, v))  
print('Done')        
```

### Inject javascript in PDF
```python
import PyPDF2

def extract(input_pdf, output_pdf, javascript_to_inject, page):
    # creating a pdf file object
    pdfFileObj = open(input_pdf, 'rb')

    # creating a pdf reader object
    # pdf_reader = PyPDF2.PdfFileReader(input_pdf)
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    pdf_writer = PyPDF2.PdfFileWriter()
    pdf_page = pdfReader.getPage(page - 1)
    pdf_writer.addPage(pdf_page)
    # pdf_writer.addJS('app.alert("Startup");')
    # pdf_writer.addJS('this.print({bUI:true,bSilent:false,bShrinkToFit:true});')
    pdf_writer.addJS(javascript_to_inject)
    with open(output_pdf, 'wb') as f:
        pdf_writer.write(f)


javascript = """var f = this.getField("notes"); 
f.value = util.printd("dd/mm/yyyy", new Date());
"""
input = 'Helix QAC License Request.pdf'
output = 'b.pdf'
extract(input, output, javascript, 1)
```

## Desktop GUI

### Pyside2
porting of Qt5 to python
**Reference**
* [https://wiki.qt.io/Qt_for_Python_UiFiles](https://wiki.qt.io/Qt_for_Python_UiFiles)



#### Install Qt5 Designer
* **Windows**
* **Linux**
	```bash
	sudo apt-get install qttools5-dev-tools  # install Qt5 designer
	```

#### Import the GUI in python
1. Convert `.ui` file to `.py`

```bash
pyside2-uic mainwindow.ui > ui_mainwindow.py # convert Qt5 designer file to python
```

or import it directly in python


```python
# File: main.py
import sys
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QFile

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ui_file = QFile("mainwindow.ui")
    ui_file.open(QFile.ReadOnly)

    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()
    window.show()

    sys.exit(app.exec_())
```


#### WebBrowser object
```python
from PySide2.QtCore import QUrl
from PySide2.QtGui import QDesktopServices
from PySide2.QtWidgets import QApplication
from PySide2.QtWebEngineWidgets import QWebEngineView, QWebEnginePage


class WebEnginePage(QWebEnginePage):
    def acceptNavigationRequest(self, url,  _type, isMainFrame):
        if _type == QWebEnginePage.NavigationTypeLinkClicked:
            QDesktopServices.openUrl(url);
            return False
        return True

class HtmlView(QWebEngineView):
    def __init__(self, *args, **kwargs):
        QWebEngineView.__init__(self, *args, **kwargs)
        self.setPage(WebEnginePage(self))

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    w = HtmlView()
    w.load(QUrl("https://stackoverflow.com/questions/47736408/pyside2-qwebview-how-to-open-links-in-system-browser"));
    w.show()
    sys.exit(app.exec_())

```

### PyQt5

#### Installation

* **Linux**
	```bash
	pip3 install pyqt5
	sudo apt-get install pyqt5-dev-tools
	```

#### Start
```bash
/usr/lib/x86_64-linux-gnu/qt5/bin/designer
```

File --> New --> Qt --> Qt Designer Form

#### Convert .ui → .py
```bash
pyuic5 -o window1.py window1.ui
```

#### Set an icon for the window (it works with pyinstaller)
* https://stackoverflow.com/questions/11534293/pyinstaller-wont-load-the-pyqts-images-to-the-gui 

1. Create the .spec file with the following command:
    ```bash
    python Makespec.py --noconsole --icon="youricon.ico" --name="App name" program.py
    ```


1. Open the .spec file (eg.: `App name/App name.spec`) and you should see something like this:


1. before a.binaries you should add this piece of code:
    ```python
    Tree('C:\\\\Your\\\\App\\\\Path\\\\To\\\\Images'),
    ```

1. create the .qrc file, which will load our images. And this file should look something like this:

    ```xml
	<RCC>
	 <qresource prefix="/" >
	   <file>img/image1.png</file> 
	   <file>img/image2.png</file> 
	   <file>img/image3.png</file> 
	 </qresource> 
	</RCC>
    ```

1. this needs to be compiled to .py format, with the following command:


1. And finally, we need to add this to our script, for example like this:
    ```python
	import images_qr # ... Some code here and there ... self.setWindowIcon(QtGui.QIcon(':/img/image1.png')) # The colon is important, it must be there
	```

1. once you compile you should see the images just fine, like this:
**![](https://lh6.googleusercontent.com/VQASotKIuqHNTC2jkXzM9M7Wk-7SMgTQUt1G5acclV298ztnej4utOuqy4_R5mfTL9OMujrAJDt9rtnrIoQvB9gs9Tk16IzSjSubq9HJGRu69W0WibVudQu1THhk_3RUpL3B98C4)**


## Compilation
### pyinstaller

`pyinstaller` allows to create an executable of your application.

#### Installation
```bash
pip install pyinstaller
```


#### Usage
```bash
pyinstaller script.py --onefile --clean -i icon.ico
```

`-i` e' opzionale, serve ad aggiungere un'icona all'exe

The result is in the `dist` directory, `build` can be ignored.


#### How it works
The executable generated is a wrapper (an extractor package) of the python interpreter and the python script with all modules needed for the script execution.
Running the executable, everything is extracted in a temp directory (on Windows is in `%localappdata%\\Temp`).

When `os.getcwd()` (current working directory) is used, that could be a confusion: it could be the executable path or the temp directory?

Below a snippet which creates a variable for both cases:

```python
# I obtain the app directory
if getattr(sys, 'frozen', False):
    # frozen
    dirapp = os.path.dirname(sys.executable)
    dirapp_bundle = sys._MEIPASS
    executable_name = os.path.basename(sys.executable)
else:
    # unfrozen
    dirapp = os.path.dirname(os.path.realpath(__file__))
    dirapp_bundle = dirapp
    executable_name = os.path.basename(__file__)
```

where `dirapp` is the executable path, whereas `dirapp_bundle` is the temp one.

For adding files to the package (wrapper) - for having access with `dirapp_bundle` variable - `--add-data` can be used.

Windows syntax:
```
"<file>;<bundle_location>"
```

Unix syntax:
```
"<file>:<bundle_location>"
```

Example:
```
--add-data "./pdftk.exe;."
```

The executables are compatible for platform: if the package is created on Windows x64, it will run only there.


#### Troubleshooting
* `pyinstaller checking for library z not found`
    ```bash
    sudo apt-get install zlib1g-dev
    ```

* `ImportError: cannot import name 'sysconfig' from 'distutils' (/usr/lib/python3.8/distutils/__init__.py)`
    ```bash
    sudo apt install python3.9-distutils
    ```

* `pip3 on python3.9 fails on 'HTMLParser' object has no attribute 'unescape' [duplicate]`
    ```bash
    pip3 install --upgrade setuptools

    pip3 install --upgrade pip
    pip3 install --upgrade distlib
    ```
    
### cross-compilation with docker image 1
#### Setup
[https://github.com/webcomics/pywine](https://github.com/webcomics/pywine)

1. Clone [https://github.com/webcomics/pywine](https://github.com/webcomics/pywine)
    ```bash
    git clone https://github.com/webcomics/pywine.git
    ```
2. Create a docker image building the **Dockerfile** just cloned
    ```bash
    sudo docker build -t py_win .
    ```
3. Create a docker container interacting with it:
    ```bash
    sudo docker run -it py_win
    ```
4. Run pyinstaller for windows
    ```bash
    wine pyinstaller
    ```
#### Compilation


1. Run container of image `py_win`, without  holding the terminal (`d` option)
    ```bash
    sudo docker run -itd py_win
    ```
2. copy all files to compile to the container
    ```bash
   find . -iname '*.py' -exec sudo docker cp "{}" $container_id:/home \\;
   ```
3. Compile
    ```bash
    sudo docker exec -it $container_id wine pyinstaller
    ```
    **Script**
```bash
PY_SCRIPT=download_tvseries
SCRIPT_DIRECTORY="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
# SCRIPT_DIRECTORY=`dirname $0`
# SCRIPT_DIRECTORY=$(pwd)

# echo $SCRIPT_DIRECTORY
# read -p "Press [Enter] key to start backup..."

# 1. Run container
container_id=$(sudo docker run -itd py_win)  # it returns the container_id just created
echo $container_id

# 2. create compilation directory
sudo docker exec -it $container_id mkdir /home/$PY_SCRIPT

# 3. copy all files to compile to the container
# find . -iname '*.py' -exec sudo docker cp "{}" $container_id:/home \\;
for f in *.*; do sudo docker cp "$f" "$container_id:/home/$PY_SCRIPT"; done

# 4. Compile
sudo docker exec -it $container_id wine pyinstaller /home/$PY_SCRIPT/$PY_SCRIPT.py --clean --onefile --distpath /home/$PY_SCRIPT/dist

# 5. Copy the binary to the real machine
sudo docker cp "$container_id:/home/$PY_SCRIPT/dist" "$SCRIPT_DIRECTORY/dist_win"

```

### cross-compilation with docker image 2
#### Setup

1. Clone [https://github.com/cdrx/docker-pyinstaller](https://github.com/cdrx/docker-pyinstaller)
    ```bash
    git clone https://github.com/cdrx/docker-pyinstaller
    ```
2. Create a docker image building the **Dockerfile** just cloned
    ```bash
    sudo docker build -t py_win .
    ```
3. Create a docker container interacting with it:
    ```bash
    sudo docker run -it py_win
    ```
4. Run pyinstaller for windows
    ```bash
    wine pyinstaller
    ```
#### Compilation


1. Run container of image `py_win`, without  holding the terminal (`d` option)
    ```bash
    sudo docker run -itd py_win
    ```
2. copy all files to compile to the container
    ```bash
   find . -iname '*.py' -exec sudo docker cp "{}" $container_id:/home \\;
   ```
3. Compile
    ```bash
    sudo docker exec -it $container_id wine pyinstaller
    ```
    **Script**
```bash
PY_SCRIPT=download_tvseries
SCRIPT_DIRECTORY="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
# SCRIPT_DIRECTORY=`dirname $0`
# SCRIPT_DIRECTORY=$(pwd)

# 1. Run container
container_id=$(sudo docker run -itd py_win)  # it returns the container_id just created
echo $container_id

# 2. create compilation directory
sudo docker exec -it $container_id mkdir /home/$PY_SCRIPT

# 3. copy all files to compile to the container
# find . -iname '*.py' -exec sudo docker cp "{}" $container_id:/home \\;
for f in *.*; do sudo docker cp "$f" "$container_id:/home/$PY_SCRIPT"; done

# 4. Compile
sudo docker exec -it $container_id wine pyinstaller /home/$PY_SCRIPT/$PY_SCRIPT.py --clean --onefile --distpath /home/$PY_SCRIPT/dist

# 5. Copy the binary to the real machine
sudo docker cp "$container_id:/home/$PY_SCRIPT/dist" "$SCRIPT_DIRECTORY/dist_win"
```
## Publish python module
**Resources:**
* [How to Publish an Open-Source Python Package to PyPI – Real Python](https://realpython.com/pypi-publish-python-package/)
* [Packaging Python Projects — Python Packaging User Guide](https://packaging.python.org/tutorials/packaging-projects/)
* [How to upload your python package to PyPi - joelbarmettlerUZH - Medium](https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56)

## Miscellaneous
### Loading animation
```python
import itertools
import threading
import time
import sys

done = False
#here is the animation
def animate(text):  
    for c in itertools.cycle(['|', '/', '-', '\\\\']):  
        if done:  
            break  
        sys.stdout.write('\\r' + text + ' ' + c)
        sys.stdout.flush()  
        time.sleep(0.1)  
    sys.stdout.write('\\rDone!\\n')

t = threading.Thread(target=animate, args=['Copying files'])
t.start()

# long process here
time.sleep(10)  # replace with the process to run

# restore the variable, in order to stop the thread
done = True
```

### get list value lap Rotate list
```python
def get_list_value_lap(list_var, index):
    len_list = len(list_var)
    if index <= len_list:
        return list_var[index]
    else:
        molt1 = int( index / len_list )
        sott1 = len_list * molt1

        new_index = index - sott1

        return (new_index)

l = ['A', 'B', 'C', 'D']
l = ['default', 'primary', 'success', 'info', 'warning', 'danger']
print(get_list_value_lap(l, 15))
```


### create_directory_tree
```python
def create_directory_tree(tree_dir):
    dirs_in_output_path = tree_dir.split(os.sep)
    out_dir_temp = ''
    for out_dir in dirs_in_output_path:

        # fix for os.path.join: since it removed the \\ in the drive, I put it back
        if out_dir.endswith(':'):
            out_dir += '\\\\'
        out_directory = os.path.join(out_dir_temp, out_dir)
        out_dir_temp = os.path.join(out_dir_temp, out_dir)
        if not os.path.exists(out_directory):
            os.mkdir(out_directory)
```


### Create csv

```python
from openpyxl import Workbook  
import csv


def _convert_to_number(cell):  
    if cell.isnumeric():  
        return int(cell)  
    try:  
        return float(cell)  
    except ValueError:  
        return cell


def create_csv(csv_content, header, delimiter=';', output_filename='output.csv'):
    wb = Workbook()  
    worksheet = wb.active  
    if not header == '':  
        worksheet.append(header)  
    for row in csv.reader(csv_content, delimiter=delimiter):  
        worksheet.append([_convert_to_number(cell) for cell in row])  
    wb.save(output_filename)
```

**Reference:** 
* https://stackabuse.com/reading-and-writing-csv-files-in-python/
* https://realpython.com/python-csv/
* https://code.tutsplus.com/tutorials/how-to-read-and-write-csv-files-in-python--cms-29907
```python
def write_csv(csvfilepath, csv_content=[]):
	# csv_content = [ ['HEADER_COLUMN1', HEADER_COLUMN2], ['row1'] ]
    myFile = io.open(csvfilepath, 'w', encoding='utf-8', errors='ignore', newline='')  
    with myFile:  
        writer = csv.writer(myFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)  
        writer.writerows(csv_content)  
  
    print("Writing complete")
```
-   If  `quoting`  is set to  `csv.QUOTE_MINIMAL`, then  `.writerow()`  will quote fields only if they contain the  `delimiter`  or the  `quotechar`. This is the default case.
-   If  `quoting`  is set to  `csv.QUOTE_ALL`, then  `.writerow()`  will quote all fields.
-   If  `quoting`  is set to  `csv.QUOTE_NONNUMERIC`, then  `.writerow()`  will quote all fields containing text data and convert all numeric fields to the  `float`  data type.
-   If  `quoting`  is set to  `csv.QUOTE_NONE`, then  `.writerow()`  will escape delimiters instead of quoting them. In this case, you also must provide a value for the  `escapechar`  optional parameter.


### get variable name in string
```python
# TODO : checl in python 3
>>> my_var = 5
>>> my_var_name = [ k for k,v in locals().iteritems() if v == my_var][0]
>>> my_var_name
'my_var'
```


### get human readable file size
```python
def sizeof_fmt(num, suffix='B'):
    magnitude = int(math.floor(math.log(num, 1024)))
    val = num / math.pow(1024, magnitude)
    if magnitude > 7:
        return '{:.1f}{}{}'.format(val, 'Yi', suffix)
    return '{:3.1f}{}{}'.format(val, ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi'][magnitude], suffix)
```

or

```python
def sizeof_fmt(num, suffix='o'):
    """Readable file size
    :param num: Bytes value
    :type num: int
    :param suffix: Unit suffix (optionnal) default = o
    :type suffix: str
    :rtype: str
    """
    for unit in ['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(num) < 1024.0:
            return "%3.1f %s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)
```

or
```python
def sizeof_fmt(num, suffix='B'):  
    for unit in ['','K','M','G','T','P','E','Z']:  
        if abs(num) < 1024.0:  
            return "%3.1f %s%s" % (num, unit, suffix)  
        num /= 1024.0  
  return "%.1f %s%s" % (num, 'Yi', suffix)
```



## My Tips
### format amount
```python
def format_amount(amount, country):
    amount = float(amount)
    amount_formatted = '{:20,.2f}'.format(amount).strip()

    if country.upper() == 'IT':
        amount_formatted = amount_formatted.replace('.', '<dot>').replace(',', '<comma>')
        amount_formatted = amount_formatted.replace('<dot>', ',').replace('<comma>', '.')

    return amount_formatted
```


### round numbers
```python
def round_str(number, useless_dec=True, r=2):
    """
    rounds the number making it integer if decimal are useless
    """
    rn = format(float(number), '.{}f'.format(r))  # => float

    if str(rn).endswith('.' + '0'*r):
        if useless_dec:
            pass
        else:
            rn = str(int(float(rn)))
    else:
        pass

    return rn
```

### remove io elements (files or directories)
```python
def remove(element, debug=False):
    exception_text = f'[WARNING] : {element} cannot be removed.'
    if os.path.isdir(element):
        try:
            shutil.rmtree(element)
        except:
            if debug:
                print(exception_text)
    elif os.path.isfile(element):
        try:
            os.remove(element)
        except:
            if debug:
                print(exception_text)
    elif not os.path.exists:
        if debug:
            print(f'{element} does not exist')
    else:
        pass
```

### get list value lap: never get a out of index rotating the values
```python
def get_list_value_lap(list_var, index):
    len_list = len(list_var)
    if index < len_list:
        return list_var[index]
    else:
        molt1 = int(index / len_list)
        sott1 = len_list * molt1

        new_index = index - sott1

        return list_var[new_index]
```

### CRLF_auto
```python
def CRLF_auto(sentence, n_chars_per_line, chars_for_control = ['.',',','?', '!']):
   position_sentence = 0
   position_line = 0

   for char in sentence:
       position_sentence = position_sentence + 1
       position_line = position_line + 1

       if (position_line >= n_chars_per_line) and char in chars_for_control:
           sentence = sentence[0:position_sentence-1] + '\\n' + sentence[position_sentence:]
           if '\\n ' in sentence:
               sentence = sentence.replace('\\n ','\\n')
           position_line = 0
   return(sentence)
```

### Zip without tree
```python
def zip_no_tree(filenamezip, list_files_to_zip, path_zip=os.path.dirname(os.path.realpath(__file__)), path_list_files=''):
   import zipfile

   zip = zipfile.ZipFile(os.path.join(path_zip, filenamezip), 'w')

   for file in list_files_to_zip:
       if os.path.dirname(os.path.realpath(__file__)) != path_list_files:
           # Copy temp files
           shutil.copy(os.path.join(path_list_files, file), os.path.join(os.path.dirname(os.path.realpath(__file__)), file))

       try: # Create zip
           zip.write(file)
       except:
           print('[ERROR] : %s does not exist' %(file))

       if os.path.dirname(os.path.realpath(__file__)) != path_list_files:
           # Remove temp file
           os.remove(os.path.join(os.path.dirname(os.path.realpath(__file__)), file))

   # Close Stream zip
   zip.close()
   print('\\n\\n%s package created!' %(filenamezip))
```


### Zip with tree
---


### Remove Prefix
```python
def remove_prefix(text, prefix):
   if text.startswith(prefix):
       return text[len(prefix):]
   return text #or whatever
```

or 

```python
def remove_prefix(text, prefix):
    return text[text.startswith(prefix) and len(prefix):]
```


### Remove Suffix
```python
#DON’T USE FOR REMOVING EXTENSION, SINCE IT IS NOT COMPATIBLE WITH UNIX
def remove_suffix(text, suffix):
   if text.endswith(suffix):
       return text[:len(text)-len(suffix)]
   return text #or whatever
```

or 

```python
def remove_suffix(text, suffix):
    return text[:-len(suffix)] if text.endswith(suffix) and len(suffix) != 0 else text
```


### Lreplace / Rreplace
```python
import re

def lreplace(pattern, sub, string):
   """
   Replaces 'pattern' in 'string' with 'sub' if 'pattern' starts 'string'.
   """
   return re.sub('^%s' % pattern, sub, string)

def rreplace(pattern, sub, string):
   """
   Replaces 'pattern' in 'string' with 'sub' if 'pattern' ends 'string'.
   """
   return re.sub('%s$' % pattern, sub, string)
```


### Convert Html to string
```python
def Html2str(string):
   string = string.replace('&lt;', '<')
   string = string.replace('&gt;', '>')
   string = string.replace('&amp;', '&')
   string = string.replace('&quot;', '"')
   #string = string.replace('&apos', "'")
   string = string.replace('&middot', '·')

   return string
```

### Convert string to Html
```python
def str2Html(string):
   string = string.replace('<', '&lt;')
   string = string.replace('>', '&gt;')
   if '&' in string:
       string = re.sub('&(?!gt)+(?!amp)+(?!lt)+(?!quot)+(?!copy)', '&amp;', string)
   #string = string.replace('&', '&amp;')
   string = string.replace('©', '&copy;')
   string = string.replace('"', '&quot;')
   string = string.replace('·', '&middot')
   #string = string.replace("'", '&apos')

   return string
```


### Copy file
```python
def cpfile(src, dest):
   try:
       #shutil.copy2(src, dest)
       #raise Exception('I know Python!')  # TEST exception
       copy_file(src, dest)
       print(Style.BRIGHT + Back.BLACK + Fore.GREEN + 'Copied successfully: ' + Style.RESET_ALL + Back.BLACK + Fore.GREEN + src + ' --> ' + dest + Style.RESET_ALL)
   except:
       print(Style.BRIGHT + Back.BLACK + Fore.RED + 'Copy failed: ' + Style.RESET_ALL + Back.BLACK + Fore.RED + src + ' --> ' + dest + Style.RESET_ALL)
       traceback.print_exc(file=sys.stdout)

      Copy directory
def cpdir(src, dest):
   try:
       #shutil.copy2(src, dest)
       #raise Exception('I know Python!')  # TEST exception
       #shutil.copytree(src, dest)
       dir_util.copy_tree(src, os.path.join(dest, os.path.basename(src)))
       print(Style.BRIGHT + Back.BLACK + Fore.GREEN + 'Copied successfully: ' + Style.RESET_ALL + Back.BLACK + Fore.GREEN + src + ' --> ' + dest + Style.RESET_ALL)
   except:
       print(Style.BRIGHT + Back.BLACK + Fore.RED + 'Copy failed: ' + Style.RESET_ALL + Back.BLACK + Fore.RED + src + ' --> ' + dest + Style.RESET_ALL)
       traceback.print_exc(file=sys.stdout)
```


### Python script as configuration file
```python
# import dynamic python file for settings
sys.path.insert(0, dirapp)  # or sys.path.insert(0, '.')

try:
   with open('test_suite_settings.py', 'r') as read_settings:
       settings_content = read_settings.readlines()

   top_settings = """
try:
   from colorama import init

   init(strip=False)

   from colorama import Fore, Back, Style

except:
   print('Colorama not imported')

   class Fore(object):
       BLACK = ''
       RED = ''
       GREEN = ''
       YELLOW = ''
       BLUE = ''
       MAGENTA = ''
       CYAN = ''
       WHITE = ''
       RESET = ''


   class Back(object):
       BLACK = ''
       RED = ''
       GREEN = ''
       YELLOW = ''
       BLUE = ''
       MAGENTA = ''
       CYAN = ''
       WHITE = ''
       RESET = ''


   class Style(object):
       DIM = ''
       NORMAL = ''
       BRIGHT = ''
       RESET_ALL = ''
"""
   temp_include = 'test_suite_settings_py.py'
   with open(temp_include, 'w') as write_settings:
       write_settings.writelines([top_settings] + settings_content)
   exec("from test_suite_settings_py import *")

except:
   print('Error: "%s" not found. It is necessary for configure the test suite' % 'test_suite_settings.py')
   sys.exit(10)
```

### Download spreadsheet from Google
```python
# read xls file # set "data_only=True" if you want to get the cell content as a text even if it is a formula  
if 'docs.google.com' in args.excel_file:  
  if args.excel_file.endswith('/'):  
  slash = ''  
  else:  
  slash = '/'  
  args.excel_file = args.excel_file.strip('/')  
  
  # extract id from url  
  if re.match(r'edit\\/?$', args.excel_file):  
  google_spreasheet_id = re.findall(r'(?:d\\/)(.*)(?:\\/edit)', args.excel_file)  
  else:  
  google_spreasheet_id = re.findall(r'(?:d\\/)(.*)', args.excel_file)  
  if len(google_spreasheet_id) > 0:  
  google_spreasheet_id = google_spreasheet_id[0]  
  else:  
  print('\\n\\n[ERROR] : Google Document ID not found. Exit!')  
  sys.exit(1)  
  url = 'https://docs.google.com/spreadsheet/ccc?key={}&output=xlsx'.format(google_spreasheet_id)  
  
  print('Downloading Google Spreadsheet: {}'.format(url), end='\\r')  
  
  google_spreasheet_filename = 'GestioneMoney.xlsx'  
  response = requests.get(url)  
  google_spreasheet_content = response.content  
    with open(google_spreasheet_filename, 'wb') as write_google_spreasheet:  
  write_google_spreasheet.write(google_spreasheet_content)  
  
  print('Download complete! : {}'.format(url))  
  excel_file = google_spreasheet_filename  
else:  
  excel_file = args.excel_file
```


### Retrieve variable name
```python
def retrieve_name(var):
    """
    Gets the name of var. Does it from the out most frame inner-wards.
    :param var: variable to get name from.
    :return: string
    """
    for fi in reversed(inspect.stack()):
        names = [var_name for var_name, var_val in fi.frame.f_locals.items() if var_val is var]
        if len(names) > 0:
            return names[0]


a = {1: 'one', 2: 'two'}
print(retrieve_name(a))
>>>a
```


## API

### Slack
Resources: https://api.slack.com/docs/working-with-workspace-tokens#getting_started

1. Create App in Slack: https://api.slack.com/apps?new_app_token=1
  1. Fill `App Name`
  1. Select your Workspace

2. 

### qbittorrent
* [https://pypi.org/project/python-qbittorrent/](https://pypi.org/project/python-qbittorrent/)
* [https://python-qbittorrent.readthedocs.io/en/latest/modules/api.html](https://python-qbittorrent.readthedocs.io/en/latest/modules/api.html)

```python
pip install python-qbittorrent
```

```python
from qbittorrent import Client

qb = Client('http://127.0.0.1:8080/')

qb.login('admin', 'your-secret-password')
# not required when 'Bypass from localhost' setting is active.
# defaults to admin:admin.
# to use defaults, just do qb.login()

torrents = qb.torrents()

for torrent in torrents:
    print torrent['name']
```

#### Get all active torrents:
```python
qb.torrents()
```


* Filter torrents:
```python
qb.torrents(filter='downloading', category='my category')
# This will return all torrents which are currently
# downloading and are labeled as ``my category``.

qb.torrents(filter='paused', sort='ratio')
# This will return all paused torrents sorted by their Leech:Seed ratio.
```

* Download torrents by link:

```python
magnet_link = "magnet:?xt=urn:btih:e334ab9ddd91c10938a7....."
qb.download_from_link(magnet_link)

# No matter the link is correct or not,
# method will always return empty JSON object.
Download multipe torrents by list of links:

link_list = [link1, link2, link3]
qb.download_from_link(link_list)
```

* Downloading torrents by file:
```python
torrent_file = open('my-torrent-file.torrent', 'rb')
qb.download_from_file(torrent_file)
Downloading multiple torrents by using files:

torrent_file_list = [open('1.torrent', 'rb'), open('2.torrent', 'rb')]
qb.download_from_file(torrent_file_list)
```

* Specifing save path for downloads:
```python
dl_path = '/home/user/Downloads/special-dir/'
qb.download_from_file(myfile, savepath=dl_path)

# same for links.

qb.download_from_link(my_magnet_uri, savepath=dl_path)
```

* Applying labels to downloads:
```python
qb.download_from_file(myfile, label='secret-files ;) ')

# same for links.
qb.download_from_link(my_magnet_uri, category='anime')
```

* Pausing/ Resuming all torrents:
```python
qb.pause_all()
qb.resume_all()
```

* Pausing/ Resuming a speicific torrent:
```python
info_hash = 'e334ab9ddd....infohash....5d7fff526cb4'
qb.pause(info_hash)
qb.resume(info_hash)
```

* Pausing/ Resuming multiple torrents:
```python
info_hash_list = ['e334ab9ddd9......infohash......fff526cb4',
                  'c9dc36f46d9......infohash......90ebebc46',
                  '4c859243615......infohash......8b1f20108']

qb.pause_multiple(info_hash_list)
qb.resume_multipe(info_hash_list)
```


### Salesforce
**Resources :**
* [salesforce-api](https://pypi.org/project/salesforce-api/)
* [simple-salesforce](https://pypi.org/project/simple-salesforce/)

```python
from simple_salesforce import Salesforce

sf = Salesforce(instance_url=args.url, username=args.user, password=args.password, security_token=args.token)

# Account Select
account_list = sf.query_all("SELECT Account.Id, Account.Name, External_Account_Id__c FROM Account")
account_list = account_list['records']
```

```python
case_desc = sf.Case.describe()  # get fields of a table
case_field_names = [field['name'] for field in case_desc['fields']]

# in a single line:
[field['name'] for field in sf.Case.describe()['fields']]

# as string
case_fields_str = ', '.join(case_field_names).strip(', ')
```

### Dropbox

* [http://99rabbits.com/get-dropbox-access-token/](http://99rabbits.com/get-dropbox-access-token/)
#### STEP 1. Create an app in your Dropbox account

1.  Go to [https://www.dropbox.com/developers/apps/create](https://www.dropbox.com/developers/apps/create)
2.  Authorize, if you weren’t.
3.  Choose Dropbox API on the first step.
4.  Choose Full Dropbox access on the second.
5.  Give your app a name. That name will become a folder in your Dropbox account.
6.  Push ‘Create app’ button.


#### STEP2. Generate access token

You’ll be presented with your app’s settings.

1.  Scroll down to ‘OAuth 2’ block and  **hit ‘Generate’** button near ‘Generated access token’ text.
2.  After the token is generated you’ll see a string of letters and numbers, which looks something like this:

> fkeqazcnlytdghf2hgfjh41hfghjhgk1jhk11fhyiko11ghkllre6ooo111fgheww

This is your Dropbox API access token . You should now hand over this token to your developer.

> You can get acquainted with the possibilities of Dropbox API using their  [API explorer](https://dropbox.github.io/dropbox-api-v2-explorer/).

### Slack
* Resource: [https://api.slack.com/incoming-webhooks](https://api.slack.com/incoming-webhooks)
1. Create a slack app here: [https://api.slack.com/apps?new_app=1](https://api.slack.com/apps?new_app=1) 
1. Enable `Incoming Webhook` int your slack app
1. Create a incoming webhook for each slack receiver from here: [https://api.slack.com/apps/ACGRH6B5X/incoming-webhooks?](https://api.slack.com/apps/ACGRH6B5X/incoming-webhooks?) (`Add New Webhook to Workspace`)

```python
import slackpy

INCOMING_WEB_HOOK = 'your_web_hook_url'
CHANNEL = '#general'
USER_NAME = 'Logger'
ICON_URL = 'http://lorempixel.com/48/48'

# Create a new instance.
logging = slackpy.SlackLogger(INCOMING_WEB_HOOK, CHANNEL, USER_NAME, ICON_URL)

# You can set a log level. The default level is INFO.
logging.set_log_level(slackpy.LogLv.DEBUG) # Or logging.set_log_level(10)

## Minimum Parameter
## logging = slackpy.SlackLogger(INCOMING_WEB_HOOK)

# Simple Usage
logging.info('INFO Message')

# LogLevel's only required parameter is "message", all others are optional.

# LogLevel: DEBUG
logging.debug(message='DEBUG Message', title='DEBUG Title', fields='')

# LogLevel: INFO
logging.info(message='INFO Message', title='INFO Title', fields='')

# LogLevel: WARN
logging.warn(message='WARN Message', title='WARN Title', fields='')

# LogLevel: ERROR
logging.error(message='ERROR Message', title='ERROR Title', fields='')

# LogLevel: CUSTOM
logging.message(message='CUSTOM Message', title='CUSTOM Title', color='good',
                fields=[{"title": "CUSTOM", "value": "test", "short": True}],
                log_level=40)

# Title Link (New v2.1.0)
logging.info(message='INFO Message', title='slackpy Repository here',
             title_link='https://github.com/iktakahiro/slackpy')
```


## QAC
### get_framework_path
```python
def get_framework_path():  
    if os.sep == '/':  
        # Linux  
  pass  
 else:  
        # Windows  
  _, p_out = run_process('where qacli')  
  
        framework_list = p_out.split()  
        if framework_list:  
            return os.path.dirname(os.path.dirname(os.path.dirname(framework_list[0])))  # return the latest release  
  else:  
            print_colour('error', 'Please specify the framework/HelixQAC path. For instance: "C:\\Perforce\\Helix-QAC-2019.2"')  
            sys.exit(1)  
```

###   get_latest_component
```python
def get_latest_component(component_regex, framework_path):  
    component_regex_obj = re.compile(component_regex)  
  
    framework_components_path = os.path.join(framework_path, 'components')  
    componet_list = os.listdir(framework_components_path)  
    component_target_list = [x for x in componet_list if re.match(component_regex_obj, x)]  
  
    if component_target_list:  
        return sorted(component_target_list, reverse=True)[0]  
    else:  
        print_colour('error', 'Component {} missing'.format(component_regex.strip('-')))  
        sys.exit(1)
```


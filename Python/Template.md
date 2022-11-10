# Template

----

[[_TOC_]]

----

## Full
```python
# -*- coding: utf-8 -*-
#
# Author:   Dario Necco
# Company:  Programming Research Ltd.
#
# This script allows to ...
__version__ = '1.0'
intern_version = '0001'
 
 
import locale
locale.setlocale(locale.LC_ALL, 'C')
import os
import sys
import shutil
import io
import re
# import chardet  # uncomment only if necessary, it requires installation
import subprocess
from subprocess import Popen, PIPE
from sys import platform as _platform
import argparse
from argparse import ArgumentParser, RawTextHelpFormatter
import traceback
import pprint
from distutils import dir_util
from xml.dom import minidom
import datetime
import logging
import inspect
import time

try:
    from types import SimpleNamespace as Namespace  # available from Python 3.3
except:
    class Namespace:
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

if sys.version[0] == '2':
    from imp import reload
    reload(sys)
    sys.setdefaultencoding("utf-8")

try:
    from colorama import init, Fore, Back, Style
    init()
except ImportError:
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
 
##############################################################################################
# DEBUG
this_scriptFile = inspect.getfile(inspect.currentframe())
this_scriptFile_filename = os.path.basename(this_scriptFile)
this_scriptFile_filename_noext, ext = os.path.splitext(this_scriptFile_filename)
 
logging.basicConfig(filename=this_scriptFile_filename_noext + '.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
 
#sys.argv = [sys.argv[0], '...']
# if len(sys.argv) == 1:
#     sys.argv = [sys.argv[0], '-h']
 
 
def main():
    global debug
 
    welcome_text = '{char1} {appname} v.{version} {char2}'.format(char1='-' * 5, appname=os.path.splitext(os.path.basename(__file__))[0], version=__version__, char2='-' * 5)
    print(welcome_text)
    logging.info(welcome_text)
     
    # check args
    parser = ArgumentParser(formatter_class=RawTextHelpFormatter, description="""
Description
 
""")
     
    # Options
    parser.add_argument("-debug",
                        dest="debug",
                        action='store_true',
                        help=argparse.SUPPRESS
                        # help='Increase output verbosity. Output files don\\'t overwrite original ones'
                        )
 
    parser.add_argument("-op", "--output",
                        dest="output_path",
                        help="qac output path. it has given in input to this application",
                        #nargs="+",
                        #nargs='?',  # optional argument
                        #default=""
                        #type=int
                        )
 
    parser.add_argument("source_file",
                        help="source file must be analyzed")
 
    args = parser.parse_args()  # it returns args.output_path and args.source_file
 
    # end check args
     
     
    print('Working dir: \\"' + dirapp + '\\"')
 
    """
    In case of recursive search
    """
    # Recusive search
    for dirpath, dirnames, filenames in os.walk(source_dir):
        for filename in [f for f in filenames]:  # for all files in subdirs
            #print os.path.join(dirpath, filename)
 
            if filename.endswith(".h") or filename.endswith(".c") or filename.endswith(".cpp"):
                file = os.path.join(dirpath, filename)
 
        for filename in filenames:  # for all files in current dir
            #print os.path.join(dirpath, filename)
 
            if filename.endswith(".h") or filename.endswith(".c") or filename.endswith(".cpp"):
                file = os.path.join(dirpath, filename)
 
    """
    In case of endless script - it executes a process every n seconds
    """
    refresh_time = args.refresh_time
 
    print("Starting... I'll retrieve data every %s seconds\\n" % refresh_time)
 
    while True:
        # do something
 
        time_to_wait = refresh_time
         
        # Wait for n seconds - countdown
        for sec in range(time_to_wait):
            time_to_wait = time_to_wait - 1
            print(str(time_to_wait) + "      ", end='\\r')
            time.sleep(1)
        print('', end='\\r')
        print('Updating...', end='\\r')
 
 
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\\n\\nBye!')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
```


## Light
* disabled logging
* import on top
* no classes for colorama

```python
# -*- coding: utf-8 -*-
#
# Author:   Dario Necco
# Company:  Programming Research Ltd.
#
# This script allows to ...
import locale
import os
import sys
import argparse
from argparse import ArgumentParser, RawTextHelpFormatter
import logging
import inspect
import time
import shutil
import io
import re
import subprocess
from subprocess import Popen, PIPE
from sys import platform as _platform
import traceback
import pprint
from distutils import dir_util
from xml.dom import minidom
import datetime
# import chardet  # uncomment only if necessary, it requires installation

# import Namespace
try:
    from types import SimpleNamespace as Namespace  # available from Python 3.3
except ImportError:
    class Namespace:
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

if sys.version[0] == '2':
    from imp import reload

    reload(sys)
    sys.setdefaultencoding("utf-8")

# import Colorama
try:
    from colorama import init

    init()

    from colorama import Fore, Back, Style

except ImportError:
    print('Colorama not imported')

locale.setlocale(locale.LC_ALL, 'C')  # set locale

# set version and author  
__version__ = '1.0'  
intern_version = '0001'

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

##############################################################################################
# DEBUG
this_scriptFile = inspect.getfile(inspect.currentframe())
this_scriptFile_filename = os.path.basename(this_scriptFile)
this_scriptFile_filename_noext, ext = os.path.splitext(this_scriptFile_filename)

# logging.basicConfig(filename=this_scriptFile_filename_noext + '.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')  # uncomment for Logging


def main():
    welcome_text = '{char1} {appname} v.{version} {char2}'.format(char1='-' * 5, 
                                                                  appname=os.path.splitext(os.path.basename(__file__))[0], 
                                                                  version=__version__, char2='-' * 5)
    print(welcome_text)
    logging.info(welcome_text)

    # check args
    parser = ArgumentParser(formatter_class=RawTextHelpFormatter, description="""
Description

""")

    # Options
    parser.add_argument("-debug",
                        dest="debug",
                        action='store_true',
                        help=argparse.SUPPRESS
                        # help='Increase output verbosity. Output files don\\'t overwrite original ones'
                        )

    parser.add_argument("-op", "--output",
                        dest="output_path",
                        help="qac output path. it has given in input to this application",
                        # nargs="+",
                        # nargs='?',  # optional argument
                        # default=""
                        # type=int
                        )

    parser.add_argument("source_file",
                        help="source file must be analyzed")

    args = parser.parse_args()  # it returns args.output_path and args.source_file

    # end check args

    print('Working dir: \\"' + dirapp + '\\"')

    """
    In case of recursive search
    """
    # Recusive search
    for dirpath, dirnames, filenames in os.walk(source_dir):
        for filename in [f for f in filenames]:  # for all files in subdirs
            # print os.path.join(dirpath, filename)

            if filename.endswith(".h") or filename.endswith(".c") or filename.endswith(".cpp"):
                file = os.path.join(dirpath, filename)

        for filename in filenames:  # for all files in current dir
            # print os.path.join(dirpath, filename)

            if filename.endswith(".h") or filename.endswith(".c") or filename.endswith(".cpp"):
                file = os.path.join(dirpath, filename)

    """
    In case of endless script - it executes a process every n seconds
    """
    refresh_time = args.refresh_time

    print("Starting... I'll retrieve data every %s seconds\\n" % refresh_time)

    while True:
        # do something

        time_to_wait = refresh_time

        # Wait for n seconds - countdown
        for sec in range(time_to_wait):
            time_to_wait = time_to_wait - 1
            print(str(time_to_wait) + "      ", end='\\r')
            time.sleep(1)
        print('', end='\\r')
        print('Updating...', end='\\r')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\\n\\nBye!')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

```

## Light beta
* args have been moved outside the main() function

```python
# -*- coding: utf-8 -*-
#
# Author:   Dario Necco
# Company:  Programming Research Ltd.
#
# This script allows to ...
import locale
import os
import sys
import argparse
from argparse import ArgumentParser, RawTextHelpFormatter
import logging
import inspect
import time
import shutil
import io
import re
import subprocess
from subprocess import Popen, PIPE
from sys import platform as _platform
import traceback
import pprint
from distutils import dir_util
from xml.dom import minidom
import datetime
# import chardet  # uncomment only if necessary, it requires installation

# import Namespace
try:
    from types import SimpleNamespace as Namespace  # available from Python 3.3
except ImportError:
    class Namespace:
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

if sys.version[0] == '2':
    from imp import reload

    reload(sys)
    sys.setdefaultencoding("utf-8")

# import Colorama
try:
    from colorama import init

    init()

    from colorama import Fore, Back, Style

except ImportError:
    print('Colorama not imported')

locale.setlocale(locale.LC_ALL, 'C')  # set locale

# set version and author  
__version__ = '1.0'  
intern_version = '0001'

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

#
# check args
#
parser = ArgumentParser(formatter_class=RawTextHelpFormatter, description="""
Description

""")

# Options
parser.add_argument("-debug", dest="debug", action='store_true', help=argparse.SUPPRESS)
                    # help='Increase output verbosity. Output files don\\'t overwrite original ones'

parser.add_argument("-op", "--output", dest="output_path",
                    help="qac output path. it has given in input to this application")
                    # action='store_true'
                    # nargs="+",
                    # nargs='?',  # optional argument
                    # default=""
                    # type=int
                    # choices=[]

parser.add_argument("source_file",
                    help="source file must be analyzed")

args = parser.parse_args()  # it returns input as variables (args.dest)

# end check args

##############################################################################################
# DEBUG
this_scriptFile = inspect.getfile(inspect.currentframe())
this_scriptFile_filename = os.path.basename(this_scriptFile)
this_scriptFile_filename_noext, ext = os.path.splitext(this_scriptFile_filename)

# logging.basicConfig(filename=this_scriptFile_filename_noext + '.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')  # uncomment for Logging


def main(args):
    print('Working dir: \\"' + dirapp + '\\"')
    welcome_text = '{char1} {appname} v.{version} {char2}'.format(char1='-' * 5, 
                                                                  appname=os.path.splitext(os.path.basename(__file__))[0], 
                                                                  version=__version__, char2='-' * 5)
    print(welcome_text)
    logging.info(welcome_text)

    """
    In case of recursive search
    """
    # Recusive search
    for dirpath, dirnames, filenames in os.walk(source_dir):
        for filename in [f for f in filenames]:  # for all files in subdirs
            # print os.path.join(dirpath, filename)

            if filename.endswith(".h") or filename.endswith(".c") or filename.endswith(".cpp"):
                file = os.path.join(dirpath, filename)

        for filename in filenames:  # for all files in current dir
            # print os.path.join(dirpath, filename)

            if filename.endswith(".h") or filename.endswith(".c") or filename.endswith(".cpp"):
                file = os.path.join(dirpath, filename)

    """
    In case of endless script - it executes a process every n seconds
    """
    refresh_time = args.refresh_time

    print("Starting... I'll retrieve data every %s seconds\\n" % refresh_time)

    while True:
        # do something

        time_to_wait = refresh_time

        # Wait for n seconds - countdown
        for sec in range(time_to_wait):
            time_to_wait = time_to_wait - 1
            print(str(time_to_wait) + "      ", end='\\r')
            time.sleep(1)
        print('', end='\\r')
        print('Updating...', end='\\r')


if __name__ == '__main__':
    try:
        main(args)
    except KeyboardInterrupt:
        print('\\n\\nBye!')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
```

## Light beta 2
* checking of args is now in a dedicated function `check_args` in order to make it easy the import from another script
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Dario Necco"

import locale
import os
import sys
import argparse
from argparse import ArgumentParser, RawTextHelpFormatter
import logging
import inspect
import time
import shutil
import io
import re
import subprocess
from subprocess import Popen, PIPE
from sys import platform as _platform
import traceback
import pprint
from distutils import dir_util
from xml.dom import minidom
import datetime
# import chardet  # uncomment only if necessary, it requires installation

# import Namespace
try:
    from types import SimpleNamespace as Namespace  # available from Python 3.3
except ImportError:
    class Namespace:
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

if sys.version[0] == '2':
    from imp import reload

    reload(sys)
    sys.setdefaultencoding("utf-8")

# import Colorama
try:
    from colorama import init, Fore, Back, Style
    init(strip=True)  # strip makes colorama working in PyCharm
except ImportError:
    print('Colorama not imported')

locale.setlocale(locale.LC_ALL, 'C')  # set locale

# set version and author  
__version__ = 1.0

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

##############################################################################################
# DEBUG
this_scriptFile = inspect.getfile(inspect.currentframe())
this_scriptFile_filename = os.path.basename(this_scriptFile)
this_scriptFile_filename_noext, ext = os.path.splitext(this_scriptFile_filename)

# logging.basicConfig(filename=this_scriptFile_filename_noext + '.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')  # uncomment for Logging

print('Working dir: \\"' + dirapp + '\\"')
welcome_text = '{char1} {appname} v.{version} {char2}'.format(char1='-' * 5, 
                                                              appname=os.path.splitext(os.path.basename(__file__))[0], 
                                                              version=__version__, char2='-' * 5)
print(welcome_text)
logging.info(welcome_text)


def print_color(text, color):
    print('{color}{text}{reset_color}'.format(color=color, text=text, reset_color=Style.RESET_ALL))


def print_error(text):
    print('{color}{text}{reset_color}'.format(color=Fore.RED, text=text, reset_color=Style.RESET_ALL))


def print_warning(text):
    print('{color}{text}{reset_color}'.format(color=Fore.YELLOW, text=text, reset_color=Style.RESET_ALL))


def check_args():
    parser = ArgumentParser(formatter_class=RawTextHelpFormatter, description="""
    Description

    """)

    # Options
    parser.add_argument("-debug", dest="debug", action='store_true', help=argparse.SUPPRESS)
                        # help='Increase output verbosity. Output files don\\'t overwrite original ones'

    parser.add_argument("-op", "--output", dest="output_path",
                        help="qac output path. it has given in input to this application")
                        # action='store_true'
                        # nargs="+",
                        # nargs='?',  # optional argument
                        # default=""
                        # type=int
                        # choices=[]

    parser.add_argument("source_file",
                        help="source file must be analyzed")

    args, unknown = parser.parse_known_args()  # args = parser.parse_args()  # it returns input as variables (args.dest)

    # end check args

    return args


def main(args=None):
    if args is None:
        args = check_args()

    """
    In case of recursive search
    """
    # Recusive search
    for dirpath, dirnames, filenames in os.walk(source_dir):
        for filename in [f for f in filenames]:  # for all files in subdirs
            # print os.path.join(dirpath, filename)

            if filename.endswith(".h") or filename.endswith(".c") or filename.endswith(".cpp"):
                file = os.path.join(dirpath, filename)

        for filename in filenames:  # for all files in current dir
            # print os.path.join(dirpath, filename)

            if filename.endswith(".h") or filename.endswith(".c") or filename.endswith(".cpp"):
                file = os.path.join(dirpath, filename)

    """
    In case of endless script - it executes a process every n seconds
    """
    refresh_time = args.refresh_time

    print("Starting... I'll retrieve data every %s seconds\\n" % refresh_time)

    while True:
        # do something

        time_to_wait = refresh_time

        # Wait for n seconds - countdown
        for sec in range(time_to_wait):
            time_to_wait = time_to_wait - 1
            print(str(time_to_wait) + "      ", end='\\r')
            time.sleep(1)
        print('', end='\\r')
        print('Updating...', end='\\r')


if __name__ == '__main__':
    try:
        main(args=None)
    except KeyboardInterrupt:
        print('\\n\\nBye!')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

```


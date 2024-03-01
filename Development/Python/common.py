import os
import traceback

from colorama import init, Fore, Back, Style
from sqlalchemy import create_engine

# import Namespace
try:
    from types import SimpleNamespace as Namespace  # available from Python 3.3
except ImportError:
    class Namespace:
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)


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
# Print
#
def print_color(text, color=Fore.CYAN):
    print('{color}{text}{reset_color}'.format(color=color, text=text, reset_color=Style.RESET_ALL))


def print_error(text):
    print('{color}[  ERROR  ] {text}{reset_color}'.format(color=Fore.RED, text=text, reset_color=Style.RESET_ALL))


def print_warning(text):
    print('{color}[ WARNING ] {text}{reset_color}'.format(color=Fore.YELLOW, text=text, reset_color=Style.RESET_ALL))


def print_success(text):
    print('{color}{text}{reset_color}'.format(color=Fore.GREEN, text=text, reset_color=Style.RESET_ALL))

#
# DB
#
def query_db(engine, query, list_mode=False,  key="Rule ID"):
    res = engine.execute(query).fetchall()
    res_dict = {}

    for r in res:
        r_dict = dict(r)

        k = r_dict[key]

        if list_mode:
            if k not in res_dict:
                res_dict[k] = []
            res_dict[k].append(r_dict)
        else:
            res_dict[k] = r_dict

    return res_dict, res


def query_db_sqlite(engine, query, list_mode=False,  key_index=0):
    res = engine.execute(query).fetchall()
    res_dict = {}

    for r in res:
        r_dict = {}

        k = r[key_index]

        if list_mode:
            if k not in res_dict:
                res_dict[k] = []
            res_dict[k].append(r)
        else:
            res_dict[k] = r

    return res_dict, res

#
# FTP
#
def ftp_file_exists(ftp, filepath):
    filedir = os.path.dirname(filepath)
    filename = os.path.basename(filepath)
    initial_folder = ftp.pwd()

    status = False
    if ftp_directory_exists(ftp, filedir):
        ftp.cwd('/')
        ftp.cwd(filedir)
        if filename in ftp.nlst():
            status = True

    return status


def ftp_directory_exists(ftp, dir):
    initial_folder = ftp.pwd()
    ftp.cwd('/')
    try:
        ftp.cwd(dir)
        status = True
    except:
        error = traceback.format_exc()
        status = False
    finally:
        ftp.cwd(initial_folder)
        return status

#
# Run process
# TODO : add parameter for hiding windows console in case of issues.
def run_process(cmd, exedir=dirapp):
    p = Popen(cmd, cwd=exedir, stdout=PIPE, stderr=PIPE, shell=True, universal_newlines=True)
    p_out, p_err = p.communicate()
    p_rc = p.returncode

    # arranging output according to the python version
    try:  # py2
        p_out = p_out.decode('utf-8')
        p_err = p_err.decode('utf-8')
    except:  # py3
        pass
    # Exit if there is an error during the execution
    if p_err != '':
        #sys.exit('')
        return p_rc, p_err
    if p_out != '':
        proc_output = p_out
    elif p_err != '':
        proc_output = p_err
    else:
        proc_output = ''

    return p_rc, proc_output

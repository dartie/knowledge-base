# Common
```python

def remove_common_path(ref_path, path_to_convert):
    ref_path_list = ref_path.split(os.sep)
    path_to_convert_list = path_to_convert.split(os.sep)    
    uncommon_path_ref = ()
    uncommon_path_to_convert = ()
    index_pr = 0
    for _ in ref_path_list:
        if not ref_path_list[index_pr] == path_to_convert_list[index_pr]:
            uncommon_path_ref = ref_path_list[index_pr:]
            uncommon_path_to_convert = path_to_convert_list[index_pr:]
            break
        else:
            index_pr += 1

    return uncommon_path_ref, uncommon_path_to_convert



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
            print_error('[ERROR] : %s does not exist' %(file))

        if os.path.dirname(os.path.realpath(__file__)) != path_list_files:
            # Remove temp file
            os.remove(os.path.join(os.path.dirname(os.path.realpath(__file__)), file))

    # Close Stream zip
    zip.close()
    print('\\n\\n')
    print_done('"%s"\\npackage created!' %(filenamezip))
```


## run_process
```python
def run_process(cmd, exedir=dirapp):
    """
    :param cmd:
    :param exedir:
    :return: [process-returncode, process-output]
    """
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

```

## force_carriage_return()
```python
def force_carriage_return(string, cr_char=b'\\r\\n'):
    """
    This function replaces all possible carriage return characters with the one demanded by the user.
    The output is a binary string, therefore if it needs to be written to a file, 'wb' must be used

    string:  input string to convert
    cr_char: carriage ruturn the user demands 
    return:  string converted 
    """
    regex = re.compile(b'(\\r\\n|\\r|\\n)')

    if not isinstance(string, bytes):
        string = string.encode()

    sn = re.sub(regex, cr_char, string)
    sn = sn.decode().encode()

    return sn
```


# ansi2Html
converts a text to html. Text can contains colour ansi tags.

1. import **ansi2html** module
    ```python
    from ansi2html import Ansi2HTMLConverter
    ```

1. create object instance
    ```python
    conv = Ansi2HTMLConverter()
    ```
    
1. convert a text into html
    ```python
    html = conv.convert(ansi_text)
    ```

## Snippets
```python
from ansi2html import Ansi2HTMLConverter


def generate_html_output_FromFileToFile(text, html_file):
    """

    :param terminal_log_file: input file to read
    :param html_file: output file to produce
    :return: -
    """
    conv = Ansi2HTMLConverter()

    file_stdin = open(terminal_log_file, 'r')
    file_stdin_content = file_stdin.readlines()
    file_stdin.close()

    ansi = "".join(file_stdin_content)
    html = conv.convert(ansi)

    write_html_output = io.open(html_file, 'w', encoding='utf-8', errors='replace')  # , errors='ignore')
    write_html_output.writelines(html)
    write_html_output.close()


def generate_html_output_FromTextToFile(text, html_file):
    """

    :param terminal_log_file: input file to read
    :param html_file: output file to produce
    :return: -
    """
    conv = Ansi2HTMLConverter()

    if isinstance(str, text):
        text = "".join(text)
    elif not isinstance(list, text):
        raise TypeError("input must be a string or a list of string")
    else:
        pass  # ok, it is a list
        
    html = conv.convert(text)

    write_html_output = io.open(html_file, 'w', encoding='utf-8', errors='replace')  # , errors='ignore')
    write_html_output.writelines(html)
    write_html_output.close()



def generate_html_output_FromFile(text, html_file):
    """

    :param terminal_log_file: input file to read
    :param html_file: output file to produce
    :return: -
    """
    conv = Ansi2HTMLConverter()

    file_stdin = open(terminal_log_file, 'r')
    file_stdin_content = file_stdin.readlines()
    file_stdin.close()

    ansi = "".join(file_stdin_content)
    html = conv.convert(ansi)

    return html


def generate_html_output_FromTextToFile(text, html_file):
    """

    :param terminal_log_file: input file to read
    :param html_file: output file to produce
    :return: -
    """
    conv = Ansi2HTMLConverter()

    if isinstance(str, text):
        text = "".join(text)
    elif not isinstance(list, text):
        raise TypeError("input must be a string or a list of string")
    else:
        pass  # ok, it is a list
        
    html = conv.convert(text)

    return html

```


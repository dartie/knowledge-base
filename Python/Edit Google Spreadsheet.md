# Edit Google Spreadsheet
## Links
* https://github.com/burnash/gspread
* https://gspread.readthedocs.io/en/latest/
* https://www.youtube.com/watch?v=vISRn5qFrkM
* http://www.makeuseof.com/tag/read-write-google-sheets-python/
* http://www.tothenew.com/blog/access-and-modify-google-sheet-using-python/
* https://github.com/nithinmurali/pygsheets
* https://developers.google.com/sheets/api/quickstart/python
* https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html


## Install modules
```shell
pip install gspread
pip install pygsheets
pip install --upgrade google-api-python-client
```


## Google Setup
1. Go to https://console.cloud.google.com/apis/dashboard
...



1. Rename the json in **client_secret.json**
1. Open it and copy the address value of ````"client_email":````
1. Open the document you want to read/edit and share it with the email address copied (give **edit** permissions)


## Python code steps
### import 
```python
import gspread
from oauth2client.service_account import ServiceAccountCredentials
```

### Document Setup
```python
#scope = "https://spreadsheets.google.com/feeds"
scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive'
]
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)  # 'client_secret.json' is the json file download in the Google Steps
client = gspread.authorize(creds)
```

### Open the Spreadsheet
```python
sheet = client.open('py_test').sheet1  # "py_test" is the spreadsheet's name, "sheet1" is the sheet number

# You can open a spreadsheet by its title as it appears in Google Docs
sh = client.open('My poor gym results') # <-- Look ma, no keys!

# If you want to be specific, use a key (which can be extracted from
# the spreadsheet's url)
sht1 = client.open_by_key('0BmgG6nO_6dprdS1MN3d3MkdPa142WFRrdnRRUWl1UFE')

# Or, if you feel really lazy to extract that key, paste the entire url
sht2 = client.open_by_url('https://docs.google.com/spreadsheet/ccc?key=0Bm...FE&hl')
```

# Get AKA Key
```python
aka_key = gsheet.id
```


### Get and set permissions
* **file_id** – a spreadsheet ID (aka file ID.)
* **value** – user or group e-mail address, domain name or None for ‘default’ type.
* **perm_type** – the account type. Allowed values are: ```user```, ```group```, ```domain```, ```anyone```
* **role** – the primary role for this user. Allowed values are: ```owner```, ```writer```, ```reader```
* **notify** – Whether to send an email to the target user/domain.
* **email_message** – an email message to be sent if notify=True.

```python
#
# Get permissions
client.list_permissions('1CCyAks7WzZ1WFoOAx5KqTuccRavQkS94VO69kQjbgAc')

#
# Give write permissions

client.insert_permission(
    '0BmgG6nO_6dprnRRUWl1UFE',
    'otto@example.org',
    perm_type='user',
    role='writer'
)

# Make the spreadsheet publicly readable

client.insert_permission(
    '0BmgG6nO_6dprnRRUWl1UFE',
    None,
    perm_type='anyone',
    role='reader'
)

#
# Remove permissions
remove_permission(file_id, permission_id)

# Remove Otto's write permission for this spreadsheet
gsheet.remove_permissions('otto@example.com', role='writer')

# Remove all Otto's permissions for this spreadsheet
gsheet.remove_permissions('otto@example.com')

share(value, perm_type, role, notify=True, email_message=None)

```


### Select a Worksheet
```python
# Way 1
sheet = client.open('py_test').sheet1  # "py_test" is the spreadsheet's name, "sheet1" is the sheet number

# Way 2: by name
gsheet = client.open('py_test')  # "py_test" is the spreadsheet's name
wsheet = gsheet.worksheet("Sheet1")  # Select a specific Sheet

# Way 3: by index
gsheet = client.open('py_test')  # "py_test" is the spreadsheet's name
wsheet = gsheet.get_worksheet(0)

```

### Get records
```python
#
# All records
records = wsheet.get_all_records()  # it returns a dictionary "col_header:value" for each line (list of dictionaries)

print(records)

#
# get all the values for a row
row = wsheet.row_values(1)

#
# get all the values for a column
col = wsheet.col_values(2)

```


### Write records
```python
# write to a specific cell
wsheet.update_acell('C2', 'Blue')
# or 
wsheet.update_cell(2, 3, 'Blue')

# Update cell
wsheet.update_cell(8, 1, "Dario")
```


### Create worksheet
```python
wsheet.add_worksheet(title, rows, cols)
```


### Reading Snippet
```python
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = "https://spreadsheets.google.com/feeds"
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

gsheet = client.open('py_test')  # "py_test" is the spreadsheet's name
wsheet = gsheet.worksheet("Sheet1")  # Select a specific Sheet

records = wsheet.get_all_records()  # it returns a dictionary "col_header:value" for each line (list of dictionaries)

print(records)

#
# Get a range of cells
all_cells = wsheet.range('A1:C6')
for cell in all_cells:
    value = cell.value
    row_number = cell.row
    column_number = cell.col

#
# Access cells individually
A2 = wsheet.acell('A2').value
# or
coord = wsheet.cell(3, 0).value

#
# get all the values for a row
row = wsheet.row_values(1)

#
# get all the values for a column
col = wsheet.col_values(2)

#
#Getting All Values From a Worksheet as a List of Lists
list_of_lists = wsheet.get_all_values()

#
#Finding All Matched Cells
# Find all cells with string value
cell_list = wsheet.findall("Rug store")
#
# Find all cells with regexp
criteria_re = re.compile(r'(Small|Room-tiering) rug')
cell_list = wsheet.findall(criteria_re)
```


### Writing Snippet
```python
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = "https://spreadsheets.google.com/feeds"
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

gsheet = client.open('py_test')  # "py_test" is the spreadsheet's name
wsheet = gsheet.worksheet("Sheet1")  # Select a specific Sheet

#
# write to a specific cell
wsheet.update_acell('C2', 'Blue')
# or 
wsheet.update_cell(2, 3, 'Blue')

#
# Append a row (at bottom, regardless blank lines)
wsheet.append_row(["A", "B", "C"])

#
# Insert a row on top
wsheet.insert_row(["A", "B", "C"])

#
# Update cell
wsheet.update_cell(8, 1, "Dario")

#
# append row after last filled
def get_first_row_spreadsheet(list_a):
    index = -1
    last_value_index = 0
    first_empty_cell = 0
    for x in list_a:
        index += 1

        if not x.strip(' ') == '':
            last_value_index = index
        elif first_empty_cell == 0:
            first_empty_cell = index
        else:
            pass

    # print(str(last_value_index + 1))
    #
    # print(str(first_empty_cell + 1))

    return last_value_index + 1


def append_row_content(worksheet, value_list):
    if not isinstance(value_list, list):
        raise TypeError('"value_list" must be a list')

    # get number of lines used
    #record_row = len(worksheet.get_all_records()) + 2  # +2 because the first is not returned in the count, since is used by the header

    # detect first row available (check only first cell of the column)
    #record_row = len([x for x in worksheet.col_values(1) if not x.strip(' ') == '']) +  1 # +1 for selecting the next row
    record_row = get_first_row_spreadsheet(worksheet.col_values(1)) + 1
    print(record_row)

    col = 0
    try:
        for v in value_list:
            col += 1
            worksheet.update_cell(record_row, col, v)
    except:
        worksheet.append_row(value_list)

        
append_row_content(wsheet, ['Dario', 'Necco'])  
```

## Others
### How to find the first empty row of a google spread sheet using python GSPREAD?
* https://stackoverflow.com/questions/40781295/how-to-find-the-first-empty-row-of-a-google-spread-sheet-using-python-gspread
```python
    def next_available_row(worksheet):
        str_list = filter(None, worksheet.col_values(1))  # fastest
        return str(len(str_list)+1)

    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('auth.json', scope)
    gc = gspread.authorize(credentials)
    worksheet = gc.open("sheet name").sheet1
    next_row = next_available_row(worksheet)

    #insert on the next available row

    worksheet.update_acell("A{}".format(next_row), somevar)
    worksheet.update_acell("B{}".format(next_row), somevar2)
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE1NTA1NTU3NF19
-->

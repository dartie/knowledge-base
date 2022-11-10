# Edit Excel Spreadsheet
## Links
* http://zetcode.com/articles/openpyxl/
* http://openpyxl.readthedocs.io/en/default/styles.html
* https://stackoverflow.com/questions/25318095/cell-object-has-no-attribute-styles-when-trying-to-set-cell-font-color




## Install modules
```
pip install openpyxl
```


### import 
```python
import openpyxl
from openpyxl.styles import NamedStyle, Font, Border, Side, Fill, Color, colors
from openpyxl.cell import Cell
```


### Open the Spreadsheet
```python
wb = openpyxl.load_workbook(excel_file)  


wb = openpyxl.load_workbook(excel_file, data_only=True)  # set "data_only=True" if you want to get the cell content as a text even if it is a formula


# get list of sheets
wbsheets = wb.get_sheet_names()  # it returns the list of the document sheets
```


### Select a Worksheet
```python
# Select worksheet by name
wbsheet = wb.get_sheet_by_name(sheet)

# Select worksheet by index
wb.active = 0

# get max row number
max_row_wbsheet = wbsheet.max_row


# get max col number
max_col_wbsheet = wbsheet.max_column


# turn column number into column letter
col_l = openpyxl.utils.get_column_letter(col_n)
```


### Read records
```python
cell = '{col}{row}'.format(col=col_l, row=row)
cell_content = wbsheet[cell].value


# Read a range
cells_content = sheet['A1': 'B6']
```



### Write records
```python
# numerical value
wbsheet.cell(row=row, column=col_n).value = numerical_value




# string value
wbsheet['{col}{row}'.format(col=col_l, row=row)] = string_value


#
# apply style
#
wbsheet['{col}{row}'.format(col=col_l, row=row)].style = 'Normal'  # Reset Style
wbsheet['{col}{row}'.format(col=col_l, row=row)].font = Font(color=Color(colors.BLUE))  # Set foreground colour




# save file
wb.save(output_filename)
```


## write a row (custom function)
```python
def append_row_content(worksheet, row, value_list, col_offset=0):
    if not isinstance(value_list, list):
        raise TypeError('"value_list" must be a list')


    col = 0 + col_offset
    for v in value_list:
        col += 1
        col_l = openpyxl.utils.get_column_letter(col)
        worksheet['{col}{row}'.format(col=col_l, row=row)] = v


```


### Create worksheet
```python


```


### Reading Snippet
```python
# Iterate for column, then for each row
#
# read xls file
wb = openpyxl.load_workbook(xls_file, data_only=True)  # set "data_only=True" if you want to get the cell content as a text even if it is a formula


# get list of sheets
# wbsheets = wb.get_sheet_names()  # it returns the list of the document sheets [Deprecated]
wbsheets = wb.sheetnames
        
#select worksheet
for sheet in wbsheets:
    print('Sheet: ' + sheet)
    # wbsheet = wb.get_sheet_by_name(sheet)  # [Deprecated]
    wbsheet = wb[sheet]


    # iterate for columns
    for col_n in range(1, wbsheet.max_column +1):
        # get column number into column letter
        col_l = openpyxl.utils.get_column_letter(col_n)


        # iterate for rows in columns
        for row in range(1, wbsheet.max_row +1):
            cell = '{col}{row}'.format(col=col_l, row=row)
            cell_content = wbsheet[cell].value
            print(cell_content)

    # OR
    # iterate for rows
    for row in range(1, wbsheet.max_row + 1):

        # iterate for columns in row
        for col_n in range(1, wbsheet.max_column + 1):
            # get column number into column letter
            col_l = openpyxl.utils.get_column_letter(col_n)

            cell = '{col}{row}'.format(col=col_l, row=row)
            cell_content = wbsheet[cell].value            

            if cell_content is not None:
                print(cell_content)


```


#### Convert column letter to number
```python
xy = openpyxl.utils.coordinate_from_string('A4') # returns ('A',4)
col = openpyxl.utils.column_index_from_string(xy[0]) # returns 1
row = xy[1]
```



#### Convert column number to letter
```python
col_l = openpyxl.utils.get_column_letter(col_n)
```




### Writing Snippet

#### write Carriage return in a cell
```python
from openpyxl import Workbook

workbook = Workbook()
worksheet = workbook.worksheets[0]
worksheet.title = "Sheet1"

worksheet.cell('A1').style.alignment.wrap_text = True
worksheet.cell('A1').value = "Line 1\\nLine 2\\nLine 3"

workbook.save('wrap_text1.xlsx')
```

```python
cell_content = wbsheet[cell].value
print(cell_content)
```




<!--stackedit_data:
eyJoaXN0b3J5IjpbLTk4MjA5ODk2OSwtMTAwMTYzODMxMyw1NT
UyNjc0OTUsLTE5OTMwMjQ0NjgsLTk0NTAxODcyOCwtNDMzMjI2
MzMxLC0xNDY5NTk0MzA2XX0=
-->

# TROUBLESHOOTING


## "ValueError: strftime format ends with raw %" in template
* Problem with timestamp, add the settings below in ```settings.py```:
  ```python
  DATE_INPUT_FORMATS = ('%d-%m-%Y')
  #DATE_INPUT_FORMATS = ('%d-%m-%Y','%Y-%m-%d')


  USE_I18N = True


  USE_L10N = True
  ```


<!--stackedit_data:
eyJoaXN0b3J5IjpbMTczMzI4MjgzMl19
-->

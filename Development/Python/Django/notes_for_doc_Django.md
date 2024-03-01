https://stackoverflow.com/questions/19719330/django-httpresponse-stripping-cr
https://stackoverflow.com/questions/8600843/serving-large-files-with-high-loads-in-django


================================
https://stackoverflow.com/questions/891696/jquery-what-is-the-best-way-to-restrict-number-only-input-for-textboxes-all:
If you want to restrict input (as opposed to validation), you could work with the key events. something like this:


<input type="text" class="numbersOnly" value="" />
And:


jQuery('.numbersOnly').keyup(function () { 
```javascript
this.value = this.value.replace(/[^0-9\\.]/g,'');
```
});
This immediately lets the user know that they can't enter alpha characters, etc. rather than later during the validation phase.


You'll still want to validate because the input might be filled in by cutting and pasting with the mouse or possibly by a form autocompleter that may not trigger the key events.
r the key events.
================================
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTYxMzUyNzA4OV19
-->

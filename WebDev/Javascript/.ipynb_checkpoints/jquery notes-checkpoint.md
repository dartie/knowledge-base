# jQuery


## detect event with jquery of a specific element
### .event(func()){...}


```javascript
$('element').change(function() { // do something } );


$( "#target" ).keyup(function() {
  alert( "Handler for .keyup() called." );
});
```


* example:
```javascript
$('#roam').change(function switch_roam() {
    var roam_status = $('#roam').is(":checked");
    if (roam_status){
        $("#roam_days").prop("disabled", false);
    }
    else {
        $("#roam_days").prop("disabled", "disabled");
    }
} );
```


### .on('event1 event2 ...', function (){...});
```javascript
$("#element").on('keyup change', function (){
   // Your stuff...
});
```






question:
- element is id or name? 


test it because with id should be #id_element, whereas element maybe is the name




// alternative javascript


$(function() {
```javascript
var content = $('#myContent').val();
```


```javascript
$('#myContent').keyup(function() { 
    if ($('#myContent').val() != content) {
        content = $('#myContent').val();
        alert('Content has been changed');
    }
});
```
});


### detect event with jquery of all element with a specific class


jQuery('.numbersOnly').keyup(function () { // do something } );






### show/hide
https://www.w3schools.com/jquery/jquery_hide_show.asp


equivalent javascript: https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp


function myFunction() {
```javascript
var x = document.getElementById('myDIV');
if (x.style.display === 'none') {
    x.style.display = 'block';
} else {
    x.style.display = 'none';
}
```
}




### enable/disable element jquery
http://www.jquerybyexample.net/2012/07/how-to-disable-enable-element-with-jquery.html




### trigger event
use in case an object change the triggers event and not the user. This will trigger the event with code.
```javascript
$("#single").val("Single2").trigger('change');


    $('#datepicker_exp').trigger("change"); 


```


### tick\\untick checkbox
```javascript
$('#myCheckbox').prop('checked', true); // Checks it
$('#myCheckbox').prop('checked', false); // Unchecks it


```


####jQuery (1.6+):
```javascript
// Check
$("#checkbox").prop("checked", true);


// Uncheck
$("#checkbox").prop("checked", false);
```




####jQuery (1.5-):
```javascript
// Check
$("#checkbox").attr("checked", true);


// Uncheck
$("#checkbox").attr("checked", false);
```






### if checkbox is checked
```javascript
if ($('input.checkbox_check').is(':checked')) {
```


### hide\\show elements
```javascript
$("#hide").click(function(){
    $("p").hide();
});


$("#show").click(function(){
    $("p").show();
});


$("button").click(function(){
    $("p").toggle();
});
```




## toggle button content
```javascript
$(document).ready(function(){
    $('.editbtn').click(function(){
        $(this).html($(this).html() == 'edit' ? 'modify' : 'edit');
    });
});
```


## remove a class for an element
```javascript
$('#collapse_licdata_panel').removeClass('in');
```






## Submit with jquery
1. Function definition
```javascript
// Post to the provided URL with the specified parameters.
function post(path, parameters) {
    var form = $('<form></form>');


    form.attr("method", "post");
    form.attr("action", path);


    $.each(parameters, function(key, value) {
        var field = $('<input></input>');


        field.attr("type", "hidden");
        field.attr("name", key);
        field.attr("value", value);


        form.append(field);
    });


    // The form needs to be a part of the document in
    // order for us to be able to submit it.
    $(document.body).append(form);
    form.submit();
}
```




1. Function call
```javascript
post('/contact/', {name: 'Johnny Bravo'});
    // order for us to be able to submit it.
    $(document.body).append(form);
    form.submit();
}
```


1. Function call
```javascript
post('/contact/', {name: 'Johnny Bravo'});
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbOTA2MzM1OTksOTk2NDMyNDQ0LDEwNjY4ND
I0MiwtMTE2NjA0NzUxMF19
-->

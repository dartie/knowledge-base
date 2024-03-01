## Get text from element
**innerText**  returns: `"This element has extra spacing and contains a span element."`  
**innerHTML**  returns: `" This element has extra spacing and contains <span>a span element</span>."`  
**textContent**  returns: `" This element has extra spacing and contains a span element."`

The innerText property returns just the text, without spacing and inner element tags.  
The innerHTML property returns the text, including all spacing and inner element tags.  
The textContent property returns the text with spacing, but without inner element tags.

## Strip
```javascript
function strip(str, remove) {
  while (str.length > 0 && remove.indexOf(str.charAt(0)) != -1) {
    str = str.substr(1);
  }
  while (str.length > 0 && remove.indexOf(str.charAt(str.length - 1)) != -1) {
    str = str.substr(0, str.length - 1);
  }
  return str;
}
```


## Accept only numbers in textbox
```javascript
function isNumber(evt) {
    evt = (evt) ? evt : window.event;
    var charCode = (evt.which) ? evt.which : evt.keyCode;
    if (charCode > 31 && (charCode < 48 || charCode > 57)) {
        return false;
    }
    return true;
}
```

## Replace
### using "regex"
```javascript
text = text.replace(/<br>/g, /\\r\\n/);
```


### using "replace" method
```javascript
text = text.replace("<br>", "\\r\\n");
```


### using "join"
```javascript
text = text.split("<br>").join("\\r\\n")
```


### replace carriage return to html format
```javascript
text = text.replace(/\\r?\\n|\\r/g, '<br>');
```


## List
### Get unique elements from a list
```javascript
var unique = arr.filter(function(elem, index, self) {
    return index == self.indexOf(elem);
})
```


### Get Max value from array
```javascript
var maxDate = new Date(Math.max.apply(null, dates));
```


### Get Min value from array
```javascript
var maxDate = new Date(Math.min.apply(null, dates));
```


### Move an element (of which you know the index) to the end of an array, do this:
```javascript
array.push(array.splice(index, 1)[0]);
```


### If you don't have the index, and only the element, then do this:
```javascript
array.push(array.splice(array.indexOf(element), 1)[0]);
```


```javascript
/* Example: */


var arr = [1, 2, 6, 3, 4, 5];
arr.push(arr.splice(arr.indexOf(6), 1)[0]);
console.log(arr); // [1, 2, 3, 4, 5, 6]
```




### Move an element to the end of an array:
```javascript
var ary = [8,1,2,3,4,5,6,7];
ary.push(ary.shift());  // results in [1, 2, 3, 4, 5, 6, 7, 8]
```




### 3
```javascript
input_list.push(input_list.splice(index, 1)[0]);
```




### Move an element to the beginning of an array:
```javascript
var value_to_move = input_list[index];
input_list.splice(index, 1);
input_list.splice(dest_position, 0, value_to_move);
```




## Dates
### Date to string 
```javascript
date.toString()
```


### Date to string (custom format)
```javascript
var monthNames = [
    "jan", "feb", "mar",
    "apr", "May", "jun", "jul",
    "aug", "sep", "oct",
    "nov", "dec"
];


function formatDate(date) {
  var day = date.getDate();
  var monthIndex = date.getMonth();
  var year = date.getFullYear();


  return day + '-' + monthNames[monthIndex] + '-' + year;
}
```




### Reference: https://www.w3schools.com/js/js_date_formats.asp




## Regex
### Notes To keep in mind:
* The "delimiters" / are should not be part of the expression
* If you define an expression as string, you have to escape the backslash, because it is the escape character in strings


* Characters to escape
```javascript
. \\ + * ? [ ^ ] $ ( ) { } = ! < > | : -
```


### Create a Regex object
```javascript
var regex = new RegExp('\\\\d\\\\.\\\\d');


```


### Regex can be composed by more strings
```javascript
var regex_prefix = '(';
var regex_suffix = ').*';
var regex = new RegExp(regex_prefix + VMlist[i] + regex_suffix);
```


### Find all matching elements
```javascript
var input = "A string with 3 numbers in it... 42 and 88.";
var number = /\\b(\\d+)\\b/g;
var match;
while (match = number.exec(input)){
  console.log("Found", match[1], "at", match.index);
}
```

```javascript
/* 4 */ // function, in order to work as in python
function regex_findall(regex, text){
 
    var match;
    var matches_total = [];
    do {
        match = regex.exec(text);
        if (match) {
            
            for(var i=0; i < match.length; i++){
                if(i==0){
                    continue;  // skip the full match string
                }
                matches_total.push(match[i]);
            }

        }
        
    } while (match);

    return matches_total;
}

all_matches_text = regex_findall(regex, text); // function call 
```


### Back in browser
```javascript
window.history.back()
```


### make page to tell browser not to cache preserve input values
```javascript
<form autocomplete="off" ...></form>
```




## Split
### Standard
```javascript
var sep_char = '_';
var text = "Dario_Necco";
text_split = text.split(sep_char);
```


### Split only the first instance/occurrence
```javascript
var sep_char = '_';
regex_split = new RegExp(sep_char + '(.+)');
nametext_split = nametext.split(regex_split);
```






## Save Text as File
```javascript
function saveTextAsFile()
{
    var textToSave = document.getElementById("inputTextToSave").value;
    var textToSaveAsBlob = new Blob([textToSave], {type:"text/plain"});
    var textToSaveAsURL = window.URL.createObjectURL(textToSaveAsBlob);
    var fileNameToSaveAs = document.getElementById("inputFileNameToSaveAs").value;
 
    var downloadLink = document.createElement("a");
    downloadLink.download = fileNameToSaveAs;
    downloadLink.innerHTML = "Download File";
    downloadLink.href = textToSaveAsURL;
    downloadLink.onclick = destroyClickedElement;
    downloadLink.style.display = "none";
    document.body.appendChild(downloadLink);
 
    downloadLink.click();
}
 
 
function destroyClickedElement(event)
{
    document.body.removeChild(event.target);
}
```

## Handles html elements

### iframe
```javascript
document.getElementById("iframe_id").contentWindow.location.href
```


## Listener

### 1
```javascript
function myFunction() {
  alert ("Hello World!");
}

document.getElementById("autosar").addEventListener("click", myFunction);
```

### 2
```javascript
element.addEventListener("click", myFunction);

function myFunction() {
  alert ("Hello World!");
}
```


## onload
run functions when the window is loaded
```javascript
window.onload=my_code();
```

# Missing built-in methods
## remove duplicates ("set" in python)
```javascript
function remove_duplicates(arr){   
    var unique = arr.filter(function(elem, index, self) {
            return index == self.indexOf(elem);
        });


    return unique
}
```


## Check if Substring in String (in python is: 'substring' in 'String')
1. indexOf
```javascript
var string = "foo",
    substring = "oo";
string.indexOf(substring) !== -1;
String.prototype.indexOf returns the position of the string in the other string. If not found, it will return -1.
```


2. (ES6) includes - go to answer, or this answer
```javascript
var string = "foo",
    substring = "oo";
string.includes(substring);
```


3. search - go to answer
```javascript
var string = "foo",
    expr = /oo/;
string.search(expr);
```


4. lodash includes - go to answer
```javascript
var string = "foo",
    substring = "oo";
_.includes(string, substring);
```


5. RegExp - go to answer
```javascript
var string = "foo",
    expr = /oo/;  // no quotes here
expr.test(string);
```


6. Match - go to answer
```javascript
var string = "foo",
    expr = /oo/;
string.match(expr);
```


## Retrieve all elements of a table or any tag
```javascript
var anchor = [];
var container;
var items;


container = document.getElementById('myTable');
items = container.getElementsByTagName('div');


for (var j = 0; j < items.length; j++) {
    var text = items[j].textContent;
    text = strip(text, ' ');
    anchor.push(text);
}
```


## Check\\Uncheck checkbox
```javascript
// Check
document.getElementById("checkbox").checked = true;


// Uncheck
document.getElementById("checkbox").checked = false;
```




## Submit with javascript
1. Function definition
```javascript
function post(path, params, method) {
    method = method || "post"; // Set method to post by default if not specified.


    // The rest of this code assumes you are not using a library.
    // It can be made less wordy if you use one.
    var form = document.createElement("form");
    form.setAttribute("method", method);
    form.setAttribute("action", path);


    for(var key in params) {
        if(params.hasOwnProperty(key)) {
            var hiddenField = document.createElement("input");
            hiddenField.setAttribute("type", "hidden");
            hiddenField.setAttribute("name", key);
            hiddenField.setAttribute("value", params[key]);

            form.appendChild(hiddenField);
        }
    }

    document.body.appendChild(form);
    form.submit();
}

```

1. Function call
```javascript
post('/contact/', {name: 'Johnny Bravo'});
         hiddenField.setAttribute("name", key);
            hiddenField.setAttribute("value", params[key]);


            form.appendChild(hiddenField);
        }
    }


    document.body.appendChild(form);
    form.submit();
}


```


1. Function call
```javascript
post('/contact/', {name: 'Johnny Bravo'});
```


## Replace accented characters
```javascript
function convert_accented_characters(str){
    var conversions = new Object();
    conversions['ae'] = 'ä|æ|ǽ';
    conversions['oe'] = 'ö|œ';
    conversions['ue'] = 'ü';
    conversions['Ae'] = 'Ä';
    conversions['Ue'] = 'Ü';
    conversions['Oe'] = 'Ö';
    conversions['A'] = 'À|Á|Â|Ã|Ä|Å|Ǻ|Ā|Ă|Ą|Ǎ';
    conversions['a'] = 'à|á|â|ã|å|ǻ|ā|ă|ą|ǎ|ª';
    conversions['C'] = 'Ç|Ć|Ĉ|Ċ|Č';
    conversions['c'] = 'ç|ć|ĉ|ċ|č';
    conversions['D'] = 'Ð|Ď|Đ';
    conversions['d'] = 'ð|ď|đ';
    conversions['E'] = 'È|É|Ê|Ë|Ē|Ĕ|Ė|Ę|Ě';
    conversions['e'] = 'è|é|ê|ë|ē|ĕ|ė|ę|ě';
    conversions['G'] = 'Ĝ|Ğ|Ġ|Ģ';
    conversions['g'] = 'ĝ|ğ|ġ|ģ';
    conversions['H'] = 'Ĥ|Ħ';
    conversions['h'] = 'ĥ|ħ';
    conversions['I'] = 'Ì|Í|Î|Ï|Ĩ|Ī|Ĭ|Ǐ|Į|İ';
    conversions['i'] = 'ì|í|î|ï|ĩ|ī|ĭ|ǐ|į|ı';
    conversions['J'] = 'Ĵ';
    conversions['j'] = 'ĵ';
    conversions['K'] = 'Ķ';
    conversions['k'] = 'ķ';
    conversions['L'] = 'Ĺ|Ļ|Ľ|Ŀ|Ł';
    conversions['l'] = 'ĺ|ļ|ľ|ŀ|ł';
    conversions['N'] = 'Ñ|Ń|Ņ|Ň';
    conversions['n'] = 'ñ|ń|ņ|ň|ŉ';
    conversions['O'] = 'Ò|Ó|Ô|Õ|Ō|Ŏ|Ǒ|Ő|Ơ|Ø|Ǿ';
    conversions['o'] = 'ò|ó|ô|õ|ō|ŏ|ǒ|ő|ơ|ø|ǿ|º';
    conversions['R'] = 'Ŕ|Ŗ|Ř';
    conversions['r'] = 'ŕ|ŗ|ř';
    conversions['S'] = 'Ś|Ŝ|Ş|Š';
    conversions['s'] = 'ś|ŝ|ş|š|ſ';
    conversions['T'] = 'Ţ|Ť|Ŧ';
    conversions['t'] = 'ţ|ť|ŧ';
    conversions['U'] = 'Ù|Ú|Û|Ũ|Ū|Ŭ|Ů|Ű|Ų|Ư|Ǔ|Ǖ|Ǘ|Ǚ|Ǜ';
    conversions['u'] = 'ù|ú|û|ũ|ū|ŭ|ů|ű|ų|ư|ǔ|ǖ|ǘ|ǚ|ǜ';
    conversions['Y'] = 'Ý|Ÿ|Ŷ';
    conversions['y'] = 'ý|ÿ|ŷ';
    conversions['W'] = 'Ŵ';
    conversions['w'] = 'ŵ';
    conversions['Z'] = 'Ź|Ż|Ž';
    conversions['z'] = 'ź|ż|ž';
    conversions['AE'] = 'Æ|Ǽ';
    conversions['ss'] = 'ß';
    conversions['IJ'] = 'Ĳ';
    conversions['ij'] = 'ĳ';
    conversions['OE'] = 'Œ';
    conversions['f'] = 'ƒ';
    for(var i in conversions){
        var re = new RegExp(conversions[i],"g");
        str = str.replace(re,i);
    }
    return str;
}

// function call
var text = convert_accented_characters(text);
```

### Alternatives
* http://semplicewebsites.com/removing-accents-javascript

## Equivalent jQuery methods
### .load()
```javascript
function load(url, element)
{
    req = new XMLHttpRequest();
    req.open("GET", url, false);
    req.send(null);

    element.innerHTML = req.responseText; 
}

/* Usage */
load("x.html", document.getElementById("b"));
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTg1NTYyODM3MSwtNTAyNDQzMTA3LC0zND
UzODk0NTQsMTYyNDY1MTA5MCw3ODI5NzYxMDIsLTE3NDk4NDE1
ODMsLTk5ODAzNzE5NSwtMTU3OTQxNjU3OSwxNTY3MzM0ODU5LC
0yMDAyMzM2MzU1LC0xNDM4Njc1MTUwXX0=
-->

# Acrobat Javascript
* Resource: https://www.adobe.com/content/dam/acom/en/devnet/acrobat/pdfs/Acro6JS1.pdf


## Select element
```javascript
var element = this.getField("textbox")
```


## get form element value
```javascript
var textbox_value = this.getField("textbox").value
```


## get form element value (force as string)
```javascript
var textbox_value = this.getField("textbox").valueAsString
```
## get element name
```javascript
var name = event.target.name

// OR

var name2 = event.targetName
```

## get last digit of element name
```javascript
var last_digit = event.target.name.substring(event.target.name.length - 1)
```

## Regex
```javascript
// Set up array of regular expressions  
var aRE = [ 
/^00(:|-)?50(:|-)?56.*/, 
/^00(:|-)?0C(:|-)?29.*/,
/^00(:|-)?05(:|-)?69.*/,
/^00(:|-)?03(:|-)?FF.*/,
/^00(:|-)?1C(:|-)?42.*/,
/^00(:|-)?0F(:|-)?4B.*/,
/^00(:|-)?16(:|-)?3E.*/,
/^00(:|-)?16(:|-)?3E.*/,
/^08(:|-)?00(:|-)?27.*/,
];




var res =  AFExactMatch(aRE, text);
```


## Set text color for an element
```javascript
element.textColor = color.red;
```


## check on the current element
```javascript
event.rc = true;
if (event.value != "" && event.value != "AAAA" && event.value != "BBBB")
{
    app.alert("The entered value needs to be either 'AAAA' or 'BBBB'!");
    event.target.textColor = color.red;
}
else
{
    event.target.textColor = color.black;
}
```

## Date

### get current date and time
```javascript
// Get the current date and time 
var rightNow = new Date();
```

### convert date/time to milliseconds
```javascript
var msRightNow = rightNow.getTime(); 
```

### Calculate days in milliseconds
```javascript
// Calculate 5 days in milliseconds, 
// 5 days x 24 hrs/day x 60 min/hr x 60 sec/min x 1000 ms/sec 
var delta = ndays * 24 * 60 * 60 * 1000; 
```

### Sum milliseconds
```javascript
var finalTime = msRightNow + delta; 
```

### Create date from milliseconds
```javascript
// Create a new Date from 
// the calculated value 
var theNewDate = new Date(finalTime); 
```

### Get date with a specific format 
```javascript
var newDateStr = util.printd("dd/mm/yyyy", theNewDate);
```

## tick checkbox
```javascript
this.getField("reprise_download_links").value="Yes";
```


## untick checkbox
```javascript
this.getField("reprise_download_links").value="Off";
```

## set element readonly
```javascript
this.getField("reprise_download_links").readonly=true;
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTQxMjUwMDIwLDEyODM3NzAzMDQsMTMwNT
g5ODM1XX0=
-->

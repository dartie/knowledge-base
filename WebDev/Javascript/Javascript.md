# Javascript

## Communicate with the server without submit
* https://developer.mozilla.org/en-US/docs/Web/Guide/AJAX/Getting_Started
* https://www.w3schools.com/asp/asp_ajax_asp.asp
* https://stackoverflow.com/questions/14220321/how-do-i-return-the-response-from-an-asynchronous-call
* https://javascript.info/xmlhttprequest

```javascript
var xmlhttp = new XMLHttpRequest();
xmlhttp.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {
      let response = this.responseText;
      // execute code to run once you have got the response
  }
};
xmlhttp.open("GET", "URL", true);  // replace URL with the actual url
xmlhttp.send();
```

In case of objects, the server needs to return a json result

Flask: use `jsonify({ })`


### Dedicated function for ajax
1. Best

```javascript
function AJAX(url) {
return new Promise(function(resolve, reject) {
  var xhr = new XMLHttpRequest();
  xhr.onload = function() {
    resolve(this.responseText);
  };
  xhr.onerror = reject;
  xhr.open('GET', url);
  xhr.send();
});
}


function custom_function(){
  AJAX("/update_devices")
  .then(function(result) {
      // Code depending on result
      console.log('AJAX: ', result)  // execute if everything is successfull 
  })
  .catch(function() {
      // An error occurred
  });
}
```

or (by W3Schools)

```javascript
loadDoc("url-1", myFunction1);

loadDoc("url-2", myFunction2);

function loadDoc(url, cFunction) {
var xhttp;
xhttp=new XMLHttpRequest();
xhttp.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {
    cFunction(this);
  }
 };
xhttp.open("GET", url, true);
xhttp.send();
}

function myFunction1(xhttp) {
// action goes here
}
function myFunction2(xhttp) {
// action goes here
}
```


2. Deprecated
Solution which is going to be deprecated due to the third parameter in `.open` which needs to be `true`

```javascript
function AJAX(url, cb) {
var xhr = new XMLHttpRequest();
xhr.open("GET", url, false);
xhr.send(null);
if (xhr.status === 200) {
  //console.log(xhr.responseText);
  cb(xhr.responseText);
}
}


function save_changes(){
  AJAX("/update_devices", function(data) {
    console.log('AJAX: ', data);  // execute the code once the response has been got
  })
}
```



## Repeat function every n seconds
https://javascript.info/settimeout-setinterval

```javascript
function sayHi() {
alert('Hello');
  
setTimeout(sayHi, 1000);
}

setTimeout(sayHi, 1000);
```


## Iterate a Html table
```javascript
var table=document.getElementById("mytab1");
var r=0;
while(row=table.rows[r++])
{
var c=0;
while(cell=row.cells[c++])
{
  cell.innerHTML='[Row='+r+',Col='+c+']'; // do sth with cell
}
}
```

or

```javascript
var table = document.getElementById("mytab1");
for (var i = 0, row; row = table.rows[i]; i++) {
 //iterate through rows
 //rows would be accessed using the "row" variable assigned in the for loop
 for (var j = 0, col; col = row.cells[j]; j++) {
   //iterate through columns
   //columns would be accessed using the "col" variable assigned in the for loop
 }  
}
```

Iterating all cells ignoring the row
```javascript
var table = document.getElementById("mytab1");
for (var i = 0, cell; cell = table.cells[i]; i++) {
   //iterate through cells
   //cells would be accessed using the "cell" variable assigned in the for loop
}
```

## Trigger event

### Old way

```javascript
// Add an event listener
document.addEventListener("name-of-event", function(e) {
  console.log(e.detail); // Prints "Example of an event"
});
```

### Without passing arguments

```javascript
document.querySelector("#myElement").onclick = myFunction; // without parenthesis 
```

### setAttribute()

```javascript
document.querySelector("#myElement").setAttribute("onsubmit", "return myFunction(arg1, arg2);");
```

### Binding multiple events to a listener?

```javascript
/* Add one or more listeners to an element
** @param {DOMElement} element - DOM element to add listeners to
** @param {string} eventNames - space separated list of event names, e.g. 'click change'
** @param {Function} listener - function to attach for each event as a listener
*/
function addListenerMulti(element, eventNames, listener) {
var events = eventNames.split(' ');
for (var i=0, iLen=events.length; i<iLen; i++) {
  element.addEventListener(events[i], listener, false);
}
}

addListenerMulti(window, 'mousemove touchmove', function(){…});
```

or 

```javascript
['mousemove', 'touchmove'].forEach(function(e) {
window.addEventListener(e, mouseMoveHandler);
});
```

## Set current date/time to input element

```javascript
var date = new Date();
var currentDate = date.toISOString().substring(0,10);
var currentTime = date.toISOString().substring(11,16);

document.getElementById('currentDate').value = currentDate;
document.getElementById('currentTime').value = currentTime;
```

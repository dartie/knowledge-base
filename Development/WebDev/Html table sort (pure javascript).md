# Html table sort (pure javascript)
[HTML Table Sorting with JavaScript](http://www.terrill.ca/sorting/)

<!-- toc -->

- [Terrill's solution](#Terrills-solution)
  * [Html code](#Html-code)
  * [javascript code](#javascript-code)
  * [css code](#css-code)
- [W3 School](#W3-School)

<!-- tocstop -->

## Terrill's solution

### Html code
```html
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="css/sort_arrows.css">
</head>
<body>

<h2>My Customers</h2>

<input type="text" id="myInput" onkeyup="myFunction()" placeholder="Search for names.." title="Type in a name">

<table id="myTable">
  <tr class="header">
    <th style="width:60%;">Name</th>
    <th style="width:40%;">Country</th>
  </tr>
  <tr>
    <td>Alfreds Futterkiste</td>
    <td>Germany</td>
  </tr>
  <tr>
    <td>Berglunds snabbkop</td>
    <td>Sweden</td>
  </tr>
  <tr>
    <td>Island Trading</td>
    <td>UK</td>
  </tr>
  <tr>
    <td>Koniglich Essen</td>
    <td>Germany</td>
  </tr>
  <tr>
    <td>Laughing Bacchus Winecellars</td>
    <td>Canada</td>
  </tr>
  <tr>
    <td>Magazzini Alimentari Riuniti</td>
    <td>Italy</td>
  </tr>
  <tr>
    <td>North/South</td>
    <td>UK</td>
  </tr>
  <tr>
    <td>Paris specialites</td>
    <td>France</td>
  </tr>
</table>

<script src="js/tsorter.min.js" type="text/javascript"></script>

</body>
</html>
```

### javascript code
tsorter.min.js
```
/*!
 * tsorter 2.0.0 - Copyright 2015 Terrill Dent, http://terrill.ca
 * JavaScript HTML Table Sorter
 * Released under MIT license, http://terrill.ca/sorting/tsorter/LICENSE
 */
var tsorter=function(){"use strict";var a,b,c,d=!!document.addEventListener;return Object.create||(Object.create=function(a){var b=function(){return void 0};return b.prototype=a,new b}),b=function(a,b,c){d?a.addEventListener(b,c,!1):a.attachEvent("on"+b,c)},c=function(a,b,c){d?a.removeEventListener(b,c,!1):a.detachEvent("on"+b,c)},a={getCell:function(a){var b=this;return b.trs[a].cells[b.column]},sort:function(a){var b=this,c=a.target;b.column=c.cellIndex,b.get=b.getAccessor(c.getAttribute("data-tsorter")),b.prevCol===b.column?(c.className="ascend"!==c.className?"ascend":"descend",b.reverseTable()):(c.className="ascend",-1!==b.prevCol&&"exc_cell"!==b.ths[b.prevCol].className&&(b.ths[b.prevCol].className=""),b.quicksort(0,b.trs.length)),b.prevCol=b.column},getAccessor:function(a){var b=this,c=b.accessors;if(c&&c[a])return c[a];switch(a){case"link":return function(a){return b.getCell(a).firstChild.firstChild.nodeValue};case"input":return function(a){return b.getCell(a).firstChild.value};case"numeric":return function(a){return parseFloat(b.getCell(a).firstChild.nodeValue,10)};default:return function(a){return b.getCell(a).firstChild.nodeValue}}},exchange:function(a,b){var c,d=this,e=d.tbody,f=d.trs;a===b+1?e.insertBefore(f[a],f[b]):b===a+1?e.insertBefore(f[b],f[a]):(c=e.replaceChild(f[a],f[b]),f[a]?e.insertBefore(c,f[a]):e.appendChild(c))},reverseTable:function(){var a,b=this;for(a=1;a<b.trs.length;a++)b.tbody.insertBefore(b.trs[a],b.trs[0])},quicksort:function(a,b){var c,d,e,f=this;if(!(a+1>=b)){if(b-a===2)return void(f.get(b-1)>f.get(a)&&f.exchange(b-1,a));for(c=a+1,d=b-1,f.get(a)>f.get(c)&&f.exchange(c,a),f.get(d)>f.get(a)&&f.exchange(a,d),f.get(a)>f.get(c)&&f.exchange(c,a),e=f.get(a);;){for(d--;e>f.get(d);)d--;for(c++;f.get(c)>e;)c++;if(c>=d)break;f.exchange(c,d)}f.exchange(a,d),b-d>d-a?(f.quicksort(a,d),f.quicksort(d+1,b)):(f.quicksort(d+1,b),f.quicksort(a,d))}},init:function(a,c,d){var e,f=this;for("string"==typeof a&&(a=document.getElementById(a)),f.table=a,f.ths=a.getElementsByTagName("th"),f.tbody=a.tBodies[0],f.trs=f.tbody.getElementsByTagName("tr"),f.prevCol=c&&c>0?c:-1,f.accessors=d,f.boundSort=f.sort.bind(f),e=0;e<f.ths.length;e++)b(f.ths[e],"click",f.boundSort)},destroy:function(){var a,b=this;if(b.ths)for(a=0;a<b.ths.length;a++)c(b.ths[a],"click",b.boundSort)}},{create:function(b,c,d){var e=Object.create(a);return e.init(b,c,d),e}}}();
```


In the html page of the table, init the tsorter

```javascript
function init() {
  var sorter = tsorter.create('TABLE-ID');
}
  
window.onload = init;
```


### css code
sort_arrows.css
```css
/* Up and Down Arrows */
.sortable th.descend:after{
	content: "\25B2";
	}
.sortable th.ascend:after{
	content: "\25BC";
	}
```


## W3 School
[How To Sort a Table](https://www.w3schools.com/howto/howto_js_sort_table.asp)

```html
<!DOCTYPE html>
<html>
<head>
<title>Sort a HTML Table Alphabetically</title>
<style>
table {
  border-spacing: 0;
  width: 100%;
  border: 1px solid #ddd;
}

th {
  cursor: pointer;
}

th, td {
  text-align: left;
  padding: 16px;
}

tr:nth-child(even) {
  background-color: #f2f2f2
}
</style>
</head>
<body>

<p><strong>Click the headers to sort the table.</strong></p>
<p>The first time you click, the sorting direction is ascending (A to Z).</p>
<p>Click again, and the sorting direction will be descending (Z to A):</p>

<table id="myTable">
  <tr>
   <!--When a header is clicked, run the sortTable function, with a parameter, 0 for sorting by names, 1 for sorting by country:-->  
    <th onclick="sortTable(0)">Name</th>
    <th onclick="sortTable(1)">Country</th>
  </tr>
  <tr>
    <td>Berglunds snabbkop</td>
    <td>Sweden</td>
  </tr>
  <tr>
    <td>North/South</td>
    <td>UK</td>
  </tr>
  <tr>
    <td>Alfreds Futterkiste</td>
    <td>Germany</td>
  </tr>
  <tr>
    <td>Koniglich Essen</td>
    <td>Germany</td>
  </tr>
  <tr>
    <td>Magazzini Alimentari Riuniti</td>
    <td>Italy</td>
  </tr>
  <tr>
    <td>Paris specialites</td>
    <td>France</td>
  </tr>
  <tr>
    <td>Island Trading</td>
    <td>UK</td>
  </tr>
  <tr>
    <td>Laughing Bacchus Winecellars</td>
    <td>Canada</td>
  </tr>
</table>

<script>
function sortTable(n) {
  var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
  table = document.getElementById("myTable");
  switching = true;
  //Set the sorting direction to ascending:
  dir = "asc"; 
  /*Make a loop that will continue until
  no switching has been done:*/
  while (switching) {
    //start by saying: no switching is done:
    switching = false;
    rows = table.rows;
    /*Loop through all table rows (except the
    first, which contains table headers):*/
    for (i = 1; i < (rows.length - 1); i++) {
      //start by saying there should be no switching:
      shouldSwitch = false;
      /*Get the two elements you want to compare,
      one from current row and one from the next:*/
      x = rows[i].getElementsByTagName("TD")[n];
      y = rows[i + 1].getElementsByTagName("TD")[n];
      /*check if the two rows should switch place,
      based on the direction, asc or desc:*/
      if (dir == "asc") {
        if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
          //if so, mark as a switch and break the loop:
          shouldSwitch= true;
          break;
        }
      } else if (dir == "desc") {
        if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
          //if so, mark as a switch and break the loop:
          shouldSwitch = true;
          break;
        }
      }
    }
    if (shouldSwitch) {
      /*If a switch has been marked, make the switch
      and mark that a switch has been done:*/
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
      //Each time a switch is done, increase this count by 1:
      switchcount ++;      
    } else {
      /*If no switching has been done AND the direction is "asc",
      set the direction to "desc" and run the while loop again.*/
      if (switchcount == 0 && dir == "asc") {
        dir = "desc";
        switching = true;
      }
    }
  }
}
</script>

</body>
</html>
```

**Sort Table Numerically**
```html
<!DOCTYPE html>
<html>
<head>
<title>Sort a HTML Table Numerically</title>
<style>
table {
  border-spacing: 0;
  width: 100%;
  border: 1px solid #ddd;
}

th, td {
  text-align: left;
  padding: 16px;
}

tr:nth-child(even) {
  background-color: #f2f2f2
}
</style>
</head>
<body>

<p>Click the button to sort the table numerically:</p>
<p><button onclick="sortTable()">Sort</button></p>

<table id="myTable">
  <tr>
    <th>ID</th>
    <th>Name</th>
  </tr>
  <tr>
    <td>5</td>
    <td>Berglunds snabbkop</td>
  </tr>
  <tr>
    <td>3</td>
    <td>North/South</td>
  </tr>
  <tr>
    <td>6</td>
    <td>Alfreds Futterkiste</td>
  </tr>
  <tr>
    <td>2</td>
    <td>Koniglich Essen</td>
  </tr>
  <tr>
    <td>1</td>
    <td>Magazzini Alimentari Riuniti</td>
  </tr>
  <tr>
    <td>7</td>
    <td>Paris specialites</td>
  </tr>
  <tr>
    <td>4</td>
    <td>Island Trading</td>
  </tr>
 
</table>

<script>
function sortTable() {
  var table, rows, switching, i, x, y, shouldSwitch;
  table = document.getElementById("myTable");
  switching = true;
  /*Make a loop that will continue until
  no switching has been done:*/
  while (switching) {
    //start by saying: no switching is done:
    switching = false;
    rows = table.rows;
    /*Loop through all table rows (except the
    first, which contains table headers):*/
    for (i = 1; i < (rows.length - 1); i++) {
      //start by saying there should be no switching:
      shouldSwitch = false;
      /*Get the two elements you want to compare,
      one from current row and one from the next:*/
      x = rows[i].getElementsByTagName("TD")[0];
      y = rows[i + 1].getElementsByTagName("TD")[0];
      //check if the two rows should switch place:
      if (Number(x.innerHTML) > Number(y.innerHTML)) {
        //if so, mark as a switch and break the loop:
        shouldSwitch = true;
        break;
      }
    }
    if (shouldSwitch) {
      /*If a switch has been marked, make the switch
      and mark that a switch has been done:*/
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
    }
  }
}
</script>

</body>
</html>
```

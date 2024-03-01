# HTML

## Add options to datalist 

### 1

```html
<input name="car" list="anrede" />
<datalist id="anrede"></datalist>

<script type="text/javascript">
  var mycars = new Array();
  mycars[0]='Herr';
  mycars[1]='Frau';

  var options = '';

  for(var i = 0; i < mycars.length; i++)
    options += '<option value="'+mycars[i]+'" />';

  document.getElementById('anrede').innerHTML = options;
</script>
```


### 2
```html
<!DOCTYPE html>
<html>
<body>

<p>Click the button to create an INPUT field, a DATALIST element and an OPTION element.</p>

<form id="myForm">
</form>

<button onclick="myFunction()">Try it</button>

<p><strong>Note:</strong> The datalist element is not supported in Internet Explorer 9 and earlier versions, or in Safari.</p>

<script>
function myFunction() {
    var x = document.createElement("INPUT");
    x.setAttribute("list", "browsers");
    document.getElementById("myForm").appendChild(x);

    var y = document.createElement("DATALIST");
    y.setAttribute("id", "browsers");
    document.getElementById("myForm").appendChild(y);

    var z = document.createElement("OPTION");
    z.setAttribute("value", "Chrome");
    document.getElementById("browsers").appendChild(z);
}
</script>

</body>
</html>


```

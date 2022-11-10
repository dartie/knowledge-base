## Combobox
### Links
* https://www.aspsnippets.com/Articles/Call-JavaScript-function-on-SelectedIndexChanged-of-HTML-DropDownList-using-JavaScript-and-jQuery.aspx
* http://jsfiddle.net/JGp9e/
* https://silviomoreto.github.io/bootstrap-select/examples/
* https://getbootstrap.com/docs/3.3/components/#btn-dropdowns



### Video

* https://www.youtube.com/watch?v=e6VYRVRoC40
* https://www.youtube.com/playlist?annotation_id=annotation_303471105&feature=iv&list=PLvAAZChoagM3Ch63apDSE6Ra6NeI62sQV&src_vid=e6VYRVRoC40
* https://www.youtube.com/watch?v=6FbSf2P39LI
* https://www.youtube.com/watch?v=oxGmXOKazw0



### Snippets

* Html
```html
<select name="dropdown" size=1>
    <option value="1">option 1</option>
    <option value="2">option 2</option>
</select>
```

* js
```
$('select[name="dropdown"]').change(function(){
  
    if ($(this).val() == "2")
        alert("call the do something function on option 2");
    
});
```

## Combox sol 3
```html
Select Fruit:
<select id="ddlFruits" onchange="GetSelectedTextValue(this)">
    <option value=""></option>
    <option value="1">Apple</option>
    <option value="2">Mango</option>
    <option value="3">Orange</option>
</select>
<script type="text/javascript">
    function GetSelectedTextValue(ddlFruits) {
        var selectedText = ddlFruits.options[ddlFruits.selectedIndex].innerHTML;
        var selectedValue = ddlFruits.value;
        alert("Selected Text: " + selectedText + " Value: " + selectedValue);
    }
</script>
```



## Combox sol 4

```html
Select Fruit:
<select id="ddlFruits">
    <option value=""></option>
    <option value="1">Apple</option>
    <option value="2">Mango</option>
    <option value="3">Orange</option>
</select>
<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js"></script>
<script type="text/javascript">
    $(function () {
        $("#ddlFruits").change(function () {
            var selectedText = $(this).find("option:selected").text();
            var selectedValue = $(this).val();
            alert("Selected Text: " + selectedText + " Value: " + selectedValue);
        });
    });
</script>
```

## empty element in grid
```
<div class="col-md-2" >&nbsp;</div>
```

## Datatable
### link:
  * options: https://datatables.net/reference/option/dom
  * buttons: https://datatables.net/reference/button/#tabletools
  * checkbox: https://datatables.net/extensions/select/examples/initialisation/checkbox.html
  * row select: https://datatables.net/extensions/select/examples/api/select.html

  ````html
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>

<link rel="stylesheet" href="css/bootstrap.min.css">
<link rel="stylesheet" href="css/dataTables.bootstrap.min.css">
<link rel="stylesheet" href="css/jquery.dataTables.min.css">
<link rel="stylesheet" href="css/buttons.dataTables.min.css">

</head>
<body>

<!-- TESTCODE -->
<div>
<table id="example" class="table table-striped table-bordered" cellspacing="0" width="100%">
        <thead>
            <tr>
                <th>Name</th>
                <th>Position</th>
                <th>Office</th>
                <th>Age</th>
                <th>Start date</th>
                <th>Salary</th>
            </tr>
        </thead>
        <tfoot>
            <tr>
                <th>Name</th>
                <th>Position</th>
                <th>Office</th>
                <th>Age</th>
                <th>Start date</th>
                <th>Salary</th>
            </tr>
        </tfoot>
        <tbody>
            <tr>
                <td>Tiger Nixon</td>
                <td>System Architect</td>
                <td>Edinburgh</td>
                <td>61</td>
                <td>2011/04/25</td>
                <td>$320,800</td>
            </tr>
        </tbody>
    </table>

</div>
<!-- /TESTCODE -->

    <script src = "js/jquery.js"></script>
    <script src = "js/bootstrap.min.js"></script>
    <script src = "js/jquery.dataTables.min.js"></script>
    <script src = "js/dataTables.bootstrap.min.js"></script>
    
    
    <script src = "js/dataTables.buttons.min.js"></script>
    <script src = "js/jszip.min.js"></script>
    <script src = "js/pdfmake.min.js"></script>
    <script src = "js/vfs_fonts.js"></script>
    <script src = "js/buttons.html5.min.js"></script>
    <script src = "js/buttons.colVis.min.js"></script>

<script>
$(document).ready(function() {
    $('#example').DataTable( {
        dom: 'Blfrtip',
        buttons: [
            'copyHtml5',
            'excelHtml5',
            'csvHtml5',
            'pdfHtml5',
            'colvis'
        ],
        paging: true,
        lengthMenu: [[10, 25, 50, -1], [10, 25, 50, "All"]]
    } );
} );
</script>
    
</body>
</html>
  ````

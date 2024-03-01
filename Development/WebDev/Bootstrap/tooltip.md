# Tooltip

## Html element

* ```data-toggle``` : tooltip
* ```data-html``` : true (for supporting html, otherwise remove)
* ```style``` : set tooltip text style
* ```title``` : text

```html
<div data-toggle="tooltip" data-html="true" data-placement="left" style="text-align:left;" title="text"></div>
```



### Example

```html
<td data-toggle="tooltip" data-html="true" data-placement="left" style="text-align:left;" title="{{ field|get_prod_help }}">{{ field|replacecr_prod_sep }}</td>
```



## JavaScript code

```javascript
$(function () {
  $('[data-toggle="tooltip"]').tooltip()
});
```



* Call it

  ```javascript
  $('#Customer').tooltip({'trigger':'input', 'data-html':true, 'title': ''});
  ```

  **or**

  ```javascript
  $('#Customer').attr('title', 'NEW_TITLE')
  			  .tooltip('fixTitle')
  			  .tooltip('show');
  ```

  ​

## CSS code (only in case of custom settings)

```css
.tooltip {
    position: relative;
    display: inline-block;
    border-bottom: 1px dotted black;
}

.tooltip .tooltiptext {
    visibility: hidden;
    width: 120px;
    background-color: black;
    color: #fff;
    text-align: center;
    border-radius: 6px;
    padding: 5px 0;
    position: absolute;
    z-index: 1;
    top: 150%;
    left: 50%;
    margin-left: -60px;
}

.tooltip .tooltiptext::after {
    content: "";
    position: absolute;
    bottom: 100%;
    left: 50%;
    margin-left: -5px;
    border-width: 5px;
    border-style: solid;
    border-color: transparent transparent black transparent;
}

.tooltip:hover .tooltiptext {
    visibility: visible;
}

```



# Popup

## Html element

- ```class``` : add **popup**
- ```class``` : add **popuptext**
- ```data-html``` : true (for supporting html, otherwise remove)
- ```title``` : text
- ```onclick="show_popup(<element_id>)``` : 

```html
<div class="popup btn btn-primary" onclick="show_popup('RequestPopup')">Request ID:<span class="popuptext" data-html="true" id="RequestPopup">Text</span></div>
```



### Example

```html
<div class="popup btn btn-primary navbar-right" onclick="show_popup('RequestPopup')">Request ID: <span class="badge">{{request_id}}</span><span class="popuptext" data-html="true" id="RequestPopup">{{ request_id|get_request_popup|safe}}</span></div> <!-- works with text -->
```



## JavaScript code

```javascript
function show_popup(element_id) {
// When the user clicks on <div>, open the popup
    var popup = document.getElementById(element_id);
    popup.classList.toggle("show");
}
```



## CSS code (only in case of custom settings)

```css
/* Popup container */
.popup {
    position: relative;
    display: inline-block;
    cursor: pointer;
}

/* The actual popup (appears on top) */
.popup .popuptext {
    visibility: hidden;
    width: 300px;
    height: auto;
    background-color: #555;
    color: #fff;
    text-align: left;
    border-radius: 6px;
    padding: 20px 0;
    padding-left: 10px;
    position: absolute;
    z-index: 1;
    bottom: 90%;
    /*top: 100%;*/
    left: 50%;
    margin-left: -280px;
    white-space: pre;
}

/* Popup arrow */
.popup .popuptext::after {
    content: "";
    position: absolute;
    top: 100%;
    left: 50%;
    margin-left: 100px;
    border-width: 5px;
    border-style: solid;
    border-color: #555 transparent transparent transparent;
    word-wrap: break-word;
}

/* Toggle this class when clicking on the popup container (hide and show the popup) */
.popup .show {
    visibility: visible;
    -webkit-animation: fadeIn 1s;
    animation: fadeIn 1s
}

/* Add animation (fade in the popup) */
@-webkit-keyframes fadeIn {
    from {opacity: 0;} 
    to {opacity: 1;}
}

@keyframes fadeIn {
    from {opacity: 0;}
    to {opacity:1 ;}
}
```



# Html dropdown menu

* https://www.cssscript.com/multiple-select-dropdown/
* https://www.cssscript.com/multi-select-dropdown-component-vanilla-javascript-sellect-js/
* https://www.cssscript.com/tags-multi-input/
* https://www.cssscript.com/multi-select-autocomplete-selectpure/
* https://www.cssscript.com/lightweight-customizable-select-box-enhancement-library-selectr/


## Html code
```html
  <div class="container" id="myMulti_container">
      <select multiple="multiple" id="myMulti">
        {% for item in network_cards %}
        <option>{{ item }}</option>
        {% endfor %}
      </select>
  </div>
```

## Javascript code
Code for retrieving selected values. Tune `var myDrop = new drop` function
```js
let settings_to_send = {};
  let netcard_dropdown = document.getElementById('myMulti_container');
  let netcard_items = netcard_dropdown.getElementsByClassName('item');

  // only keep elements with "item" class (remove "hide" class)
  let netcard_values = [];
  for(i=0; i < netcard_items.length; i++){
      element_classes = netcard_items[i].attributes.class.value;

      if(element_classes.includes('hide')){
        // skip
      }
      else{
          let value = netcard_items[i].textContent;
          netcard_values.push(value.slice(0, -1));
      }
  }

  settings_to_send['network_cards'] = netcard_values;
  let settings_to_send_json = JSON.stringify(settings_to_send);
```

Static Code
```js
//Varun Dewan 2019
var $ = {
 get: function(selector){ 
    var ele = document.querySelectorAll(selector);
    for(var i = 0; i < ele.length; i++){
       this.init(ele[i]);
    }
    return ele;
 },
 template: function(html){
    var template = document.createElement('div');
    template.innerHTML = html.trim();
    return this.init(template.childNodes[0]);
 },
 init: function(ele){
    ele.on = function(event, func){ this.addEventListener(event, func); }
    return ele;
 }
};

//Build the plugin
var drop = function(info){var o = {
 options: info.options,
 selected: info.selected || [],
 preselected: info.preselected || [],
 open: false,
 html: {
    select: $.get(info.selector)[0],
    options: $.get(info.selector + ' option'),
    parent: undefined,
 },
 init: function(){
    //Setup Drop HTML
    this.html.parent = $.get(info.selector)[0].parentNode
    this.html.drop = $.template('<div class="drop"></div>')
    this.html.dropDisplay = $.template('<div class="drop-display">Display</div>')
    this.html.dropOptions = $.template('<div class="drop-options">Options</div>')
    this.html.dropScreen = $.template('<div class="drop-screen"></div>')
    
    this.html.parent.insertBefore(this.html.drop, this.html.select)
    this.html.drop.appendChild(this.html.dropDisplay)
    this.html.drop.appendChild(this.html.dropOptions)
    this.html.drop.appendChild(this.html.dropScreen)
    //Hide old select
    this.html.drop.appendChild(this.html.select);
    
    //Core Events
    var that = this;
    this.html.dropDisplay.on('click', function(){ that.toggle() });
    this.html.dropScreen.on('click', function(){ that.toggle() });
    //Run Render
    this.load()
    this.preselect()
    this.render();
 },
 toggle: function(){
    this.html.drop.classList.toggle('open');
 },
 addOption: function(e, element){ 
    var index = Number(element.dataset.index);
    this.clearStates()
    this.selected.push({
       index: Number(index),
       state: 'add',
       removed: false
    })
    this.options[index].state = 'remove';
    this.render()
 },
 removeOption: function(e, element){
    e.stopPropagation();
    this.clearStates()
    var index = Number(element.dataset.index);
    this.selected.forEach(function(select){
       if(select.index == index && !select.removed){
          select.removed = true
          select.state = 'remove'
       }
    })
    this.options[index].state = 'add'
    this.render();
 },
 load: function(){
    this.options = [];
    for(var i = 0; i < this.html.options.length; i++){
       var option = this.html.options[i]
       this.options[i] = {
          html:  option.innerHTML,
          value: option.value,
          selected: option.selected,
          state: ''
       }
    }
 },
 preselect: function(){
    var that = this;
    this.selected = [];
    this.preselected.forEach(function(pre){
       that.selected.push({
          index: pre,
          state: 'add',
          removed: false
       })
       that.options[pre].state = 'remove';
    })
 },
 render: function(){
    this.renderDrop()
    this.renderOptions()
 },
 renderDrop: function(){ 
    var that = this;
    var parentHTML = $.template('<div></div>')
    this.selected.forEach(function(select, index){ 
       var option = that.options[select.index];
       var childHTML = $.template('<span class="item '+ select.state +'">'+ option.html +'</span>')
       var childCloseHTML = $.template(
          '<i class="material-icons btnclose" data-index="'+select.index+'">&#xe5c9;</i></span>')
       childCloseHTML.on('click', function(e){ that.removeOption(e, this) })
       childHTML.appendChild(childCloseHTML)
       parentHTML.appendChild(childHTML)
    })
    this.html.dropDisplay.innerHTML = ''; 
    this.html.dropDisplay.appendChild(parentHTML)
 },
 renderOptions: function(){  
    var that = this;
    var parentHTML = $.template('<div></div>')
    this.options.forEach(function(option, index){
       var childHTML = $.template(
          '<a data-index="'+index+'" class="'+option.state+'">'+ option.html +'</a>')
       childHTML.on('click', function(e){ that.addOption(e, this) })
       parentHTML.appendChild(childHTML)
    })
    this.html.dropOptions.innerHTML = '';
    this.html.dropOptions.appendChild(parentHTML)
 },
 clearStates: function(){
    var that = this;
    this.selected.forEach(function(select, index){ 
       select.state = that.changeState(select.state)
    })
    this.options.forEach(function(option){ 
       option.state = that.changeState(option.state)
    })
 },
 changeState: function(state){
    switch(state){
       case 'remove':
          return 'hide'
       case 'hide':
          return 'hide'
       default:
          return ''
     }
 },
 isSelected: function(index){
    var check = false
    this.selected.forEach(function(select){ 
       if(select.index == index && select.removed == false) check = true
    })
    return check
 }
}; o.init(); return o;}


//Set up some data
var options = [
 { html: 'cats', value: 'cats' },
 { html: 'fish', value: 'fish' },
 { html: 'squids', value: 'squids' },
 { html: 'cats', value: 'whales' },
 { html: 'cats', value: 'bikes' },
];

var myDrop = new drop({
 selector:  '#myMulti',
 preselected: [0]  // [0, 2]
});
 // myDrop.toggle();
```


## Css
```css
@charset "UTF-8";
/* CSS Document * Varun Dewan 2019 */
/*
html, body {
padding: 0px;
margin: 0px;
background: #222;
font-family: 'Raleway', sans-serif;
color: #444;
}

body * {
box-sizing: border-box;
margin: 0px;
padding: 0px;
color: #222;
}
*/

body section {
margin-bottom: 10px;
}

.container {
  max-width: 200px;
  /* margin: 40px auto; */
  background: #cdcdcd;
  /* min-height: 230px; */
  /* height: 200px; */
  /* padding: 20px 20px; */ /* adds the square around */
}

.drop {
position: relative;
-webkit-user-select: none;
   -moz-user-select: none;
    -ms-user-select: none;
        user-select: none;
}
.drop.open {
z-index: 100;
}
.drop.open .drop-screen {
z-index: 100;
display: block;
}
.drop.open .drop-options {
z-index: 200;
max-height: 200px;
}
.drop.open .drop-display {
z-index: 200;
/* border-color: #465; */
}
.drop select {
display: none;
}
.drop .drop-screen {
position: fixed;
width: 100%;
height: 100%;
background: #000;
top: 0px;
left: 0px;
opacity: 0;
display: none;
z-index: 1;
}

.link {
text-align: center;
margin: 20px 0px;
color:#8CACD7;
}


.drop .drop-display {
position: relative;
padding: 0px 20px 5px 5px;
border: 4px solid #444;
width: 100%;
background: #FFF;
z-index: 1;
margin: 0px;
font-size: 16px;
min-height: 58px;
}
.drop .drop-display:hover:after {
opacity: 0.75;
}
.drop .drop-display:after {
font-family: 'Material Icons';
content: "\e5c6";
position: absolute;
right: 10px;
top: 12px;
font-size: 24px;
color: #444;
}
.drop .drop-display .item {
position: relative;
display: inline-block;
border: 2px solid #333;
margin: 5px 5px -4px 0px;
padding: 0px 25px 0px 10px;
overflow: hidden;
height: 40px;
line-height: 36px;
}
.drop .drop-display .item .btnclose {
color: #444;
position: absolute;
font-size: 16px;
right: 5px;
top: 10px;
cursor: pointer;
}
.drop .drop-display .item .btnclose:hover {
opacity: 0.75;
}
.drop .drop-display .item.remove {
-webkit-animation: removeSelected 0.2s, hide 1s infinite;
        animation: removeSelected 0.2s, hide 1s infinite;
-webkit-animation-delay: 0s, 0.2s;
        animation-delay: 0s, 0.2s;
}
.drop .drop-display .item.add {
-webkit-animation: addSelected 0.2s;
        animation: addSelected 0.2s;
}
.drop .drop-display .item.hide {
display: none;
}
.drop .drop-options {
background: #444;
box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.25);
position: absolute;
width: 100%;
max-height: 0px;
overflow-y: auto;
transition: all 0.25s linear;
z-index: 1;
}
.drop .drop-options a {
display: block;
height: 40px;
line-height: 40px;
padding: 0px 20px;
color: white;
position: relative;
max-height: 40px;
transition: all 1s;
overflow: hidden;
}
.drop .drop-options a:hover {
/* background: #465; */
cursor: pointer;
}
.drop .drop-options a.remove {
-webkit-animation: removeOption 0.2s;
        animation: removeOption 0.2s;
max-height: 0px;
}
.drop .drop-options a.add {
-webkit-animation: addOption 0.2s;
        animation: addOption 0.2s;
}
.drop .drop-options a.hide {
display: none;
}

@-webkit-keyframes pop {
from {
  -webkit-transform: scale(0);
          transform: scale(0);
}
to {
  -webkit-transform: scale(1);
          transform: scale(1);
}
}

@keyframes pop {
from {
  -webkit-transform: scale(0);
          transform: scale(0);
}
to {
  -webkit-transform: scale(1);
          transform: scale(1);
}
}
@-webkit-keyframes removeOption {
from {
  max-height: 40px;
}
to {
  max-height: 0px;
}
}
@keyframes removeOption {
from {
  max-height: 40px;
}
to {
  max-height: 0px;
}
}
@-webkit-keyframes addOption {
from {
  max-height: 0px;
}
to {
  max-height: 40px;
}
}
@keyframes addOption {
from {
  max-height: 0px;
}
to {
  max-height: 40px;
}
}
@-webkit-keyframes removeSelected {
from {
  -webkit-transform: scale(1);
          transform: scale(1);
}
to {
  -webkit-transform: scale(0);
          transform: scale(0);
}
}
@keyframes removeSelected {
from {
  -webkit-transform: scale(1);
          transform: scale(1);
}
to {
  -webkit-transform: scale(0);
          transform: scale(0);
}
}
@-webkit-keyframes addSelected {
from {
  -webkit-transform: scale(0);
          transform: scale(0);
}
to {
  -webkit-transform: scale(1);
          transform: scale(1);
}
}
@keyframes addSelected {
from {
  -webkit-transform: scale(0);
          transform: scale(0);
}
to {
  -webkit-transform: scale(1);
          transform: scale(1);
}
}
@-webkit-keyframes hide {
from, to {
  max-height: 0px;
  max-width: 0px;
  padding: 0px;
  margin: 0px;
  border-width: 0px;
}
}
@keyframes hide {
from, to {
  max-height: 0px;
  max-width: 0px;
  padding: 0px;
  margin: 0px;
  border-width: 0px;
}
}
```
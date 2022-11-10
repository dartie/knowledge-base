# Collapse panel with checkbox
```html

    <!-- Transfer input -->
    <div class="form-group row">
        <div class="panel panel-default" id="panel_transfer">
            <div class="panel-heading">
                <input class="checkbox-collapsepanel" type="checkbox" value="" id="macAddress_enable" name="macAddress_enable" >
                <label class="control-label" id="panel_transfer_label"> Transfer. Enable for setting the new MAC Address</label>
                <a data-toggle="collapse" href="#collapse_panel_transfer" class="collapsepanelheader"></a>
            </div>
            <div id="collapse_panel_transfer" class="panel-collapse collapse in">
                <div class="panel-body">
                    <input type="text" class="form-control" id="request_transfer_macAddress" placeholder="MAC Address" maxlength="17" disabled>
                    <div class="checkbox">
                        <label><input type="checkbox" value="" id="vm">Virtual Machine</label>
                    </div>
                </div>
            </div>
        </div>
    </div>

```

```javascript
/* listener for showing icons during collapse/expand */

$(".checkbox-collapsepanel").on("change", function () {
    var panel_header_element = $(this).parent();  // get the header panel element
    var panel_element = panel_header_element.parent();  // get the panel element
    var panel_body_collapse_element = panel_element.find('.panel-collapse');  // get the body element
    var panel_header_label = panel_element.find('.control-label');
    var panel_header_label_current_text = panel_header_label.text();

    if($(this).is(':checked')){
        panel_body_collapse_element.addClass('in');
        panel_body_collapse_element.slideDown("slow");
        // add icon (note: add '&ensp;' in text element if you want space between text and icon)
        panel_header_label.html(panel_header_label_current_text + ' <span class="glyphicon glyphicon-minus-sign pull-left"></span>');
    }
    else{
        panel_body_collapse_element.removeClass('in');
        panel_body_collapse_element.slideUp("slow");
        // add icon (note: add '&ensp;' in text element if you want space between text and icon)
        panel_header_label.html(panel_header_label_current_text + ' <span class="glyphicon glyphicon-plus-sign pull-left"></span>');
    }
});


```

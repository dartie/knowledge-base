# Plotly


## Installation


```bash
pip install plotly
```






## Import


```python
import plotly.offline
from plotly.offline import plot
import plotly.graph_objs as go
```


## Reference
* https://plot.ly/python/reference/



## Prepare data


### 1


```python
trace0 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[10, 15, 13, 17]
)
trace1 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[16, 5, 11, 9]
)
data = Data([trace0, trace1])
```






## Create graph


### Scatter


```python
from plotly.offline import plot
import plotly.graph_objs as go


trace0 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[10, 15, 13, 17]
)
trace1 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[16, 5, 11, 9]
)
data = Data([trace0, trace1])


py.plot(data, filename = 'basic-line.html')
```






### Bar


```python
from plotly.offline import plot
import plotly.graph_objs as go


trace0 = go.Bar(
    x=[1, 2, 3, 4],
    y=[10, 15, 13, 17]
)
trace1 = go.Bar(
    x=[1, 2, 3, 4],
    y=[16, 5, 11, 9]
)
data = Data([trace0, trace1])


py.plot(data, filename = 'basic-line.html')
```


### Pie Chart
```python
labels = ['home', 'transports', 'food']  
sizes = ['500', '300', '100']

# Data to plot with plotly  
trace = go.Pie(labels=labels, values=sizes)  
  
plot([trace], filename='chart.html')  
```

or

```python
labels = ['home', 'transports', 'food']  
sizes = ['500', '300', '100']

# Data to plot with plotly  
trace = go.Pie(labels=labels, values=sizes) 

div_tag = plotly.offline.plot([trace], include_plotlyjs=False,  output_type='div')
```
## more advanced options
```python
label_texts = ['label 1', 'label 2']
labels = ['label_1', 'label_2']
values = [1, 15]
# create go.Pie object
trace = go.Pie(labels=labels, values=values, text=label_texts, hoverinfo='text+label', textinfo='text+label+percent')
# create go.Layout object
layout = go.Layout(title=title)
# create go.Figure object
fig = go.Figure(data=[trace], layout=layout)

div_tag = plotly.offline.plot(fig, include_plotlyjs=False, output_type='div')
```
* `hoverinfo` : text display when the mouse hovers above the chart. Options: `label`, `text`, `"value"`, `"percent"`, `name` joined with a `+` OR `all`. If `none` or `skip` are set, no information is displayed upon hovering. But, if `none` is set, click and hover events are still fired.
* `textinfo` : text displayed in the pie chart. Options: `"label"`, `"text"`, `"value"`, `"percent"` joined with a `"+"` OR `"none"`.
* `textposition` : ( enumerated or array of enumerateds: Sets the positions of the `text` elements with respects to the (x,y) coordinates.
`"top left"`  |  `"top center"`  |`"top right"`  |  `"middle left"`  |  `"middle center"`  |  `"middle right"`  |  `"bottom left"`  |`"bottom center"`  |  `"bottom right"`)  
    default:  `"middle center"`  
* `colorscale` : Sets the colorscale. The colorscale must be an array containing arrays mapping a normalized value to an rgb, rgba, hex, hsl, hsv, or named color string. At minimum, a mapping for the lowest (0) and highest (1) values are required. For example, `[[0, 'rgb(0,0,255)', [1, 'rgb(255,0,0)']]`. To control the bounds of the colorscale in color space, use`zmin` and `zmax`. Alternatively, `colorscale` may be a palette name string of the following list: `Greys,YlGnBu,Greens,YlOrRd,Bluered,RdBu,Reds,Blues,Picnic,Rainbow,Portland,Jet,Hot,Blackbody,Earth,Electric,Viridis,Cividis`


**More options for `layout`:**
```python
layout = go.Layout(
    title='Plot Title',
    xaxis=dict(
        title='x Axis',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=dict(
        title='y Axis',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    )
)
```

## get html content
```python
def get_div_id(div):
    # get div id
    regex_div_id = re.compile(r'id="(.*?)"')
    div_id = re.findall(regex_div_id, div)[0]

    return div_id


def generate_plotly_report_html(div):
    div_id = get_div_id(div)

    template = """<html>
    <head>
        <meta charset="utf-8" />
    </head>
    <body>
    <script src="../requirements/js/plotly-latest.min.js"></script>
    %s
    <script type="text/javascript">window.addEventListener("resize", function(){Plotly.Plots.resize(document.getElementById("%s"));});</script>
    </body>
</html>
""" % (div, div_id)

    return template
	

layout = {
    # 'barmode': 'stack',  # enable this if bar must be overlapped with same X value
    'title': '<b>' + srcfile_basename + '</b>',
    "titlefont": {"size": 36, 'family': 'Consolas, monospace', 'color': '#c12b05'},
    # 'shapes': [
    #     {  # threshold line in bar graph
    #         'type': 'rect',
    #         'x0': 0,
    #         'y0': 5,
    #         'layer': 'below',
    #         'fillcolor': 'rgba(128, 0, 128, 0.3)'
    #     }],

    'xaxis' : dict(title='time'),
    # 'yaxis' : dict(title='value')
}

fig =  {'data': traces,  'layout': layout}

div_tag = plotly.offline.plot(fig,  include_plotlyjs=False,  output_type='div')
full_html_content = generate_plotly_report_html(div_tag)
```



## Add Threshold
```javascript
var trace1 = {
    x: [1, 2, 3, 4],
    y: [10, 15, 13, 17],
    type: 'scatter' 
};

var layout = {
    shapes: [
    {
        type: 'line',
        xref: 'paper',
        x0: 0,
        y0: 12.0,
        x1: 1,
        y1: 12.0,
        line:{
            color: 'rgb(255, 0, 0)',
            width: 4,
            dash:'dot'
        }
    }
    ]
}
Plotly.newPlot(myDiv,[trace1],layout);
```


## JavaScript


### References


* [Plotly-Python](https://plot.ly/python)
* [Plotly Function reference](https://plot.ly/javascript/plotlyjs-function-reference/#plotlyupdate)
* [Dropdown menus](https://plot.ly/python/dropdowns/)
* [Trasforms (filters-groups)](https://plot.ly/python/multiple-transforms/)


### get list of traces


```javascript
var graphDiv = document.getElementById(/* id of your graph */)


graphDiv.data // => returns array of traces
```






### delete trace


```javascript
Plotly.deleteTraces(graphDiv, 0);
```


**Snippet**


Links:


* https://codepen.io/plotly/pen/wabPJb
* https://plot.ly/javascript/remove-trace/


```javascript
function plotGraph(){
var trace1 = {
  x: [1, 2, 3, 4],
  y: [10, 15, 13, 17],
  type: 'scatter',
  line: {
    color: 'rgb(55, 128, 191)',
  }
};


var trace2 = {
  x: [1, 2, 3, 4],
  y: [16, 5, 11, 9],
  type: 'scatter',
  line: {
    color: 'rgb(255,140,0)',
  }
};


var layout = {
  title:'Click Buttons to Delete Traces',
  showlegend:false
};


var data = [trace1, trace2];


Plotly.newPlot('myDiv', data, layout);
}


function deleteTrace(divId){
  Plotly.deleteTraces('myDiv', 0);
};
```






### make a new plot with new data


```javascript
Plotly.newPlot(graphDiv, data, layout);
```

```

ivId){
  Plotly.deleteTraces('myDiv', 0);
};
```



### make a new plot with new data

```javascript
Plotly.newPlot(graphDiv, data, layout);
```

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEwMDU5MTk5MTAsLTE4NjU4MjgzODksOT
Q1MTc2MTk2LC0xNDM3MTY4MDU4LDI4NzEwMTQ1NSwxMDgzNDc2
MzIyLC04MjE5MTI5MDgsNjkwODkwNTM1LC0xODk1MjI2Mjc3LD
U5MDg4NTQzMywtMTkxMTk2Njk3MywxMTE4OTQ1MTc5LDEwNjMx
ODY5MzQsLTQ5OTQ4NzUzMCwxMjkwMDkzODE5LC02NDI4Nzc3Mz
hdfQ==
-->

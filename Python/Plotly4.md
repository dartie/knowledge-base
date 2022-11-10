# Plotly4

* https://community.plotly.com/t/introducing-plotly-py-4-0-0/25639
* https://plotly.com/python/getting-started/
* https://plotly.com/python/static-image-export/
* https://plotly.com/python/creating-and-updating-figures/
* https://plotly.github.io/plotly.py-docs/generated/plotly.io.to_html.html
* https://plotly.com/python/subplots/
* https://plotly.com/python/v3/html-reports/ (probably for plotly3)
* https://plotly.com/python/line-charts/ 
* https://plotly.com/python/bar-charts/
* https://plotly.com/python/tick-formatting/

## Offline files
* Plotly.js :
* Latest: https://cdn.plot.ly/plotly-latest.min.js
* Latest Un-minified : https://cdn.plot.ly/plotly-latest.js
* Specific version: https://cdn.plot.ly/plotly-1.52.3.min.js
  ```javascript
  <!-- Latest compiled and minified plotly.js JavaScript -->
  <script src="https://cdn.plot.ly/plotly-latest.min.js" charset="utf-8"></script>

  <!-- OR use a specific plotly.js release (e.g. version 1.52.3) -->
  <script src="https://cdn.plot.ly/plotly-1.52.3.min.js" charset="utf-8"></script>

  <!-- OR an un-minified version is also available -->
  <script src="https://cdn.plot.ly/plotly-latest.js" charset="utf-8"></script>
  ```



* MathJax.js: https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.3/MathJax.js

## Getting Started
```python
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

# Make figure with subplots
fig = make_subplots(rows=1, cols=2, specs=[[{"type": "bar"},
                                          {"type": "surface"}]])

# Add bar traces to subplot (1, 1)
fig.add_trace(go.Bar(y=[2, 1, 3]), row=1, col=1)
fig.add_trace(go.Bar(y=[3, 2, 1]), row=1, col=1)
fig.add_trace(go.Bar(y=[2.5, 2.5, 3.5]), row=1, col=1)
fig.add_trace(go.Bar(y=[4, 2, 3]), row=1, col=1)
fig.add_trace(go.Bar(y=[5, 1, 2]), row=1, col=1)

# Add surface trace to subplot (1, 2)
# Read data from a csv
z_data = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv")
fig.add_surface(z=z_data)

# Hide legend
fig.update_layout(
  showlegend=True,
  title_text="Version 4 Default Theme",
  height=1000,
  width=1500,
)
fig.layout.template = 'plotly_dark'

html_content = fig.to_html(full_html=False, include_plotlyjs=False, include_mathjax=False)
html_content = fig.to_html()
open('plotly4_test.html', 'w', encoding='utf-8').write(html_content)

```

## Add Scroll Zoom / Wheel Zoom
By default plotly python doesn't allow to use this feature, however the javascript makes this possible.
In the html plot (got with `fig.to_html(full_html=False)`, replace:
```js
{"responsive": true}
```
with
```js
{"responsive": true, scrollZoom: true}
```

## Custom buttons
* https://plotly.com/python/custom-buttons/
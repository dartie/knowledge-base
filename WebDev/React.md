# React
* Free and open-source front-end JavaScript library for building user interfaces.
* Based on components.
* It is maintained by Meta and a community of individual developers and companies.

- [React](#react)
  - [Why React](#why-react)
  - [Requirements](#requirements)
  - [Setup](#setup)
    - [Install on Fedora](#install-on-fedora)
  - [Getting started](#getting-started)
  - [Create a new Component](#create-a-new-component)
  - [Include the component in the main page](#include-the-component-in-the-main-page)
  - [Render a variable value](#render-a-variable-value)
  - [Add style](#add-style)
  - [Add CSS style](#add-css-style)
    - [Add style with Bootstrap](#add-style-with-bootstrap)
  - [Component properties](#component-properties)


## Why React
* Reusable components
* Fast rendering

## Requirements
* [Node.js](https://nodejs.org/en/download/current)
* [NPM](https://docs.npmjs.com/)
* [npx](https://www.npmjs.com/package/npx) : [package runner tool that comes with npm 5.2+](https://medium.com/@maybekatz/introducing-npx-an-npm-package-runner-55f7d4bd282b)


## Setup

### Install on Fedora
```bash
sudo dnf install -y nodejs npm
```



## Getting started

1. Create react-app project with:
    ```bash
    npx create-react-app my-app
    ```
    or
    ```bash
    npm init react-app my-app
    ```
2. Move to the app folder (`my-app` folder)
    ```bash
    cd my-app
    ```
    The folder structure is 
    ```
    .
    ├── node_modules
    ├── package.json
    ├── package-lock.json
    ├── public
    │   ├── favicon.ico
    │   ├── index.html
    │   ├── logo192.png
    │   ├── logo512.png
    │   ├── manifest.json
    │   └── robots.txt
    ├── README.md
    └── src
        ├── App.css
        ├── App.js
        ├── App.test.js
        ├── index.css
        ├── index.js
        ├── logo.svg
        ├── reportWebVitals.js
        └── setupTests.js
    ``` 
3. Install dependencies
    ```bash
    npm install
    ```
4. Run the development server
    ```bash
    npm start
    ```
   This will run the web server on port 3000
5. Open a browser and navigate to [http://localhost:3000](http://localhost:3000)
6. To start by scratch, from `src` folder, delete all files except: `index.css` and `index.js`
7. Open `index.js`, delete the entire content and type:
    ```js title="src/index.js"
    import React, { Component } from 'react';
    import ReactDOM from 'react-dom';

    class App extends Component {  // (1)
        render () {
            return <div>           // (2)
            <h1>Hello world!</h1>
            </div>;
        }
    }

    ReactDOM.render(<App/>, document.querySelector("#root"))  // (3)
    ```

    1. A component always needs to return a function
    2. The content returned by `render()` function is XML
    3. To render the component, call `ReactDOM.render(Class, HtmlElementId)` 
    
## [Create a new Component](https://www.youtube.com/watch?v=TD53gWBFIS4&list=PLo2whFYDwVT6VYMM3EvXKiHF1sTPiB3MS&index=10)

1. Under `src` folder, create a file `AppFooter.js`

```js title="src/AppFooter.js" linenums="1"
import React, { Component, Fragment } from 'react';

export default class AppFooter extends Component {

    render() {
        return (
            <Fragment>  // (1)
                <hr />
                <p>Copyright &copy; 2021 Acme Ltd.</p>
            </Fragment>
        );
    }
}
```

1. To make a valid XML, we need to use `#!html <fragment>` tag, only used by React and never rendered in HTML

## Include the component in the main page

```js title="src/index.js" linenums="1" hl_lines="3 8 12 13"
import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import AppFooter from './AppFooter';

class App extends Component {
    render () {
        return (
            <div>  // (1)
                <div> 
                    <h1>Hello world!</h1>
                </div>
                <AppFooter>
            </div> 
        );
    }
}

ReactDOM.render(<App/>, document.querySelector("#root"))
```

1. We need to have one root level tag that surround everything in `return`


## Render a variable value

```js title="src/AppFooter.js" linenums="1" hl_lines="6 10"
import React, { Component, Fragment } from 'react';

export default class AppFooter extends Component {

    render() {
        const currentYear = new Date().getFullYear();
        return (
            <Fragment>
                <hr />
                <p>Copyright &copy; { currentYear } Acme Ltd.</p>  // (1)
            </Fragment>
        );
    }
}
```

1. A variable is used surrounding it with curly brackets `{` `}`


## Add style

## Add CSS style

Style is added using `className` attribute. Remember this is XML in javascript, and `class` keyword is already used by javascript. 

```js title="src/index.js" linenums="1" hl_lines="4 9"
import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import AppFooter from './AppFooter';
import './index.css'

class App extends Component {
    render () {
        return (
            <div className="app">
                <div> 
                    <h1>Hello world!</h1>
                </div>
                <AppFooter>
            </div> 
        );
    }
}

ReactDOM.render(<App/>, document.querySelector("#root"))
```


```css title="src/index.css" linenums="1"
@import url('https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;1,100;1,300&display=swap');

.app {
    max-width: 80%;
    margin: 0 auto;
    font-family: 'Roboto';
}
```

### Add style with Bootstrap

1. Install Bootstrap
    ```bash
    npm install bootstrap
    ```
1. Include it in `index.js`
    ```js title="src/index.js" linenums="1" hl_lines="6"
    import React, { Component } from 'react';
    import ReactDOM from 'react-dom';
    import AppFooter from './AppFooter';
    import AppContent from './AppContent';
    
    import 'bootstrap/dist/css/bootstrap.min.css';  // (1)
    import 'bootstrap/dist/js/bootstrap.bundle.min.js';
    import './index.css'

    class App extends Component {
        render () {
            return (
                <div className="app">
                    <div> 
                        <h1>Hello world!</h1>
                    </div>
                    <AppFooter>
                </div> 
            );
        }
    }

    ReactDOM.render(<App/>, document.querySelector("#root"))
    ``` 

    1. Relative path from `node_modules` folder

1. Use it:
    ```js title="src/AppContent.js" linenums="1" hl_lines="10"
    import React, { Component } from "react";

    export default class AppContent extends Component {

        render() {
            return (
                <p>
                    This is a content
                    <br/>
                    <button className="btn btn-primary" href="#">My button</button>
                </p>
            )
        }
    }
    ```

## Component properties

They allow to have dynamic data and make the components reusable.


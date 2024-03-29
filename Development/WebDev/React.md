# React
* Free and open-source front-end JavaScript library for building user interfaces.
* Based on components.
* It is maintained by Meta and a community of individual developers and companies.

- [React](#react)
  - [Why React](#why-react)
  - [Requirements](#requirements)
  - [Resources](#resources)
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
    - [Inline properties](#inline-properties)
    - [Object properties](#object-properties)
    - [React events](#react-events)
    - [Refs](#refs)
    - [State](#state)


## Why React
* Reusable components
* Fast rendering

## Requirements
* [Node.js](https://nodejs.org/en/download/current)
* [NPM](https://docs.npmjs.com/)
* [npx](https://www.npmjs.com/package/npx) : [package runner tool that comes with npm 5.2+](https://medium.com/@maybekatz/introducing-npx-an-npm-package-runner-55f7d4bd282b)


## Resources

* Book [Road To React](https://www.roadtoreact.com/)
* Docs [React](https://react.dev/)
* Course [Deep Dive Into Modern Web Development](https://fullstackopen.com/en/)
* Docs [Learn reactjs from scratch - ngeducate](https://ngeducate.blogspot.com/p/learn-reactjs-from-scratch.html)
* Course [Learn React (scrimba)](https://scrimba.com/learn/learnreact/introduction-to-react-coa99496098ff5fb511f5235f)
* Book [Eloquent Javascript: A Modern Introduction to Programming - Marijn Haverbeke](https://eloquentjavascript.net/index.html)
* Mozilla [React_getting_started - Mozilla](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Client-side_JavaScript_frameworks/React_getting_started)



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

                // (1)
                <p>Copyright &copy; { currentYear } Acme Ltd.</p>
            </Fragment>
        );
    }
}
```

1. A variable is used surrounding it with curly brackets `{` `}`


## Add style

## Add CSS style

Style is added using `className` attribute. Remember this is XML in javascript, and `class` keyword is already used by javascript. 

```css title="src/index.css" linenums="1"
@import url('https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;1,100;1,300&display=swap');

.app {
    max-width: 80%;
    margin: 0 auto;
    font-family: 'Roboto';
}
```


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
                    <AppContent>
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

### Inline properties

Set them with:

```js
<AppHeader title="Cool App!" subject="Subject">
```

Use them with:

```js
{ this.props.title }
```

Let's create another component: AppHeader

```js title="src/AppHeader.js" linenums="1" hl_lines="7"
import React, { Component } from "react";

export default class AppHeader extends Component {

    render() {
        return (
            // (1)
            <h1>{ this.props.title }</h1>
        )
    }
}
```

1. Use the properties with `{ this.props.propsName }` syntax



```js title="src/index.js" linenums="1" hl_lines="3 15"
import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import AppFooter from './AppHeader';
import AppFooter from './AppFooter';
import AppContent from './AppContent';

import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';
import './index.css'

class App extends Component {
    render () {
        return (
            <div className="app">
                <AppHeader title="Cool App!" subject="My subject">  // (1)
                <AppContent>
                <AppFooter>
            </div> 
        );
    }
}

ReactDOM.render(<App/>, document.querySelector("#root"))
``` 

1. Pass the properties using `propertyName="propertyValue"` syntax


### Object properties

Set them with:

```js
// Define property object
const myProps = {
    title: "My Cool App!",    
    subject: "My subject",    
    favorite_color: "red",    
}

...

// pass the object to the component
<AppHeader { ...myProps }>
```

Use them with:

```js
{ this.props.title }
```

Let's create another component: AppHeader

```js title="src/AppHeader.js" linenums="1" hl_lines="7"
import React, { Component } from "react";

export default class AppHeader extends Component {

    render() {
        return (
            // (1)
            <h1>{ this.props.title }</h1>  
        )
    }
}
```

1. Use the properties with `{ this.props.propsName }` syntax



```js title="src/index.js" linenums="1" hl_lines="13-17 21"
import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import AppFooter from './AppHeader';
import AppFooter from './AppFooter';
import AppContent from './AppContent';

import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';
import './index.css'

class App extends Component {
    render () {
        const myProps = {  // (1)
            title: "My Cool App!",    
            subject: "My subject",    
            favorite_color: "red",    
        } 

    return (
            <div className="app">
                <AppHeader { ...myProps }>
                <AppContent>
                <AppFooter>
            </div> 
        );
    }
}

ReactDOM.render(<App/>, document.querySelector("#root"))
``` 

1. Pass the properties using 
    ```js
    // Define property object
    const myProps = {
        title: "My Cool App!",    
        subject: "My subject",    
        favorite_color: "red",    
    }

    ...
    // pass the object to the component
    <AppHeader { ...myProps }>
    ```

### React events

```js title="src/AppContent.js" linenums="1" hl_lines=""
import React, { Component } from 'react';

export default class AppContent extends Component {

    fetchList = () => {
        console.log("I was clicked");
    }

    render(){
        return (
            <p>
                This is the content

                <br />

                <button onClick={this.fetchList} className="btn btn-primary">Fetch Data</button>
            </p>
        )
    }
}
```

```js title="src/AppContent.js" linenums="1" hl_lines=""
import React, { Component } from 'react';

export default class AppContent extends Component {

    fetchList = () => {
        fetch('https://jsonplaceholder.typicode.com/posts')
            .then((response) => response.json())
            .then(json => {
                console.log(json);

                let posts = document.getElementById("post-list");

                json.forEach(function(obj){
                    let li = document.createElement("li");
                    li.appendChild(document.createTextNode(obj.title));
                    posts.appendChild(li);
                })
            })
    }

    render(){
        return (
            <div>
                This is the content

                <br />

                <button onClick={this.fetchList} className="btn btn-primary">Fetch Data</button>

                <hr />

                <ul id="post-list"></ul>
            </div>
        )
    }
}
```

!!! failure
    Arrow functions are mandatory to access the keyword `this`.
    If we use the old function definition syntax:

    ```js title="src/AppContent.js" linenums="1" hl_lines="9 14"
    import React, { Component } from 'react';

    export default class AppContent extends Component {

        anotherFunction() {
            console.log("Another function");
        }

        fetchList () {
            fetch('https://jsonplaceholder.typicode.com/posts')
                .then((response) => response.json())
                .then(json => {
                    console.log(json);
                    this.anotherFunction();

                    let posts = document.getElementById("post-list");

                    json.forEach(function(obj){
                        let li = document.createElement("li");
                        li.appendChild(document.createTextNode(obj.title));
                        posts.appendChild(li);
                    })
                })
        }

        render(){
            return (
                <div>
                    This is the content

                    <br />

                    <button onClick={this.fetchList} className="btn btn-primary">Fetch Data</button>

                    <hr />

                    <ul id="post-list"></ul>
                </div>
            )
        }
    }
    ```

!!! success
    Function should be defined using the arrow syntax introduced in ES6 version, which allow accessing other functions with `this` keyword.


    ```js title="src/AppContent.js" linenums="1" hl_lines="9 14"
    import React, { Component } from 'react';

    export default class AppContent extends Component {

        anotherFunction = () => {
            console.log("Another function");
        }

        fetchList = () => {
            fetch('https://jsonplaceholder.typicode.com/posts')
                .then((response) => response.json())
                .then(json => {
                    console.log(json);
                    this.anotherFunction();

                    let posts = document.getElementById("post-list");

                    json.forEach(function(obj){
                        let li = document.createElement("li");
                        li.appendChild(document.createTextNode(obj.title));
                        posts.appendChild(li);
                    })
                })
        }

        render(){
            return (
                <div>
                    This is the content

                    <br />

                    <button onClick={this.fetchList} className="btn btn-primary">Fetch Data</button>

                    <hr />

                    <ul id="post-list"></ul>
                </div>
            )
        }
    }
    ```

    !!! note "Javascript function definitions"

        1. Traditional way
 
            ```js 
            function handleClick () {
            enableOTPBox(false);
            };
            ```
 
        2. arrow function
        
            ```js
            const handleClick = () =>{
            enableOTPBox(false);
            };
            ```
 
        3. Expression function

            ```js
            let handleClick = function handleClick(){
            enableOTPBox(false);
            };
            ```


### Refs

React has its own life cycle and elements appear and disappear on the DOM without your really knowing when that's happening because it all happens asynchronously.

**Refs** allow to create reusable components with unique reference. If `id` is used as reference, and the component is used more than once, you'll get multiple components with the same id, which is not great.

!!! Warning
    Overuse of refs will almost certainly result in problems in your application as grows in complexity and the easiest way to avoid problems is to not use refs unless it's absolutely critical that you do so. 

```js title="src/AppContent.js" linenums="1" hl_lines="5-8 17 38"
import React, { Component } from 'react';

export default class AppContent extends Component {

    constructor(props) {  // (1)
        super(props);
        this.listRef = React.createRef();
    }

    fetchList = () => {
        fetch('https://jsonplaceholder.typicode.com/posts')
            .then((response) => response.json())
            .then(json => {
                console.log(json);

                //let posts = document.getElementById("post-list");
                const posts = this.listRef.current;  // (3)

                json.forEach(function(obj){
                    let li = document.createElement("li");
                    li.appendChild(document.createTextNode(obj.title));
                    posts.appendChild(li);
                })
            })
    }

    render(){
        return (
            <div>
                This is the content

                <br />

                <button onClick={this.fetchList} className="btn btn-primary">Fetch Data</button>

                <hr />

                <ul ref={this.listRef}></ul>  
                // (2)
            </div>
        )
    }
}
```

1. `constructor` method always takes the argument `props` (you can call it however you want, but tipically called **props**).
A constructor is a method that is called automatically when we created an object from that class. It can manage initial initialization tasks such as defaulting certain object properties or sanity testing the arguments passed in. Simply placed, the constructor is a method that helps in the creation of objects. 
The constructor is no different in React. This can connect event handlers to the component and/or initialize the component’s local state. Before the component is mounted, the constructor() function is shot, and, like most things in React, it has a few rules that you can follow when using them.
First thing to do is call `super(props)`.
`this.listRef = React.createRef();` creates the reference

2. Use `ref={this.listRef}` (defined in the constructur above) as reference of the element, instead of the `id`.

3. Refer to the element (`ul` in our example) using `ref` instead of `id`.


### State

```js title="src/AppContent.js" linenums="1" hl_lines="5-8 17 38"
import React, { Component } from 'react';

export default class AppContent extends Component {

    state = {posts: []}  // (1)

    constructor(props) {
        super(props);
        this.listRef = React.createRef();
    }

    fetchList = () => {
        fetch('https://jsonplaceholder.typicode.com/posts')
            .then((response) => response.json())
            .then(json => {
                this.setState({posts: json});  // (2)
            })
    }

    ckickedItem = (x) => {
        console.log("clicked", x);
    }

    render(){
        return (
            <div>
                This is the content

                <br />

                <button onClick={this.fetchList} className="btn btn-primary">Fetch Data</button>

                <hr />

                <ul>
                    // (3)
                    {this.state.posts.map((c) => (  // (4)
                        <li key={c.id}>
                            <a href="#!" onClick={() => this.clickedItem(c.id)}>
                                {c.title}
                            </a>
                        </li>
                    ))}
                </ul>  
            </div>
        )
    }
}
```

1. a
2. b
3. c
4. `map()` creates a new array from calling a function for every array element. <br> • does not execute the function for empty elements. <br> • does not change the original array.
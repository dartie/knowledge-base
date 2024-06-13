# Go Web Development



[[_TOC_]]

* [Writing Web Applications](https://golang.org/doc/articles/wiki/)

## VSCode extensions

* [Nunjucks](https://marketplace.visualstudio.com/items?itemName=ronnidc.nunjucks)
* [gotemplate-syntax](https://marketplace.visualstudio.com/items?itemName=casualjim.gotemplate)



## Run a server

```go
package main

import (
	"fmt"
	"net/http"
)

func main() {
	http.ListenAndServe(":8080", nil)
}
```



##  Handle a request

```go
package main

import (
	"fmt"
	"net/http"
)

func main() {
	http.HandleFunc("/index", Index)
	http.ListenAndServe(":8080", nil)
}

func Index(w http.ResponseWriter, r *http.Request) {
	fmt.Fprint(w, "Hello, World!")
}
```


## Routing

### Method check


* From Go 1.22 the method can be specified in the route

=== "Old code"

    ```go linenums="1" hl_lines="10-14"
    package main

    import "net/http"

    func main() {

        mux := http.NewServeMux()

        mux.HandleFunc("/hello", func(w http.ResponseWriter, r *http.Request) {
            if r.Method != http.MethodGet {
                w.WriteHeader(http.StatusMethodNotAllowed)
                w.Write([]byte(""))
                return
            }

            w.Write([]byte(`Hello`))
        })

        if err := http.ListenAndServe(":9002", mux); err != nil {
            panic(err)
        }
    }
    ```

=== "New Code"

    ```go linenums="1" hl_lines="9"
    package main

    import "net/http"

    func main() {

        mux := http.NewServeMux()

        mux.HandleFunc("GET /hello", func(w http.ResponseWriter, r *http.Request) {
            w.Write([]byte(`Hello`))
        })

        if err := http.ListenAndServe(":9002", mux); err != nil {
            panic(err)
        }
    }
    ```


### Path parameter

=== "Old Code"

    ```go linenums="1" hl_lines="15-22"
    package main

    import (
        "fmt"
        "net/http"
        "strings"
    )

    func main() {

        mux := http.NewServeMux()

        mux.HandleFunc("/hello/", func(w http.ResponseWriter, r *http.Request) {

            path := r.URL.Path

            parts := strings.Split(path, "/")

            if len(parts) < 3 {
                http.Error(w, "Invalid request", http.StatusBadRequest)
                return
            }

            name := parts[2]

            w.Write([]byte(fmt.Sprintf("Hello %s!", name)))
        })

        if err := http.ListenAndServe(":9002", mux); err != nil {
            panic(err)
        }
    }
    ```


=== "New Code"

    ```go linenums="1" hl_lines="13"
    package main

    import (
        "fmt"
        "net/http"
        "strings"
    )

    func main() {

        mux := http.NewServeMux()

        mux.HandleFunc("GET /hello/{name}", func(w http.ResponseWriter, r *http.Request) {

            name := r.PathValue("name")

            w.Write([]byte(fmt.Sprintf("Hello %s!", name)))
        })

        if err := http.ListenAndServe(":9002", mux); err != nil {
            panic(err)
        }
    }
    ```

**Multiple Path parameters:**

`{name...}`

```go linenums="1" hl_lines="13"
package main

import (
    "fmt"
    "net/http"
    "strings"
)

func main() {

    mux := http.NewServeMux()

    mux.HandleFunc("GET /hello/{name...}", func(w http.ResponseWriter, r *http.Request) {

        name := r.PathValue("name")

        w.Write([]byte(fmt.Sprintf("Hello %s!", name)))
    })

    if err := http.ListenAndServe(":9002", mux); err != nil {
        panic(err)
    }
}
```

### Match a route

* Match a prefix

    ```go
    mux.HandleFunc("GET /hello", func(w http.ResponseWriter, r *http.Request) {
    ```

* Match an exact path

    ```go
    mux.HandleFunc("GET /hello/{$}", func(w http.ResponseWriter, r *http.Request) {
    ```


## Render a template

* [Template operations](https://www.golangtraining.in/lessons/templates/template-operations.html)
* [Golang Templates Cheatsheet](https://curtisvermeeren.github.io/2017/09/14/Golang-Templates-Cheatsheet)
* [How to use template blocks in go 1.6](https://www.josephspurrier.com/how-to-use-template-blocks-in-go-1-6)
* https://www.calhoun.io/intro-to-templates-p2-actions/

### Render a specific template

```go
package main

import (
	"html/template"
	"net/http"
)

var tpl *template.Template

func main() {
	tpl, _ = template.ParseFiles("index1.html")
    // OR
    // tpl, _ = tpl.ParseFiles("index1.html")

    http.HandleFunc("/", index)
	http.ListenAndServe(":8080", nil)
}

func index(w http.ResponseWriter, r *http.Request) {
	tpl.Execute(w, nil)
}
```



* `index1.html`

  ```html
  <!DOCTYPE html>
  <html>
    <head>
      <title>index1.html Temp</title>
      <meta charset="UTF-8">
    </head>
    
    <body>
        <h1>Hello from index1.html</h1>    
    </body>
  </html>
  ```

  

### Render a template from template folder

```go
package main

import (
	"html/template"
	"net/http"
)

var tpl *template.Template

func main() {
	// func ParseGlob(pattern string) (*Template, error)
	// tpl, _ = template.ParseGlob("templates/*.html")
	// func (t *Template) ParseFiles(filenames ...string) (*Template, error)
	tpl, _ = tpl.ParseGlob("templates/*.html")

	http.HandleFunc("/", indexHandler)
	http.HandleFunc("/about", aboutHandler)
	http.HandleFunc("/contact", contactHandler)
	http.HandleFunc("/login", loginHandler)
	http.ListenAndServe(":8080", nil)
}

func indexHandler(w http.ResponseWriter, r *http.Request) {
	// func (t *Template) ExecuteTemplate(wr io.Writer, name string, data interface{}) error
	tpl.ExecuteTemplate(w, "index.html", nil)
}

func aboutHandler(w http.ResponseWriter, r *http.Request) {
	tpl.ExecuteTemplate(w, "about.html", nil)
}

func contactHandler(w http.ResponseWriter, r *http.Request) {
	tpl.ExecuteTemplate(w, "contact.html", nil)
}

func loginHandler(w http.ResponseWriter, r *http.Request) {
	tpl.ExecuteTemplate(w, "login.html", nil)
}
```



### Render a template with variables

* https://stackoverflow.com/questions/35243493/cant-execute-template-well-in-golang

```go
package main

import (
	"fmt"
	"html/template"
	"net/http"
)

var tpl *template.Template
var name = "John"

func main() {
	tpl, _ = tpl.ParseGlob("templates/*.html")
	http.HandleFunc("/welcome", welcomeHandler)
	http.ListenAndServe(":8080", nil)
}

func welcomeHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Println("indexHandler running")
	// func (t *Template) ExecuteTemplate(wr io.Writer, name string, data interface{}) error
	tpl.ExecuteTemplate(w, "welcome.html", name)
}
```

```html
<!-- This is a HTML comment-->
{{/* This is a Go template comment */}}
<h1>Welcome {{.}}!</h1>
```

* `{{/* a comment */}}` Defines a comment
* `{{.}}` Renders the root element
* `{{.Name}}` Renders the “Name”-field in a nested element
* `{{if .Done}} {{else}} {{end}}` Defines an if/else-Statement
* `{{range .List}} {{.}} {{end}}`  Loops over all “List” field and renders each using `{{.}}`



**Examples:**

```go
package main

import (
	"html/template"
	"net/http"
)

type prodSpec struct {
	Size   string
	Weight float32
	Descr  string
}

type product struct {
	ProdID int
	// Name   string
	Name  string
	Cost  float64
	Specs prodSpec
}

var tpl *template.Template
var prod1 product

func main() {
	prod1 = product{
		ProdID: 15,
		Name:   "Wicked Cool Phone",
		Cost:   899,
		Specs: prodSpec{
			Size:   "150 x 70 x 7 mm",
			Weight: 65,
			Descr:  "Over priced shiny thing designed to shatter on impact",
		},
	}

	tpl, _ = tpl.ParseGlob("templates/*.html")
	http.HandleFunc("/productinfo", productInfoHandler)
	http.ListenAndServe(":8080", nil)
}

func productInfoHandler(w http.ResponseWriter, r *http.Request) {
	// func (t *Template) ExecuteTemplate(wr io.Writer, name string, data interface{}) error
	tpl.ExecuteTemplate(w, "productinfo2.html", prod1)
}
```

```html
<!--
	prod1 = product{
		ProdID: 15,
		Name:   "Wicked Cool Phone",
		Cost:   899,
		Specs: prodSpec{
			Size:   "150 x 70 x 7 mm",
			Weight: 65,
			Descr:  "Over priced shiny thing designed to shatter impact",
		},
	}
-->

<!DOCTYPE html>
<html>
  <head>
    <title>Product Info</title>
    <meta charset="UTF-8">
  </head>
  
  <body>
      <h1>Product Info</h1>
      <ul>
          <li>{{.Name}} Id#:{{.ProdID}}</li>
          <li>${{.Cost}}</li>
          <li>
              Specs
              <ul>
                  <li>Size: {{.Specs.Size}}</li>
                  <li>Weight: {{.Specs.Weight}}</li>
                  <li>Description: {{.Specs.Descr}}</li>
              </ul>
          </li>
      </ul>
  </body>
</html>
```



### If - Else

```go
package main

import (
	"html/template"
	"net/http"
)

var tpl *template.Template

// User first letter must be capitalized to be exported
type User struct {
	Name     string
	Language string
	Member   bool
}

// U struct for export
var u User

func main() {
	u = User{"Bob Smith", "English", false}
	// u = User{"Juan Hernández", "Spanish", true}
	// u = User{"Zhang Wei", "Mandarin", true}
	// u = User{"007", "?", true}

	tpl, _ = tpl.ParseGlob("templates/*.html")
	http.HandleFunc("/welcome", welcomeHandler)
	http.ListenAndServe(":8080", nil)
}

func welcomeHandler(w http.ResponseWriter, r *http.Request) {
	// func (t *Template) ExecuteTemplate(wr io.Writer, name string, data interface{}) error
	tpl.ExecuteTemplate(w, "membership.html", u)
}
```



```html
<!--
    type user struct {
	Name     string
	Language string
	Member   bool
    }

    bob := user{"Bob Smith", "English", false}
	bob := user{"Juan Hernández", "Spanish", true}
	bob := user{"Zhang Wei", "Mandarin", true}
-->

<!DOCTYPE html>
<html>
    <head>
        <title>Membership Status</title>
    <meta charset="UTF-8">
    </head>
    <body>
        {{if .Member}}   
            <h1>Thank you for joining</h1>
        {{else}}
            <h1>Please signup to enjoy memborship benefits</h1>
        {{end}}

    </body>
</html>
```

A pipeline is a possibly chained sequence of "commands". A command is a simple value (argument) or a function or method call, possibly with multiple arguments:

* If the value of the pipeline is empty, no output is generated;
* The empty values are false, 0, any nil pointer or interface value, and any array, slice, map, or string of length zero.




* binary comparison operators defined as functions
  * `eq` Returns the boolean truth of `arg1 == arg2`
  * `ne` Returns the boolean truth of `arg1 != arg2`
  * `lt` Returns the boolean truth of `arg1 < arg2`
  * `le` Returns the boolean truth of `arg1 <= arg2`
  * `gt` Returns the boolean truth of `arg1 > arg2`
  * `ge` Returns the boolean truth of `arg1 >= arg2`



**Example with more conditions**

```html
<!--
    type user struct {
	Name     string
	Language string
	Member   bool
    }

    bob := user{"Bob Smith", "English", false}
	bob := user{"Juan Hernández", "Spanish", true}
	bob := user{"Zhang Wei", "Mandarin", true}
-->

<!DOCTYPE html>
<html>
    <head>
        <title>Greeting</title>
    <meta charset="UTF-8">
    </head>
    <body>

        passed in value: {{.}}<br><br>
        
        eq .Language "English": {{eq .Language "English"}}<br>
        eq .Language "Mandarin": {{eq .Language "Mandarin"}}<br>
        eq .Language "Spanish": {{eq .Language "Spanish"}}<br><br>

        {{if eq .Language "English"}}
            <h1>Hello</h1>
        {{else if eq .Language "Mandarin"}}
            <h1>你好</h1>
        {{else if eq .Language "Spanish"}}
            <h1>Hola</h1>
        {{else}}
        <hi>
            <ul>
                <li>Hello</li>
                <li>你好</li>
                <li>Hola</li>
            </ul>
        </hi>
        {{end}}

    </body>
</html>
```



### Range

```go
package main

import (
	"html/template"
	"net/http"
)

// GroceryList data type for export
type GroceryList []string

var tpl *template.Template
var g GroceryList

func main() {
	g = GroceryList{"milk", "eggs", "green beans", "cheese", "flour", "sugar", "broccoli"}
	tpl, _ = tpl.ParseGlob("templates/*.html")
	http.HandleFunc("/list", listHandler)
	http.ListenAndServe(":8080", nil)
}

func listHandler(w http.ResponseWriter, r *http.Request) {
	// func (t *Template) ExecuteTemplate(wr io.Writer, name string, data interface{}) error
	tpl.ExecuteTemplate(w, "groceries.html", g)
}
```

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Grocery List</title>
    <meta charset="UTF-8">
    </head>
    <body>
        <h3>Grocery List</h3>
        <ul>
            {{range .}}
                <li>{{.}}</li>
            {{end}}
        </ul>
    </body>
</html>
```

OR

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Grocery List</title>
    <meta charset="UTF-8">
    </head>
    <body>
        <h3>Grocery List</h3>
        <ol>
            {{range $element := .}}
                <li>Element: {{$element}} Value:{{.}}</li>
            {{end}}
        </ol>
    </body>
</html>
```



* For getting index and element

    ```html
    <!DOCTYPE html>
    <html>
        <head>
            <title>Grocery List</title>
        <meta charset="UTF-8">
        </head>
        <body>
            <h3>Grocery List</h3>
            <ol>
                {{range $index, $element := .}}
                    <li>Index: {{$index}} Element: {{$element}} Value:{{.}}</li>
                {{end}}
            </ol>
        </body>
    </html>
    ```

* Example with both `range` and `if-else`

    ```go
    package main
    
    import (
        "html/template"
        "net/http"
    )
    
    type task struct {
        Name string
        Done bool
    }
    
    var tpl *template.Template
    
    // Todo list to be exported
    var Todo []task
    
    func main() {
        Todo = []task{{"give dog a bath", true}, {"mow the lawn", false}, {"pickup groceries", false}, {"take out trash", false}, {"paint kitchen", false}, {"feed dog", false}, {"water plants", false}}
        // Todo = []task{{"give dog a bath", true}, {"mow the lawn", true}, {"pickup groceries", true}, {"take out trash", true}, {"paint living room", false}, {"feed dog", true}, {"water plants", true}}
        tpl, _ = tpl.ParseGlob("templates/*.html")
        http.HandleFunc("/todo", todoHandler)
        http.ListenAndServe(":8080", nil)
    }
    
    func todoHandler(w http.ResponseWriter, r *http.Request) {
        // func (t *Template) ExecuteTemplate(wr io.Writer, name string, data interface{}) error
        tpl.ExecuteTemplate(w, "todolist.html", Todo)
    }
    ```

    ```html
    <!DOCTYPE html>
    <html>
        <head>
            <title>Todo List</title>
        <meta charset="UTF-8">
        </head>
        <body>  
            <ul>
                <b>Todo</b>
                {{range .}}
                    {{if ne .Done true}}
                        <li>{{.Name}}</li>
                    {{end}}
                {{end}}
            </ul>
            <br>
            <ul>
                <b>Done</b>
                {{range .}}
                    {{if .Done}}
                        <li>{{.Name}}</li>
                    {{end}}
                {{end}}
            </ul>
        </body>
    </html>
    ```



### Nested template (include a template in another)

* https://lets-go.alexedwards.net/sample/02.08-html-templating-and-inheritance.html
* https://www.josephspurrier.com/how-to-use-template-blocks-in-go-1-6

```go
package main

import (
	"html/template"
	"net/http"
)

type task struct {
	Name string
	Done bool
}

var tpl *template.Template

func main() {
	tpl, _ = tpl.ParseGlob("templates/*.html")
	http.HandleFunc("/", indexHandler)
	http.ListenAndServe(":8080", nil)
}

func indexHandler(w http.ResponseWriter, r *http.Request) {
	tpl.ExecuteTemplate(w, "index.html", nil)
}
```



* `index.html`

  ```html
  {{template "Header"}}
  <h1>Body</h1>
  {{template "Footer"}}
  ```

  

* `header.html`

  ```html
  {{define "Header"}}
      <h1>Header</h1>
  {{end}}
  ```

  

* `footer.html`

  ```html
  {{define "Footer"}}
      <h1>Footer</h1>
  {{end}}
  ```

  

Final html rendered

```html
<h1>Header</h1>
<h1>Body</h1>
<h1>Footer</h1>
```



### Template methods

Function are called from the template using `.FunctionName` and arguments separated by a space

```html
{{.FunctionName arg1 arg2}}
```



```go
package main

import (
	"fmt"
	"html/template"
	"net/http"
)

var tpl *template.Template

// Price of item
type Price float64

// CanCashPr converts Canadian price to cash price (no 1 cent coins)
func (p Price) CanCashPr() string {
	remainder := int(p*100) % 5
	quotiant := int(p*100) / 5
	if remainder < 3 {
		pr := float64(quotiant*5) / 100
		s := fmt.Sprintf("%.2f", pr)
		return s
	}
	pr := (float64(quotiant*5) + 5) / 100
	s := fmt.Sprintf("%.2f", pr)
	return s
}

var p Price

func main() {
	p = 3.91
	tpl, _ = tpl.ParseFiles("index.html")
	http.HandleFunc("/", indexHandler)
	http.ListenAndServe(":8080", nil)
}

func indexHandler(w http.ResponseWriter, r *http.Request) {
	tpl.ExecuteTemplate(w, "index.html", p)
}
```

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Home Page</title>
    <meta charset="UTF-8">
    </head>
    <body>  
        Canadian Cash Price: ${{.CanCashPr}}
    </body>
</html>
```



### Template Function mapping

```go
package main

import (
	"fmt"
	"html/template"
	"net/http"
	"strings"
)

// func (t *Template) New(name string) *Template
// Funcs adds the elements of the argument map to the template's function map.
// Funcs must be called before the template is parsed
var tpl, _ = template.New("index.html").Funcs(template.FuncMap{
	"CanCashPr": func(p float64) string {
		remainder := int(p*100) % 5
		quotiant := int(p*100) / 5
		if remainder < 3 {
			pr := float64(quotiant*5) / 100
			s := fmt.Sprintf("%.2f", pr)
			return s
		}
		pr := (float64(quotiant*5) + 5) / 100
		s := fmt.Sprintf("%.2f", pr)
		return s
	},
	"Upper": strings.ToUpper,
}).ParseFiles("index.html")

var p float64

func main() {
	fmt.Println("tpl.Tree", *tpl.Tree)
	p = 3.33
	tpl, _ = tpl.ParseFiles("index.html")
	http.HandleFunc("/", indexHandler)
	http.ListenAndServe(":8080", nil)
}

func indexHandler(w http.ResponseWriter, r *http.Request) {
	tpl.ExecuteTemplate(w, "index.html", p)
}
```

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Home Page</title>
    <meta charset="UTF-8">
    </head>
    <body>  
        Canadian Cash Price: ${{CanCashPr .}}<br><br>

        {{Upper "this will all be capitalized"}}
    </body>
</html>
```


### Concatenate strings in template
* [github.com/hashicorp](https://github.com/hashicorp/consul-template/issues/267)
* [stackoverflow](https://stackoverflow.com/questions/45389802/is-there-an-efficient-way-to-concatenate-strings/45390194#45390194)


#### printf

```html
{{ range $hkey, $hval := scratch.Get "map" }}
    {{ $combine := (printf "%v@%v" $hkey $hval) }}
    {{ $combine }}
{{end}}
```

#### Custom template function

```go
func TestFunc(strs ...string) string {
   return strings.Trim(strings.Join(strs, ""), " ")
}
```

```html
{{ TestFunc "x"  $var }}
```


## Serve static files

```golang
http.Handle("/", http.FileServer(http.Dir("css/")))
```

Would serve your `css` directory at `/`. Of course you can serve whichever directory at whatever path you choose.

You probably want to make sure that the static path isn't in the way of other paths and use something like this.

```golang
http.Handle("/static/", http.StripPrefix("/static/", http.FileServer(http.Dir("static"))))
```

Placing both your `js` and `css` in the directory `static` in your project. This would then serve them at `domain.com/static/css/filename.css` and `domain.com/static/js/filename.js`

The `StripPrefix` method removes the prefix, so it doesn't try to search e.g. in the `static` directory for `static/css/filename.css` which, of course, it wouldn't find. It would look for `css/filename.css` in the `static` directory, which would be correct.



## Authentication

* [session-based-authentication](https://www.sohamkamani.com/golang/session-based-authentication/)



### Register



### Login



### Logout



### Check if user authenticated

```go
package main

import (
	"fmt"
	"net/http"
    "github.com/gorilla/sessions"
)

// Auth adds authentication code to handler before returning handler
// func (f HandlerFunc) ServeHTTP(w ResponseWriter, r *Request)
func Auth(HandlerFunc http.HandlerFunc) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		session, _ := store.Get(r, "session")
		_, ok := session.Values["userID"]
		if !ok {
			http.Redirect(w, r, "/login", 302)
			return
		}
		// ServeHTTP calls f(w, r)
		// func (f HandlerFunc) ServeHTTP(w ResponseWriter, r *Request)
		HandlerFunc.ServeHTTP(w, r)
	}
}

func main() {
    http.HandleFunc("/index", Auth(Index))
	http.ListenAndServe(":8080", nil)
}

func Index(w http.ResponseWriter, r *http.Request) {
	fmt.Fprint(w, "Hello, World!")
}
```

`Auth()` function wraps `Index` function in the request handler

```go
http.HandleFunc("/index", Auth(Index))
```

## Embed static files in package
You can keep the templates folder in the main folder and embed them from there. Then you need to inject the FS variable into the other handler package. It's always easy after you figure it out.

e.g.

```go
package main

//go:embed templates/*
var templateFs embed.FS

func main() {
    handlers.TemplateFs = templateFs
...
```

```go
package handlers

var TemplateFs embed.FS

func handlerIndex() {
    ...
    tmpl, err = tmpl.ParseFS(TemplateFs, "templates/layout.gohtml",...
...
```



## Host web app

* https://github.com/dokku/dokku
* 


# Todo
* Prevent escape html
* custom functions in template 

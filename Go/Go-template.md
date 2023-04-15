# Go template

- [Go template](#go-template)
  - [Introduction](#introduction)
  - [Go code](#go-code)
  - [Template syntax](#template-syntax)
    - [Variables](#variables)
    - [Concatenate strings in template](#concatenate-strings-in-template)
      - [printf](#printf)
      - [Custom template function](#custom-template-function)
      - [Variables scope behaviour](#variables-scope-behaviour)
    - [If - Else](#if---else)
      - [Multiple conditions](#multiple-conditions)
    - [Loop (Range)](#loop-range)
      - [Using secure variable syntax `.$Var`](#using-secure-variable-syntax-var)
      - [Using shorter variable syntax `.Var`](#using-shorter-variable-syntax-var)
      - [Getting the index too](#getting-the-index-too)
    - [Nested template (include a template in another)](#nested-template-include-a-template-in-another)
    - [Template methods](#template-methods)
    - [Template Function mapping](#template-function-mapping)


## Introduction
Go provides 2 packages for creating content using templates:

* `text/template` : generic template package
* `html/template` : specific for html web pages


## Go code

```go
// Write license text
var outputBytes bytes.Buffer
var templateOutput string
funcMap := template.FuncMap{
    "dec":       func(i int) int { return i - 1 },
    "replace":   strings.ReplaceAll,
    "contains":  strings.Contains,
    "toUpper":   strings.ToUpper,
    "toLower":   strings.ToLower,
    "hasPrefix": strings.HasPrefix,
    "hasSuffix": strings.HasSuffix,
    "split":     strings.Split,
    "splits": func(s string, ss string) []string {
        return strings.Split(s, ss)
    },
    "unescapeHTML": func(s string) template.HTML {
        return template.HTML(s)
    },
    "indexn": func(s []string, i int) string {
        if i < len(s) {
            return s[i]
        } else {
            return "ERROR!"
        }
    },
}
var tmplFile = "template.tpl"
tmpl, err := template.New("template").Funcs(funcMap).ParseGlob("templates/*.tpl")
checkErr(err)
err = tmpl.ExecuteTemplate(&outputBytes, tmplFile, licenseNamespaceInfo)
checkErr(err)
templateOutput = outputBytes.String()

// write license content to file
fullpathTemplate := filepath.Join("output", "output.txt")
errWriteTemplate := os.WriteFile(fullpathTemplate, []byte(templateOutput), 0644)
checkErr(errWriteTemplate)
```

## Template syntax

### Variables

To access variables in the template, better to use `{{ $.StructField }}` instead of simply `{{ .StructField }}` as in case of usage in a loop, the dot `.` has a different value (it refers to the current iteration value).

### Concatenate strings in template
* [github.com/hashicorp](https://github.com/hashicorp/consul-template/issues/267)
* [stackoverflow](https://stackoverflow.com/questions/45389802/is-there-an-efficient-way-to-concatenate-strings/45390194#45390194)


```
$var := (printf "%s%s" "x" "y")
```

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

#### Variables scope behaviour

```go
package main

import (
  "log"
  "os"
  "text/template"
)

func main() {
  // Define a template.
  const templateContent = `
{{-   $a := true    }}
{{-   $b := "pippo" }}
{{-   if $a         }}
{{-   $b := "pluto" }}
{{-   end           }}
{{- $b }}
`
  // Create a new template and parse the template content into it.
  t := template.Must(template.New("letter").Parse(templateContent))

  // Execute the template.
  err := t.Execute(os.Stdout, nil)
  if err != nil {
    log.Println("executing template:", err)
  }
}
```

Changing line 15 from $b := "pluto" to $b = "pluto" the issue is fixed and the output is how expected.


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

#### Multiple conditions

```go-tmpl
{{ if and (eq .var1 "8") (eq .var2 "9") (eq .var "10") }}
<!-- SHOW SOMETHING -->
{{ end }}
```

### Loop (Range)

```go
type myType struct {
  FieldList          [][]string
}

myType {
  FieldList:          [][]string{"a", "b", "c"},
}
```

#### Using secure variable syntax `.$Var`

```
{{- range $element := index $.FieldList }}
{{ index $element 0 }}
{{- end }}
```

#### Using shorter variable syntax `.Var`

```
{{- range $element := .FieldList }}
{{ index $element 0 }}
{{- end }}
```

#### Getting the index too

```
{{ range $index, $element := .FieldList }}
{{ index $element 0 }}
{{- end }}
```
----------------------------------

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


# Gin Gonic

- [Gin Gonic](#gin-gonic)
	- [Include Templates](#include-templates)
	- [Render html](#render-html)
	- [Response](#response)
		- [Use http methods](#use-http-methods)
	- [Serve static files](#serve-static-files)
	- [Routes](#routes)
		- [Basic - route and function in one place](#basic---route-and-function-in-one-place)
		- [Basic route calls a function](#basic-route-calls-a-function)
		- [Group route](#group-route)
	- [Use middleware](#use-middleware)
		- [Use middleware for a specific route](#use-middleware-for-a-specific-route)
		- [Use middleware for a group of routes](#use-middleware-for-a-group-of-routes)
			- [Syntax1 - Use in different statement](#syntax1---use-in-different-statement)
			- [Syntax2 - Use in group definition](#syntax2---use-in-group-definition)
			- [Two groups with the same URI index can be defined](#two-groups-with-the-same-uri-index-can-be-defined)
		- [Popular middleware](#popular-middleware)
			- [AUTH](#auth)
		- [AuthRequired](#authrequired)
	- [Read POST request](#read-post-request)
		- [Using interface{}](#using-interface)
		- [Using struct](#using-struct)
- [Notes from websites](#notes-from-websites)
	- [Training 1 by Pragmatic Reviews](#training-1-by-pragmatic-reviews)
	- [Training 2 by WesionaryTEAM](#training-2-by-wesionaryteam)
		- [Routes in different file](#routes-in-different-file)
- [To see](#to-see)


## Include Templates

* [Template documentation](https://gohugo.io/templates/introduction/)

* File `snippet.html`
	```html
	{{define "snippet1"}}
	...
	{{end}}
	```

* File `index.html`
	```html
	{{ template "snippet1" . }}
	```



* https://github.com/golang-samples/template/blob/ac9a811d648957c6b8d773cb3e62f7a86a4e9538/extends/main.go#L10
* https://siongui.github.io/2017/02/05/go-template-inheritance-jinja2-extends-include/


## Render html

* go file
    ```go
	var files []string
	filepath.Walk("./templates", func(path string, info os.FileInfo, err error) error {
		if strings.HasSuffix(path, ".html") {
			files = append(files, path)
		}
		return nil
	})
    
	r.LoadHTMLFiles(files...)
	```

    or (it doesn't work properly, some templates are not caught)

    ```go
	//router.LoadHTMLGlob("templates/structure/*html")
	router.LoadHTMLGlob("templates/**/*")
    ```

## Response

### Use http methods

```go
fileBytes, err := os.ReadFile(targetPath)
if err != nil {
	panic(err)
}

c.Writer.WriteHeader(http.StatusOK)
c.Writer.Write(fileBytes)
```



## Serve static files

* go file

    ```go
    router.Static("/static", "./static")
    ```

* html file

    ```html
    <link rel="stylesheet" href="static/css/uploadFiles.css">
    ```



## Routes

### Basic - route and function in one place

```go
package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func main() {
	r := gin.Default()
  
  // Route and function together
	r.GET("/ping", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{
			"message": "pong",
		})
	})
  
	r.Run() // listen and serve on 0.0.0.0:8080 (for windows "localhost:8080")
}
```



### Basic route calls a function

```go
package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func Function(c *gin.Context) {
			c.JSON(http.StatusOK, gin.H{
			"message": "pong",
		})
}

func main() {
	r := gin.Default()
  
  // Route and function together
	r.GET("/ping", Function)
  
	r.Run() // listen and serve on 0.0.0.0:8080 (for windows "localhost:8080")
}
```



### Group route

```go
func main() {
	router := gin.Default()

	// Simple group: v1
	v1 := router.Group("/v1")
	{
		v1.POST("/login", loginEndpoint)
		v1.POST("/submit", submitEndpoint)
		v1.POST("/read", readEndpoint)
	}

	// Simple group: v2
	v2 := router.Group("/v2")
	{
		v2.POST("/login", loginEndpoint)
		v2.POST("/submit", submitEndpoint)
		v2.POST("/read", readEndpoint)
	}

	router.Run(":8080")
}
```



## Use middleware

```go
// Default With the Logger and Recovery middleware already attached
r := gin.Default()
```

enables Logger and Recovery middleware by default, whereas

```
r := gin.New()
```

initializes blank Gin without middleware by default



### Use middleware for a specific route

```go
r.GET("/ping", middlewareFunction, Function)
```



### Use middleware for a group of routes

#### Syntax1 - Use in different statement

```go
package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func Function(c *gin.Context) {
			c.JSON(http.StatusOK, gin.H{
			"message": "pong",
		})
}

func main() {
	r := gin.Default()
 
  authorized := r.Group("/")
	// per group middleware! in this case we use the custom created
	// AuthRequired() middleware just in the "authorized" group.
	authorized.Use(AuthRequired())
	{
		authorized.GET("/ping", Function)
	}

	r.Run() // listen and serve on 0.0.0.0:8080 (for windows "localhost:8080")
}
```



#### Syntax2 - Use in group definition 

```go
package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func Function(c *gin.Context) {
			c.JSON(http.StatusOK, gin.H{
			"message": "pong",
		})
}

func main() {
	r := gin.Default()
 
  authorized := r.Group("/").Use(AuthRequired())
	// per group middleware! in this case we use the custom created
	// AuthRequired() middleware just in the "authorized" group.
	authorized.GET("/ping", Function)

	r.Run() // listen and serve on 0.0.0.0:8080 (for windows "localhost:8080")
}
```



#### Two groups with the same URI index can be defined

```go
package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func Function(c *gin.Context) {
			c.JSON(http.StatusOK, gin.H{
			"message": "pong",
		})
}

func main() {
	r := gin.Default()
	
  // Define groups
  authorized := r.Group("/").Use(AuthRequired())
  free := r.Group("/").Use(AuthRequired())
  
	authorized.GET("/protected-content", Function)
  free.GET("/unprotected-content", Function)

	r.Run() // listen and serve on 0.0.0.0:8080 (for windows "localhost:8080")
}
```





### Popular middleware

#### AUTH

```go
// auth middleware checks if logged in by looking at session
func auth(c *gin.Context) {
	store.Options.HttpOnly = true // since we are not accessing any cookies w/ JavaScript, set to true
	store.Options.Secure = true   // requires secuire HTTPS connection
	gob.Register(&User{})

	nextUrl := c.Request.RequestURI

	session, _ := store.Get(c.Request, "session")
	_, ok := session.Values["user"]
	if !ok {
		//c.HTML(http.StatusForbidden, "login.html", nil)
		c.HTML(http.StatusForbidden, "login.html", gin.H{"nextUrl": nextUrl})
		c.Abort()
		return
	}
	c.Next()
}
```



### AuthRequired

```go
//Authenticate User
func AuthRequired() gin.HandlerFunc {
    return func(c *gin.Context) {
        //Get token and e-mail from header
        token := c.Request.Header.Get("AuthToken")
        email := c.Request.Header.Get("AuthEmail")

        //check to see if email & token were provided
        if len(token) == 0 || len(email) == 0 {     
        }   
        //Find email in database
        //Compare stored token with token provided in header
        //Return - Authentication was success or fail
    }
}
```

## Read POST request

### Using interface{}

```go
// Get post data
var postData interface{}
c.BindJSON(&postData)

value := postData.(map[string]interface{})["VM"])
```

### Using struct

```go
type Result struct {
    Assets []string `json: "assets"`
    VM     bool     `json: "vm"`
    HostId string   `json:"hostid"`
}

// Get post data
var postData Result
c.BindJSON(&postData)

value := postData.VM
```

# Notes from websites

## Training 1 by Pragmatic Reviews

- [https://www.youtube.com/watch?v=qR0WnWL2o1Q&t=27s](https://www.youtube.com/watch?v=qR0WnWL2o1Q&t=27s)

```go
package main

import (
	"github.com/gin-gonic/gin"
)

var Router *gin.Engine

func main() {
	server := gin.Default()

	server.GET("/test", func(ctx *gin.Context) {
		ctx.JSON(200, gin.H{
			"message": "OK!!",
		})
	})

	server.Run(":5000")

}
```

## Training 2 by WesionaryTEAM

1. Install Gin and setup the project

    ```bash
    # Install GIN
    go get github.com/gin-gonic/gin

    # init project
    mkdir -p src/go-gin-api
    cd src/go-gin-api/
    go mod init go-gin-api
    ```

1. Create file `main.go` in `go-gin-api`

    ```go
    package main

    import (
    	"github.com/gin-gonic/gin"
    )

    var Router *gin.Engine

    func main() {
    	Router = gin.Default()
    	api := Router.Group("/api")
    	{
    		api.GET("/test", func(ctx *gin.Context) {
    			ctx.JSON(200, gin.H{
    				"message": "test successful",
    			})
    		})
    	}
    	Router.Run(":5000")
    }
    ```

    or, without route group

    ```go
    package main

    import (
    	"github.com/gin-gonic/gin"
    )

    var Router *gin.Engine

    func main() {
    	server := gin.Default()

    	server.GET("/test", func(ctx *gin.Context) {
    		ctx.JSON(200, gin.H{
    			"message": "OK!!",
    		})
    	})

    	server.Run(":5000")

    }
    ```

1. Download required packages

    ```bash
    go mod tidy
    ```

1. Start the server

    ```bash
    go run main.go
    ```

1. Navigate to [http://127.0.0.1/api/test/](http://127.0.0.1/api/test/) 

    ```json
    {"message":"test successful"}
    ```

### Routes in different file

```go
package mappings

import (
	"github.com/gin-gonic/gin"
)

var Router *gin.Engine

func CreateUrlMappings() {
	Router = gin.Default()
	api := Router.Group("/api")
	{
		api.GET("/test", func(ctx *gin.Context) {
			ctx.JSON(200, gin.H{
				"message": "test successful",
			})
		})
	}
}
```

```go
package main

import (
	//import mapping module
	"go-gin-api/mappings"
)

func main() {
	mappings.CreateUrlMappings()
	mappings.Router.Run(":5000")

}
```


# To see
* [gin_html_render](https://pkg.go.dev/github.com/madhums/go-gin-mgo-demo/gin_html_render)
* [https://www.programmersought.com/article/68203968189/](https://www.programmersought.com/article/68203968189/)

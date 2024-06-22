# Slog

- [Slog](#slog)
  - [Key concepts](#key-concepts)
  - [Levels](#levels)
  - [Grouping Records](#grouping-records)
  - [Binding Records to Logger](#binding-records-to-logger)
  - [Built-in Handlers](#built-in-handlers)


Compared to the `log` package, brings more features:

* Structured logs
* Logging levels
* Customization

Using slog without options, the logs are not looking organized and machine readable:

```go title="main.go" linenums="1"
package main

import (
	"log/slog"
)

func main() {
    slog.Debug("Debug message")
    slog.Info("Info message")
    slog.Warn("Warning message")
    slog.Error("Error message")
}
```

```
time=2009-11-10T23:00:00.000Z level=INFO msg="Info message"
time=2009-11-10T23:00:00.000Z level=WARN msg="Warning message"
time=2009-11-10T23:00:00.000Z level=ERROR msg="Error message"
```

Adding structure:

```go title="main.go" linenums="1" hl_lines="8"
package main

import (
	"log/slog"
)

func main() {
    logger := slog.New(slog.NewTextHandler(os.Stdout, nil))
    logger.Debug("Debug message")
    logger.Info("Info message")
    logger.Warn("Warning message")
    logger.Error("Error message")
}
```

```
time=2009-11-10T23:00:00.000Z level=INFO msg="Info message"
time=2009-11-10T23:00:00.000Z level=WARN msg="Warning message"
time=2009-11-10T23:00:00.000Z level=ERROR msg="Error message"
```

Adding options:

```go title="main.go" linenums="1" hl_lines="10"
package main

import (
	"log/slog"
	"os"
)

func main() {
	logger := slog.New(slog.NewTextHandler(os.Stdout, nil))
	slog.SetDefault(logger)

	slog.Debug("Debug message")
	slog.Info("Info message")
	slog.Warn("Warning message")
	slog.Error("Error message")
}
```

* no changes to the output, but this version can be customized easily.

!!! info
    The Debug message is not printed as by default the Debug Level is off.

Enable Debug Level:

```go title="main.go" linenums="1" hl_lines="9"
package main

import (
	"log/slog"
	"os"
)

func main() {
	logger := slog.New(slog.NewTextHandler(os.Stdout, &slog.HandlerOptions{Level: slog.LevelDebug}))
	slog.SetDefault(logger)

	slog.Debug("Debug message")
	slog.Info("Info message")
	slog.Warn("Warning message")
	slog.Error("Error message")
}
```

```
time=2009-11-10T23:00:00.000Z level=DEBUG msg="Debug message"
time=2009-11-10T23:00:00.000Z level=INFO msg="Info message"
time=2009-11-10T23:00:00.000Z level=WARN msg="Warning message"
time=2009-11-10T23:00:00.000Z level=ERROR msg="Error message"
```

Use the JSON Handler instead of the Text one:

```go title="main.go" linenums="1" hl_lines="9"
package main

import (
	"log/slog"
	"os"
)

func main() {
	logger := slog.New(slog.NewJSONHandler(os.Stdout, &slog.HandlerOptions{Level: slog.LevelDebug}))
	slog.SetDefault(logger)

	slog.Debug("Debug message")
	slog.Info("Info message")
	slog.Warn("Warning message")
	slog.Error("Error message")
}
```

```JSON
{"time":"2009-11-10T23:00:00Z","level":"DEBUG","msg":"Debug message"}
{"time":"2009-11-10T23:00:00Z","level":"INFO","msg":"Info message"}
{"time":"2009-11-10T23:00:00Z","level":"WARN","msg":"Warning message"}
{"time":"2009-11-10T23:00:00Z","level":"ERROR","msg":"Error message"}
```

With JSON format we can use key:values in our log message:

```go title="main.go" linenums="1" hl_lines="10 13"
package main

import (
	"log/slog"
	"os"
	"runtime"
)

func main() {
	logger := slog.New(slog.NewJSONHandler(os.Stdout, &slog.HandlerOptions{Level: slog.LevelDebug}))
	slog.SetDefault(logger)

	slog.Info("Info message", "version", runtime.Version())
}
```

```JSON
{"time":"2009-11-10T23:00:00Z","level":"INFO","msg":"Info message","version":"go1.22.4"}
```

!!! note
    The first parameter is the message, the rest are a sequence of key:value. To better visibility can be written as

    ```go
    slog.Info("Info message", 
        "version", runtime.Version(),
    )
    ```

In case of too many key:values it becomes hard to keep track of them. For this purpose, we can club the key and value together


```go title="main.go" linenums="1" hl_lines="15 16"
package main

import (
	"log/slog"
	"math/rand"
	"os"
	"runtime"
)

func main() {
	logger := slog.New(slog.NewJSONHandler(os.Stdout, &slog.HandlerOptions{Level: slog.LevelDebug}))
	slog.SetDefault(logger)

	slog.Info("Info message",
		slog.String("version", runtime.Version()),
		slog.Int("Random number:", rand.Int()),
	)
}
```

```JSON
{"time":"2009-11-10T23:00:00Z","level":"INFO","msg":"Info message","version":"go1.22.4","Random number:":1942320674122205340}
```

Logs can be also organized with groups:

```go title="main.go" linenums="1" hl_lines="15-19"
package main

import (
	"log/slog"
	"os"
	"runtime"
)

func main() {
	logger := slog.New(slog.NewJSONHandler(os.Stdout, &slog.HandlerOptions{Level: slog.LevelDebug}))
	slog.SetDefault(logger)

	slog.Info("Info message",
		slog.String("version", runtime.Version()),
		slog.Group("OS Info:",
			slog.String("OS", runtime.GOOS),
			slog.Int("CPUs", runtime.NumCPU()),
			slog.String("arch", runtime.GOARCH),
		),
	)
}
```

```JSON
{"time":"2009-11-10T23:00:00Z","level":"INFO","msg":"Info message","version":"go1.22.4","OS Info:":{"OS":"linux","CPUs":8,"arch":"amd64"}}
```

To add a pair key:value to all log prints

(for example the version of the app in all prints)


```go title="main.go" linenums="1" hl_lines="11"
package main

import (
	"log/slog"
	"os"
	"runtime"
)

func main() {
	logger := slog.New(slog.NewJSONHandler(os.Stdout, &slog.HandlerOptions{Level: slog.LevelDebug}).WithAttrs(
		[]slog.Attr{slog.String("app_version", "v1.0.0")},
	))
	slog.SetDefault(logger)

	slog.Info("Info message",
		slog.String("version", runtime.Version()),
		slog.Group("OS Info:",
			slog.String("OS", runtime.GOOS),
			slog.Int("CPUs", runtime.NumCPU()),
			slog.String("arch", runtime.GOARCH),
		),
	)
}
```

```JSON
{"time":"2009-11-10T23:00:00Z","level":"INFO","msg":"Info message","version":"go1.22.4","OS Info:":{"OS":"linux","CPUs":8,"arch":"amd64"}}
```

## Key concepts

1. **Logger**: The Logger is the component you interact with when you write log statements in your code. It's responsible for assembling your messages and sending them to the handlers.
1. **Handler**: The Handler is the component that takes log messages from the logger and writes them to whatever destination you've configured, such as a console, file, or logging service.
1. **Fields** (or Records): These are the additional contextual information you attach to your log messages, formatted as key-value pairs. They help to provide more detail and make your logs easier to understand and query.
1. **Level**: The log level indicates the severity or importance of the log message, common levels are debug, info, warn, error.

## Levels

* **DEBUG (-4)**: DEBUG is the least severe level, it's meant for detailed and potentially verbose information that can help developers during the debugging process.

* **INFO (0)**: This is default level. It's used for routine messages that confirm the program is functioning correctly and useful for tracking the flow of the application.

* **WARN (4)**: WARN indicates a level of logging more serious than INFO but not as critical as ERROR. It's not an error, but it could be a potential problem or a sign that you might need to take a closer look at something

* **ERROR (8)**: Use it to log when bad things happen, such as an exception being thrown that might affect the program's operation and require immediate attention.


## Grouping Records
As the complexity of logging increases and we're adding numerous fields, the slog.Group function can be incredibly useful.

It lets us gather related fields under a single key and we just pick a name for our group, then stack the attributes that fit within that group:

```go
logger.Info("a test message", 
    slog.Group("user",
        slog.Int("user_id", 123),
        slog.String("user_name", "John Doe"),
    ),
    slog.Group("account",
        "money", 1000000,
        slog.String("type", "premium"),
    ),
)
```

Now, our log output becomes a neatly structured JSON object, the groups "user" and "account" are represented as keys, with the related fields neatly tucked inside as values:

```json
{
  "time":"2024-03-31T20:25:15.723681+07:00",
  "level": "info",
  "msg": "a test message",
  "user": {
    "user_id": 123,
    "user_name": "John Doe"
  },
  "account": {
    "money": 1000000,
    "type": "premium"
  }
}
```

If you look at the second group, you can see that we've combined implicit and explicit fields: For the "account" group, the "money" field is inputted implicitly, while the "type" field is included explicitly with the help of slog.String.

(This mixed way in the example is really just to demonstrate what's possible, but for clarity and consistency, sticking to one style is generally the better practice.)


## Binding Records to Logger
If you're logging the same thing over and over, there's a smart way to make things more efficient.

Let's say you've got a `"user_id"` that shows up multiple times like this:

```go
logger.Info("checkout", "user_id", 123, "checkout_from", "Brazil")

logger.Info("confirm checkout", "user_id", 123, "money", 1000000)

logger.Info("receive checkout", "user_id", 123)
```

Instead of typing out `"user_id"` and its value every single time, you can attach them to your logger once. After you do that, they'll show up automatically in every log message this logger sends out.

Here's how you set it up using slog.With to create a new logger that remembers certain details:

```go
logger = logger.With("user_id", 123)

logger.Info("checkout", "checkout_from", "Brazil")
logger.Info("confirm checkout", "money", 1000000)
logger.Info("receive checkout")
```

Your log output will look just like it did before, but now it's cleaner and easier to work with.

This `logger.With()` grabs the pieces of information you want to keep reusing and gives you back a new logger that includes them. So any time you make a log with this new logger, the "user_id" will be there, without you having to add it every time.

It's now time to learn more about Loggers and Handlers.

## Built-in Handlers
We've got two types of built-in handlers that handle your logs in different ways:

* `TextHandler`: This handler writes logs in a human-readable format.
* `JSONHandler`: This handler writes logs in JSON format.

Here's how you can use the JSON handler, which we already did in the previous section:

```go
func main() {
    handler := slog.NewJSONHandler(os.Stdout, nil)
    logger := slog.New(handler)
    logger.Info("This is a test message", "user_id", 123, "user_name", "John Doe")
}
```

This will give you a log in JSON format:

```json
{
  "level": "info",
  "message": "This is a test message",
  "user_id": 123,
  "user_name": "John Doe"
}
```

Even with these built-in handlers, you still get a lot of room to make changes, with 3 settings you can adjust:

```go
type HandlerOptions struct {
  AddSource   bool
  Level       Leveler
  ReplaceAttr func(groups []string, a Attr) Attr
}
```

* `AddSource`: This setting lets the handler add details about where in your code the log was created.
* `Level`: This controls which levels of messages the handler will pay attention to. For instance, setting it to INFO means it will ignore the DEBUG messages.
* `ReplaceAttr`: This gives you control over the data in your logs. You can use it to hide private information by swapping out real data for something like "***"

Let's give the AddSource option a go:

```go
opts := &slog.HandlerOptions{
    AddSource: true,
}
logger := slog.New(slog.NewJSONHandler(os.Stdout, opts))
logger.Info("This is a test message", "user_id", 123, "user_name", "John Doe")
```

Now, the output you get will be all on one line, but I've made it easier to read here by spreading it out:

```json
{
  "time": "2024-03-29T21:51:53.920183+07:00",
  "level": "INFO",
  "source": {
    "function": "main.main",
    "file": "/Users/phuong/articles/slog/main.go",
    "line": 13
  },
  "msg": "This is a test message",
  "user_id": 123,
  "user_name": "John Doe"
}
```

Our log now includes the source field, it's not just a simple string but it's an object with three fields: function, file, and line. This detail can be really helpful when you need to quickly figure out where a message or an issue is coming from in your code.

"But every time I use a custom logger, do I have to create it or pass it around?”

We don't have to keep making new loggers or pass them around every time.

There's a way to avoid that, by setting a global logger right in the slog package, we don't need to create our own package just for that:

```go
func main() {
    handler := slog.NewJSONHandler(os.Stdout, nil)
    logger := slog.New(handler)

    slog.SetDefault(logger)

    slog.Info("This is a test message", "user_id", 123, "user_name", "John Doe")
}
```

Once you set the default logger, you can use slog.Info straight away without having to create a new logger every time. But there's something interesting here, the change also impacts the standard log package:

```go
log.Println("This is a test message")

// Output: {"time":"2024-03-31T10:06:10.945147+07:00","level":"INFO","msg":"This is a test message"}
```

This happens because we usually want just one format for logging in our application to keep things clean and consistent.

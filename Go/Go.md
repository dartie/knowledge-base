# Go

----

- [Go](#go)
  - [Introduction](#introduction)
    - [Adopters](#adopters)
  - [Installation](#installation)
    - [Linux setup](#linux-setup)
    - [Windows setup](#windows-setup)
  - [Upgrade an existing version](#upgrade-an-existing-version)
    - [Upgrade on Linux](#upgrade-on-linux)
      - [My Steps on Linux](#my-steps-on-linux)
  - [IDE](#ide)
    - [LiteIDE](#liteide)
    - [VSCode](#vscode)
      - [Debugging with vscode](#debugging-with-vscode)
      - [Enable STDIN with Vscode](#enable-stdin-with-vscode)
  - [Environment variables](#environment-variables)
    - [Linux](#linux)
  - [Project structure](#project-structure)
    - [Example](#example)
    - [File globals \& locals](#file-globals--locals)
    - [Package visibility](#package-visibility)
    - [Import package inside a package](#import-package-inside-a-package)
  - [File structure](#file-structure)
  - [Getting started](#getting-started)
  - [Go Command line](#go-command-line)
    - [version](#version)
    - [env](#env)
    - [get](#get)
    - [run](#run)
    - [build](#build)
      - [Cross compilation](#cross-compilation)
      - [Pass value to variables at linker time](#pass-value-to-variables-at-linker-time)
      - [Build Tags](#build-tags)
      - [Set icon for binary](#set-icon-for-binary)
    - [go mod tidy](#go-mod-tidy)
    - [go mod download](#go-mod-download)
    - [clean](#clean)
    - [go mod vendor](#go-mod-vendor)
    - [go list](#go-list)
    - [go fmt](#go-fmt)
    - [go test](#go-test)
      - [Test run control](#test-run-control)
        - [Options to run](#options-to-run)
        - [Verbose flag `-v`](#verbose-flag--v)
        - [Failing test `-failfast`](#failing-test--failfast)
        - [Fast Failing](#fast-failing)
      - [Coverage](#coverage)
    - [Go doc](#go-doc)
  - [Generators](#generators)
  - [Conventions](#conventions)
  - [Best practice](#best-practice)
  - [Comments](#comments)
  - [Import](#import)
    - [Import structure](#import-structure)
  - [Variables](#variables)
  - [Pointers](#pointers)
  - [Types](#types)
    - [Const](#const)
    - [Integers](#integers)
    - [Floats](#floats)
      - [Round float value](#round-float-value)
    - [Complex](#complex)
    - [Bytes and rune](#bytes-and-rune)
    - [String](#string)
      - [String methods](#string-methods)
        - [EqualFold](#equalfold)
        - [ToUpper](#toupper)
        - [ToLower](#tolower)
        - [Contains](#contains)
        - [Replace](#replace)
        - [Replace case insentive](#replace-case-insentive)
        - [Split](#split)
        - [Partition](#partition)
        - [Trim](#trim)
        - [TrimSpace](#trimspace)
        - [Title](#title)
        - [EqualFold](#equalfold-1)
        - [HasPrefix](#hasprefix)
        - [HasSuffix](#hassuffix)
        - [Create string pointer](#create-string-pointer)
        - [Convert number to string](#convert-number-to-string)
        - [Convert string to number](#convert-string-to-number)
      - [Generate random string](#generate-random-string)
        - [Generate random string - Most efficient](#generate-random-string---most-efficient)
        - [Generate random string - Benchmark](#generate-random-string---benchmark)
      - [Hash a password](#hash-a-password)
    - [Array](#array)
    - [Slice](#slice)
      - [Remove element from slice](#remove-element-from-slice)
      - [Clear slice](#clear-slice)
      - [Sort a slice in reverse mode](#sort-a-slice-in-reverse-mode)
    - [Map](#map)
      - [Map declaration and initialization as global](#map-declaration-and-initialization-as-global)
      - [Check if a key is in the map](#check-if-a-key-is-in-the-map)
        - [Check second return value](#check-second-return-value)
        - [Use second return value directly in an if statement](#use-second-return-value-directly-in-an-if-statement)
        - [Check for zero value](#check-for-zero-value)
      - [Iterate map in order](#iterate-map-in-order)
      - [Iterate map in numerical order](#iterate-map-in-numerical-order)
      - [Nested maps](#nested-maps)
    - [Struct](#struct)
      - [Anonymous struct](#anonymous-struct)
      - [Embedded Struct](#embedded-struct)
      - [Struct as class](#struct-as-class)
        - [New constructor like](#new-constructor-like)
      - [Tags](#tags)
      - [Interface](#interface)
    - [Empty Interface](#empty-interface)
    - [Type Declarations](#type-declarations)
    - [Type Conversions](#type-conversions)
    - [Error](#error)
  - [Printing / String formatting](#printing--string-formatting)
    - [Format variables](#format-variables)
    - [Pretty print](#pretty-print)
    - [Print with colors](#print-with-colors)
      - [gookit/color](#gookitcolor)
      - [TwiN/go-color](#twingo-color)
  - [Get user input (Scan STDIN)](#get-user-input-scan-stdin)
    - [Scan](#scan)
    - [bufio](#bufio)
    - [io/ioutil](#ioioutil)
  - [Control Flow](#control-flow)
    - [IF](#if)
    - [Switch case](#switch-case)
    - [FOR Loop](#for-loop)
      - [Range](#range)
  - [panic - defer - recover](#panic---defer---recover)
    - [panic](#panic)
    - [defer](#defer)
    - [recover](#recover)
    - [End program without stack messages](#end-program-without-stack-messages)
  - [Filepath](#filepath)
    - [Get current working directory](#get-current-working-directory)
    - [Get current source code file path](#get-current-source-code-file-path)
    - [Get executable path](#get-executable-path)
  - [File](#file)
    - [Check if file exists](#check-if-file-exists)
    - [Get Folder content](#get-folder-content)
      - [Sort Files](#sort-files)
        - [Sort files by name](#sort-files-by-name)
      - [Compress a folder](#compress-a-folder)
    - [Iterate a path](#iterate-a-path)
    - [Get file info](#get-file-info)
    - [Read a file](#read-a-file)
      - [Read entire file](#read-entire-file)
      - [Read file line by line](#read-file-line-by-line)
      - [Read file and store as slice](#read-file-and-store-as-slice)
    - [Write file from array](#write-file-from-array)
    - [Parse XML](#parse-xml)
    - [Parse JSON](#parse-json)
      - [Parse JSON with struct (typed)](#parse-json-with-struct-typed)
      - [Parse JSON with interface (untyped)](#parse-json-with-interface-untyped)
      - [My functions](#my-functions)
      - [Float with decimal](#float-with-decimal)
    - [Write a file](#write-a-file)
  - [Database](#database)
    - [Sqlite3](#sqlite3)
      - [Init](#init)
      - [Update/Insert](#updateinsert)
      - [Select one row](#select-one-row)
      - [Select multiple rows](#select-multiple-rows)
    - [Postgres](#postgres)
  - [Path handling](#path-handling)
    - [Join](#join)
    - [Dir](#dir)
    - [Base](#base)
    - [IsAbs](#isabs)
    - [Ext](#ext)
    - [Rel](#rel)
    - [Split](#split-1)
    - [Clean](#clean-1)
    - [Real Path](#real-path)
    - [Detect the user's home directory without the use of cgo](#detect-the-users-home-directory-without-the-use-of-cgo)
      - [Detect the user's home directory without the use of cgo](#detect-the-users-home-directory-without-the-use-of-cgo-1)
  - [Time](#time)
    - [Overview](#overview)
    - [Get current timestamp](#get-current-timestamp)
    - [Format](#format)
    - [Time fun fact](#time-fun-fact)
    - [Sleep](#sleep)
    - [Format dates/times as in python](#format-datestimes-as-in-python)
    - [Parse dates/times](#parse-datestimes)
    - [Add days/time to time](#add-daystime-to-time)
    - [Get difference between two dates](#get-difference-between-two-dates)
    - [Compare dates](#compare-dates)
    - [Get execution time](#get-execution-time)
    - [Convert float time to time.Time](#convert-float-time-to-timetime)
  - [Execute command](#execute-command)
    - [Convert a string of arguments into a slice](#convert-a-string-of-arguments-into-a-slice)
    - [Run](#run-1)
    - [exec.Command](#execcommand)
    - [Multiple arguments](#multiple-arguments)
    - [Stdin and Stdout](#stdin-and-stdout)
    - [Capture output](#capture-output)
    - [Get realtime output](#get-realtime-output)
  - [Run external process](#run-external-process)
    - [Run the command](#run-the-command)
      - [Output() vs Run()](#output-vs-run)
    - [Custom Output Writer](#custom-output-writer)
    - [Passing Input To Commands With STDIN](#passing-input-to-commands-with-stdin)
    - [Killing a Child Process](#killing-a-child-process)
    - [Capture output and error seperately](#capture-output-and-error-seperately)
    - [Get return code](#get-return-code)
    - [Set current working directory (cwd)](#set-current-working-directory-cwd)
    - [Set environment variables](#set-environment-variables)
    - [Hide window](#hide-window)
    - [Custom commands for a different OS](#custom-commands-for-a-different-os)
    - [Check early that a program is installed](#check-early-that-a-program-is-installed)
    - [My function](#my-function)
  - [Application's arguments](#applications-arguments)
    - [Flags](#flags)
    - [Argparse](#argparse)
  - [Functions](#functions)
    - [Variadic functions](#variadic-functions)
  - [Go Routines](#go-routines)
    - [Channels](#channels)
      - [Buffer](#buffer)
  - [Concurrency](#concurrency)
    - [Channel vs Buffer](#channel-vs-buffer)
  - [Handle Ctrl+C (Signal Interrupt) Close in the Terminal](#handle-ctrlc-signal-interrupt-close-in-the-terminal)
    - [Solution 1](#solution-1)
    - [Solution 2](#solution-2)
  - [Regex](#regex)
    - [Replace text using regex](#replace-text-using-regex)
  - [Evaluate](#evaluate)
  - [Make http requests](#make-http-requests)
  - [Embed files in the binary](#embed-files-in-the-binary)
    - [Embed a text file and get the content in a variable](#embed-a-text-file-and-get-the-content-in-a-variable)
    - [Embed a folder and access all files](#embed-a-folder-and-access-all-files)
    - [Recreate embedded filesystems from embed.FS](#recreate-embedded-filesystems-from-embedfs)
  - [Send email](#send-email)
  - [Misc](#misc)
    - [Windows registry](#windows-registry)
    - [Notify in os](#notify-in-os)
  - [API](#api)
    - [Slack](#slack)
      - [slack-go-webhook](#slack-go-webhook)
    - [Salesforce](#salesforce)
      - [simplesalesforce](#simplesalesforce)
      - [go-soapforce](#go-soapforce)
    - [Prometheus](#prometheus)
  - [Database](#database-1)
  - [Reference](#reference)
  - [Bibliography](#bibliography)
  - [Web development](#web-development)
  - [To learn](#to-learn)
- [To check](#to-check)

----

## Introduction

* Open-source
* Compiled
* Binaries can be created for all platforms
* Strongly Typed language
* Fast : [https://benchmarksgame-team.pages.debian.net/benchmarksgame/fastest/go-python3.html](https://benchmarksgame-team.pages.debian.net/benchmarksgame/fastest/go-python3.html)
* Readability and minimalism
    provides methods for automatic formatting of your code.
* Concurrent programming
    The Go language is built with concurrent programming. It means that goroutines, select statements and channels of Golang are primitives and are specifically build for concurrency. So, this means you can run the language on multiple processes at the same time and on the same core.
    One particular disadvantage with Go's concurrency is that it may lead to race conditions. However, Go provides race condition detection but it works only after race condition actually happened.
* Garbage collection
    Go is a garbage-collected programming language, so it will automatically free up the program memory that you no longer require. So one can say that, Go garbage collectors will act as the knob that will let you adjust CPU memory as per your need. It will also enable you to protect your projects against memory leakages.
* Cross-platform
    Go is a cross-platform language, which means you can compile it on your machine and run it anywhere, including Windows, Linux, Mac, etc. So, with Golang, you can generate tons of cross-platform binaries. This feature makes the language truly adaptable and portable.
* Fun fact : The language is just called Go, but the term "Golang" became popular with their website golang.org which is taken as "go.org" was unavailable!



### Adopters

* **Google** - Being the father of Go, the company itself utilizes the language for its cloud services and infrastructure.

* **Uber** - for scaling up its geofence microservices to enhance map processing speed.

* **Netflix** - for handling big data processing, for the recommendation of TV series and movies, in particular.

* **Salesforce** - also migrated to Go for Einstein Analytics to resolve its readability issue.

* **Novartis** - this Pharma giant uses Go to develop web apps and execute PL/SQL scripts.

* **YouTube** - for handling and managing the ever-increasing load on their website.

-----------------------------------------------------------------------------------

## Installation

### Linux setup

```bash
export version=1.16.4

# Download package
wget https://golang.org/dl/go${version}.linux-amd64.tar.gz

# extract the package in /usr/local
sudo rm -rf /usr/local/go && sudo tar -C /usr/local -xzf go${version}.linux-amd64.tar.gz

# 
export PATH=$PATH:/usr/local/go/bin

# print version
go version
```

### Windows setup

1. Download package from the website
1. Install it using the wizard

```bash
#
SET PATH=c:\Go\bin;%PATH%

# print version
go version
```

-----------------------------------------------------------------------------------

## Upgrade an existing version
* [khongwooilee.medium.com](https://khongwooilee.medium.com/how-to-update-the-go-version-6065f5c8c3ec)


### Upgrade on Linux

1. Remove the golang-go package
    ```bash
    sudo apt-get remove golang-go
    ```
1. Remove the golang-go dependencies
    ```bash
    sudo apt-get remove --auto-remove golang-go
    ```
1. Uninstall the existing Go package
    ```bash
    sudo rm -rvf /usr/local/go
    ```
1. Download specific binary release for your system
    ```bash
    wget https://dl.google.com/go/go1.14.linux-amd64.tar.gz
    ```

    > Note: Replace the go release in **bold** above to the version for your system. List of version can be found [here](https://golang.org/dl/).

1. Extract the archive file
    ```bash
    sudo tar -xvf go1.14.linux-amd64.tar.gz
    ```

    > Note: Replace the go release in **bold** above to the downloaded one.

1. Place the extracted file to desired location on the system
    ```bash
    sudo mv go /usr/local
    ```

    > Tips: Above location is recommended on Linux.

1. Setup Go environment variable. Open .profile file located at home directory (~/.profile) and add the following lines:
    ```bash
    export GOROOT=/usr/local/go
    export GOPATH=$HOME/go
    export PATH=$GOPATH/bin:$GOROOT/bin:$PATH
    ```

    **GOROOT** is the location where the Go package is installed on your system.
    **GOPATH** is the work directory of your go project.

1. Reload environment variables for the change to take effect. *(Thanks Luis V. for suggestion in the comment)*

    This can be done by either running the following command in terminal or doing a re-login of current shell.

    ```bash
    source ~/.profile
    ```

1. Verify the go version
    ```bash
    go version
    ```

1. Verify the configured environment variables
    ```bash
    go env
    ```

#### My Steps on Linux
```bash
# Download specific binary release for your system 
wget https://dl.google.com/go/go1.14.linux-amd64.tar.gz

# Extract go package
sudo tar -xvf go1.14.linux-amd64.tar.gz

# Remove the golang-go package
sudo apt-get remove golang-go

# Remove the golang-go dependencies
sudo apt-get remove --auto-remove golang-go

# Uninstall the existing Go package
sudo rm -rvf /usr/local/go

# Place the extracted file to desired location on the system
sudo mv go /usr/local

# Setup Go environment variable
export GOROOT=/usr/local/go
export GOPATH=$HOME/go
export PATH=$GOPATH/bin:$GOROOT/bin:$PATH

# Reload environment variables
source ~/.profile

# Verify the go version
go version
```


-----------------------------------------------------------------------------------

## IDE

### LiteIDE

```bash
wget -O liteide.tar.gz https://github.com/visualfc/liteide/releases/download/x37.4/liteidex37.4.linux64-qt5.5.1.tar.gz

tar -zxvf liteide.tar.gz

```

### VSCode
The VS Code plugin is developed and maintened by Google developers: [Go](https://marketplace.visualstudio.com/items?itemName=golang.go)

```bash
# download the vscode package
wget -O vscode.deb https://az764295.vo.msecnd.net/stable/3c4e3df9e89829dce27b7b5c24508306b151f30d/code_1.55.2-1618307277_amd64.deb

# install the package 
sudo dpkg -i vscode.deb
```

1. Install the [Go](https://marketplace.visualstudio.com/items?itemName=golang.go) extension
1. `View -> Command Palette...`
1. Type **goinstall** `-> Go Install/Update Tools`
1. Select All -> wait for installation

#### Debugging with vscode

1. In debug, create the `.vscode/launch.json`
    ```json
    {
        // Use IntelliSense to learn about possible attributes.
        // Hover to view descriptions of existing attributes.
        // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
        "version": "0.2.0",
        "configurations": [
            {
                "name": "Launch Package",
                "type": "go",
                "request": "launch",
                "mode": "auto",
                "program": "${fileDirname}",
                "args": ["-e", "http://127.0.0.1:9001/api/", "-m", "Test", "-t", "9903be34923b5c0fff66a249f1f7b2bc3bee6734", "-H", "111111111111"],
                "buildFlags": "",
                "console": "integratedTerminal",
                "asRoot": true
            }
        ]
    }
    ```
1. Add `args` for adding Debug arguments and `buildFlags` for adding compilation arguments (e.g : tags)
1. Add `"console": "integratedTerminal"` and `"asRoot": true` for debugging STDIN (it uses the integrated terminal instead of the debugger console)


#### Enable STDIN with Vscode

By default, using `fmt.Scan` (and similar) from catching user input leads to error message

```go
package main

import "fmt"

func main() {
    fmt.Print("Enter text: ")
    var input string
    fmt.Scanln(&input)
    fmt.Print(input)
}
```

```
Unable to evaluate expression: could not find symbol value for text
```

Here the solution:
1. Edit `lauch.json` adding `"console": "integratedTerminal"` and `"asRoot": true`
1. By default go installation isn't visible to root user. sudo has its own $PATH which is defined by the secure_path setting in your sudo config.
    To fix it:
    1. Open your sudo config: 
        ```
        sudo visudo
        ```
    1. Locate the line staring with `Defaults    secure_path =`
    1. Add `:/usr/local/go/bin` to the end of the line (the go installation folder)
    1. Save the file


-----------------------------------------------------------------------------------

## Environment variables

* `GOPATH` is discussed [in the `cmd/go` documentation](http://golang.org/cmd/go/#hdr-GOPATH_environment_variable):

> The GOPATH environment variable lists places to look for Go code. On Unix, the value is a colon-separated string. On Windows, the value is a semicolon-separated string. On Plan 9, the value is a list.GOPATH must be set to get, build and install packages outside the standard Go tree.

* `GOROOT` is discussed in [the installation instructions](http://golang.org/doc/install#tarball_non_standard):

> The Go binary distributions assume they will be installed in /usr/local/go (or c:\Go under Windows), but it is possible to install the Go tools to a different location. In this case you must set the GOROOT environment variable to point to the directory in which it was installed.For example, if you installed Go to your home directory you should add the following commands to $HOME/.profile:export GOROOT=$HOME/go
export PATH=$PATH:$GOROOT/bin
Note: GOROOT must be set only when installing to a custom location.

### Linux

```bash
export GOROOT=/usr/local/go
export GOPATH=$HOME/go
export PATH=$PATH:$GOPATH/bin
export PATH=$PATH:$GOROOT/bin
```

-----------------------------------------------------------------------------------

## Project structure

* The project is formed of packages
* The main packages is required (and it's unique)
* Non main packages cannot be executed!
    * E.g.: considering the file `s1.go`
    ```go
    package services
    
    import "fmt"
    
    func NewS1() {
        fmt.Println("Creating new service")
    }
    ```
    ```bash
    > go run s1.go
    go run: cannot run non-main package
    ```

The workspace directory contains the following sub directories at its root -

* `src`: contains Go source files.

    The `src` directory typically contains many version control repositories containing one or more Go packages. Every Go source file belongs to a package. You generally create a new subdirectory inside your repository for every separate Go package.

* `bin`: contains the binary executables.

    The Go tool builds and installs binary executables to this directory. All Go programs that are meant to be executables must contain a source file with a special package called main and define the entry point of the program in a special function called main().

* `pkg`: contains Go package archives (.a).

    All the non-executable packages (shared libraries) are stored in this directory. You cannot run these packages directly as they are not binary files. They are typically imported and used inside other executable packages.


### Example

```
bin/
    myapp							# Executable binary
    hello						    # Executable binary
pkg/
   github.com/callicoder/example/
       numbers.a                    # Package archive
       strings.a                    # Package archive
   github.com/gorilla/
       mux.a                        # Package archive
   go.uber.org/
       zap.a                        # Package archive
src/
    github.com/callicoder/example/  # Project repository
       .git/
       myapp/
          app.go                    # Executable program containing main package and function
       numbers/                     # Go Package (contains utility functions for working with numbers)
          prime.go
          prime_test.go             
       strings/                     # Go Package (contains utility functions for working with strings)
          reverse.go
          trim.go
    github.com/gorilla/mux/			# 3rd Party package
       #... package contents
    go.uber.org/zap/				# 3rd Party package
       #... package contents
    hello/     						# Local package (not published anywhere)
       hello.go  

	# ... (more repositories and packages omitted) ...
```

> https://golang.org/doc/code describes how to write code Go code

> https://www.golangprograms.com/golang-import-struct-from-another-or-child-package.html

### File globals & locals

* Locals:
    * Package declaration
    * Import paths

* Globals:
    * Constants
    * Variables
    * Functions
    * Types

Example:

* `square.go`
    ```go
    package main
    
    import "fmt"
    
    func squareDelta(x float64) float64 {
        fmt.Println("squaring with delta", delta)
        return x * x * delta
    }
    ```

* `main.go`
    ```go
    package main
    
    import "fmt"
    
    var (
        number = 10.0
        delta = .33333
    )
    
    func main() {
        fmt.Println(squareDelta(number))
    }
    ```

* `package` and `import` are declared in each file, because they are locals
* `number` and `delta` are visible in `square.go` because they are globals and because `square.go` and `main.go` are both part of the same package ("main").
* `squareDelta` is visible in `main.go` because it's global and `square.go` and `main.go` are both part of the same package ("main").
* For running the package you need:
    ```bash
    go run *.go
    ```

### Package visibility

* `Exported` : visible and accessible in all files of the same package and outiside the package
* `unExported` : visible and accessible inside all files of the same package, and inaccessible outside of it.

### Import package inside a package
* [https://www.golangprograms.com/golang-import-package-inside-package.html](https://www.golangprograms.com/golang-import-package-inside-package.html)
* [https://dev.to/takakd/go-package-is-not-in-goroot-3pec](https://dev.to/takakd/go-package-is-not-in-goroot-3pec)


-----------------------------------------------------------------------------------

## File structure

* `go.mod`: contains dependencies (which can be get with `go get` command or just writing the .go file and running `go mod tidy`)
    ```go
    module github.com/steevehook/go-modules
    
    go 1.14
    
    require (
        github.com/julienschmidt/httprouter v1.3.0 // indirect
        go.uber.org/zap v1.14.1 // indirect
    )
    ```
    
    `indirect` comment means the package is downloaded but not used in the project
    
* `go.sum`: it is containing the expected cryptographic hashes of the content of specific module versions.

-----------------------------------------------------------------------------------

## Getting started

```bash
mkdir hello
cd hello
go mod init example.com/hello

nano hello.go

```

```bash
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

```bash
go run .
```

- Add package **`"rsc.io/quote"`**

    ```bash
    **package main
    
    import "fmt"
    
    import "rsc.io/quote"
    
    func main() {
        fmt.Println(quote.Go())
    }**
    ```

-----------------------------------------------------------------------------------

## Go Command line

```
Go is a tool for managing Go source code.

Usage:

        go <command> [arguments]

The commands are:

        bug         start a bug report
        build       compile packages and dependencies
        clean       remove object files and cached files
        doc         show documentation for package or symbol
        env         print Go environment information
        fix         update packages to use new APIs
        fmt         gofmt (reformat) package sources
        generate    generate Go files by processing source
        get         add dependencies to current module and install them
        install     compile and install packages and dependencies
        list        list packages or modules
        mod         module maintenance
        run         compile and run Go program
        test        test packages
        tool        run specified go tool
        version     print Go version
        vet         report likely mistakes in packages

Use "go help <command>" for more information about a command.

Additional help topics:

        buildconstraint build constraints
        buildmode       build modes
        c               calling between Go and C
        cache           build and test caching
        environment     environment variables
        filetype        file types
        go.mod          the go.mod file
        gopath          GOPATH environment variable
        gopath-get      legacy GOPATH go get
        goproxy         module proxy protocol
        importpath      import path syntax
        modules         modules, module versions, and more
        module-get      module-aware go get
        module-auth     module authentication using go.sum
        packages        package lists and patterns
        private         configuration for downloading non-public code
        testflag        testing flags
        testfunc        testing functions
        vcs             controlling version control with GOVCS
```

### version

### env

### get
Add dependencies to current module and install them

Looks in all files for import paths and download the dependencies to `$GOPATH/src`

### run

### build
Downloads all packages required and compiles the source code, creating the binary output.

#### Cross compilation
* [Description of necessary environment variables](https://golang.org/doc/install/source#environment)
* [Blog](https://freshman.tech/snippets/go/cross-compile-go-programs/)

* For linux on linux
    ```go
    # 64-bit
    GOOS=linux GOARCH=amd64 go build -o bin/app-amd64-linux app.go

    # 32-bit
    GOOS=linux GOARCH=386 go build -o bin/app-386-linux app.go
    ```

* For windows on linux
    ```go
    GOOS=windows GOARCH=amd64 go build
    ```

    or, adding the output folder

    ```go
    GOOS=windows GOARCH=amd64 go build -o bin/app-amd64.exe app.go
    ```

* For windows on windows
    * 32bit
        ```go
        set GOOS=windows
        set GOARCH=386
        go build -o hello.exe hello.go
        ```

    * 64bit
        ```go

        ```

* For MacOS
    ```go
    # 64-bit
    GOOS=darwin GOARCH=amd64 go build -o bin/app-amd64-darwin app.go

    # 32-bit
    GOOS=darwin GOARCH=386 go build -o bin/app-386-darwin app.go
    ```

#### Pass value to variables at linker time

* [DigitalOcean - Using ldflags to Set Version Information for Go Applications](https://www.digitalocean.com/community/tutorials/using-ldflags-to-set-version-information-for-go-applications)

```bash
go build -ldflags "-X main.days=30"
```

```go
package main

import "fmt"

var days string

func main() {
    fmt.Println(days)  // days is equel to "" if ldflags isn't used.
}
```

#### Build Tags

* [digitalocean](https://www.digitalocean.com/community/tutorials/customizing-go-binaries-with-build-tags)

* Identifier added to a piece of code that determines when the file should be included in a package during the build process. 
* This allows you to build different versions of your Go application from the same source code and to toggle between them in a fast and organized manner.

Example: handle Free, Pro and Enterprise level of your application:

```go
package main

import "fmt"

var features = []string{
  "Free Feature #1",
  "Free Feature #2",
}

func main() {
  for _, f := range features {
    fmt.Println(">", f)
  }
}
```

#### Set icon for binary
* [How to set desktop shortcut icons for GoLand in Ubuntu](https://www.programmersought.com/article/17185835067/)
* [github.com/josephspurrier/goversioninfo](https://pkg.go.dev/github.com/josephspurrier/goversioninfo)
* [Howdo you set the application icon in golang](https://stackoverflow.com/questions/25602600/how-do-you-set-the-application-icon-in-golang)

### go mod tidy
Cleans the `go.mod` from unused required packages.

### go mod download
Download dependencies only looking at the `go.mod` file


### clean

```bash
go clean -cache -modcache -i -r
```
cleans the local cache and all packages downloaded locally

### go mod vendor


### go list

```bash
go list -m -versions go.uber.org/zap
```

Displayes all versions available for a specific package.

!!! info "if the `vendor` directory is present, it doesn't work."

### go fmt

```bash
gofmt -w file.go

go fmt path/to/your/package
```

* easier to write: never worry about minor formatting concerns while hacking away.

* easier to read: when all code looks the same you need not mentally convert others' formatting style into something you can understand.

* easier to maintain: mechanical changes to the source don't cause unrelated changes to the file's formatting; diffs show only the real changes.

* uncontroversial: never have a debate about spacing or brace position ever again!


### go test

* Allows to test files and functions in Go projects


#### Test run control

* [ieftimov.com](https://ieftimov.com/post/testing-in-go-go-test/)

1. Local directory mode, or running without arguments: go test compiles the package sources and tests found in the current directory and then runs the resulting test binary. This mode disables caching. After the package test finishes, go test prints a summary line showing the test status (‘ok’ or ‘FAIL’), the package name, and elapsed time.
1. Package list mode, or running with arguments: go test compiles the package sources and tests found in the current directory and then runs the resulting test binary. This mode disables caching. After the package test finishes, go test prints a summary line showing the test status (‘ok’ or ‘FAIL’), the package name, and elapsed time.


* `person.go`

```go
package person

import "errors"

type Person struct {
	age int
}

func NewPerson(age int) (*Person, error) {
	if age < 1 {
		return nil, errors.New("A person is at least 1 years old")
	}

	return &Person{
		age: age,
	}, nil
}

func (p *Person) older(other *Person) bool {
	return p.age > other.age
}
```

* `person_tests.go`

```go
package person

import (
	"testing"
)

func TestNewPersonPositiveAge(t *testing.T) {
	_, err := NewPerson(1)
	if err != nil {
		t.Errorf("Expected person, received %v", err)
	}
}

func TestNewPersonNegativeAge(t *testing.T) {
	p, err := NewPerson(-1)
	if err == nil {
		t.Errorf("Expected error, received %v", p)
	}
}

func TestOlderFirstOlderThanSecond(t *testing.T) {
	p1, _ := NewPerson(1)
	p2, _ := NewPerson(2)

	if p1.older(p2) {
		t.Errorf("Expected p1 with age %d to be younger than p2 with age %d", p1.age, p2.age)
	}
}

func TestOlderSecondOlderThanFirst(t *testing.T) {
	p1, _ := NewPerson(2)
	p2, _ := NewPerson(1)

	if !p1.older(p2) {
		t.Errorf("Expected p1 with age %d to be older than p2 with age %d", p1.age, p2.age)
	}
}
```

```bash
$ go test person.go person_test.go
ok  	command-line-arguments	0.005s
```

!!! info

    Brief output since there are no errors



##### Options to run

* Test a specific test file
    ```bash
    $ go test person.go person_test.go
    ok  	command-line-arguments	0.005s
    ```

* Test a go package
    ```bash
    $ go test person
    ok  	person	0.004s
    ```

* Test a specific function
    ```bash
    $ go test -run TestNewPerson -v
    === RUN   TestNewPersonPositiveAge
    --- PASS: TestNewPersonPositiveAge (0.00s)
    === RUN   TestNewPersonNegativeAge
    --- PASS: TestNewPersonNegativeAge (0.00s)
    PASS
    ok  	person	0.004s
    ```


##### Verbose flag `-v`

```bash
$ go test person.go person_test.go -v
=== RUN   TestNewPersonPositiveAge
--- PASS: TestNewPersonPositiveAge (0.00s)
=== RUN   TestNewPersonNegativeAge
--- PASS: TestNewPersonNegativeAge (0.00s)
=== RUN   TestOlderFirstOlderThanSecond
--- PASS: TestOlderFirstOlderThanSecond (0.00s)
=== RUN   TestOlderSecondOlderThanFirst
--- PASS: TestOlderSecondOlderThanFirst (0.00s)
PASS
ok  	command-line-arguments	0.005s
```

!!! info

    Verbose output with `-v` flag

##### Failing test `-failfast`

Cause a fail replacing `TestOlderFirstOlderThanSecond` function with 

```go
func TestOlderFirstOlderThanSecond(t *testing.T) {
	p1, _ := NewPerson(100)
	p2, _ := NewPerson(2)

	if p1.older(p2) {
		t.Errorf("Expected p1 with age %d to be younger than p2 with age %d", p1.age, p2.age)
	}
}
```

* `person_test.go`

```go
package person

import (
	"testing"
)

func TestNewPersonPositiveAge(t *testing.T) {
	_, err := NewPerson(1)
	if err != nil {
		t.Errorf("Expected person, received %v", err)
	}
}

func TestNewPersonNegativeAge(t *testing.T) {
	p, err := NewPerson(-1)
	if err == nil {
		t.Errorf("Expected error, received %v", p)
	}
}

func TestOlderFirstOlderThanSecond(t *testing.T) {
	p1, _ := NewPerson(100)
	p2, _ := NewPerson(2)

	if p1.older(p2) {
		t.Errorf("Expected p1 with age %d to be younger than p2 with age %d", p1.age, p2.age)
	}
}

func TestOlderSecondOlderThanFirst(t *testing.T) {
	p1, _ := NewPerson(2)
	p2, _ := NewPerson(1)

	if !p1.older(p2) {
		t.Errorf("Expected p1 with age %d to be older than p2 with age %d", p1.age, p2.age)
	}
}
```

```bash
$ go test -v
=== RUN   TestNewPersonPositiveAge
--- PASS: TestNewPersonPositiveAge (0.00s)
=== RUN   TestNewPersonNegativeAge
--- PASS: TestNewPersonNegativeAge (0.00s)
=== RUN   TestOlderFirstOlderThanSecond
--- FAIL: TestOlderFirstOlderThanSecond (0.00s)
    person_test.go:26: Expected p1 with age 100 to be younger than p2 with age 2
=== RUN   TestOlderSecondOlderThanFirst
--- PASS: TestOlderSecondOlderThanFirst (0.00s)
FAIL
exit status 1
FAIL	person	0.004s
```

`TestOlderFirstOlderThanSecond` is failed while others have passed.


##### Fast Failing

It allows to stop at the first fail

```bash
$ go test -v -failfast
=== RUN   TestNewPersonPositiveAge
--- PASS: TestNewPersonPositiveAge (0.00s)
=== RUN   TestNewPersonNegativeAge
--- PASS: TestNewPersonNegativeAge (0.00s)
=== RUN   TestOlderFirstOlderThanSecond
--- FAIL: TestOlderFirstOlderThanSecond (0.00s)
    person_test.go:26: Expected p1 with age 100 to be younger than p2 with age 2
FAIL
exit status 1
FAIL	person	0.004s
```

#### Coverage

* https://stackoverflow.com/questions/10516662/how-to-measure-test-coverage-in-go


Run the test and provide the coverage percentage
```bash
go test -cover
```

Sample output:

```
--- FAIL: TestOlderFirstOlderThanSecond (0.00s)
    person_test.go:26: Expected p1 with age 100 to be younger than p2 with age 2
FAIL
coverage: 100.0% of statements
exit status 1
FAIL	Go-Nalug/test-project	0.014s
```


```bash
go test -v -coverprofile cover.out ./YOUR_CODE_FOLDER/...  # creates "cover.out"
go tool cover -html=cover.out -o cover.html
open cover.html
```

Creates a coverage html file which shows with colors what has been covered.


### Go doc

* [linkedin.com](https://www.linkedin.com/pulse/how-generate-documentation-from-code-golang-alex-guidi)
* [yourbasic.org](https://yourbasic.org/golang/package-documentation/)

```go
//Package math provide mathematical functions
package math


//Sum two integers and returns a result
func Sum(x int, y int) int {
    return x + y
}
```

* Print plain text documentation to standard output

```bash
go doc
```

```
package math // import "Go-Nalug/doctest"

Package math provide mathematical functions

func Sum(x int, y int) int
```


* Print full plain text documentation

```bash
go doc -all
```

```
package math // import "Go-Nalug/doctest"

Package math provide mathematical functions

FUNCTIONS

func Sum(x int, y int) int
    Sum two integers and returns a result
```


* Run a web server and presents the documentation as a web page

```bash
# install "godoc"
go get golang.org/x/tools/cmd/godoc
```

```bash
godoc -http=:6060  # or "godoc -http=127.0.0.1:6060"
```




-----------------------------------------------------------------------------------

## Generators

* https://eli.thegreenplace.net/2021/a-comprehensive-guide-to-go-generate/
* https://blog.carlmjohnson.net/post/2016-11-27-how-to-use-go-generate/

-----------------------------------------------------------------------------------
## Conventions

!!! info
    ```go
    import "fmt"
    
    int main() {
    
    }
    
    ```

1. Folder package and package name should have the same name
    * !!! success "Folder `app/network` -> package `network`"
        ```
        .
        ├─ app/
        │  └─ network/
        │  	      └─ main.go/
        ```
        ```go
        package network
        
        // ...
        ```

    * !!! danger "Folder `app/net` -> package `network`"
        ```
        .
        ├─ app/
        │  └─ net/
        │  	      └─ main.go/
        ```
        ```go
        package network
        
        // ...
        ```

1. Directory or package name should never be with underscore or camel case. It should be one word.
    *  !!! success
        ```
        .
        ├─ app/
        │  └─ network/
        │  	      └─ main.go/
        ```

    *  !!! danger 
        ```
        .
        ├─ app/
        │  └─ net_err/
        │  	      └─ main.go/
        ```
        ```
        .
        ├─ app/
        │  └─ netErr/
        │  	      └─ main.go/
        ```

1. Directory or package name should be specific

    * !!! danger 
        ```
        .
        ├─ app/
        │  └─ utils/
        │  	      └─ main.go/
        ```

1. Avoid nested packages - keep the structure flat

    * !!! danger
        ```
        .
        ├─ app/
        │  └─ pkg/
        │  	   └─ sub_pkg/
        │  	          └─ sub_pkg/        
        │        	          └─ sub_pkg/                
        ```

1. Tabs are recommended over spaces
1. Go follows a convention where source files are all lower case with underscore separating multiple words.
1. Compound file names are separated with `_`
1. File names that begin with `.` or `_` are ignored by the go tool
1. Files with the suffix `_test.go` are only compiled and run by the `go test` tool.

> `go fmt` or `gofmt -w .` take care of the formatting

## Best practice
* [go-best-practices](https://github.com/smallnest/go-best-practices)

-----------------------------------------------------------------------------------

## Comments

```go
// Single-line Comment

/* 
	Block comment
*/
```

-----------------------------------------------------------------------------------

## Import

- One statement

    ```go
    import ("fmt"; "math")

    // OR

    import ("fmt"
            "math")
    ```

- Multiple statements

    ```go
    import "fmt"
    import "math"
    ```
    
- Import with alias
    ```go
    import (
        quoteV3 "rsc.io/quote/v3"
    )
    ```

!!! fail
    Go doesn't allow recursive import (cross reference):
    main -> p1 -> p2 -> p1

### Import structure

```go
package pkg
import "github.com/gophertuts/go-basics/net"
```

* `github.com`: Host
* `gophertuts`: User/Organization 
* `go-basics`: Project/Repo
* `net`: package

-----------------------------------------------------------------------------------

## Variables

Variables are names used to hold values.

- Full declaration

    ```go
    var <variable-name/s> <type>

    var x int

    var x,y int
    
    var x,y int = 2  // declaring and initializing more variable in one statement.
    ```

- Implicit type : type is not specified (requires initialization)

    ```go
    var <variable> = <value>

    var x = 100
    ```

- Short variable declaration

    > allowed only inside a fuction

    ```go
    <variable-name>:=<value>
    x := 100
    ```

- Parens Declaration
Used in case of multiple declarations. 
It is useful when declaring lots of vars at once. Instead of

```go
var one string
var two string
var three string
```

You can write

```go
var (
    one string
    two string
    three string
)
```

```go
var (  
      name1 = initialvalue1
      name2 = initialvalue2
)
```

```go
var (
	name   = "naveen"
	age    = 29
	height int
)
```

> Uninitialized variables have a zero value

```go
var x int     // x = 0
var x string  // x = ""
```


-----------------------------------------------------------------------------------

## Pointers

Variables contain the **memory address** of a variable.

Usually used for modifying a value of a variable within a function.

* `*` (deference operator) before a type means 
* `*` (deference operator) before a variable name means get the value of the value of the variable (from the address, which is what the variable is storing) 
* `&` before a variable name gets the address of the item

```go
package main

import (
	"fmt"
)

func main() {
    toChange := "hello"
    var pointer *string = &toChange
    fmt.Println(pointer, *pointer, &pointer)
}

/*
0xc000010240 hello 0xc00000e028
*/
```

* `pointer` :  address where the content of `toChange` (`"hello"`) is stored
* `*pointer` : access the content of the address (`"hello"`)
* `&pointer` : gets the pointer that points to `toChange` (pointer to the pointer)



```go
package main

import (
	"fmt"
)

func changeValue(str *string) {
	*str = "changed!"
}

func changeValue2(str string) {
	str = "changed!"
}

func main() {
    toChange := "hello"
    fmt.Println(toChange)  // Print before
    changeValue(toChange)
    fmt.Println(toChange)  // Print after
}
```

```
hello
changed!
```

in case of 

```go
func main() {
    toChange := "hello"
    fmt.Println(toChange)  // Print before
    changeValue2(toChange)
    fmt.Println(toChange)  // Print after
}
```

```
hello
hello
```

The value only changed locally in the function because I didn't pass the pointer and I passed the value "hello" to the function.


For struct there is no need to use `*` for pointing to the value.

```go
package main

import (
	"fmt"
)

type Point struct {
	x int32
	y int32
}

func changeX(pt *Point) {
	pt.x = 100
}

func main() {
	pt := Point{y: 3, x: 4}
	changeX(&pt)      // the x of "pt" becomes 100

	fmt.Println(pt)   // {100 3} 
}
```



```go
func main() {
    x := 7
    
    y := &x  // access the address of "x" variable
    fmt.Println(x, y)  // 7 0xc0000140b8
    
    *y = 8   // Dereference: access where it's pointing to
    fmt.Println(x, y)  // 8 0xc0000140b8
    
}
```


-----------------------------------------------------------------------------------

## Types

Determines the values that the variable can have and the operations that can be performed on it.

### Const

```go
const pi = 3.14
```

### Integers

* `int`
* `int8` : has size 1 byte. Covers range -128 to 127;
* `int16` : has size 2 bytes : -32.768 to 32.767;
* `int32` : has size 4 bytes: -2.147.483.648 to 2.147.483.647;
* `int64` : has size 8 bytes : -9 X 10 to 9 X 1018.
* `uint8` : unsigned integer of 1 byte : 0 to 255;
* `uint16` : unsigned integer of 2 bytes : 0 to 65.535;
* `uint32` : unsigned integer of 4 bytes :  4.294.967.295;
* `uint64` : unsigned integer of 8 bytes : 18 X 1018;

### Floats
- `float32` ~ 6 digits precision

    ```go
    var d float32 = 1.222
    ```

- `float64` ~ 15 digits precision

    ```go
    123.45
    1.2345e2
    ```

#### Round float value
```go
package main

import (
	"fmt"
)

func main() {
	k := 10 / 3.0
	fmt.Printf("%.2f", k)
}
```

```
3.33 // instead of 3.333333
```

### Complex

- `complex64`
- `complex128`

```go
var z complex128 = complex(2,3)  // real and imaginary

var x complex128 = cmplx.Sqrt(-5 + 12i)
```


### Bytes and rune

Golang has two additional integer types called `byte` and `rune` that are aliases for `uint8` and `int32` data types respectively -

| Type | Alias For |
| :--- | :-------- |
| byte | uint8     |
| rune | int32     |

In Go, the `byte` and `rune` data types are used to distinguish characters from integer values.

Golang doesn’t have a `char` data type. It uses `byte` and `rune` to represent character values. The `byte` data type represents [ASCII](https://en.wikipedia.org/wiki/ASCII) characters and the `rune` data type represents a more broader set of [Unicode](http://www.unicode.org/) characters that are encoded in [UTF-8](http://www.utf-8.com/) format.

Characters are expressed in Golang by enclosing them in single quotes like this: `'A'`.

The default type for character values is `rune`. That means, if you don’t declare a type explicitly when declaring a variable with a character value, then Go will infer the type as `rune` -

```go
var firstLetter = 'A' // Type inferred as `rune` (Default type for character values)
```

You can create a `byte` variable by explicitly specifying the type -

```go
var lastLetter byte = 'Z'
```

Both `byte` and `rune` data types are essentially integers. For example, a `byte` variable with value `'a'` is converted to the integer 97.

Similarly, a `rune` variable with a unicode value `'♥'` is converted to the corresponding unicode codepoint `U+2665`, where `U+` means unicode and the numbers are hexadecimal, which is essentially an integer.

```go
package main
import "fmt"

func main() {
	var myByte byte = 'a'
	var myRune rune = '♥'

	fmt.Printf("%c = %d and %c = %U\n", myByte, myByte, myRune, myRune)
}
# Output
a = 97 and ♥ = U+2665
```

In the above example, I’ve printed the variable `myByte` in character and decimal format, and the variable `myRune` in character and Unicode format.


### String

A "string" is a sequence of bytes (not of a rune). 

* Double quotes
* Backtick

```go
var d string = "hello world"

var e string = `This is a 
Multiline
string
`
```

#### String methods

* [String methods doc](https://golang.org/pkg/strings)

Import `strings`
```go
import "strings"
```

##### EqualFold

Reports whether 2 strings are equal under Unicode case-folding, which is a more general form of case-insensitivity.

* [geeksforgeeks](https://www.geeksforgeeks.org/strings-equalfold-function-in-golang-with-examples/)


```go
if strings.EqualFold(x, y) {

}
```

##### ToUpper

Turn the string to upper case

```go
strings.ToUpper("Gopher")
```
```
GOPHER
```

##### ToLower

Turn the string to lower case

```go
strings.ToLower("Gopher")
```
```
gopher
```

##### Contains

Check whether a substring is in a string

```go
strings.Contains("seafood", "foo")
```
```
true
```

##### Replace

Replace a portion of string with another

```go
strings.Replace("oink oink oink", "k", "ky", 2)          // replace only the first n (2) occurrences
strings.Replace("oink oink oink", "oink", "moo", -1)     // replace all occurrences
```

```
oinky oinky oink
moo moo moo
```

##### Replace case insentive

Replace a portion of string with another matching the string without caring about case.

```go
newContent := regexp.MustCompile(`(?i)BLOB`).ReplaceAllString(string(content), "bytea")
```

##### Split

Split a string into a list of strings

```go
strings.Split("a,b,c", ",")
```

```
["a" "b" "c"]
```


##### Partition

Split a string keeping the separator

```go
func Partition(s string, sep string) (string, string, string) {
    parts := strings.SplitN(s, sep, 2)
    if len(parts) == 1 {
        return parts[0], "", ""
    }
    return parts[0], sep, parts[1]
}
```

##### Split last element only

```go
package main

import (
	"fmt"
	"strings"
)

func main() {
	s := "Hello,Stack,Overflow"

	first := s[0:strings.LastIndex(s, ",")]
	fmt.Println(first)

	last := s[strings.LastIndex(s, ",")+1:]
	fmt.Println(last)
}
```

##### Trim

Strips one or more characters from a string

```go
strings.Trim("¡¡¡Hello, Gophers!!!", "!¡")
```

```
Hello, Gophers
```

##### TrimSpace

Strips whitespaces from a string

```go
s := strings.TrimSpace("\t Goodbye hair!\n ")
fmt.Printf("%q", s) // "Goodbye hair!"
```

##### Title

Makes the first letter of each word uppercase

```go
strings.Title("her royal highness")
```

```
Her Royal Highness
```

##### EqualFold

Compares strings with different cases

```go
strings.EqualFold("Go", "go")
```

```
true
```

##### HasPrefix

Checks if a string ends with a string

```go
if strings.HasPrefix(myString, "Hello") {

}
```

##### HasSuffix

Checks if a string starts with a string

```go
if strings.HasSuffix(myString, ".xml") {
    
}
```

##### Create string pointer

* [aguidehub.com](https://aguidehub.com/blog/2022-09-12-golang-convert-pointer-to-string/)

```go
package main

import "fmt"

func main() {
  var strPointer = new(string)
  *strPointer = "aGuideHub"

  strPointerValue := *strPointer
  fmt.Println(strPointerValue)
}
```


##### Convert number to string
```go
package main

import (
    "strconv"
)
s, err := strconv.Atoi(2)
```

##### Convert string to number
```go
package main

import (
    "strconv"
)
i, err := strconv.Atoi("2")
```

#### Generate random string

##### Generate random string - Most efficient

* [StackOverflow](https://stackoverflow.com/a/31832326/4768254)

```go

// generates random string (most efficient: https://stackoverflow.com/a/31832326/4768254)
func RandStringBytesMaskImprSrcUnsafe(n int) string {
	var src = rand.NewSource(time.Now().UnixNano())
	const letterBytes = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	const (
		letterIdxBits = 6                    // 6 bits to represent a letter index
		letterIdxMask = 1<<letterIdxBits - 1 // All 1-bits, as many as letterIdxBits
		letterIdxMax  = 63 / letterIdxBits   // # of letter indices fitting in 63 bits
	)

	b := make([]byte, n)
	// A src.Int63() generates 63 random bits, enough for letterIdxMax characters!
	for i, cache, remain := n-1, src.Int63(), letterIdxMax; i >= 0; {
		if remain == 0 {
			cache, remain = src.Int63(), letterIdxMax
		}
		if idx := int(cache & letterIdxMask); idx < len(letterBytes) {
			b[i] = letterBytes[idx]
			i--
		}
		cache >>= letterIdxBits
		remain--
	}

	return *(*string)(unsafe.Pointer(&b))
}
```

##### Generate random string - Benchmark

```go
package main

import (
	"math/rand"
	"strings"
	"testing"
	"time"
	"unsafe"
)

// Implementations

func init() {
	rand.Seed(time.Now().UnixNano())
}

var letterRunes = []rune("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

func RandStringRunes(n int) string {
	b := make([]rune, n)
	for i := range b {
		b[i] = letterRunes[rand.Intn(len(letterRunes))]
	}
	return string(b)
}

const letterBytes = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
const (
	letterIdxBits = 6                    // 6 bits to represent a letter index
	letterIdxMask = 1<<letterIdxBits - 1 // All 1-bits, as many as letterIdxBits
	letterIdxMax  = 63 / letterIdxBits   // # of letter indices fitting in 63 bits
)

func RandStringBytes(n int) string {
	b := make([]byte, n)
	for i := range b {
		b[i] = letterBytes[rand.Intn(len(letterBytes))]
	}
	return string(b)
}

func RandStringBytesRmndr(n int) string {
	b := make([]byte, n)
	for i := range b {
		b[i] = letterBytes[rand.Int63()%int64(len(letterBytes))]
	}
	return string(b)
}

func RandStringBytesMask(n int) string {
	b := make([]byte, n)
	for i := 0; i < n; {
		if idx := int(rand.Int63() & letterIdxMask); idx < len(letterBytes) {
			b[i] = letterBytes[idx]
			i++
		}
	}
	return string(b)
}

func RandStringBytesMaskImpr(n int) string {
	b := make([]byte, n)
	// A rand.Int63() generates 63 random bits, enough for letterIdxMax letters!
	for i, cache, remain := n-1, rand.Int63(), letterIdxMax; i >= 0; {
		if remain == 0 {
			cache, remain = rand.Int63(), letterIdxMax
		}
		if idx := int(cache & letterIdxMask); idx < len(letterBytes) {
			b[i] = letterBytes[idx]
			i--
		}
		cache >>= letterIdxBits
		remain--
	}

	return string(b)
}

var src = rand.NewSource(time.Now().UnixNano())

func RandStringBytesMaskImprSrc(n int) string {
	b := make([]byte, n)
	// A src.Int63() generates 63 random bits, enough for letterIdxMax characters!
	for i, cache, remain := n-1, src.Int63(), letterIdxMax; i >= 0; {
		if remain == 0 {
			cache, remain = src.Int63(), letterIdxMax
		}
		if idx := int(cache & letterIdxMask); idx < len(letterBytes) {
			b[i] = letterBytes[idx]
			i--
		}
		cache >>= letterIdxBits
		remain--
	}

	return string(b)
}

func RandStringBytesMaskImprSrcSB(n int) string {
	sb := strings.Builder{}
	sb.Grow(n)
	// A src.Int63() generates 63 random bits, enough for letterIdxMax characters!
	for i, cache, remain := n-1, src.Int63(), letterIdxMax; i >= 0; {
		if remain == 0 {
			cache, remain = src.Int63(), letterIdxMax
		}
		if idx := int(cache & letterIdxMask); idx < len(letterBytes) {
			sb.WriteByte(letterBytes[idx])
			i--
		}
		cache >>= letterIdxBits
		remain--
	}

	return sb.String()
}

func RandStringBytesMaskImprSrcUnsafe(n int) string {
	b := make([]byte, n)
	// A src.Int63() generates 63 random bits, enough for letterIdxMax characters!
	for i, cache, remain := n-1, src.Int63(), letterIdxMax; i >= 0; {
		if remain == 0 {
			cache, remain = src.Int63(), letterIdxMax
		}
		if idx := int(cache & letterIdxMask); idx < len(letterBytes) {
			b[i] = letterBytes[idx]
			i--
		}
		cache >>= letterIdxBits
		remain--
	}

	return *(*string)(unsafe.Pointer(&b))
}

// Benchmark functions

const n = 16

func BenchmarkRunes(b *testing.B) {
	for i := 0; i < b.N; i++ {
		RandStringRunes(n)
	}
}

func BenchmarkBytes(b *testing.B) {
	for i := 0; i < b.N; i++ {
		RandStringBytes(n)
	}
}

func BenchmarkBytesRmndr(b *testing.B) {
	for i := 0; i < b.N; i++ {
		RandStringBytesRmndr(n)
	}
}

func BenchmarkBytesMask(b *testing.B) {
	for i := 0; i < b.N; i++ {
		RandStringBytesMask(n)
	}
}

func BenchmarkBytesMaskImpr(b *testing.B) {
	for i := 0; i < b.N; i++ {
		RandStringBytesMaskImpr(n)
	}
}

func BenchmarkBytesMaskImprSrc(b *testing.B) {
	for i := 0; i < b.N; i++ {
		RandStringBytesMaskImprSrc(n)
	}
}
func BenchmarkBytesMaskImprSrcSB(b *testing.B) {
	for i := 0; i < b.N; i++ {
		RandStringBytesMaskImprSrcSB(n)
	}
}

func BenchmarkBytesMaskImprSrcUnsafe(b *testing.B) {
	for i := 0; i < b.N; i++ {
		RandStringBytesMaskImprSrcUnsafe(n)
	}
}
```

#### Hash a password

```go
package main

import (
	"fmt"
	"log"

	"golang.org/x/crypto/bcrypt"
)

func main() {
	pw := "mypassword"

	isPasswordValid := checkPassword(hashPassword("mypassword"), pw)
	fmt.Println("Is password valid?", isPasswordValid)

}

func hashPassword(password string) (hashedPassword string) {

	hash, err := bcrypt.GenerateFromPassword([]byte(password), bcrypt.DefaultCost)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println("Hashed password", string(hash))

	return string(hash)

}

func checkPassword(hashedPassword string, password string) (isPasswordValid bool) {

	if err := bcrypt.CompareHashAndPassword([]byte(hashedPassword), []byte(password)); err != nil {
		return false
	}

	return true
}
```

### Array
Elements of the same type with a fixed length definined at the declaration stage. It cannot be expanded.

```go
var a [5]int                 // fixed 
var multiD [2][3]int         // multidimensional array       
```

### Slice
As arrays, but the length can be expanded.

```go
var b []int

numbers := make([]int,5,10)  // initial length of 5 and capacity of 10
```

Sub-slice can be created starting from another slice.

```go
// initialize a slice with 4 len and values
number2 = []int{1,2,3,4}
fmt.Println(numbers)     // -> [1 2 3 4]

// create sub slices
slice1 := number2[2:]
fmt.Println(slice1)      // -> [3 4]

slice2 := number2[:3]
fmt.Println(slice2)      // -> [1 2 3]

slice3 := number2[1:4]
fmt.Println(slice3)      // -> [2 3 4]
```

#### Remove element from slice

```go
if os.Args[1] == "QAC" || os.Args[1] == "QACPP" {
	os.Args = append(os.Args[:1], os.Args[2:]...)
}
```

#### Clear slice

```go
slice1 = nil
```

```go
slice1 := []int{1,2,3,4}
slice1 = nil
slice1 = []int{5}
fmt.Println(slice1)
```

```
[5]
```

#### Sort a slice in reverse mode

* [askgolang.com](https://askgolang.com/how-to-sort-a-slice-of-string-in-reverse-in-golang/)

```go
sort.Sort(sort.Reverse(sort.StringSlice(mySlice)))
```

### Map
Structure key-value

```go
var m map[string]int      // key is string - value is integer
```

```go
// adding key/value
m["clearity"] = 2
m["simplicity"] = 3

// printing the values
fmt.Println(m["clearity"])   // -> 2
fmt.Println(m["simplicity"]) // -> 3
```

```go
countryCapitalMap := map[string]string {
    "France": "Paris",
    "Italy":  "Rome",
    "Japan":  "Tokyo",
}
```

!!! info
    Last element needs to have the comma `,`


As usual in Go, we can declare our variable first, and then assign it a value:

```go
var menu map[string]float64
menu = map[string]float64{
    "eggs": 1.75,
    "bacon": 3.22,
    "sausage": 1.89,
}
```

Alternatively, we can use the short declaration syntax to do both operations in one step:

```go
menu := map[string]float64{
    "eggs": 1.75,
    "bacon": 3.22,
    "sausage": 1.89,
}
```

#### Map declaration and initialization as global
```go
package main

import "fmt"

var romanNumeralDict = map[int]string {
    1000: "M",
    900 : "CM",
    500 : "D",
    400 : "CD",
    100 : "C",
    90  : "XC",
    50  : "L",
    40  : "XL",
    10  : "X",
    9   : "IX",
    5   : "V",
    4   : "IV",
    1   : "I",
}

func main() {
    fmt.Println(romanNumeralDict[50])
}
```

!!! fail "panic: assignment to entry in nil map"
    It's raised when the map is declared global (and not inizialized) and the initialization occurs in a function:
    
    ```go
    package main
    
    var romanNumeralDict map[int]string
    
    func main() {
        romanNumeralDict[1000] = "M"
    }   
    ```

!!! fail "Why does this program panic?"
    ```go
    var m map[string]float64
    m["pi"] = 3.1416
    ```

    ```
    panic: assignment to entry in nil map
    ```
    
    **Answer**
    
    You have to initialize the map using the make function (or a map literal) before you can add any elements:
    ```go
    m := make(map[string]float64)
    m["pi"] = 3.1416
    ```

#### Check if a key is in the map
```go
if val, ok := dict["foo"]; ok {
    //do something here
}
```

##### Check second return value

```go
m := map[string]float64{"pi": 3.14}
v, found := m["pi"] // v == 3.14  found == true
v, found = m["pie"] // v == 0.0   found == false
_, found = m["pi"]  // found == true
```

##### Use second return value directly in an if statement

```go
m := map[string]float64{"pi": 3.14}
if v, found := m["pi"]; found {
    fmt.Println(v)
}
// Output: 3.14
```

##### Check for zero value

```go
m := map[string]float64{"pi": 3.14}

v := m["pi"] // v == 3.14
v = m["pie"] // v == 0.0 (zero value)
```

#### Iterate map in order

```go
package main

import (
	"fmt"
	"sort"
)

func main() {
	m := map[string]string{
		"2021.3": "C:\\Perforce\\Helix-QAC-2021.3",
		"2020.1": "C:\\Perforce\\Helix-QAC-2020.1",
		"2021.2": "C:\\Perforce\\Helix-QAC-2021.2",
		"2022.1": "C:\\Perforce\\Helix-QAC-2022.1",
	}

	keys := make([]string, 0, len(m))
	for k := range m {
		keys = append(keys, k)
	}
	sort.Strings(keys)

	for _, k := range keys {
		fmt.Println(k, m[k])
	}
}
```

#### Iterate map in numerical order

```go
var romanNumeralDict map[int]string = map[int]string{
  1000: "M",
  900 : "CM",
  500 : "D",
  400 : "CD",
  100 : "C",
  90  : "XC",
  50  : "L",
  40  : "XL",
  10  : "X",
  9   : "IX",
  5   : "V",
  4   : "IV",
  1   : "I",
}

keys := make([]int, 0)
for k, _ := range romanNumeralDict {
    keys = append(keys, k)
}
sort.Ints(keys)

for _, k := range keys {
    fmt.Println(k, romanNumeralDict[k])
}
```

!!! note
    Simple iteration would print:
    ```go
    for k, v := range romanNumeralDict {
        fmt.Println("k:", k, "v:", v)
    }
    ```
    However, this prints out
    ```
    k: 1000 v: M
    k: 40 v: XL
    k: 5 v: V
    k: 4 v: IV
    k: 900 v: CM
    k: 500 v: D
    k: 400 v: CD
    k: 100 v: C
    k: 90 v: XC
    k: 50 v: L
    k: 10 v: X
    k: 9 v: IX
    k: 1 v: I
    ```

#### Nested maps

```go
var x = map[string]map[string]string{}
```

```go
package main

import (
    "fmt"
)

func main() {
    var x = map[string]map[string]string{}

    x["fruits"] = map[string]string{}
    x["colors"] = map[string]string{}

    x["fruits"]["a"] = "apple"
    x["fruits"]["b"] = "banana"

    x["colors"]["r"] = "red"
    x["colors"]["b"] = "blue"

    fmt.Println(x)
}
```

```go
data["Date_2"]["Sistem_A"]["command_5"] = "violet"
```

The expression data["Date_2"] will return a nil-map. It is never initialized, so looking for the index ["Sistem_A"] panics. Initialize the map first:

```go
data["Date_2"]=make(map[string]map[string]string)
data["Date_2"]["Sistem_A"]=make(map[string]string)
data["Date_2"]["Sistem_A"]["command_5"] = "violet"
```


### Struct

* https://www.golangprograms.com/go-language/struct.html
* https://yourbasic.org/golang/structs-explained/

```go
package main

type Point struct {
    x int32
    y int32
}

func main() {
    var p1 Point = Point{1,2}
    var p2 Point = Point{-5,7}
}
```

* Struct methods: if used for modifying a struct value, the Struct argument needs to be passed as pointer.

    ```go
    package main
    
    import "fmt"
    
    type Student struct {
        name   string
        grades []int
        age    int
    }
    
    func (s Student) getAge() int {
        return s.age
    }
    
    func (s *Student) setAge(age int) {
        s.age = age
    }
    
    func main() {
        // create student
        s1 := Student{"Tim", []int{70, 90, 80, 85}, 19}
    
        // use method ".getAge()"
        fmt.Println(s1.getAge()) // 19
    
        // use method ".setAge()"
        s1.setAge(7)
        fmt.Println(s1) // {Tim [70 90 80 85] 7}
    
    }
    ```

#### Anonymous struct
* Useful especially for passing data to a template (see `http/template` or `text/template` packages)

```go
struct{Foo1, Foo2 string}{"Bar1", "Bar2"}
```

#### Embedded Struct

Struct inside another struct

```go
package main

import "fmt"

type Point struct {
    x int32
    y int32
}

type Circle struct {
    radius float64
    center *Point          // Struct inside another struct
}

func main() {
    c1 := Circle{4.56, &Point{4,5}}
    
    fmt.Println(c1.center)  // &{4,5}
}
```



```go
package main

import "fmt"

type Point struct {
    x int32
    y int32
}

type Circle struct {
    radius float64
    *Point          // Struct inside another struct
}

func main() {
    c1 := Circle{4.56, &Point{4,5}}
    
    fmt.Println(c1.x)  // 4
}
```


#### Struct as class

* [Class](https://golangbot.com/structs-instead-of-classes/)
* [Class and object in Go](https://www.geeksforgeeks.org/class-and-object-in-golang/)

```bash
go mod init oop 
```

```
├── Documents
│   └── oop
│       ├── employee
│       │   └── employee.go
│       ├── go.mod
│       └── main.go
```

```go
package employee

import (  
    "fmt"
)

type Employee struct {  
    FirstName   string
    LastName    string
    TotalLeaves int
    LeavesTaken int
}

func (e Employee) LeavesRemaining() {  
    fmt.Printf("%s %s has %d leaves remaining\n", e.FirstName, e.LastName, (e.TotalLeaves - e.LeavesTaken))
}
```

```go
package main

import "oop/employee"

func main() {  
    e := employee.Employee {
        FirstName: "Sam",
        LastName: "Adolf",
        TotalLeaves: 30,
        LeavesTaken: 20,
    }
    e.LeavesRemaining()
}
```

```
Sam Adolf has 10 leaves remaining  
```


!!! fail
    ```go
    package main

    import "oop/employee"
    
    func main() {  
        var e employee.Employee
        e.LeavesRemaining()
    }
    ```
    ```
      has 0 leaves remaining
    ```


!!! success
    * Starting letter `e` of Employee struct to lower case in line no. 7, that is we have changed `type Employee struct` to `type employee struct` => By doing so we have successfully unexported the employee struct and prevented access from other packages.
    * Since we don't need to access the fields of the employee struct anywhere outside the employee package, we have unexported all the fields too.
    * We are providing an exported New function in line no. 14 which takes the required parameters as input and returns a newly created employee. 
    * In the `main.go` we have created a new employee by passing the required parameters to the New function.
    ```go
    package employee

    import (  
        "fmt"
    )
    
    type employee struct {  
        firstName   string
        lastName    string
        totalLeaves int
        leavesTaken int
    }
    
    func New(firstName string, lastName string, totalLeave int, leavesTaken int) employee {  
        e := employee {firstName, lastName, totalLeave, leavesTaken}
        return e
    }
    
    func (e employee) LeavesRemaining() {  
        fmt.Printf("%s %s has %d leaves remaining\n", e.firstName, e.lastName, (e.totalLeaves - e.leavesTaken))
    }
    ```
    
    ```go
    package main  
    
    import "oop/employee"
    
    func main() {  
        e := employee.New("Sam", "Adolf", 30, 20)
        e.LeavesRemaining()
    }
    ```
    
    ```
    Sam Adolf has 10 leaves remaining  
    ```



##### New constructor like

```go
package employee

import (  
    "fmt"
)

type employee struct {  
    firstName   string
    lastName    string
    totalLeaves int
    leavesTaken int
}

func New(firstName string, lastName string, totalLeave int, leavesTaken int) employee {  
    e := employee {firstName, lastName, totalLeave, leavesTaken}
    return e
}

func (e employee) LeavesRemaining() {  
    fmt.Printf("%s %s has %d leaves remaining\n", e.firstName, e.lastName, (e.totalLeaves - e.leavesTaken))
}
```

```go
package main  

import "oop/employee"

func main() {  
    e := employee.New("Sam", "Adolf", 30, 20)
    e.LeavesRemaining()
}
```


#### Tags
A tag for a field allows you to attach meta-information to the field which can be acquired using reflection.

Usually it is used to provide transformation info on how a struct field is encoded to or decoded from another format (or stored/retrieved from a database), but you can use it to store whatever meta-info you want to, either intended for another package or for your own use.

```go
type User struct {
    Name string `json:"name" xml:"name"`
}
```

The key usually denotes the package that the subsequent "value" is for, for example json keys are processed/used by the encoding/json package.

Here is a list of commonly used tag keys:

- `json   ` - used by the [`encoding/json`](https://golang.org/pkg/encoding/json/) package, detailed at [`json.Marshal()`](https://golang.org/pkg/encoding/json/#Marshal)
- `xml   ` - used by the [`encoding/xml`](https://golang.org/pkg/encoding/xml/) package, detailed at [`xml.Marshal()`](https://golang.org/pkg/encoding/xml/#Marshal)
- `bson   ` - used by [gobson](https://labix.org/gobson), detailed at [`bson.Marshal()`](http://godoc.org/gopkg.in/mgo.v2/bson#Marshal)
- `protobuf ` - used by [`github.com/golang/protobuf/proto`](http://godoc.org/github.com/golang/protobuf/proto), detailed in the package doc
- `yaml   ` - used by the [`gopkg.in/yaml.v2`](https://godoc.org/gopkg.in/yaml.v2) package, detailed at [`yaml.Marshal()`](https://godoc.org/gopkg.in/yaml.v2#Marshal)
- `db    ` - used by the [`github.com/jmoiron/sqlx`](https://godoc.org/github.com/jmoiron/sqlx) package; also used by [`github.com/go-gorp/gorp`](https://github.com/go-gorp/gorp) package
- `orm   ` - used by the [`github.com/astaxie/beego/orm`](https://godoc.org/github.com/astaxie/beego/orm) package, detailed at [Models – Beego ORM](https://beego.me/docs/mvc/model/overview.md)
- `gorm   ` - used by the [`github.com/jinzhu/gorm`](https://github.com/jinzhu/gorm) package, examples can be found in their doc: [Models](http://jinzhu.me/gorm/models.html)
- `valid  ` - used by the [`github.com/asaskevich/govalidator`](https://github.com/asaskevich/govalidator) package, examples can be found in the project page
- `datastore` - used by [`appengine/datastore`](https://cloud.google.com/appengine/docs/go/datastore/reference) (Google App Engine platform, Datastore service), detailed at [Properties](https://cloud.google.com/appengine/docs/go/datastore/reference#hdr-Properties)
- `schema  ` - used by [`github.com/gorilla/schema`](http://godoc.org/github.com/gorilla/schema) to fill a `struct` with HTML form values, detailed in the package doc
- `asn   ` - used by the [`encoding/asn1`](https://golang.org/pkg/encoding/asn1/) package, detailed at [`asn1.Marshal()`](https://golang.org/pkg/encoding/asn1/#Marshal) and [`asn1.Unmarshal()`](https://golang.org/pkg/encoding/asn1/#Unmarshal)
- `csv   ` - used by the [`github.com/gocarina/gocsv`](https://github.com/gocarina/gocsv) package



#### Interface

Allows to implement a slice containing values of different types (as lists in python)

```go
func main() {
arr := []interface{}{1, 2, "apple", true}
fmt.Println(arr)

i := arr[0].(int)
fmt.Printf("i: %d, i type: %T\n", i, i)

s := arr[2].(string)
fmt.Printf("b: %s, i type: %T\n", s, s)

fmt.Printf("b: %s, i type: %T\n", arr[2], arr[2])
}
```

```
[1 2 apple true]
i: 1, i type: int
b: apple, i type: string
b: apple, i type: string
```

* Convert interface to a type
```go
switch record[field].(type) {
case int:
    value = record[field].(int)
case float64:
    value = record[field].(float64)
case string:
    value = record[field].(string)
}
```

### Empty Interface

The interface type that specifies zero methods is known as the *empty interface*:

```
interface{}
```

An empty interface may hold values of any type. (Every type implements at least zero methods).

They are used by code that handles values of unknown type. 

```go
package main

import "fmt"

func main() {
	var i interface{}
	describe(i)

	i = 42
	describe(i)

	i = "hello"
	describe(i)
}

func describe(i interface{}) {
	fmt.Printf("(%v, %T)\n", i, i)
}
```

```
(<nil>, <nil>)
(42, int)
(hello, string)
```


### Type Declarations

Craetes a type alias which can make more sense in the application

```go
// Create types
type Celsius float64
type IDnum int

// Use new types
var temp Celsius
var pid IDnum
```

### Type Conversions

```go
T()  // where T is the final type 
```

```go
var x int32 = 1
var y int16 = 2
x = y // not possible as the types are different: cannot use y (type int16) as type int32 in assignment

x = int32(y)
```


### Error

Error type is returned by functions

```go
err := router.Run(":8081")
if err != nil {
    fmt.Println(err)
    return
}
```

* Create an error
    ```go
    errors.New("math: square root of negative number")
    ```

    ```go
    func Sqrt(f float64) (float64, error) {
        if f < 0 {
            return 0, errors.New("math: square root of negative number")
        }
        // implementation
    
        return 0, nil
    }
    ```

* Convert error type to string
    ```go
    fmt.Sprint(err)
    ```


-----------------------------------------------------------------------------------

## Printing / String formatting

* `Print` : formats using the default formats for its operands and writes to standard output. Spaces are added between operands when neither is a string. It returns the number of bytes written and any write error encountered.
* `Printf` : formats according to a format specifier and writes to standard output. It returns the number of bytes written and any write error encountered.
* `Println` : formats using the default formats for its operands and writes to standard output. Spaces are always added between operands and a newline is appended. It returns the number of bytes written and any write error encountered.
* `Sprint` : formats using the default formats for its operands and returns the resulting string. Spaces are added between operands when neither is a string.
* `Sprintf` : formats according to a format specifier and returns the resulting string.
* `Sprintln` : formats using the default formats for its operands and returns the resulting string. Spaces are always added between operands and a newline is appended.
* `io.WriteString(os.Stdout, s)`

```go
package main

import (
	"fmt"
	"io"
	"os"
)

func main() {
	const name, age = "Kim", 22

    /* Print */
    fmt.Print(name, " is ", age, " years old.\n")

    /* Printf */
    fmt.Printf("%s is %d years old.\n", name, age)

    /* Println */
    fmt.Println(name, "is", age, "years old.")

    /* Sprint */
	s := fmt.Sprint(name, " is ", age, " years old.\n")
	io.WriteString(os.Stdout, s) // Ignoring error for simplicity.

    /* Sprintf */
	s := fmt.Sprintf("%s is %d years old.\n", name, age)
	io.WriteString(os.Stdout, s) // Ignoring error for simplicity.

    /* Sprintln */
    s := fmt.Sprintln(name, "is", age, "years old.")
	io.WriteString(os.Stdout, s) // Ignoring error for simplicity.
}
```

```go
fmt.Printf("Hi")

x := "Joe"

fmt.Printf("Hi " + x)

> Hi Joe
```

```go
fmt.Printf("Hi %s", x)
```

### Format variables

* [https://golang.org/pkg/fmt/](https://golang.org/pkg/fmt/)

```go
package main

import (
	"fmt"		
)

var(
	a = 654
	b = false
	c   = 2.651
	d  = 4 + 1i
	e   = "Australia"
	f = 15.2 * 4525.321
)

func main(){	
	fmt.Printf("d for Integer: %d\n", a)
	fmt.Printf("6d for Integer: %6d\n", a)
	
	fmt.Printf("t for Boolean: %t\n", b)
	fmt.Printf("g for Float: %g\n", c)
	fmt.Printf("e for Scientific Notation: %e\n", d)
	fmt.Printf("E for Scientific Notation: %E\n", d)
	fmt.Printf("s for String: %s\n", e)
	fmt.Printf("G for Complex: %G\n", f)
	
	fmt.Printf("15s String: %15s\n", e)
	fmt.Printf("-10s String: %-10s\n",e)
	
	t:= fmt.Sprintf("Print from right: %[3]d %[2]d %[1]d\n", 11, 22, 33)
	fmt.Println(t)	
}
```

```
d for Integer: 654
6d for Integer:    654
t for Boolean: false
g for Float: 2.651
e for Scientific Notation: (4.000000e+00+1.000000e+00i)
E for Scientific Notation: (4.000000E+00+1.000000E+00i)
s for String: Australia
G for Complex: 68784.8792
15s String:     Australia
-10s String: Australia
Print from right: 33 22 11
```

* General:

    ```
    %v	the value in a default format
        when printing structs, the plus flag (%+v) adds field names
    %#v	a Go-syntax representation of the value
    %T	a Go-syntax representation of the type of the value
    %%	a literal percent sign; consumes no value
    ```

* Boolean:

    ```
    %t	the word true or false
    ```

* Integer:

    ```
    %b	base 2
    %c	the character represented by the corresponding Unicode code point
    %d	base 10
    %o	base 8
    %O	base 8 with 0o prefix
    %q	a single-quoted character literal safely escaped with Go syntax.
    %x	base 16, with lower-case letters for a-f
    %X	base 16, with upper-case letters for A-F
    %U	Unicode format: U+1234; same as "U+%04X"
    ```

* Floating-point and complex constituents:

    ```
    %b	decimalless scientific notation with exponent a power of two,
        in the manner of strconv.FormatFloat with the 'b' format,
        e.g. -123456p-78
    %e	scientific notation, e.g. -1.234456e+78
    %E	scientific notation, e.g. -1.234456E+78
    %f	decimal point but no exponent, e.g. 123.456
    %F	synonym for %f
    %g	%e for large exponents, %f otherwise. Precision is discussed below.
    %G	%E for large exponents, %F otherwise
    %x	hexadecimal notation (with decimal power of two exponent), e.g. -0x1.23abcp+20
    %X	upper-case hexadecimal notation, e.g. -0X1.23ABCP+20
    ```

* String and slice of bytes (treated equivalently with these verbs):

    ```
    %s	the uninterpreted bytes of the string or slice
    %q	a double-quoted string safely escaped with Go syntax
    %x	base 16, lower-case, two characters per byte
    %X	base 16, upper-case, two characters per byte
    ```

* Slice:

    ```
    %p	address of 0th element in base 16 notation, with leading 0x
    ```

* Pointer:

    ```
    %p	base 16 notation, with leading 0x
    The %b, %d, %o, %x and %X verbs also work with pointers,
    formatting the value exactly as if it were an integer.
    ```

* The default format for %v is:

    ```    
    bool:                    %t
    int, int8 etc.:          %d
    uint, uint8 etc.:        %d, %#x if printed with %#v
    float32, complex64, etc: %g
    string:                  %s
    chan:                    %p
    pointer:                 %p
    ```

* For compound objects, the elements are printed using these rules, recursively, laid out like this:

    ```
    struct:             {field0 field1 ...}
    array, slice:       [elem0 elem1 ...]
    maps:               map[key1:value1 key2:value2 ...]
    pointer to above:   &{}, &[], &map[]
    ```

* Width is specified by an optional decimal number immediately preceding the verb. If absent, the width is whatever is necessary to represent the value. Precision is specified after the (optional) width by a period followed by a decimal number. If no period is present, a default precision is used. A period with no following number specifies a precision of zero. Examples:

    ```
    %f     default width, default precision
    %9f    width 9, default precision
    %.2f   default width, precision 2
    %9.2f  width 9, precision 2
    %9.f   width 9, precision 0
    ```

### Pretty print
```go
package main

import (
	"fmt"

	"github.com/kr/pretty"
)

func main() {
	type myType struct {
		a, b int
	}
	var x = []myType{{1, 2}, {3, 4}, {5, 6}}
	fmt.Printf("%# v", pretty.Formatter(x))
}
```

Output:
```
[]pretty_test.myType{
    {a:1, b:2},
    {a:3, b:4},
    {a:5, b:6},
}
```

### Print with colors

* [gookit/color](https://github.com/gookit/color)
* [fatih/color](https://github.com/fatih/color)
* [logrusorgru/aurora](https://github.com/logrusorgru/aurora)
* [TwiN/go-color](https://github.com/TwiN/go-color)

#### gookit/color

```go
package main

import (
	"fmt"

	"github.com/gookit/color"
)

func main() {
	// quick use package func
	color.Redp("Simple to use color")
	color.Redln("Simple to use color")
	color.Greenp("Simple to use color\n")
	color.Cyanln("Simple to use color")
	color.Yellowln("Simple to use color")

	// quick use like fmt.Print*
	color.Red.Println("Simple to use color")
	color.Green.Print("Simple to use color\n")
	color.Cyan.Printf("Simple to use %s\n", "color")
	color.Yellow.Printf("Simple to use %s\n", "color")

	// use like func
	red := color.FgRed.Render
	green := color.FgGreen.Render
	fmt.Printf("%s line %s library\n", red("Command"), green("color"))

	// custom color
	color.New(color.FgWhite, color.BgBlack).Println("custom color style")

	// can also:
	color.Style{color.FgCyan, color.OpBold}.Println("custom color style")

	// internal theme/style:
	color.Info.Tips("message")
	color.Info.Prompt("message")
	color.Info.Println("message")
	color.Warn.Println("message")
	color.Error.Println("message")

	// use style tag
	color.Print("<suc>he</><comment>llo</>, <cyan>wel</><red>come</>\n")
	// Custom label attr: Supports the use of 16 color names, 256 color values, rgb color values and hex color values
	color.Println("<fg=11aa23>he</><bg=120,35,156>llo</>, <fg=167;bg=232>wel</><fg=red>come</>")

	// apply a style tag
	color.Tag("info").Println("info style text")

	// prompt message
	color.Info.Prompt("prompt style message")
	color.Warn.Prompt("prompt style message")

	// tips message
	color.Info.Tips("tips style message")
	color.Warn.Tips("tips style message")
}
```

#### TwiN/go-color
```go
package main

import "github.com/TwiN/go-color"

func main() {
    println(color.Ize(color.Red, "This is red"))
    // Or if you prefer the longer version
    println(color.Colorize(color.Red, "This is also red"))
}
```


-----------------------------------------------------------------------------------

## Get user input (Scan STDIN)

### Scan

```go
package main

import "fmt"

func main() {
    fmt.Print("Enter text: ")
    var input string
    fmt.Scanln(&input)
    fmt.Print(input)
}
```

### bufio

```go
package main

import "fmt"
import "bufio"

func main() {
    reader := bufio.NewReader(os.Stdin)
    fmt.Print("Enter text: ")
    text, _ := reader.ReadString('\n')
    fmt.Println(text)
}
```

### io/ioutil

Stdin used to read the data from command line.
After each line press "Enter" and stop writing press "Ctrl+C

```go
package main

import (
	"io"
	"io/ioutil"
	"log"
	"fmt"
	"os"
)

func main() {
	fmt.Printf("Enter the text:\n")
	writeText, err := os.Open(os.DevNull)
	if err != nil {
		log.Fatalf("failed to open a null device: %s", err)
	}
	defer writeText.Close()
	io.WriteString(writeText,"Write Text")
	
	readText, err := ioutil.ReadAll(os.Stdin)
	if err != nil {
		log.Fatalf("failed to read stdin: %s", err)
	}
	fmt.Printf("\nLength: %d", len(readText))
	fmt.Printf("\nData Read: \n%s", readText)
}
```

* [tutorialedge](https://tutorialedge.net/golang/reading-console-input-golang/)
* [freshman](https://freshman.tech/snippets/go/read-console-input/)
* [gosamples](https://gosamples.dev/read-user-input/)

-----------------------------------------------------------------------------------

## Control Flow

### IF

```go
if num := 9; num < 0 {
 fmt.Println(num, "is negative")
} else if num < 10 {
 fmt.Println(num, "has 1 digit")
} else {
 fmt.Println(num, "has multiple digits")
}
```

!!! info 
    `} else {` cannot be split in more lines like
    ```
    } 
    else
    {
    ```
    as it will result in syntax error.

### Switch case
Allows to handle multiple conditions

```go
i := 2
switch i {
case 1:
    fmt.Println("one")
case 2:
    fmt.Println("two")
default:
    fmt.Println("none")
}
```

### FOR Loop

* Standard iteration
    ```go
    for i:=0; i<10; i++ {
        fmt.Printf("Hi")
    }
    ```

* Short version
    ```go
    i=0
    for i<10 {
        fmt.Printf("Hi")
        i++
    }
    ```

* Infinite loop. You can exit with `break` keyword
    ```go
    for {
        fmt.Printf("Hi")
    }
    ```

#### Range

* [yourbasic.org](https://yourbasic.org/golang/for-loop-range-array-slice-map-channel/#basic-for-each-loop-slice-or-array)
* [tutorialspoint.com](https://www.tutorialspoint.com/go/go_range.htm)

The `range` form of the for loop iterates over an array, slice, channel or map.

When ranging over a slice, two values are returned for each iteration. The first is the index, and the second is a copy of the element at that index.

```go
package main

import "fmt"

var pow = []int{1, 2, 4, 8, 16, 32, 64, 128}

func main() {
	for i, v := range pow {
		fmt.Printf("2**%d = %d\n", i, v)
	}
}
```


| Range expression      | 1st Value   | 2nd Value(Optional) |
| --------------------- | ----------- | ------------------- |
| Array or slice a [n]E | index i int | a[i] E              |
| String s string type  | index i int | rune int            |
| map m map[K]V         | key k K     | value m[k] V        |
| channel c chan E      | element e E | none                |


* Basic for-each loop (slice or array)
    ```go
    /* create a slice */
    numbers := []int{0,1,2,3,4,5,6,7,8} 
    
    /* print the numbers */
    for i := range numbers {
        fmt.Println("Slice item", i, "is", numbers[i])
    }
    ```

* String iteration: runes or bytes
    ```go
    for i, ch := range "日本語" {
        fmt.Printf("%#U starts at byte position %d\n", ch, i)
    }
    ```

    ```
    U+65E5 '日' starts at byte position 0
    U+672C '本' starts at byte position 3
    U+8A9E '語' starts at byte position 6
    ```

    ```go
    const s = "日本語"
    for i := 0; i < len(s); i++ {
        fmt.Printf("%x ", s[i])
    }
    ```

    ```
    e6 97 a5 e6 9c ac e8 aa 9e
    ```


* Map iteration: keys and values
    ```go
    /* create a map*/
    countryCapitalMap := map[string] string {
        "France": "Paris", 
        "Italy": "Rome", 
        "Japan": "Tokyo",
    }
    
    /* print map using keys*/
    for country := range countryCapitalMap {
        fmt.Println("Capital of", country, "is", countryCapitalMap[country])
    }
    
    /* print map using key-value*/
    for country, capital := range countryCapitalMap {
        fmt.Println("Capital of", country, "is", capital)
    }
    ```
    
    ```go
    m := map[string]int{
        "one":   1,
        "two":   2,
        "three": 3,
    }
    for k, v := range m {
        fmt.Println(k, v)
    }
    ```
    ```
    two 2
    three 3
    one 1
    ```
    
* Channel iteration

    For [channels](https://yourbasic.org/golang/channels-explained/), the iteration values are the successive values sent on the channel until closed.

    ```go
    ch := make(chan int)
    
    go func() {
        ch <- 1
        ch <- 2
        ch <- 3
        close(ch)
    }()
    
    for n := range ch {
        fmt.Println(n)
    }
    ```

    ```
    1
    2
    3
    ```

    

-----------------------------------------------------------------------------------

## panic - defer - recover

* [golangbot.com](https://golangbot.com/panic-and-recover/)

* Allow to handle abnormal conditions in Go.

### panic

Terminates the program prematurely.

When a function encounters a panic:

1. Its execution is stopped
1. Any deferred functions are executed
1. The argument passed to the panic function will be printed when the program terminates.



```go
{data-line-numbers="all|7,10|all"}
package main

import "fmt"

func fullName(firstName *string, lastName *string) {  
    if firstName == nil {
        panic("runtime error: first name cannot be nil")
    }
    if lastName == nil {
        panic("runtime error: last name cannot be nil")
    }
    fmt.Printf("%s %s\n", *firstName, *lastName)
    fmt.Println("returned normally from fullName")
}

func main() {  
    firstName := "Elon"
    fullName(&firstName, nil)
    fmt.Println("returned normally from main")
}
```


```
panic: runtime error: last name cannot be nil

goroutine 1 [running]:  
main.fullName(0xc00006af58, 0x0)  
    /tmp/sandbox210590465/prog.go:12 +0x193
main.main()  
    /tmp/sandbox210590465/prog.go:20 +0x4d
```


### defer

Functions to be executed before panic leads to the program termination

```go
{data-line-numbers="all|18|20|6|11|6|18|all"}
package main

import "fmt"

func fullName(firstName *string, lastName *string) {  
    defer fmt.Println("deferred call in fullName")
    if firstName == nil {
        panic("runtime error: first name cannot be nil")
    }
    if lastName == nil {
        panic("runtime error: last name cannot be nil")
    }
    fmt.Printf("%s %s\n", *firstName, *lastName)
    fmt.Println("returned normally from fullName")
}

func main() {  
    defer fmt.Println("deferred call in main")
    firstName := "Elon"
    fullName(&firstName, nil)
    fmt.Println("returned normally from main")
}
```


```go
deferred call in fullName  
deferred call in main  
panic: runtime error: last name cannot be nil

goroutine 1 [running]:  
main.fullName(0xc00006af28, 0x0)  
    /tmp/sandbox451943841/prog.go:13 +0x23f
main.main()  
    /tmp/sandbox451943841/prog.go:22 +0xc6
```


### recover

Allows to recover from a panic, raising the error, but avoiding the program to terminate

```go
{data-line-numbers="all|5-9|all"}
package main

import "fmt"

func recoverFullName() {  
    if r := recover(); r!= nil {
        fmt.Println("recovered from ", r)
    }
}

func fullName(firstName *string, lastName *string) {  
    defer recoverFullName()
    if firstName == nil {
        panic("runtime error: first name cannot be nil")
    }
    if lastName == nil {
        panic("runtime error: last name cannot be nil")
    }
    fmt.Printf("%s %s\n", *firstName, *lastName)
    fmt.Println("returned normally from fullName")
}

func main() {  
    defer fmt.Println("deferred call in main")
    firstName := "Elon"
    fullName(&firstName, nil)
    fmt.Println("returned normally from main")
}
```

```
recovered from  runtime error: last name cannot be nil  
returned normally from main  
deferred call in main
```

### End program without stack messages
By default `panic` prints the full stack of messages. With the code below, the error message passed by the panic function is printed and no other info are disclosed.

```go

func handleError() {
	if r := recover(); r != nil {
		fmt.Println("[ERROR] : ", r)
	}
}

func main() {
	defer handleError()
    panic("No valid path has been entered. Exit!")
}
```



-----------------------------------------------------------------------------------

## Filepath

### Get current working directory

```go
// Get current working directory
func getcwd() string {
  path, _ := os.Getwd()

  return path
}
```

### Get current source code file path

```go
// Get current source code file path
func getSrcPath() string {
  _, filename, _, ok := runtime.Caller(0)
  if !ok {
    return ""
  }

  return filepath.Dir(filename)
}
```

### Get executable path

```go
// Get executable path
func getExePath() string {
  ex, err := os.Executable()
  if err != nil {
    return ""
  }
  return filepath.Dir(ex)
}
```

-----------------------------------------------------------------------------------

## File

### Check if file exists

```go
if _, err := os.Stat("/path/to/whatever"); errors.Is(err, os.ErrNotExist) {
  // path/to/whatever does not exist
}
```

To check if a file exists, equivalent to Python's if os.path.exists(filename):

```go
if _, err := os.Stat("/path/to/whatever"); err == nil {
  // path/to/whatever exists

} else if errors.Is(err, os.ErrNotExist) {
  // path/to/whatever does *not* exist

} else {
  // Schrodinger: file may or may not exist. See err for details.

  // Therefore, do *NOT* use !os.IsNotExist(err) to test for file existence


}
```


### Get Folder content

```go
package main

import (
    "fmt"
    "os"
     "log"
)

func main() {
    fileOpen, err := os.Open(serverPath)
    if err != nil {
        log.Fatal(err)
    }
    defer fileOpen.Close()
    files, _ := fileOpen.Readdir(0)
}
```

* deprecated
```go
package main

import (
    "fmt"
    "io/ioutil"
     "log"
)

func main() {
    files, err := ioutil.ReadDir("./")
    if err != nil {
        log.Fatal(err)
    }
 
    for _, f := range files {
            fmt.Println(f.Name())
    }
}
```

#### Sort Files

##### Sort files by name

```go
// this is the default sort order of golang os.Open -> ReadDir
func SortFileNameAscend(files []os.FileInfo) {
	sort.Slice(files, func(i, j int) bool {
		return files[i].Name() < files[j].Name()
	})
}

func SortFileNameDescend(files []os.FileInfo) {
	sort.Slice(files, func(i, j int) bool {
		return files[i].Name() > files[j].Name()
	})
}
```

#### Compress a folder

```go
package nain

import (
    "archive/zip"
    "os"
    "path/filepath"
)

// compress a folder
func zipFolder(source, target string) error {
	// 1. Create a ZIP file and zip.Writer
	f, err := os.Create(target)
	if err != nil {
		return err
	}
	defer f.Close()

	writer := zip.NewWriter(f)
	defer writer.Close()

	// 2. Go through all the files of the source
	return filepath.Walk(source, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}

		// 3. Create a local file header
		header, err := zip.FileInfoHeader(info)
		if err != nil {
			return err
		}

		// set compression
		header.Method = zip.Deflate

		// 4. Set relative path of a file as the header name
		header.Name, err = filepath.Rel(filepath.Dir(source), path)
		if err != nil {
			return err
		}
		if info.IsDir() {
			header.Name += "/"
		}

		// 5. Create writer for the file header and save content of the file
		headerWriter, err := writer.CreateHeader(header)
		if err != nil {
			return err
		}

		if info.IsDir() {
			return nil
		}

		f, err := os.Open(path)
		if err != nil {
			return err
		}
		defer f.Close()

		_, err = io.Copy(headerWriter, f)
		return err
	})
}
```

### Iterate a path

* [https://xojoc.pw/blog/golang-file-tree-traversal](https://xojoc.pw/blog/golang-file-tree-traversal)

```go
filepath.Walk("/path/to/folder", func(name string, info os.FileInfo, err error) error {
    fmt.Println(name)
    return nil
})
```

```go
package main

import (
    "fmt"
    "io/ioutil"
     "log"
)

func main() {
    var files []string
    err := filepath.Walk(root, func(path string, info os.FileInfo, err error) error {
        if !info.IsDir() {
            files = append(files, path)  // here the action before moving to the next element
        }
        return nil
    })
    return files, err
}
```

### Get file info

```go
package main
 
import (
	"fmt"
	"log"
	"os"
)
 
func main() {
	fileStat, err := os.Stat("test.txt")
 
	if err != nil {
		log.Fatal(err)
	}
 
	fmt.Println("File Name:", fileStat.Name())        // Base name of the file
	fmt.Println("Size:", fileStat.Size())             // Length in bytes for regular files
	fmt.Println("Permissions:", fileStat.Mode())      // File mode bits
	fmt.Println("Last Modified:", fileStat.ModTime()) // Last modification time
	fmt.Println("Is Directory: ", fileStat.IsDir())   // Abbreviation for Mode().IsDir()
}
```

```go
package main

import (
    "fmt"
    "os"
)

func main() {
    name := "FileOrDir"
    fi, err := os.Stat(name)
    if err != nil {
        fmt.Println(err)
        return
    }
    switch mode := fi.Mode(); {
    case mode.IsDir():
        // do directory stuff
        fmt.Println("directory")
    case mode.IsRegular():
        // do file stuff
        fmt.Println("file")
    }
}
```

### Read a file

#### Read entire file
```go


package main

import (
    "fmt"
    "io/ioutil"
    "log"
)

func main() {

    // Read entire file content, giving us little control but
    // making it very simple. No need to close the file.
    content, err := ioutil.ReadFile("golangcode.txt")
    if err != nil {
        log.Fatal(err)
    }

    // Convert []byte to string and print to screen
    text := string(content)
    fmt.Println(text)
}
```

#### Read file line by line
```go
package main

import (
    "bufio"
    "fmt"
    "log"
    "os"
)

func main() {

    f, err := os.Open("thermopylae.txt")

    if err != nil {
        log.Fatal(err)
    }

    defer f.Close()

    scanner := bufio.NewScanner(f)

    for scanner.Scan() {

        fmt.Println(scanner.Text())
    }

    if err := scanner.Err(); err != nil {
        log.Fatal(err)
    }
}
```

#### Read file and store as slice
```go
// readLines reads a whole file into memory
// and returns a slice of its lines.
func readLines(path string) ([]string, error) {
    file, err := os.Open(path)
    if err != nil {
        return nil, err
    }
    defer file.Close()

    var lines []string
    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        lines = append(lines, scanner.Text())
    }
    return lines, scanner.Err()
}
```


### Write file from array
```go
// writeLines writes the lines to the given file.
func writeLines(lines []string, path string) error {
    file, err := os.Create(path)
    if err != nil {
        return err
    }
    defer file.Close()

    w := bufio.NewWriter(file)
    for _, line := range lines {
        fmt.Fprintln(w, line)
    }
    return w.Flush()
}
```

### Parse XML
* [antchfx/xmlquery](https://github.com/antchfx/xmlquery) - [golangprograms.com](https://www.golangprograms.com/dynamic-xml-parser-without-struct-in-go.html)
* [antchfx/htmlquery](https://github.com/antchfx/htmlquery)
* [beevik/etree](https://github.com/beevik/etree)
* [tutorialedge.net](https://tutorialedge.net/golang/parsing-xml-with-golang/)
* [https://gobyexample.com/xml](https://gobyexample.com/xml)
* [https://medium.com/swlh/parsing-xml-with-golang-aeeb69222532](https://medium.com/swlh/parsing-xml-with-golang-aeeb69222532)

* [XPath reference](https://www.w3schools.com/xml/xpath_syntax.asp)

**Selecting Nodes**

XPath uses path expressions to select nodes in an XML document. The node is selected by following a path or steps.  The most useful  path expressions are listed below:

| Expression | Description                                                  |
| ---------- | ------------------------------------------------------------ |
| *nodename* | Selects all nodes with the name "*nodename*"                 |
| /          | Selects from the root node                                   |
| //         | Selects nodes in the document from the current node that match the selection no matter where they are |
| .          | Selects the current node                                     |
| ..         | Selects the parent of the current node                       |
| @          | Selects attributes                                           |

In the table below we have listed some path expressions and the result of the  expressions:

| Path Expression | Result                                                       |
| --------------- | ------------------------------------------------------------ |
| bookstore       | Selects all nodes with the name "bookstore"                  |
| /bookstore      | Selects the root element bookstore**Note:** If the path starts with a slash ( / ) it always represents an absolute  path to an element! |
| bookstore/book  | Selects all book elements that are children of bookstore     |
| //book          | Selects all book elements no matter where they are in the document |
| bookstore//book | Selects all book elements that are descendant of the bookstore element, no matter where they are under the bookstore element |
| //@lang         | Selects all attributes that are named lang                   |

* `/ancestor` : It's more powerful than parent since it can get even the grandparent or great great grandparent

    ```go
    ancestorRuleNodes := xmlquery.Find(rule, "/ancestor::rule")
    ```

```go
func getXmlAttrs(node *xmlquery.Node) map[string]string {
	AttrsMap := make(map[string]string)

	for _, att := range node.Attr {

		AttrsMap[att.Name.Local] = att.Value
	}

	return AttrsMap
}
```

### Parse JSON

#### Parse JSON with struct (typed)

```go
package main

import (
    "encoding/json"
    "log"
    "os"
)

func main() {
    // read file
	settingsBytes, err1 := os.ReadFile(settingFile)
	if err1 != nil {
		log.Fatal(err1)
	}

	settingsStr := string(settingsBytes)

	rawData := []byte(settingsStr)
	var payload interface{}                  //The interface where we will save the converted JSON data.
	err := json.Unmarshal(rawData, &payload) // Convert JSON data into interface{} type
	if err != nil {
		log.Fatal(err)
	}

	m := payload.(map[string]interface{}) // To use the converted data we will need to convert it into a map[string]interface{}
}
```


#### Parse JSON with interface (untyped)

```go
package main

import (
    "encoding/json"
    "log"
    "os"
)

func main() {
    // read file
	settingsBytes, err1 := os.ReadFile(settingFile)
	if err1 != nil {
		log.Fatal(err1)
	}

	settingsStr := string(settingsBytes)

	rawData := []byte(settingsStr)
	var payload interface{}                  //The interface where we will save the converted JSON data.
	err := json.Unmarshal(rawData, &payload) // Convert JSON data into interface{} type
	if err != nil {
		log.Fatal(err)
	}

	m := payload.(map[string]interface{}) // To use the converted data we will need to convert it into a map[string]interface{}
}
```

#### My functions

```go
func readSettingsInterface(settingFile string) map[string]interface{} {
	/* Read settings */
	settingsMap = make(map[string]string)

	if _, err := os.Stat(settingsFile); err == nil {
		settingsBytes, err := os.ReadFile(settingsFile)
		if err != nil {
			log.Fatal(err)
		}
		settingsStr := string(settingsBytes)

		json.Unmarshal([]byte(settingsStr), &settingsMap)

	} else {
		log.Fatalf(color.Red.Sprint(settingsFile + " does not exist!"))
	}

	return settingsMap
}

func readSettings(settingsFile string) map[string]string {
	/* Read settings */
	settingsMap = make(map[string]string)

	if _, err := os.Stat(settingsFile); err == nil {
		settingsBytes, err := os.ReadFile(settingsFile)
		if err != nil {
			log.Fatal(err)
		}
		settingsStr := string(settingsBytes)

		// remove json comments
		settingsStrNoComments := removeJsonComments(settingsStr)

		json.Unmarshal([]byte(settingsStrNoComments), &settingsMap)

	} else {
		log.Fatalf(color.Red.Sprint(settingsFile + " does not exist!"))
	}

	return settingsMap
}
```

#### Float with decimal
Float with decimal = 0 (e..g 2.0 ) to json is rapresented as an int (e.g. 2). Here a way to get the decimal part when writing to json (e.g. 2.0 )

* [stackoverflow.com](https://stackoverflow.com/questions/52446730/stop-json-marshal-from-stripping-trailing-zero-from-floating-point-number/52446854#52446854)

```go
package main

import (
	"encoding/json"
	"fmt"
)

type Pt struct {
	Value json.Number
	Unit  string
}

func main() {
	data, err := json.Marshal(Pt{json.Number("40.0"), "some_string"})
	fmt.Println(string(data), err)
}
```

### Write a file
* [https://golangbot.com/write-files/](https://golangbot.com/write-files/)
* [https://gobyexample.com/writing-files](https://gobyexample.com/writing-files)


```go
package main

import (
    "bufio"
    "fmt"
    "io/ioutil"
    "os"
)

func check(e error) {
    if e != nil {
        panic(e)
    }
}

func main() {
    
    /* ioutil */
    d1 := []byte("hello\ngo\n")
    err := ioutil.WriteFile("/tmp/dat1", d1, 0644)
    check(err)

    f, err := os.Create("/tmp/dat2")
    check(err)

    defer f.Close()

    /* Write */
    d2 := []byte{115, 111, 109, 101, 10}
    n2, err := f.Write(d2)
    check(err)
    fmt.Printf("wrote %d bytes\n", n2)

    /* WriteString */
    n3, err := f.WriteString("writes\n")
    check(err)
    fmt.Printf("wrote %d bytes\n", n3)
    f.Sync()
    
    /* bufio */
    w := bufio.NewWriter(f)
    n4, err := w.WriteString("buffered\n")
    check(err)
    fmt.Printf("wrote %d bytes\n", n4)
    w.Flush()

}
```

-----------------------------------------------------------------------------------

## Database

### Sqlite3

* [Tutorial](https://zetcode.com/golang/sqlite3/)

#### Init

```go
package main

import (
	"database/sql"
	_ "github.com/mattn/go-sqlite3"
)

/* Global variables */
var db *sql.DB

func main() {
	/* Load settings */
	settingsMap = readSettings()

	// Connect to database
	var dberr error
	db, dberr = sql.Open("sqlite3", "./db.sqlite3"). // type (fixed for sqlite), "connection = database filepath for Sqlite)
    if err != nil {
		log.Fatal(err)
	}
	// defer close
	defer db.Close()
}
```

#### Update/Insert

```go
package main

import (
	"database/sql"
	_ "github.com/mattn/go-sqlite3"
)

/* Global variables */
var db *sql.DB

func main() {
	/* Load settings */
	settingsMap = readSettings()

	// Connect to database
	var dberr error
	db, dberr = sql.Open("sqlite3", "./db.sqlite3"). // type (fixed for sqlite), "connection = database filepath for Sqlite)
    if err != nil {
		log.Fatal(err)
	}
	// defer close
	defer db.Close()

    sqlInsertString := `INSERT INTO User( 
Id, username, password, first_name, last_name, email, birthday, picture, phone, date_joined, last_login, role, is_admin, active
)
VALUES
(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
`
    sqlCommand, err := db.Prepare(sqlInsertString)
    checkErr(err)
    sqlResult, sqlErr := sqlCommand.Exec(username, password, firstName, lastName, email, birthday, profileData, phone, "", "", "", true, true)
    checkErr(sqlErr)
    recordId, err := sqlResult.LastInsertId()
    if err != nil {
        recordId = 0
    }
}
```

#### Select one row

```go
package main

import (
	"database/sql"
	_ "github.com/mattn/go-sqlite3"
)

/* Global variables */
var db *sql.DB

func main() {
	/* Load settings */
	settingsMap = readSettings()

	// Connect to database
	var dberr error
	db, dberr = sql.Open("sqlite3", "./db.sqlite3"). // type (fixed for sqlite), "connection = database filepath for Sqlite)
    if err != nil {
		log.Fatal(err)
	}
	// defer close
	defer db.Close()

    query := "SELECT id, username, password FROM User WHERE username=?;"
	row := db.QueryRow(query, user)

	var dbid int
	var dbusername, dbpassword string
	err := row.Scan(&dbid, &dbusername, &dbpassword)
}
```

#### Select multiple rows


```go

var (
	id int
	name string
)

rows, err := db.Query("select id, name from users where id = ?", 1)

if err != nil {
	log.Panic(err)
}
defer rows.Close()

for rows.Next() {
	err := rows.Scan(&id, &name)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(id, name)
}
err = rows.Err()

if err != nil {
	log.Fatal(err)
}
```

```go
rows := sqlQuery("SELECT id, username, password FROM User;")
_ = rows
var id int
var username, password string
for rows.Next() {
    // Get values from row.
    err := rows.Scan(&id, &username, &password)
    if err != nil {
        fmt.Print(err)
    }
}

defer rows.Close()
```

### Postgres
* [Postgres doesn't return id](https://www.calhoun.io/inserting-records-into-a-postgresql-database-with-gos-database-sql-package/)

-----------------------------------------------------------------------------------

## Path handling

```go
import "path/filepath"
```

### Join
Concatenates paths

```go
p := filepath.Join("dir1", "dir2", "filename")
fmt.Println("p:", p)
```

### Dir

```go
fmt.Println("Dir(p):", filepath.Dir(p))
```

### Base

```go
fmt.Println("Base(p):", filepath.Base(p))
```

### IsAbs

```go
fmt.Println(filepath.IsAbs("dir/file"))
fmt.Println(filepath.IsAbs("/dir/file"))
```

```
false
true
```

### Ext
Splits the extension out from the filename

```go
filename := "config.json"

ext := filepath.Ext(filename)
fmt.Println(ext)
```

```
.json
```

To get the filename only:

```go
/* Solution 1 */
filename[0:len(filename)-len(ext)]

/* Solution 2 */
fmt.Println(strings.TrimSuffix(filename, ext))  // requires "strings" package 
```

* Example
    ```go
    ext := filepath.Ext(*outputFile)
    *outputFile = strings.TrimSuffix(*outputFile, ext) + ".png"
    ```

### Rel
finds a relative path between a base and a target. It returns an error if the target cannot be made relative to base.

```go
rel, err := filepath.Rel("a/b", "a/b/t/file")
if err != nil {
    panic(err)
}
fmt.Println(rel)

	
rel, err = filepath.Rel("a/b", "a/c/t/file")
if err != nil {
    panic(err)
}
fmt.Println(rel)
```

```
t/file
../c/t/file
```

### Split
```go
import "path"
```

* https://golang.org/pkg/path/

```
dir, file := path.Split("test/static/myfile.css")
```

```
dir: "test/static/", file: "myfile.css"
```

### Clean
1. Replace multiple slashes with a single slash.
1. Eliminate each . path name element (the current directory).
1. Eliminate each inner .. path name element (the parent directory) along with the non-.. element that precedes it.
1. Eliminate .. elements that begin a rooted path: that is, replace "/.." by "/" at the beginning of a path.

```go
import "path"

//...

path.Clean("a/c")                 // "a/c"
path.Clean("a//c")                // "a/c"
path.Clean("a/c/.")               // "a/c"
path.Clean("a/c/b/..")            // "a/c"
path.Clean("/../a/c")             // "/a/c"
path.Clean("/../a/b/../././/c")   // "/a/c"
path.Clean("")                    // "."
```

### Real Path
Go doesn't have a native implementation of it.

It can be achieved with Clean and `filepath.EvalSymlinks`

* [realpath](https://github.com/yookoala/realpath) has been written for coping this case.

### Detect the user's home directory without the use of cgo
```go
package main

import (
    "fmt"
    "os"
    "os/user"
)

func main() {

    user, err := user.Current()
    if err != nil {
        panic(err)
    }

    // Current User
    fmt.Println("Hi " + user.Name + " (id: " + user.Uid + ")")
    fmt.Println("Username: " + user.Username)
    fmt.Println("Home Dir: " + user.HomeDir)

    // Get "Real" User under sudo.
    // More Info: https://stackoverflow.com/q/29733575/402585
    fmt.Println("Real User: " + os.Getenv("SUDO_USER"))
}
```

> Why not just use os/user? The built-in os/user package requires cgo on Darwin systems. This means that any Go code that uses that package cannot cross compile. But 99% of the time the use for os/user is just to retrieve the home directory, which we can do for the current user without cgo. This library does that, enabling cross-compilation.

#### Detect the user's home directory without the use of cgo
* https://github.com/mitchellh/go-homedir

> Allows cross-compilation

```go
import homedir "github.com/mitchellh/go-homedir"
```

* `homedir.Dir()` to get the home directory for a user 
* `homedir.Expand()` to expand the ~ in a path to the home directory.


-----------------------------------------------------------------------------------

## Time

* [](https://yourbasic.org/golang/format-parse-string-time-date-example/)


### Overview

- **time.Time** object

    ```go
    t := time.Now() //It will return time.Time object with current timestamp
    ```

- **Unix Time (Also known as Epoch Time)** – It is the number of seconds elapsed since 00:00:00 UTC on 1 January 1970. This time is also known as the Unix epoch. 

    ```go
    t := time.Now().Unix() 
    //Will return number of seconds passed since Unix epoch
    ```

- **Unix Nano** –  It is number of nanoseconds elapsed since 00:00:00 UTC on 1 January 1970

    ```go
    t := time.Now().UnixNano() 
    //Will return number of nano seconds passed since Unix epoch
    ```

- **Unix MilliSecond** – It is the number of milliseconds elapsed since 00:00:00 UTC on 1 January 1970

    ```go
    t:= int64(time.Nanosecond) * t.UnixNano() / int64(time.Millisecond)/ time.Millisecond  
    //Number of millisecond elapsed since Unix epoch
    ```

- **Unix MicroSecond** – It is the number of microseconds elapsed since 00:00:00 UTC on 1 January 1970

    ```go
    t:= int64(time.Nanosecond) * t.UnixNano() / int64(time.Millisecond)/ time.Millisecond  
    //Number of millisecond elapsed since Unix epoch
    ```


### Get current timestamp

```go
now := time.Now()      // current local time
sec := now.Unix()      // number of seconds since January 1, 1970 UTC
nsec := now.UnixNano() // number of nanoseconds since January 1, 1970 UTC

fmt.Println(now)  // time.Time
fmt.Println(sec)  // int64
fmt.Println(nsec) // int64
```
```
2009-11-10 23:00:00 +0000 UTC m=+0.000000000
1257894000
1257894000000000000
```

### Format

```go
fmt.Println(t.Format("20060102150405"))

const (
    stdLongMonth      = "January"
    stdMonth          = "Jan"
    stdNumMonth       = "1"
    stdZeroMonth      = "01"
    stdLongWeekDay    = "Monday"
    stdWeekDay        = "Mon"
    stdDay            = "2"
    stdUnderDay       = "_2"
    stdZeroDay        = "02"
    stdHour           = "15"
    stdHour12         = "3"
    stdZeroHour12     = "03"
    stdMinute         = "4"
    stdZeroMinute     = "04"
    stdSecond         = "5"
    stdZeroSecond     = "05"
    stdLongYear       = "2006"
    stdYear           = "06"
    stdPM             = "PM"
    stdpm             = "pm"
    stdTZ             = "MST"
    stdISO8601TZ      = "Z0700"  // prints Z for UTC
    stdISO8601ColonTZ = "Z07:00" // prints Z for UTC
    stdNumTZ          = "-0700"  // always numeric
    stdNumShortTZ     = "-07"    // always numeric
    stdNumColonTZ     = "-07:00" // always numeric
)
```

```go


package main
 
import (
    "fmt"
    "time"
)
func main() {
 
    currentTime := time.Now()
 
    fmt.Println("Current Time in String: ", currentTime.String())
     
    fmt.Println("MM-DD-YYYY : ", currentTime.Format("01-02-2006"))
     
    fmt.Println("YYYY-MM-DD : ", currentTime.Format("2006-01-02"))
     
    fmt.Println("YYYY.MM.DD : ", currentTime.Format("2006.01.02 15:04:05"))
     
    fmt.Println("YYYY#MM#DD {Special Character} : ", currentTime.Format("2006#01#02"))
     
    fmt.Println("YYYY-MM-DD hh:mm:ss : ", currentTime.Format("2006-01-02 15:04:05"))
         
    fmt.Println("Time with MicroSeconds: ", currentTime.Format("2006-01-02 15:04:05.000000"))
     
    fmt.Println("Time with NanoSeconds: ", currentTime.Format("2006-01-02 15:04:05.000000000"))
     
    fmt.Println("ShortNum Month : ", currentTime.Format("2006-1-02"))
     
    fmt.Println("LongMonth : ", currentTime.Format("2006-January-02"))
     
    fmt.Println("ShortMonth : ", currentTime.Format("2006-Jan-02"))
     
    fmt.Println("ShortYear : ", currentTime.Format("06-Jan-02"))
     
    fmt.Println("LongWeekDay : ", currentTime.Format("2006-01-02 15:04:05 Monday"))
     
    fmt.Println("ShortWeek Day : ", currentTime.Format("2006-01-02 Mon"))   
     
    fmt.Println("ShortDay : ", currentTime.Format("Mon 2006-01-2"))
     
    fmt.Println("Short Hour Minute Second: ", currentTime.Format("2006-01-02 3:4:5"))   
     
    fmt.Println("Short Hour Minute Second: ", currentTime.Format("2006-01-02 3:4:5 PM"))    
     
    fmt.Println("Short Hour Minute Second: ", currentTime.Format("2006-01-02 3:4:5 pm"))    
}
```

```
Current Time in String:  2017-07-04 00:47:20.1424751 +0530 IST
MM-DD-YYYY :  07-04-2017
YYYY-MM-DD :  2017-07-04
YYYY.MM.DD :  2017.07.04 00:47:20
YYYY#MM#DD {Special Character} :  2017#07#04
YYYY-MM-DD hh:mm:ss :  2017-07-04 00:47:20
Time with MicroSeconds:  2017-07-04 00:47:20.142475
Time with NanoSeconds:  2017-07-04 00:47:20.142475100
ShortNum Month :  2017-7-04
LongMonth :  2017-July-04
ShortMonth :  2017-Jul-04
ShortYear :  17-Jul-04
LongWeekDay :  2017-07-04 00:47:20 Tuesday
ShortWeek Day :  2017-07-04 Tue
ShortDay :  Tue 2017-07-4
Short Hour Minute Second:  2017-07-04 12:47:20
Short Hour Minute Second:  2017-07-04 12:47:20 AM
Short Hour Minute Second:  2017-07-04 12:47:20 am
```

### Time fun fact
The layout string is a representation of the time stamp, `Jan 2 15:04:05 2006 MST`. An easy way to remember this value is that it holds, when presented in this order, the values (lined up with the elements above): `1 2 3 4 5 6 -7`

This date is easier to remember when written as `01/02 03:04:05PM ‘06 -0700`.



Since MST is GMT-0700, the reference time can be thought of as

`01/02 03:04:05PM '06 -0700`

It's a simple increasing sequence: 01 02 03 04 05 (PM) 06 07.

Using 03:04 PM rather than 03:04 AM makes it possible to show the two time representations 15:04 and 03:04PM more clearly.

### Sleep

time.Sleep() stops the thread execution for the number specified (the number is formed of an integer and the measure unit).

```go
package main

import (
    "fmt"
    "time"
)

func main() {
    fmt.Println("A")
    time.Sleep(5 * time.Second)
    fmt.Println("B")
}

### Compare time/dates

* [geeksforgeeks](https://www.geeksforgeeks.org/how-to-compare-times-in-golang/)

```go
package main
  
import "fmt"
  
// importing time module
import "time"
  
// Main function
func main() {
  
    today := time.Now()
    tomorrow := today.Add(24 * time.Hour)
  
    // Using time.Before() method
    g1 := today.Before(tomorrow)
    fmt.Println("today before tomorrow:", g1)
  
    // Using time.After() method
    g2 := tomorrow.After(today)
    fmt.Println("tomorrow after today:", g2)
  
}
```

```
today before tomorrow: true
tomorrow after today: true
```

### Format dates/times as in python

```go
package main

import (
	"fmt"
	"log"

	"github.com/itchyny/timefmt-go"
)

func main() {
	t, err := timefmt.Parse("2020/07/24 09:07:29", "%Y/%m/%d %H:%M:%S")
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(t) // 2020-07-24 09:07:29 +0000 UTC

	str := timefmt.Format(t, "%Y/%m/%d %H:%M:%S")
	fmt.Println(str) // 2020/07/24 09:07:29

	str = timefmt.Format(t, "%a, %d %b %Y %T %z")
	fmt.Println(str) // Fri, 24 Jul 2020 09:07:29 +0000
}
```

### Parse dates/times

```go
package main

import (
	"flag"
	"fmt"
	"time"

	"github.com/araddon/dateparse"
)

func main() {
    // Normal parse.  Equivalent Timezone rules as time.Parse()
    t, err := dateparse.ParseAny("3/1/2014")

    // Parse Strict, error on ambigous mm/dd vs dd/mm dates
    t, err := dateparse.ParseStrict("3/1/2014")
    // > returns error 

    // Return a string that represents the layout to parse the given date-time.
    layout, err := dateparse.ParseFormat("May 8, 2009 5:57:51 PM")
    // > "Jan 2, 2006 3:04:05 PM"
}
```

### Add days/time to time

```go
currentTime.Add(time.Hour * 24 * time.Duration(numberOfDays))
```

```go
func checkLicense() {
	currentTime := time.Now()
	numberOfDays, daysErr := strconv.Atoi(days)

	if daysErr != nil {
		log.Fatal("SA license check failed")
	}

	expireDate := currentTime.Add(time.Hour * 24 * time.Duration(numberOfDays))

	if expireDate.Before(currentTime) {
		log.Fatal(fmt.Sprintf("SA license expired (%s)", timefmt.Format(expireDate, "%Y/%m/%d")))
	}
}
```

### Get difference between two dates
```go
func main() {
    // The leap year 2016 had 366 days.
    t1 := Date(2016, 1, 1)
    t2 := Date(2017, 1, 1)
    days := t2.Sub(t1).Hours() / 24
    fmt.Println(days) // 366
}
```

### Compare dates

```go
package main
  
import "fmt"
  
// importing time module
import "time"
  
// Main function
func main() {
  
    today := time.Now()
    tomorrow := today.Add(24 * time.Hour)
  
    // Using time.Before() method
    g1 := today.Before(tomorrow)
    fmt.Println("today before tomorrow:", g1)
  
    // Using time.After() method
    g2 := tomorrow.After(today)
    fmt.Println("tomorrow after today:", g2)
  
}
```

Output :
```
today before tomorrow: true
tomorrow after today: true
```

### Get execution time

```go
package main

// importing time module
import (
	"fmt"
	"time"
)

// Main function
func main() {

	// init start variable for measuring the execution time
	start := time.Now()

    // ... Do things
	//time.Sleep(2 * time.Second)

	// get execution time
	executionTime := time.Since(start)

	fmt.Println(executionTime)
}
```

Output:
```
2s
```

`executionTime` can be converted to string using 

```go
executionTime.String()
```

### Convert float time to time.Time

```go
func floatToTime(timeFloat float64) time.Time {
	ts := fmt.Sprintf("%f", timeFloat)
	v := strings.Split(ts, ".")
	if len(v[1]) > 0 {
		for len(v[1]) < 9 {
			v[1] += "0"
		}
	}
	a, _ := strconv.ParseInt(v[0], 10, 64)
	b, _ := strconv.ParseInt(v[1], 10, 64)
	t := time.Unix(a, b).UnixNano()
	timeTime := time.Unix(0, t).UTC()

	return timeTime
}
```

-----------------------------------------------------------------------------------

## Execute command

```go
import "os/exec"
```

### Convert a string of arguments into a slice
Required as `exec.Command` requires a slice.

```go
package main

import (
  "github.com/buildkite/shellwords"
  "fmt"
)

func main() {
  words := shellwords.Split(`/usr/bin/bash -e -c "llamas are the \"best\" && echo 'alpacas'"`)
  for _, word := range words {
    fmt.Println(word)
  }
}

// Outputs:
// /usr/bin/bash
// -e
// -c
// llamas are the "best" && echo 'alpacas'
```

### Run
Starts the specified command and waits for it to complete.

```go
package main

import (
    "log"
    "os/exec"
)

func main() {

    cmd := exec.Command("firefox")

    err := cmd.Run()

    if err != nil {
        log.Fatal(err)
    }
}
```

### exec.Command
The `exec.Command` helper creates an object to represent this external process.
`.Output` is another helper that handles the common case of running a command, waiting for it to finish, and collecting its output. If there were no errors, dateOut will hold bytes with the date info.

```go
dateCmd := exec.Command("hostname")

dateOut, err := dateCmd.Output()
if err != nil {
        panic(err)
}
fmt.Println("> hostname")
fmt.Println(string(dateOut))
```

The Command returns the Cmd struct to execute the specified program with the given arguments. The first parameter is the program to be run; the other arguments are parameters to the program.

```go
cmd := exec.Command("tr", "a-z", "A-Z")

cmd.Stdin = strings.NewReader("and old falcon")

var out bytes.Buffer
cmd.Stdout = &out

err := cmd.Run()

if err != nil {
    log.Fatal(err)
}

fmt.Printf("translated phrase: %q\n", out.String())
```

### Multiple arguments

```go
prg := "echo"

arg1 := "there"
arg2 := "are three"
arg3 := "falcons"

cmd := exec.Command(prg, arg1, arg2, arg3)
stdout, err := cmd.Output()

if err != nil {
    fmt.Println(err.Error())
    return
}

fmt.Print(string(stdout))
```

### Stdin and Stdout

```go
grepCmd := exec.Command("grep", "hello")

grepIn, _ := grepCmd.StdinPipe()
grepOut, _ := grepCmd.StdoutPipe()
grepCmd.Start()
grepIn.Write([]byte("hello grep\ngoodbye grep"))
grepIn.Close()
grepBytes, _ := ioutil.ReadAll(grepOut)
grepCmd.Wait()

fmt.Println("> grep hello")
fmt.Println(string(grepBytes))
```

### Capture output

```go
out, err := exec.Command("ls", "-l").Output()

if err != nil {
    log.Fatal(err)
}

fmt.Println(string(out))
```

### Get realtime output
* [https://gist.github.com/hivefans/ffeaf3964924c943dd7ed83b406bbdea](https://gist.github.com/hivefans/ffeaf3964924c943dd7ed83b406bbdea)

    ```go
    package main

    import (
        "bufio"
        "fmt"
        "io"
        "os"
        "os/exec"
        "strings"
    )

    func main() {
        cmdName := "ping 127.0.0.1"
        cmdArgs := strings.Fields(cmdName)

        cmd := exec.Command(cmdArgs[0], cmdArgs[1:len(cmdArgs)]...)
        stdout, _ := cmd.StdoutPipe()
        cmd.Start()
        oneByte := make([]byte, 100)
        num := 1
        for {
            _, err := stdout.Read(oneByte)
            if err != nil {
                fmt.Printf(err.Error())
                break
            }
            r := bufio.NewReader(stdout)
            line, _, _ := r.ReadLine()
            fmt.Println(string(line))
            num = num + 1
            if num > 3 {
                os.Exit(0)
            }
        }

        cmd.Wait()
    }
    ```

-----------------------------------------------------------------

## Run external process

### Run the command

```go
cmd.Dir = ".."
```

```go
package main
import (
    "fmt"
    "log"
    "os/exec"
)
funcmain() {
    cmd := exec.Command("dir")
    cmd.Dir = ".."
    output, err := cmd.CombinedOutput()
    if err != nil {
        log.Fatal(err)
    }
    fmt.Printf("Output:\n%s\n", string(output))
}
```

#### Output() vs Run()

**Resources:**
* [sohamkamani.com](https://www.sohamkamani.com/golang/exec-shell-command/)
* [blog.kowalczyk.info](https://blog.kowalczyk.info/article/wOYk/advanced-command-execution-in-go-with-osexec.html)


* `Output()` method waits for the command to execute. Good for commands returning the output immediately (`ls`)
    
    ```go
    // create a new *Cmd instance
    // here we pass the command as the first argument and the arguments to pass to the command as the
    // remaining arguments in the function
    cmd := exec.Command("ls", "./")

    // The `Output` method executes the command and
    // collects the output, returning its value
    out, err := cmd.Output()
    if err != nil {
    // if there was any error, print it here
    fmt.Println("could not run command: ", err)
    }
    // otherwise, print the output from running the command
    fmt.Println("Output: ", string(out))
    ```


* `Run()` method allows to print the output continuosly. Useful with long commands or commands which run indefinitely. Interact with the command using `cmd.Stdin` and `cmd.Stdout`

    ```go
    cmd := exec.Command("ping", "google.com")

    // pipe the commands output to the applications
    // standard output
    cmd.Stdout = os.Stdout

    // Run still runs the command and waits for completion
    // but the output is instantly piped to Stdout
    if err := cmd.Run(); err != nil {
    fmt.Println("could not run command: ", err)
    }    
    ```

    ```
    > go run shellcommands/main.go

    PING google.com (142.250.195.142): 56 data bytes
    64 bytes from 142.250.195.142: icmp_seq=0 ttl=114 time=9.397 ms
    64 bytes from 142.250.195.142: icmp_seq=1 ttl=114 time=37.398 ms
    64 bytes from 142.250.195.142: icmp_seq=2 ttl=114 time=34.050 ms
    64 bytes from 142.250.195.142: icmp_seq=3 ttl=114 time=33.272 ms

    # ...
    # and so on
    ```

### Custom Output Writer

Instead of using `os.Stdout`, we can create our own writer that implements the `io.Writer` interface.

Let’s create a writer that adds a "received output:" prefix before each output chunk:

```go
type customOutput struct{}

func (c customOutput) Write(p []byte) (int, error) {
	fmt.Println("received output: ", string(p))
	return len(p), nil
}
```

Now we can assign a new instance of customWriter as the output writer:

```go
cmd.Stdout = customOutput{}
```

If we run the application now, we will get the below output:


```
received output:  PING google.com (142.250.195.142): 56 data bytes
64 bytes from 142.250.195.142: icmp_seq=0 ttl=114 time=187.825 ms

received output:  64 bytes from 142.250.195.142: icmp_seq=1 ttl=114 time=19.489 ms

received output:  64 bytes from 142.250.195.142: icmp_seq=2 ttl=114 time=117.676 ms

received output:  64 bytes from 142.250.195.142: icmp_seq=3 ttl=114 time=57.780 ms
```

### Passing Input To Commands With STDIN
In the previous examples, we executed commands without giving any input (or providing limited inputs as arguments). In most cases, input is given through the STDIN stream.

One popular example of this is the grep command, where we can pipe the input from another command:

```bash
➜  ~ echo "1. pear\n2. grapes\n3. apple\n4. banana\n" | grep apple
3. apple
```

Here, the input is passed to the grep command through STDIN. In this case the input is a list of fruit, and grep filters the line that contains "apple"

The *Cmd instance provides us with an input stream which we can write into. Let’s use it to pass input to a grep child process:

```go
cmd := exec.Command("grep", "apple")

// Create a new pipe, which gives us a reader/writer pair
reader, writer := io.Pipe()
// assign the reader to Stdin for the command
cmd.Stdin = reader
// the output is printed to the console
cmd.Stdout = os.Stdout

go func() {
  defer writer.Close()
  // the writer is connected to the reader via the pipe
  // so all data written here is passed on to the commands
  // standard input
  writer.Write([]byte("1. pear\n"))
  writer.Write([]byte("2. grapes\n"))
  writer.Write([]byte("3. apple\n"))
  writer.Write([]byte("4. banana\n"))
}()

if err := cmd.Run(); err != nil {
  fmt.Println("could not run command: ", err)
}
```

Output:

```
3. apple
```

### Killing a Child Process
There are several commands that run indefinitely, or need an explicit signal to stop.

For example, if we start a web server using `python3 -m http.server` or execute `sleep 10000` the resulting child processes will run for a very long time (or indefinitely).

To stop these processes, we need to send a kill signal from our application. We can do this by adding a context instance to the command.

If the context gets cancelled, the command terminates as well.

```go
ctx := context.Background()
// The context now times out after 1 second
// alternately, we can call `cancel()` to terminate immediately
ctx, cancel = context.WithTimeout(ctx, 1*time.Second)

cmd := exec.CommandContext(ctx, "sleep", "100")

out, err := cmd.Output()
if err != nil {
  fmt.Println("could not run command: ", err)
}
fmt.Println("Output: ", string(out))
```

This will give the following output after 1 second has elapsed:

```
could not run command:  signal: killed
Output:
```

Terminating child processes is useful when you want to limit the time spent in running a command or want to create a fallback incase a command doesn’t return a result on time.


### Capture output and error seperately

```go
    cmd := exec.Command("dir")
    cmd.Dir = ".."
    var stdout, stderr bytes.Buffer
    cmd.Stderr = &stderr
    cmd.Stdout = &stdout
    
    err := cmd.Run()
    if err != nil {
        log.Fatal(err)
    }
    
    output, err := string(stdout.Bytes()), string(stderr.Bytes())
```

### Get return code
Since golang version 1.12, the exit code is available natively and in a cross-platform manner. See [ExitError](https://golang.org/pkg/os/exec/#ExitError) and [ExitCode()](https://golang.org/pkg/os/#ProcessState.ExitCode).

> ExitCode returns the exit code of the exited process, or -1 if the process hasn't exited or was terminated by a signal.

* Basic snippet

    ```go
    if err := cmd.Run() ; err != nil {
        if exitError, ok := err.(*exec.ExitError); ok {
            return exitError.ExitCode()
        }
    }
    ```

* Complete snippet

    ```go
    package main

    import "os/exec"
    import "log"
    import "syscall"

    func main() {
        cmd := exec.Command("git", "blub")

        if err := cmd.Start(); err != nil {
            log.Fatalf("cmd.Start: %v", err)
        }

        if err := cmd.Wait(); err != nil {
            if exiterr, ok := err.(*exec.ExitError); ok {
                log.Printf("Exit Status: %d", exiterr.ExitCode())
            } else {
                log.Fatalf("cmd.Wait: %v", err)
            }
        }
    }
    ```


* Advanced snippet

    ```go
    package utils

    import (
        "bytes"
        "log"
        "os/exec"
        "syscall"
    )

    const defaultFailedCode = 1

    func RunCommand(name string, args ...string) (stdout string, stderr string, exitCode int) {
        log.Println("run command:", name, args)
        var outbuf, errbuf bytes.Buffer
        cmd := exec.Command(name, args...)
        cmd.Stdout = &outbuf
        cmd.Stderr = &errbuf

        err := cmd.Run()
        stdout = outbuf.String()
        stderr = errbuf.String()

        if err != nil {
            // try to get the exit code
            if exitError, ok := err.(*exec.ExitError); ok {
                ws := exitError.Sys().(syscall.WaitStatus)
                exitCode = ws.ExitStatus()
            } else {
                // This will happen (in OSX) if `name` is not available in $PATH,
                // in this situation, exit code could not be get, and stderr will be
                // empty string very likely, so we use the default fail code, and format err
                // to string and set to stderr
                log.Printf("Could not get exit code for failed program: %v, %v", name, args)
                exitCode = defaultFailedCode
                if stderr == "" {
                    stderr = err.Error()
                }
            }
        } else {
            // success, exitCode should be 0 if go is ok
            ws := cmd.ProcessState.Sys().(syscall.WaitStatus)
            exitCode = ws.ExitStatus()
        }
        log.Printf("command result, stdout: %v, stderr: %v, exitCode: %v", stdout, stderr, exitCode)
        return
    }
    ```

* Alternative version

    ```go
    err := cmd.Run()

    var (
        ee *exec.ExitError
        pe *os.PathError
    )

    if errors.As(err, &ee) {
        log.Println("exit code error:", ee.ExitCode()) // ran, but non-zero exit code

    } else if errors.As(err, &pe) {
        log.Printf("os.PathError: %v", pe) // "no such file ...", "permission denied" etc.

    } else if err != nil {
        log.Printf("general error: %v", err) // something really bad happened!

    } else {
        log.Println("success!") // ran without error (exit code zero)
    }
    ```

### Set current working directory (cwd)

```go
cmd := exec.Command("dir")
cmd.Dir = ".."
```

```go
package main
import (
    "fmt"
    "log"
    "os/exec"
)
funcmain() {
    cmd := exec.Command("dir")
    cmd.Dir = ".."
    output, err := cmd.CombinedOutput()
    if err != nil {
        log.Fatal(err)
    }
    fmt.Printf("Output:\n%s\n", string(output))
}
```

### Set environment variables

```go
env := make(map[string]string)  // env can be nil if used as function argument

env["variable"] = "value"

// set the environment variables
cmd.Env = os.Environ()
if env != nil {
    for k, v := range env {
        cmd.Env = append(cmd.Env, k+"="+v)
    }
}
```

or


```go
cmd := exec.Command("programToExecute")

additionalEnv := "FOO=bar"
newEnv := append(os.Environ(), additionalEnv))
cmd.Env = newEnv

out, err := cmd.Output()
if err != nil {
    log.Fatalf("cmd.Run() failed with %s\n", err)
}
fmt.Printf("%s", out)
```

### Hide window
Useful when some confirmation messageboxes are prompted in case of issue, and the user interaction is then required.

```go
cmd.SysProcAttr = &syscall.SysProcAttr{HideWindow: true}
```

avoid the code execution to hang.

```go
cmd := exec.Command("tasklist", "/fo", "csv", "/nh")
cmd.SysProcAttr = &syscall.SysProcAttr{HideWindow: true}
out, err := cmd.Output()
if err != nil {
    fmt.Println(err)
}
fmt.Printf(string(out))
```

### Custom commands for a different OS

In same cases, you need to detect the operative system where the program is running:

```go
import "runtime"
```

```go
if runtime.GOOS == "windows" {
    cmd = exec.Command("dir")
} else {
    cmd = exec.Command("ls")
}
```


### Check early that a program is installed

Imagine you wrote a program that takes a long time to run. At the end, you call executable foo to perform an essential task.
If foo executable is not present, the call will fail.
It’s a good idea to detect lack of executable foo at the beginning and fail early with descriptive error message.
You can do it using `exec.LookPath`.

```go
func checkLsExists() {
    path, err := exec.LookPath("ls")
    if err != nil {
        fmt.Printf("didn't find 'ls' executable\n")
    } else {
        fmt.Printf("'ls' executable is in '%s'\n", path)
    }
}
```

-----------------------------------------------------------------

### My function

```go
func runProcess(command string, env map[string]string) (string, string) {
	// prepare arguments for running the command.
	opSys := runtime.GOOS
	var args []string
	if opSys == "windows" {
		args = []string{"cmd", "/c"}
	} else {
		args = []string{"bash", "-c"}
	}
	args = append(args, strings.Fields(command)...)
	args, _ = shellwords.Split(command)

	cmd := exec.Command(args[0], args[1:]...)

	// Add attributes: hide window, passed via the map
	cmd.SysProcAttr = &syscall.SysProcAttr{HideWindow: true}

	// set the environment variables
	cmd.Env = os.Environ()
	if env != nil {
		for k, v := range env {
			cmd.Env = append(cmd.Env, k+"="+v)
		}
	}

	// execute and get the output
	out, err := cmd.Output()

	return fmt.Sprintf("%s", out), err
}
```


-----------------------------------------------------------------------------------

## Application's arguments

- [https://yourbasic.org/golang/command-line-arguments/](https://yourbasic.org/golang/command-line-arguments/)

- `os.Args` holds the arguments passed to the application call

### Flags

- [https://gobyexample.com/command-line-flags](https://gobyexample.com/command-line-flags)

```go
package main

import (
    "flag"
    "fmt"
)

func main() {

    wordPtr := flag.String("word", "foo", "a string")

    numbPtr := flag.Int("numb", 42, "an int")
    boolPtr := flag.Bool("fork", false, "a bool")

    var svar string
    flag.StringVar(&svar, "svar", "bar", "a string var")

    flag.Parse()

    fmt.Println("word:", *wordPtr)
    fmt.Println("numb:", *numbPtr)
    fmt.Println("fork:", *boolPtr)
    fmt.Println("svar:", svar)
    fmt.Println("tail:", flag.Args())
}
```

```go
$ go build command-line-flags.go

$ ./command-line-flags -word=opt -numb=7 -fork -svar=flag
word: opt
numb: 7
fork: true
svar: flag
tail: []

$ ./command-line-flags -word=opt
word: opt
numb: 42
fork: false
svar: bar
tail: []

$ ./command-line-flags -word=opt a1 a2 a3
word: opt
...
tail: [a1 a2 a3]

$ ./command-line-flags -word=opt a1 a2 a3 -numb=7
word: opt
numb: 42
fork: false
svar: bar
tail: [a1 a2 a3 -numb=7]

$ ./command-line-flags -h
Usage of ./command-line-flags:
  -fork=false: a bool
  -numb=42: an int
  -svar="bar": a string var
  -word="foo": a string

$ ./command-line-flags -wat
flag provided but not defined: -wat
Usage of ./command-line-flags:
...
```

### Argparse

- [https://github.com/akamensky/argparse](https://github.com/akamensky/argparse)

```go
package main

import (
	"fmt"
	"github.com/akamensky/argparse"
	"os"
)

func main() {
	// Create new parser object
	parser := argparse.NewParser("print", "Prints provided string to stdout")
	// Create string flag
	s := parser.String("s", "string", &argparse.Options{Required: true, Help: "String to print"})
	// Parse input
	err := parser.Parse(os.Args)
	if err != nil {
		// In case of error print error and print usage
		// This can also be done by passing -h or --help flags
		fmt.Print(parser.Usage(err))
	}
	// Finally print the collected string
	fmt.Println(*s)
}
```

- [github.com/hellflame/argparse](https://github.com/hellflame/argparse)
Fork of `https://github.com/hellflame/argparse`

```go
package main

import (
    "github.com/hellflame/argparse"
)

func main() {
    parser := argparse.NewParser("rcf2csv  " + Version, `Converts an input rcf to csv. 
    If 2 rcf files are given, it converts them to csv and compare the first (user rcf) with second one (reference rcf) and the output csv for user rcf will display the changes in an extra column.`, nil)

	/* ---- List of arguments -------------------------------------------------- */
	// customRcfFilePath for user-rcf
	customRcfFilePath := parser.String("", "user-rcf", &argparse.Option{
		Positional: true,
		Validate: func(arg string) error {
			if _, e := os.Stat(arg); e != nil {
				return fmt.Errorf("Cannot read file: '%s'", arg)
			}
			return nil
		},
	})

	// refRcfFilePath for reference-rcf
	refRcfFilePath := parser.String("", "reference-rcf", &argparse.Option{
		Positional: true,
		Validate: func(arg string) error {
			if _, e := os.Stat(arg); e != nil {
				return fmt.Errorf("Cannot read file: '%s'", arg)
			}
			return nil
		},
	})

	/* ---- Parse -------------------------------------------------------------- */
	if e := parser.Parse(nil); e != nil {
		fmt.Println(e.Error())
		return
	}
}
```

-----------------------------------------------------------------------------------

## Functions
* Functions having a name starting with lower case, will only be available within the package. If you need to import the package in others and use that function, it needs to start with uppercase.

```
func function_name(variable1_name, variable2_name variable1-2_type, variable3_name variable3_type) <function_return_type> {

    <function_body>

}
```

```go
package mymath


func Add(a, b int) int {
    return a + b
}

func subtract(a, b int) int {
    return a - b
}
```

* `subtract` is going to be available only in the current package, whereas `Add` in both `mymath` and in any packages which imports `mymath`



* If return values are declared in the function definition, `return` statement is enough for returning the function values

  ```go
  func rectangle(l int, b int) (area int) {
  	var parameter int
  	parameter = 2 * (l + b)
  	fmt.Println("Parameter: ", parameter)
  
  	area = l * b
  	return // Return statement without specify variable name
  }
  
  func main() {
  	fmt.Println("Area: ", rectangle(20, 30))
  }
  ```

  ```go
  // Main Method
  func main() {
    
      // calling the function, here
      // function returns two values
      m, d := calculator(105, 7)
    
      fmt.Println("105 x 7 = ", m)
      fmt.Println("105 / 7 = ", d)
  }
    
  // function having named arguments
  func calculator(a, b int) (mul int, div int) {
    
      // here, simple assignment will
      // initialize the values to it
      mul = a * b
      div = a / b
    
      // here you have return keyword
      // without any resultant parameters
      return
  }
  ```

### Variadic functions
Variadic functions can be called with any number of trailing arguments. 

> For example, `fmt.Println` is a common variadic function.

* If you already have multiple args in a slice, apply them to a variadic function using func(slice...) like this.

```go
package main

import "fmt"

func sum(nums ...int) {
    fmt.Print(nums, " ")
    total := 0
    for _, num := range nums {
        total += num
    }
    fmt.Println(total)
}

func main() {

    sum(1, 2)
    sum(1, 2, 3)

    nums := []int{1, 2, 3, 4}
    sum(nums...)
}
```

-----------------------------------------------------------------------------------

## Go Routines

Run functions in a async way

* Synchronized call

```go
package main

import "fmt"
import "time"

func Foo(){
    fmt.Println("Hello World!")
    time.Sleep(2 * time.Second)
    fmt.Println("Done Waiting!")
}

func Bar{
    fmt.Println("Something Else!")
}

func main(){
    Foo()
    Bar()
}
```


* Async call

```go
package main

import "fmt"
import "time"

func Foo(){
    fmt.Println("Hello World!")
    time.Sleep(2 * time.Second)
    fmt.Println("Done Waiting!")
}

func Bar{
    fmt.Println("Something Else!")
}

func main(){
    go Foo()
    go Bar()
}
```

The output will be empty because main() starts running in async way `Foo` and `Bar` then ends terminating the application before statements in `Foo` and `Bar` are executed. 


* Async call

```go
package main

import "fmt"
import "time"

func Foo(){
    fmt.Println("Hello World!")
    time.Sleep(2 * time.Second)
    fmt.Println("Done Waiting!")
}

func Bar{
    fmt.Println("Something Else!")
}

func main(){
    go Foo()
    go Bar()
    
    time.Sleep(5 * time.Second)
}
```

Adding a wait (only for understanding purposes), will give the time to `Foo` and `Bar` functions to run their statements.


### Channels

* Allow to send and receive from/to functions
* Communication connection between routines


```go
package main

import "fmt"
import "time"

func sendInformation(channel chan<- string) { /*send into a channel*/
    channel <- info
}

func printInformation(channel <-chan string) {
    fmt.Println(<-channel)
}

func main(){
    
    information := make(chan string)
    
    printInformation(information)
    sendInformation(information, "Hello")
}
```

* This causes a deadlock as the `printInformation` will keep waiting for something in the channel, which is empty, so it will never proceed.


```go
package main

import "fmt"
import "time"

func sendInformation(channel chan<- string) { /*send into a channel*/
    channel <- info
}

func printInformation(channel <-chan string) {
    fmt.Println(<-channel)
}

func main(){
    
    information := make(chan string)
    
    go printInformation(information)
    go sendInformation(information, "Hello")
}
```

1. `printInformation` is run (as async) and will be waiting for items in the channel
1. `sendInformation` is run (as async) populates the channel, triggering `fmt.Println(<-channel)` statement.


#### Buffer

* Declare the size of the channel
    ```go
    information := make(chan string, 5)
    ```
    
* Population: 
    ```go
    information <- "Hello"
    ```

!!! warning "If you try to add more elements than the buffer size, go returns deadlock error" 

* Take elements out from the buffer

    ```go
    <-information
    ```


```go
package main

import "fmt"
import "time"

func main(){
    
    information := make(chan string, 5)    
    fmt.Println(<-information)
}
```

## Concurrency

* Achieved with Routines and channels
* Breaks the program into indipendent tasks and get one result at the end
* Different from parallelism, where processes run exactly at the same time (it happens when you have multicores)
* Channels blocking nature allows to syncronize go routines 

```go
package main

import (
    "fmt"
    "time"
)

func main() {
    count("sheep")
    count("fish")
}

func count(thing string) {
    for i := 1; true; i++ {
        fmt.Println(i, thing)
        time.Sleep(time.Millisecond * 500)
    }
}
```

### Channel vs Buffer

```go
package main

import "fmt"

func main() {
    c := make(chan string)
    c <- "hello"
    
    msg := <-c
    fmt.Println(msg)
}
```

* 

```go
package main

import "fmt"

func main() {
    c := make(chan string, 2)
    c <- "hello"
    
    msg := <-c
    fmt.Println(msg)
}
```

-----------------------------------------------------------------------------------

## Handle Ctrl+C (Signal Interrupt) Close in the Terminal

* [golangcode.com](https://golangcode.com/handle-ctrl-c-exit-in-terminal/)

### Solution 1

```go
// SetupCloseHandler creates a 'listener' on a new goroutine which will notify the
// program if it receives an interrupt from the OS. We then handle this by calling
// our clean up procedure and exiting the program.
func SetupCloseHandler() {
	c := make(chan os.Signal)
	signal.Notify(c, os.Interrupt, syscall.SIGTERM)
	go func() {
		<-c
		fmt.Println("\r- Ctrl+C pressed in Terminal")
		DeleteFiles()
		os.Exit(0)
	}()
}
```

```go
package main

import (
	"fmt"
	"os"
	"os/signal"
	"syscall"
	"time"
)

const FileNameExample = "go-example.txt"

func main() {

	// Setup our Ctrl+C handler
	SetupCloseHandler()

	// Run our program... We create a file to clean up then sleep
	CreateFile()
	for {
		fmt.Println("- Sleeping")
		time.Sleep(10 * time.Second)
	}
}

// SetupCloseHandler creates a 'listener' on a new goroutine which will notify the
// program if it receives an interrupt from the OS. We then handle this by calling
// our clean up procedure and exiting the program.
func SetupCloseHandler() {
	c := make(chan os.Signal)
	signal.Notify(c, os.Interrupt, syscall.SIGTERM)
	go func() {
		<-c
		fmt.Println("\r- Ctrl+C pressed in Terminal")
		DeleteFiles()
		os.Exit(0)
	}()
}

// DeleteFiles is used to simulate a 'clean up' function to run on shutdown. Because
// it's just an example it doesn't have any error handling.
func DeleteFiles() {
	fmt.Println("- Run Clean Up - Delete Our Example File")
	_ = os.Remove(FileNameExample)
	fmt.Println("- Good bye!")
}

// Create a file so we have something to clean up when we close our program.
func CreateFile() {
	fmt.Println("- Create Our Example File")
	file, _ := os.Create(FileNameExample)
	defer file.Close()
}
```

### Solution 2

```go
c := make(chan os.Signal, 1)
signal.Notify(c, os.Interrupt)
go func(){
    for sig := range c {
        // sig is a ^C, handle it
    }
}()
```

-----------------------------------------------------------------------------------

## Regex
* [regular-expressions](https://gobyexample.com/regular-expressions)

* Flags (Multiline, Ignore case, etc) are added in the regex itself by using the flags `(?m)` at beginning.

```go
package main

import (
"fmt"
"regexp"
)

func main() {
	s := "Data: 23/07/2021 - 29/07/2021"

	r, _ := regexp.Compile("(\\d{2}/\\d{2}/\\d{4})")
	groups := r.FindAllStringSubmatch(s, -1)

	for _, group := range groups {
		for _, m := range group {
			fmt.Println(m)
		}
	}
}
```

### Replace text using regex

```go
package main

import (
"fmt"
"regexp"
)

func main() {
    originalString := `
    
    `
    var re = regexp.MustCompile(Myregex)
    s := re.ReplaceAllString(originalString, "replaced")
    fmt.Println(s)
}

var Myregex = `//==start==\n.*\n//==end==`
```


## Evaluate 
Evaluates a string treating it as golang code. Useful for dynamic code.

* [https://github.com/Knetic/govaluate](https://github.com/Knetic/govaluate)
* [https://github.com/antonmedv/expr](https://github.com/antonmedv/expr)

```go
import "gopkg.in/Knetic/govaluate.v2"
```

```go
expression, err := govaluate.NewEvaluableExpression("10 > 0");
result, err := expression.Evaluate(nil);
// result is now set to "true", the bool value.
```

* With parameters:
```go
expression, err := govaluate.NewEvaluableExpression("foo > 0");

parameters := make(map[string]interface{}, 8)
parameters["foo"] = -1;

result, err := expression.Evaluate(parameters);
// result is now set to "false", the bool value.
```

-----------------------------------------------------------------------------------

## Make http requests

```go
package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
)

func main() {
    url := "http://restapi3.apiary.io/notes"
    fmt.Println("URL:>", url)

	requestData := map[string]string{
		"name":  "Toby",
		"email": "Toby@example.com",
	}
    postBody, _ := json.Marshal(requestData)
    _ = postBody
    
    var jsonStr = []byte(`{"title":"Buy cheese and bread for breakfast."}`)

    req, err := http.NewRequest("POST", url, bytes.NewBuffer(jsonStr))
    req.Header.Set("X-Custom-Header", "myvalue")
    req.Header.Set("Content-Type", "application/json")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        panic(err)
    }
    defer resp.Body.Close()

    fmt.Println("response Status:", resp.Status)
    fmt.Println("response Headers:", resp.Header)
    body, _ := ioutil.ReadAll(resp.Body)
    fmt.Println("response Body:", string(body))
}
```

-----------------------------------------------------------------------------------

## Embed files in the binary

* [https://pkg.go.dev/embed](https://pkg.go.dev/embed)
* [https://blog.jetbrains.com/go/2021/06/09/how-to-use-go-embed-in-go-1-16/](https://blog.jetbrains.com/go/2021/06/09/how-to-use-go-embed-in-go-1-16/)
* [box](https://levelup.gitconnected.com/how-i-embedded-resources-in-go-514b72f6ef0a)
* [https://stackoverflow.com/questions/13904441/whats-the-best-way-to-bundle-static-resources-in-a-go-program](https://stackoverflow.com/questions/13904441/whats-the-best-way-to-bundle-static-resources-in-a-go-program)
* [https://blog.carlmjohnson.net/post/2021/how-to-use-go-embed/](https://blog.carlmjohnson.net/post/2021/how-to-use-go-embed/)
* [Working example](https://developpaper.com/golang1-16-embedded-static-resource-guide/)


### Embed a text file and get the content in a variable

* String
```go
package main

import (
    _ "embed"
    "fmt"
)

//go:embed config.txt
var content string

func main() {
    fmt.Print(content)
}
// output: I am a file that you need me ;)
```

* Byte 
```go
package main

import (
    _ "embed"
    "fmt"
)

//go:embed config.txt
var content []byte

func main() {
    fmt.Print(content)
}
// output: [73 32 97 109 32 97 32 102 105 108 101 32 116 104 97 116 32 121 111 117 32 110 101 101 100 32 109 101 32 59 41]
```

### Embed a folder and access all files

```go
package main

import (
    _ "embed"
    "fmt"
)

//go:embed resources
var res embed.FS

func main() {
    resourcePath := "resources"
    embedFiles, err := res.ReadDir(resourcePath)
	
    if err != nil {
        log.Fatal(err)
	}
	
    for _, f := range embedFiles {
        fFullpath := filepath.Join(resourcePath, f.Name())

        embedFile := strings.ReplaceAll(fFullpath, "\\", "/")  // separator always needs to be / otherwise the folder isn't found
        embedIoReaderFile, err := res.Open(embedFile)
        checkError(err)

	}
}
```

> Note:
> For including empty folders and hidden files, use `all:` prefix: e.g.: `//go:embed all:embedFiles`


### Recreate embedded filesystems from embed.FS
* [soypat/rebed](https://github.com/soypat/rebed)

```go
package main

import "github.com/soypat/rebed"

//go:embed all:embedFiles
var embededFiles embed.FS

func main() {
    destPath := "/myDstPath"
    err := rebed.Write(embededFiles, destPath)
}
```

* Actions available:

    ```go
    //go:embed someFS/*
    var bdFS embed.FS

    // Just replicate folder Structure
    rebed.Tree(bdFS, "")

    // Make empty files
    rebed.Touch(bdFS, "")

    // Recreate entire FS
    rebed.Write(bdFS, "")

    // Recreate FS without modifying existing files
    rebed.Patch(bdFS, "")

    // Runs Patch if no conflicting file is found, else error.
    err := rebed.Create(bdFS, "")

    /* Walk allows you operate on each file as you wish */
    ```


-----------------------------------------------------------------------------------

## Send email

```go
package main

import (
   "fmt"
   "net/smtp"
)

func sendEmail(from string, password string, to []string, message string) error {
   // smtp server configuration.
   smtpHost := "smtp.gmail.com"
   smtpPort := "587"

   // Authentication.
   auth := smtp.PlainAuth("", from, password, smtpHost)

   // Sending email.
   err := smtp.SendMail(smtpHost+":"+smtpPort, auth, from, to, []byte(message))

   return err
}

func main() {

   err := sendEmail("from_email@gmail.com", "email_password", []string{"sender@example.com"}, "Test email")

   if err != nil {
      fmt.Println("Error happened: " + err.Error())
   }
}
```

-----------------------------------------------------------------------------------

## Misc

### Windows registry

**Import**

```go
import "golang.org/x/sys/windows/registry
```

**Methods**

* `registry.OpenKey(kroot, regPath, permissions)` : Open the registry key
* `k.ReadSubKeyNames(-1)` : lists the keys
* `key.GetStringValue("Path")` : gets the value


where:

* `kroot` is registry.CURRENT_USER, registry.LOCAL_MACHINE etc
* `regPath` is the registry path 
* `permissions` is the combination of permissions (`registry.QUERY_VALUE`, `registry.ENUMERATE_SUB_KEYS`, `registry.SET_VALUE`)

```go
//go:build windows

package main

import (
	"golang.org/x/sys/windows/registry"
	"log"
)

func getPRQAFsInstalledFromWinregistry() map[string]string {
	prqafRegRelpathBrands := [2]string{`SOFTWARE\PRQA\prqa-framework`, `SOFTWARE\Perforce\Helix-QAC`}
	keysRoots := [2]registry.Key{registry.CURRENT_USER, registry.LOCAL_MACHINE}

	var prqafVersionPathDict = make(map[string]string) // {'PRQAF_ver': 'Path'}  => {'2.3.0': 'C:\PRQA\PRQAFramework-2.3.0\'}

	for _, prqafRegRelpath := range prqafRegRelpathBrands {
		for _, kroot := range keysRoots {
			k, err := registry.OpenKey(kroot, prqafRegRelpath, registry.QUERY_VALUE|registry.ENUMERATE_SUB_KEYS)
			if err != nil {
				continue
			}

			subKeyNames, subKeyNamesErr := k.ReadSubKeyNames(-1)
			if subKeyNamesErr != nil {
				log.Fatal(subKeyNamesErr)
			}

			for _, subKey := range subKeyNames {
				subPath := prqafRegRelpath + "\\" + subKey
				subPathKey, subPathKeyErr := registry.OpenKey(kroot, subPath, registry.QUERY_VALUE|registry.ENUMERATE_SUB_KEYS)
				if subPathKeyErr != nil {
					continue
				}

				subKeyValue, _, subKeyErr := subPathKey.GetStringValue("Path")
				if subKeyErr != nil {
					continue
				}

				// populate the map with version : path
				prqafVersionPathDict[subKey] = subKeyValue
			}
		}
	}

	return prqafVersionPathDict
}
```

### Notify in os

* [Noti](https://github.com/variadico/noti)

-----------------------------------------------------------------------------------

## API

### Slack

- [https://github.com/slack-go/slack](https://github.com/slack-go/slack)
- [go-slackbot Article](https://blog.gopheracademy.com/advent-2017/go-slackbot/)
- [slack-bot-in-golang](https://www.opsdash.com/blog/slack-bot-in-golang.html)

#### slack-go-webhook

* [slack-go-webhook](https://github.com/ashwanthkumar/slack-go-webhook)

```go
package main

import "github.com/ashwanthkumar/slack-go-webhook"
import "fmt"

func main() {
    webhookUrl := "https://hooks.slack.com/services/foo/bar/baz"

    attachment1 := slack.Attachment {}
    attachment1.AddField(slack.Field { Title: "Author", Value: "Ashwanth Kumar" }).AddField(slack.Field { Title: "Status", Value: "Completed" })
    attachment1.AddAction(slack.Action { Type: "button", Text: "Book flights 🛫", Url: "https://flights.example.com/book/r123456", Style: "primary" })
    attachment1.AddAction(slack.Action { Type: "button", Text: "Cancel", Url: "https://flights.example.com/abandon/r123456", Style: "danger" })
    payload := slack.Payload {
      Text: "Hello from <https://github.com/ashwanthkumar/slack-go-webhook|slack-go-webhook>, a Go-Lang library to send slack webhook messages.\n<https://golangschool.com/wp-content/uploads/golang-teach.jpg|golang-img>",
      Username: "robot",
      Channel: "#general",
      IconEmoji: ":monkey_face:",
      Attachments: []slack.Attachment{attachment1},
    }
    err := slack.Send(webhookUrl, "", payload)
    if len(err) > 0 {
      fmt.Printf("error: %s\n", err)
    }
}
```

```go
/* Slack notifications */
func notifySlack(webhookReceiver string, msgText string, msgType string, attachments []slack.Field) {
	var color = new(string)
	switch msgType {
	case "success":
		*color = "#34eb71" // green
	case "error":
		*color = "#eb4034" // red
	case "warning":
		*color = "#f5ca20" // orange
	}

	attachment1 := slack.Attachment{Color: color}

	for _, f := range attachments {
		attachment1.AddField(f)
	}

	payload := slack.Payload{
		Text:        msgText,
		Attachments: []slack.Attachment{attachment1},
		Markdown:    true,
	}
	slackErr := slack.Send(webhookReceiver, "", payload)
	if len(slackErr) > 0 {
		fmt.Printf("error: %s\n", slackErr)
	}
}
```

### Salesforce

- [https://github.com/simpleforce/simpleforce](https://github.com/simpleforce/simpleforce)
- [https://developer.salesforce.com/blogs/2020/02/soql-tags-for-golang.html](https://developer.salesforce.com/blogs/2020/02/soql-tags-for-golang.html)
- [https://www.cdata.com/kb/tech/salesforce-odbc-go-linux.rst](https://www.cdata.com/kb/tech/salesforce-odbc-go-linux.rst)


#### simplesalesforce

* [simpleforce](github.com/simpleforce/simpleforce)

```go
package main

import (
	"fmt"

	"github.com/simpleforce/simpleforce"
)

var (
	sfURL      = "Custom or instance URL, for example, 'https://na01.salesforce.com/'"
	sfUser     = "Username of the Salesforce account."
	sfPassword = "Password of the Salesforce account."
	sfToken    = "Security token, could be omitted if Trusted IP is configured."
)

func createClient() *simpleforce.Client {
	client := simpleforce.NewClient(sfURL, simpleforce.DefaultClientID, simpleforce.DefaultAPIVersion)
	if client == nil {
		// handle the error

		return nil
	}

	err := client.LoginPassword(sfUser, sfPassword, sfToken)
	if err != nil {
		// handle the error

		fmt.Println(err)
	}

	// Do some other stuff with the client instance if needed.

	return client
}

func main() {
    client := createClient()
    
    q := "Some SOQL Query String"
	result, err := client.Query(q) // Note: for Tooling API, use client.Tooling().Query(q)
	
    if err != nil {
		// handle the error
		fmt.Println(err)
	}

	for _, record := range result.Records {
		// access the record as SObjects.
		fmt.Println(record)
	}
}
```

> Note: Use `"https://test.salesforce.com/"` if you need to access the sandbox instance instead of a Production instance


#### go-soapforce

* [go-soapforce](https://github.com/tzmfreedom/go-soapforce)

```go
package main

import (
	"fmt"

	"github.com/tzmfreedom/go-soapforce"
)

func main() {
	client := soapforce.NewClient()
	client.SetLoginUrl("test.salesforce.com")
	res, err := client.Login("Custom or instance URL, for example, 'https://na01.salesforce.com/'", "<passoword><secret-token>")
	client.SetApiVersion("52.0")
	client.SetDebug(true)
	
    resD, errD := client.DescribeSObject("Account")

	assetFields = "Id, ContactId, AccountId, Account.Name, ParentId, RootAssetId, Product2.Name, ProductCode"
	queryString := fmt.Sprintf("SELECT %s FROM Asset WHERE Id = '%s'", assetFields, "02i5Y00000hWe1IQAS")

	result, errQ := client.Query(queryString)

	for _, assetRecord_ := range result.Records {
		assetRecord := assetRecord_.Fields
		sfOpportunityAsset := assetRecord["AccountId"]
		_ = sfOpportunityAsset
	}
}
```

> Note: Use `"test.salesforce.com/"` if you need to access the sandbox instance instead of a Production instance

### Prometheus

- [https://prometheus.io/docs/instrumenting/pushing/](https://prometheus.io/docs/instrumenting/pushing/)
- [https://pkg.go.dev/github.com/prometheus/client_golang/prometheus/push?utm_source=godoc#example-Pusher.Push](https://pkg.go.dev/github.com/prometheus/client_golang/prometheus/push?utm_source=godoc#example-Pusher.Push)

    [https://github.com/prometheus/client_golang/tree/v1.10.0/prometheus/push](https://github.com/prometheus/client_golang/tree/v1.10.0/prometheus/push)

    ```go
    package main
    
    import (
    	"fmt"
    
    	"github.com/prometheus/client_golang/prometheus"
    	"github.com/prometheus/client_golang/prometheus/push"
    )
    
    func main() {
    	completionTime := prometheus.NewGauge(prometheus.GaugeOpts{
    		Name: "db_backup_last_completion_timestamp_seconds",
    		Help: "The timestamp of the last successful completion of a DB backup.",
    	})
    	completionTime.SetToCurrentTime()
    	if err := push.New("http://pushgateway:9091", "db_backup").
    		Collector(completionTime).
    		Grouping("db", "customers").
    		Push(); err != nil {
    		fmt.Println("Could not push completion time to Pushgateway:", err)
    	}
    }
    ```

-----------------------------------------------------------------------------------

## Database
* [Sqlite3](https://www.codeproject.com/Articles/5261771/Golang-SQLite-Simple-Example)

-----------------------------------------------------------------------------------

## Reference

* [Official Website](https://golang.org/doc/effective_go)
* [Official Website Tour](https://tour.golang.org/welcome/1)
* [golangprograms.com](https://www.golangprograms.com/go-language)
* [golangbot.com](https://golangbot.com/learn-golang-series/)
* [Alex Edwards Blog](https://www.alexedwards.net/blog)
* [codism.io](https://codism.io/category/golang)
* (yourbasic.org)[https://yourbasic.org/golang)

-----------------------------------------------------------------------------------

## Bibliography

* [The Go Programming Language - Alan A. A. Donovan, Brian W. Kernighan](https://www.google.it/books/edition/The_Go_Programming_Language/SJHvCgAAQBAJ?hl=it&gbpv=1&printsec=frontcover) 
* [Go Bootcamp - Matt Aimonetti](http://www.golangbootcamp.com/book) (free)
* [An introduction to programming in Go - Caleb Doxsey](http://www.golang-book.com/books/intro) (free)
* [The Little Go Book - Karl Seguin](https://www.openmymind.net/The-Little-Go-Book/)
* [Go 101 - Tapir Liu](https://go101.org/article/101.html)  ([free](https://github.com/go101/go101/releases))
* [Let's Go - Alex Edwards](https://lets-go.alexedwards.net/)
* [The way to Go - Ivo Balbaert](https://www.google.it/books/edition/The_Way_to_Go/oowq_6bAgloC?hl=it&gbpv=1&printsec=frontcover)



## Web development

* [Let's Go - Alex Edwards](https://github.com/michaeldegli/lets-go)

-----------------------------------------------------------------------------------

## To learn

- [ ] Optional function parameter in Go
- [ ] Tags
- [ ] reflect
- [ ] interface 
  - [ ] https://gobyexample.com/interfaces 
  - [ ] https://tour.golang.org/methods/9 
  - [ ] https://tour.golang.org/methods/14 
  - [ ] https://www.youtube.com/watch?v=lh_Uv2imp14&list=PLzMcBGfZo4-mtY_SE3HuzQJzuj4VlUG0q&index=22
  - [ ] https://www.alexedwards.net/blog/interfaces-explained
  - [ ] https://medium.com/rungo/interfaces-in-go-ab1601159b3a
  - [ ] https://www.golangprograms.com/go-language/interface.html
  - [ ] https://golangbot.com/interfaces-part-1/
  - [ ] Example of interface with reflection topic: https://golangbot.com/reflection/
- [ ] Collection functions: https://gobyexample.com/collection-functions
- [ ] try - catch
- [ ] reflection (inspect of python?) : https://golangbot.com/reflection/

-----------------------------------------------------------------------------------

# To check
```go
split := func(s string) { 
    // ...
}
```

```go
package main

import (
	"fmt"
	"path"
)

func main() {
	split := func(s string) {
		dir, file := path.Split(s)
		fmt.Printf("path.Split(%q) = dir: %q, file: %q\n", s, dir, file)
	}
	split("test/static/myfile.css")
	split("myfile.css")
	split("")
}
```


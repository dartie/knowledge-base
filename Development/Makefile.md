# Makefile

- [Makefile](#makefile)
  - [Installation](#installation)
    - [Linux](#linux)
  - [Windows](#windows)
      - [Winget](#winget)
      - [Choco](#choco)
      - [Scoop](#scoop)
  - [Syntax and rules](#syntax-and-rules)
  - [Suppress print of command](#suppress-print-of-command)
    - [Suppression per command](#suppression-per-command)
    - [Per-Target](#per-target)
    - [Globally](#globally)
  - [.PHONY](#phony)
  - [Variables](#variables)
    - [Makefile special (automatic) variables](#makefile-special-automatic-variables)
  - [Interate over a list](#interate-over-a-list)
    - [Range](#range)
  - [Print text](#print-text)
    - [echo](#echo)
    - [printf](#printf)
    - [Print with style](#print-with-style)
      - [tput](#tput)
      - [Print with colors](#print-with-colors)
  - [Sleep](#sleep)
  - [How to hide "no such file or directory" errors while cleaning](#how-to-hide-no-such-file-or-directory-errors-while-cleaning)
  - [How can I catch a command error and continue the compilation](#how-can-i-catch-a-command-error-and-continue-the-compilation)
  - [How to check if file exists](#how-to-check-if-file-exists)
  - [How to check if folder exists](#how-to-check-if-folder-exists)
  - [Makefile with Go](#makefile-with-go)
    - [Build for all platforms](#build-for-all-platforms)
  - [Troubleshooting](#troubleshooting)
    - [make: go: Permission denied](#make-go-permission-denied)


## Installation

### Linux

- Already installed

## Windows

- https://www.technewstoday.com/install-and-use-make-in-windows/

#### Winget

```bash
winget install GnuWin32.Make
```

#### Choco

- https://linuxhint.com/install-use-make-windows/

#### Scoop

```bash
scoop install make
```

## Syntax and rules

```makefile
target: requirement1, requirement2
	command
```

- `make` with no arguments executes the first rule in the file.
- Putting the list of files on which the command depends on the first line after the `:`, **make** knows that the rule **hellomake** needs to be executed if any of those files change.
- There is a **tab** before the gcc command in the makefile.

## Suppress print of command

*[Make](https://www.baeldung.com/linux/tag/make)* prints each command present in a *Makefile* before executing it, which can lead to the unnecessary output. In this tutorial, we’ll learn how to suppress the echo of the command invocations in a *Makefile.*

```makefile
$ cat Makefile
all: foo bar

foo:
    printf "%s\n" "Target foo executing..."
    printf "%s\n" "Hello from foo!"
bar:
    printf "%s\n" "Target bar executing..."
    printf "%s\n" "Hello from bar!"
```

⬇️

```bash
$ make
printf "%s\n" "Target foo executing..."
Target foo executing...
printf "%s\n" "Hello from foo!"
Hello from foo!
printf "%s\n" "Target bar executing..."
Target bar executing...
printf "%s\n" "Hello from bar!"
Hello from bar!
```

### Suppression per command

```makefile
$ cat Makefile
all: foo bar

foo:
    @printf "%s\n" "Target foo executing..."
    printf "%s\n" "Hello from foo!"
bar:
    @printf "%s\n" "Target bar executing..."
    printf "%s\n" "Hello from bar!"
```

⬇️

```bash
$ make
Target foo executing...
printf "%s\n" "Hello from foo!"
Hello from foo!
Target bar executing...
printf "%s\n" "Hello from bar!"
Hello from bar!
```

### Per-Target

We can suppress all command invocations for a target by marking it as a dependency of the special *[.SILENT](https://www.gnu.org/software/make/manual/html_node/Special-Targets.html#Special-Targets)* target.

Let’s silence the *foo* target:

```makefile
$ cat Makefile
.SILENT: foo

all: foo bar

foo:
    printf "%s\n" "Target foo executing..."
...Copy
```

⬇️ Now, we can see that the command invocations are printed only from the *bar* target:

```bash
$ make
Target foo executing...
Hello from foo!
printf "%s\n" "Target bar executing..."
Target bar executing...
printf "%s\n" "Hello from bar!"
Hello from bar!Copy
```

### Globally

Finally, we can pass the *`-s`* flag to *make* to silence the command invocations of every target. ****This method also has the benefit of not requiring any modifications to the *Makefile*:

```makefile
$ make -s
Target foo executing...
Hello from foo!
Target bar executing...
Hello from bar!Copy
```

**This method is quite handy as we can use it to reduce clutter once the *Makefile* is ready and fall back to executing *make* as normal during development.** The extra output is helpful during development as it aids debugging.

## .PHONY

Let's assume you have `install` target, which is a very common in makefiles. If you do *not* use `.PHONY`, and a file named `install` exists in the same directory as the Makefile, then `make install` will do *nothing*. This is because Make interprets the rule to mean "execute such-and-such recipe to create the file named `install`". Since the file is already there, and its dependencies didn't change, nothing will be done.

However if you make the `install` target PHONY, it will tell the make tool that the target is fictional, and that make should not expect it to create the actual file. Hence it will not check whether the `install` file exists, meaning: 

1. its behavior will not be altered if the file does exist and 
1. extra `stat()` will not be called.

Generally all targets in your Makefile which do not produce an output file with the same name as the target name should be PHONY. This typically includes `all`, `install`, `clean`, `distclean`, and so on.

```makefile
.PHONY: install
```

- means the word "install" doesn't represent a file name in this Makefile;
- means the Makefile has nothing to do with a file called "install" in the same directory.

- second explanation
    
    By default, Makefile targets are "file targets" - they are used to build files from other files. Make assumes its target is a file, and this makes writing Makefiles relatively easy:
    
    ```makefile
    foo: bar
      create_one_from_the_other foo bar
    
    ```
    
    However, sometimes you want your Makefile to run commands that do not represent physical files in the file system. Good examples for this are the common targets "clean" and "all". Chances are this isn't the case, but you *may* potentially have a file named `clean` in your main directory. In such a case Make will be confused because by default the `clean` target would be associated with this file and Make will only run it when the file doesn't appear to be up-to-date with regards to its dependencies.
    
    These special targets are called *phony* and you can explicitly tell Make they're not associated with files, e.g.:
    
    ```makefile
    .PHONY: clean
    clean:
      rm -rf *.o
    ```
    

## Variables

```makefile
cur-dir   := $(shell pwd)
```

### Makefile special (automatic) variables

`$@` is the name of the target being generated, and `$<` the first prerequisite (usually a source file). You can find a list of all these special variables in the [GNU Make manual](https://www.gnu.org/software/make/manual/html_node/Automatic-Variables.html#Automatic-Variables).

For example, consider the following declaration:

```
all: library.cpp main.cpp

```

In this case:

- `$@` evaluates to `all`
- `$<` evaluates to `library.cpp`
- `$^` evaluates to `library.cpp main.cpp`

From [Managing Projects with GNU Make, 3rd Edition, p. 16](http://uploads.mitechie.com/books/Managing_Projects_with_GNU_Make_Third_Edition.pdf) (it's under *GNU Free Documentation License*):

> Automatic variables are set by make after a rule is matched. They provide access to elements from the target and prerequisite lists so you don’t have to explicitly specify any filenames. They are very useful for avoiding code duplication, but are critical when defining more general pattern rules.
> 
> 
> There are seven “core” automatic variables:
> 
> - `$@`: The filename representing the target.
> - `$%`: The filename element of an archive member specification.
> - `$<`: The filename of the first prerequisite.
> - `$?`: The names of all prerequisites that are newer than the target, separated by spaces.
> - `$^`: The filenames of all the prerequisites, separated by spaces. This list has duplicate filenames removed since for most uses, such as compiling, copying, etc., duplicates are not wanted.
> - `$+`: Similar to `$^`, this is the names of all the prerequisites separated by spaces, except that `$+` includes duplicates. This variable was created for specific situations such as arguments to linkers where duplicate values have meaning.
> - `$*`: The stem of the target filename. A stem is typically a filename without its suffix. Its use outside of pattern rules is discouraged.
> 
> In addition, each of the above variables has two variants for compatibility with other makes. One variant returns only the directory portion of the value. This is indicated by appending a “D” to the symbol, `$(@D)`, `$(<D)`, etc. The other variant returns only the file portion of the value. This is indicated by appending an “F” to the symbol, `$(@F)`, `$(<F)`, etc. Note that these variant names are more than one character long and so must be enclosed in parentheses. GNU make provides a more readable alternative with the dir and notdir functions.
> 

## Interate over a list

```makefile
LIST = one two three
all:
	for i in $(LIST); do \
		echo $$i; \
	done
```

### Range

```makefile
all:
	target:
		number=1 ; while [[ $$number -le 10 ]] ; do \
		echo $$number ; \
		((number = number + 1)) ; \
	done
```

This outputs 1 through 10 inclusive, just change the `while` terminating condition from 10 to 1000 for a much larger range as indicated in your comment.

*Nested* loops can be done thus:

```makefile
target:
    num1=1 ; while [[ $$num1 -le 4 ]] ; do \
        num2=1 ; while [[ $$num2 -le 3 ]] ; do \
            echo $$num1 $$num2 ; \
            ((num2 = num2 + 1)) ; \
        done ; \
        ((num1 = num1 + 1)) ; \
    done

```

## Print text

### echo

```makefile
all:
	echo Hello World!
```

### printf

```makefile
all:
	printf "%s" Hello
```

```makefile
greeting = Hello

all:
	printf "%s" $$greeting
```

### Print with style

- **[How to change the output color of echo in Linux](https://stackoverflow.com/questions/5947742/how-to-change-the-output-color-of-echo-in-linux)**
    
    ```makefile
    Black        0;30     Dark Gray     1;30
    Red          0;31     Light Red     1;31
    Green        0;32     Light Green   1;32
    Brown/Orange 0;33     Yellow        1;33
    Blue         0;34     Light Blue    1;34
    Purple       0;35     Light Purple  1;35
    Cyan         0;36     Light Cyan    1;36
    Light Gray   0;37     White         1;37
    
    # Reset
    Color_Off='\033[0m'       # Text Reset
    
    # Regular Colors
    Black='\033[0;30m'        # Black
    Red='\033[0;31m'          # Red
    Green='\033[0;32m'        # Green
    Yellow='\033[0;33m'       # Yellow
    Blue='\033[0;34m'         # Blue
    Purple='\033[0;35m'       # Purple
    Cyan='\033[0;36m'         # Cyan
    White='\033[0;37m'        # White
    
    # Bold
    BBlack='\033[1;30m'       # Black
    BRed='\033[1;31m'         # Red
    BGreen='\033[1;32m'       # Green
    BYellow='\033[1;33m'      # Yellow
    BBlue='\033[1;34m'        # Blue
    BPurple='\033[1;35m'      # Purple
    BCyan='\033[1;36m'        # Cyan
    BWhite='\033[1;37m'       # White
    
    # Underline
    UBlack='\033[4;30m'       # Black
    URed='\033[4;31m'         # Red
    UGreen='\033[4;32m'       # Green
    UYellow='\033[4;33m'      # Yellow
    UBlue='\033[4;34m'        # Blue
    UPurple='\033[4;35m'      # Purple
    UCyan='\033[4;36m'        # Cyan
    UWhite='\033[4;37m'       # White
    
    # Background
    On_Black='\033[40m'       # Black
    On_Red='\033[41m'         # Red
    On_Green='\033[42m'       # Green
    On_Yellow='\033[43m'      # Yellow
    On_Blue='\033[44m'        # Blue
    On_Purple='\033[45m'      # Purple
    On_Cyan='\033[46m'        # Cyan
    On_White='\033[47m'       # White
    
    # High Intensity
    IBlack='\033[0;90m'       # Black
    IRed='\033[0;91m'         # Red
    IGreen='\033[0;92m'       # Green
    IYellow='\033[0;93m'      # Yellow
    IBlue='\033[0;94m'        # Blue
    IPurple='\033[0;95m'      # Purple
    ICyan='\033[0;96m'        # Cyan
    IWhite='\033[0;97m'       # White
    
    # Bold High Intensity
    BIBlack='\033[1;90m'      # Black
    BIRed='\033[1;91m'        # Red
    BIGreen='\033[1;92m'      # Green
    BIYellow='\033[1;93m'     # Yellow
    BIBlue='\033[1;94m'       # Blue
    BIPurple='\033[1;95m'     # Purple
    BICyan='\033[1;96m'       # Cyan
    BIWhite='\033[1;97m'      # White
    
    # High Intensity backgrounds
    On_IBlack='\033[0;100m'   # Black
    On_IRed='\033[0;101m'     # Red
    On_IGreen='\033[0;102m'   # Green
    On_IYellow='\033[0;103m'  # Yellow
    On_IBlue='\033[0;104m'    # Blue
    On_IPurple='\033[0;105m'  # Purple
    On_ICyan='\033[0;106m'    # Cyan
    On_IWhite='\033[0;107m'   # White
    ```
    
    ### the escape character in **bash**, **hex** and **octal** respectively:
    
    ```
    |       | bash  | hex     | octal   | NOTE                         |
    |-------+-------+---------+---------+------------------------------|
    | start | \e    | \x1b    | \033    |                              |
    | start | \E    | \x1B    | -       | x cannot be capital          |
    | end   | \e[0m | \x1b[0m | \033[0m |                              |
    | end   | \e[m  | \x1b[m  | \033[m  | 0 is appended if you omit it |
    |       |       |         |         |                              |
    
    ```
    
    ### short example:
    
    ```
    | color       | bash         | hex            | octal          | NOTE                                  |
    |-------------+--------------+----------------+----------------+---------------------------------------|
    | start green | \e[32m<text> | \x1b[32m<text> | \033[32m<text> | m is NOT optional                     |
    | reset       | <text>\e[0m  | <text>\1xb[0m  | <text>\033[om  | o is optional (do it as best practice |
    |             |              |                |                |                                       |
    
    ```
    
    ```
    |------------+----------+---------+-------+------------------+------------------------------+--------------------------------------|
    | color-mode | octal    | hex     | bash  | description      | example (= in octal)         | NOTE                                 |
    |------------+----------+---------+-------+------------------+------------------------------+--------------------------------------|
    |          0 | \033[0m  | \x1b[0m | \e[0m | reset any affect | echo -e "\033[0m"            | 0m equals to m                       |
    |          1 | \033[1m  |         |       | light (= bright) | echo -e "\033[1m####\033[m"  | -                                    |
    |          2 | \033[2m  |         |       | dark (= fade)    | echo -e "\033[2m####\033[m"  | -                                    |
    |------------+----------+---------+-------+------------------+------------------------------+--------------------------------------|
    |  text-mode | ~        |         |       | ~                | ~                            | ~                                    |
    |------------+----------+---------+-------+------------------+------------------------------+--------------------------------------|
    |          3 | \033[3m  |         |       | italic           | echo -e "\033[3m####\033[m"  |                                      |
    |          4 | \033[4m  |         |       | underline        | echo -e "\033[4m####\033[m"  |                                      |
    |          5 | \033[5m  |         |       | blink (slow)     | echo -e "\033[3m####\033[m"  |                                      |
    |          6 | \033[6m  |         |       | blink (fast)     | ?                            | not wildly support                   |
    |          7 | \003[7m  |         |       | reverse          | echo -e "\033[7m####\033[m"  | it affects the background/foreground |
    |          8 | \033[8m  |         |       | hide             | echo -e "\033[8m####\033[m"  | it affects the background/foreground |
    |          9 | \033[9m  |         |       | cross            | echo -e "\033[9m####\033[m"  |                                      |
    |------------+----------+---------+-------+------------------+------------------------------+--------------------------------------|
    | foreground | ~        |         |       | ~                | ~                            | ~                                    |
    |------------+----------+---------+-------+------------------+------------------------------+--------------------------------------|
    |         30 | \033[30m |         |       | black            | echo -e "\033[30m####\033[m" |                                      |
    |         31 | \033[31m |         |       | red              | echo -e "\033[31m####\033[m" |                                      |
    |         32 | \033[32m |         |       | green            | echo -e "\033[32m####\033[m" |                                      |
    |         33 | \033[33m |         |       | yellow           | echo -e "\033[33m####\033[m" |                                      |
    |         34 | \033[34m |         |       | blue             | echo -e "\033[34m####\033[m" |                                      |
    |         35 | \033[35m |         |       | purple           | echo -e "\033[35m####\033[m" | real name: magenta = reddish-purple  |
    |         36 | \033[36m |         |       | cyan             | echo -e "\033[36m####\033[m" |                                      |
    |         37 | \033[37m |         |       | white            | echo -e "\033[37m####\033[m" |                                      |
    |------------+----------+---------+-------+------------------+------------------------------+--------------------------------------|
    |         38 | 8/24     |                    This is for special use of 8-bit or 24-bit                                            |
    |------------+----------+---------+-------+------------------+------------------------------+--------------------------------------|
    | background | ~        |         |       | ~                | ~                            | ~                                    |
    |------------+----------+---------+-------+------------------+------------------------------+--------------------------------------|
    |         40 | \033[40m |         |       | black            | echo -e "\033[40m####\033[m" |                                      |
    |         41 | \033[41m |         |       | red              | echo -e "\033[41m####\033[m" |                                      |
    |         42 | \033[42m |         |       | green            | echo -e "\033[42m####\033[m" |                                      |
    |         43 | \033[43m |         |       | yellow           | echo -e "\033[43m####\033[m" |                                      |
    |         44 | \033[44m |         |       | blue             | echo -e "\033[44m####\033[m" |                                      |
    |         45 | \033[45m |         |       | purple           | echo -e "\033[45m####\033[m" | real name: magenta = reddish-purple  |
    |         46 | \033[46m |         |       | cyan             | echo -e "\033[46m####\033[m" |                                      |
    |         47 | \033[47m |         |       | white            | echo -e "\033[47m####\033[m" |                                      |
    |------------+----------+---------+-------+------------------+------------------------------+--------------------------------------|
    |         48 | 8/24     |                    This is for special use of 8-bit or 24-bit                                            |                                                                                       |
    |------------+----------+---------+-------+------------------+------------------------------+--------------------------------------|
    
    ```
    
    !https://raw.githubusercontent.com/k-five/badge-for-git/master/res/line/line5-900px-%23F80.svg?sanitize=true
    
    The below table shows a summary of **8 bit** version of ANSI-color
    
    ```
    |------------+-----------+-----------+---------+------------------+------------------------------------+-------------------------|
    | foreground | octal     | hex       | bash    | description      | example                            | NOTE                    |
    |------------+-----------+-----------+---------+------------------+------------------------------------+-------------------------|
    |        0-7 | \033[38;5 | \x1b[38;5 | \e[38;5 | standard. normal | echo -e '\033[38;5;1m####\033[m'   |                         |
    |       8-15 |           |           |         | standard. light  | echo -e '\033[38;5;9m####\033[m'   |                         |
    |     16-231 |           |           |         | more resolution  | echo -e '\033[38;5;45m####\033[m'  | has no specific pattern |
    |    232-255 |           |           |         |                  | echo -e '\033[38;5;242m####\033[m' | from black to white     |
    |------------+-----------+-----------+---------+------------------+------------------------------------+-------------------------|
    | foreground | octal     | hex       | bash    | description      | example                            | NOTE                    |
    |------------+-----------+-----------+---------+------------------+------------------------------------+-------------------------|
    |        0-7 |           |           |         | standard. normal | echo -e '\033[48;5;1m####\033[m'   |                         |
    |       8-15 |           |           |         | standard. light  | echo -e '\033[48;5;9m####\033[m'   |                         |
    |     16-231 |           |           |         | more resolution  | echo -e '\033[48;5;45m####\033[m'  |                         |
    |    232-255 |           |           |         |                  | echo -e '\033[48;5;242m####\033[m' | from black to white     |
    |------------+-----------+-----------+---------+------------------+------------------------------------+-------------------------|
    ```
    

#### tput

```makefile
printf-bold-1:
    @printf "normal text - `tput bold`bold text`tput sgr0`"

```

Of course, you may store the result into a Make variable, to reduce the number of subshells:

```makefile
bold := $(shell tput bold)
sgr0 := $(shell tput sgr0)

printf-bold-1:
    @printf 'normal text - $(bold)bold text$(sgr0)'

.PHONY: printf-bold-1
```

```makefile
printf-bold-1:
    @printf "normal text - \033[1mbold text\033[0m"

```

Or, as suggested in the comments, use simple quotes instead of double quotes :

```makefile
printf-bold-1:
    @printf 'normal text - \e[1mbold text\e[0m'
```

- tput with function
    
    ```makefile
    define colorecho
          @tput setaf 6
          @echo $1
          @tput sgr0
    endef
    ```
    
    Defines a makefile *function* named colorecho, with a single argument which is exposed via $1. This function sets the terminal color to cyan [with tput](http://www.tldp.org/HOWTO/Bash-Prompt-HOWTO/x405.html), echoes its argument and resets the terminal settings to default.
    
    Here's how this function can be called:
    
    ```makefile
    $(call colorecho, "Text to print")
    ```
    
    ```makefile
    $(call colorecho, "Linking with" $(LD))
    $(LD) $^ -o $@
    ```
    
    ```makefile
    # Function definitions
    define printInProgress
          @tput setaf 8
          @echo $1
          @tput sgr0
    endef
    
    define printStepCompleted
          @tput setaf 4
          @echo $1
          @tput sgr0
    endef
    
    define printWarning
          @tput setaf 3
          @echo $1
          @tput sgr0
    endef
    
    define printError
          @tput setaf 9
          @echo $1
          @tput sgr0
    endef
    
    define printDone
          @tput setaf 10
          @echo $1
          @tput sgr0
    endef
    # ------------------------------------
    
    colorf:
    	$(call printInProgress, "In progress")
    	$(call printWarning, "Warning")
    	$(call printError, "Error")
    	$(call printStepCompleted, "Step Completed")
    	$(call printDone, "Done")
    ```
    

#### Print with colors

```makefile
@echo -e "\033[92mHello World\033[0m"
```

```makefile
@printf "\033[92mHello World\033[0m"
```

```makefile
COLOUR_GREEN=\033[0;32m
COLOUR_RED=\033[0;31m
COLOUR_BLUE=\033[0;34m
COLOUR_END=\033[0m

all:
	@echo -e "$(COLOUR_GREEN)Test Passed$(COLOUR_END)"
```

## Sleep

```makefile
all:
	sleep 2
	
```

## How to hide "no such file or directory" errors while cleaning

Use the `-f` option to `rm`. That option tells `rm` to ignore non-existent files and not prompt for confirmation.

```makefile
clean:
    rm -f $(objects) $(debug_objects) solution solution.gdb
```

## How can I catch a command error and continue the compilation

1. Prefix any command with a `-` to indicate to `make` that this command is okay to fail:
    
    ```makefile
    normal_target:
             -gcc -o main main.c
             next command here
    
    ```
    
2. Test for failure in the commands:

```makefile
normal_target:
         if gcc -o main main.c; then \
            echo succeeded; \
         else \
            echo compilation failed; \
            gcc -o ...; \
         fi
```

## How to check if file exists

```makefile
bar:
	if test /home/dartie/myprojects/makefile-test/main.go; \
	then \
		echo exists; \
	else \
		echo does not; \
	fi
```

- Or omit `test` and use brackets
    
    ```makefile
    foo:
    	if [ "/home/dartie/myprojects/makefile-test/main.go" ]; then \
    		echo "Dir exists"; \
    	fi
    ```
    

## How to check if folder exists

- Add `-d` to `test`
    
    ```makefile
    bar:
    	if test -d /home/dartie/myprojects/makefile-test/; \
    	then \
    		echo exists; \
    	else \
    		echo does not; \
    	fi
    ```
    
- Or omit `test` and use brackets
    
    ```makefile
    foo:
    	if [ -d "/home/dartie/myprojects/makefile-test/" ]; then \
    		echo "Dir exists"; \
    	fi
    ```
    
- Use [wildcard](https://www.gnu.org/software/make/manual/html_node/Wildcard-Function.html)
    
    ```makefile
    DIR_TO_CHECK_FOR = 'large_directory'
    
    download_data:
    	ifeq ("$(wildcard $(DIR_TO_CHECK_FOR))", "")
    		@echo "Directory does not exist."
    		# Perform download...
    	else
    		@echo "Skipping download because directory already exists."
    	endif
    ```
    
    This leverages `wildcard` to get back a space-separated list of files that match the supplied pattern, which we set to `$(DIR_TO_CHECK_FOR)` in this case. If the list is empty, then we claim the directory does not exist and we could put our long-running download in there.
    

## Makefile with Go

- https://www.youtube.com/watch?v=QztvWSCbQLU
- `main.go`
    
    ```go
    package main
    
    import "fmt"
    
    func main() {
        fmt.Println("Hello World!")
    }
    ```
    
- `Makefile`
    
    ```makefile
    hello:
    	echo "hello"
    
    build:
    	go build -o bin/main main.go;
    
    run:
    	go run main.go;
    ```
    
    <aside>
    💡 https://stackoverflow.com/questions/73908737/permission-denied-when-running-go-from-makefile
    `;` at the end of go command, workarounds a **make** bug: if you have a *directory* named `go`, in some directory on your `PATH` (before the actual directory containing the `go` executable), the go command fails with:
    
    make: go: Permission denied
    make: *** [Makefile:8: run] Error 127
    
    </aside>
    

1. Run **make** with all different arguments (targets)
    
    ```bash
    make hello
    > echo "hello"
    > hello
    
    make build
    > go build -o bin/main main.go;
    
    make run
    > go run main.go;
    > Hello World!
    ```
    
2. Add more targets to Makefile
    
    ```makefile
    hello:
    	echo "hello"
    
    build:
    	go build -o bin/main main.go;
    
    run:
    	go run main.go;
    
    compile:
    	GOOS=linux GOARCH=386 go build -o bin/main-linux-386 main.go
    	GOOS=windows GOARCH=386 go build -o bin/main-windows-386 main.go
    
    all: compile hello
    ```
    
3. Run `make all`
    
    ```bash
    make all
    GOOS=linux GOARCH=386 go build -o bin/main-linux-386 main.go
    GOOS=windows GOARCH=386 go build -o bin/main-windows-386 main.go
    echo "hello"
    hello
    ```
    

### Build for all platforms

```makefile
.SILENT: all

PLATFORMS = linux windows darwin
ARCH = amd64
all:
	for p in $(PLATFORMS); do \
		printf "Compiling %s...\r" $$p; \
		GOOS=$$p GOARCH=$(ARCH) go build -o bin/main-$$p-$(ARCH) main.go; \
		printf "%s... done            \n" $$p; \
	done
```

```makefile
.SILENT: all

PLATFORMS = linux windows darwin
ARCH = amd64
all:
	for p in $(PLATFORMS); do \
		printf "Compiling %s...\r" $$p; \
		GOOS=$$p GOARCH=$(ARCH) go build -o bin/main-$$p-$(ARCH) main.go; \
		printf "%s... done            \n" $$p; \
	done
```

```makefile
.SILENT: build clean
.PHONY: build clean

PLATFORMS = linux windows darwin
ARCHS = amd64 386
ARCH = amd64

build:
	for p in $(PLATFORMS); do \
		for a in $(ARCHS); do \
			printf "Compiling %s...\r" $$p; \
			GOOS=$$p GOARCH=$$a go build -o bin/main-$$p-$$a main.go; \
			printf "%s... done            \n" $$p; \
		done \
	done

clean:
	if test -d bin; \
	then \
		rm -rf bin; \
		echo "Previous output removed"; \
	else \
		echo "No previous output to delete"; \
	fi
```

```makefile
## Define targets to quite (the commands are not printed)
.SILENT: build clean all
.PHONY: build clean all

## Constant definitions
TPUT_RED=1
TPUT_GREEN=2
TPUT_ORANGE=3
TPUT_BLUE=4
TPUT_VIOLET=5
TPUT_CYAN=6
TPUT_WHITE=7
TPUT_GREY=8
TPUT_RED=9
TPUT_GREEN=10

## Function definitions
define printInProgress
	tput setaf $(TPUT_GREY) ; echo $1 ; tput sgr0
endef

define printWorking
	tput setaf $(TPUT_VIOLET) ; echo -e "$1\r" ; tput sgr0
endef

define printStepCompleted
	tput setaf $(TPUT_BLUE) ; echo $1 ; tput sgr0
endef

define printWarning
	tput setaf $(TPUT_ORANGE) ; echo $1 ; tput sgr0
endef

define printError
	tput setaf $(TPUT_RED) ; echo $1 ; tput sgr0
endef

define printDone
	tput setaf $(TPUT_GREEN) ; echo $1 ; tput sgr0
endef
## ------------------------------------

## Working variables
VERSION = 1.0.0
PLATFORMS = linux windows darwin
ARCHS = amd64 386

build:
	for p in $(PLATFORMS); do \
		for a in $(ARCHS); do \
			printf "Compiling %s - %s...\r" $$p $$a; \
			sleep 1; \
			if GOOS=$$p GOARCH=$$a go build -o bin/main-$$p-$$a *.go; then \
				$(call printStepCompleted, "$$p - $$a -  done                 "); \
			else \
				$(call printError, "$$p - $$a -  failed                 "); \
			fi \
		done \
	done
	echo
	$(call printDone, "Compilation completed!")

clean:
	if test -d bin; \
	then \
		rm -rf bin; \
		$(call printDone, "Previous output removed"); \
	else \
		$(call printWarning, "No previous output to delete"); \
	fi

all: clean build
```

## Troubleshooting

### make: go: Permission denied
make: *** [Makefile:8: run] Error 127

- **Explanation:** `make` bug: if `make` is placed in a tree containing **bin** folder the error is returned.
- **Solution:** use `;` at the end of the command
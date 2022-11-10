# Batch

[[_TOC_]]

## Command concatenation
Using multiple commands and conditional processing symbols

You can run multiple commands from a single command line or script using conditional processing symbols. When you run multiple commands with conditional processing symbols, the commands to the right of the conditional processing symbol act based upon the results of the command to the left of the conditional processing symbol.

For example, you might want to run a command only if the previous command fails. Or, you might want to run a command only if the previous command is successful.

You can use the special characters listed in the following table to pass multiple commands.

`& [...]`  command1 & command2
Use to separate multiple commands on one command line. Cmd.exe runs the first command, and then the second command.

`&& [...]`  command1 && command2
Use to run the command following && only if the command preceding the symbol is successful. Cmd.exe runs the first command, and then runs the second command only if the first command completed successfully.

`|| [...]`  command1 || command2
Use to run the command following || only if the command preceding || fails. Cmd.exe runs the first command, and then runs the second command only if the first command did not complete successfully (receives an error code greater than zero).

`( ) [...]`  (command1 & command2)
Use to group or nest multiple commands.

`;` or `,` command1 parameter1;parameter2
Use to separate command parameters.

## escape % in batch file
  
_(Explanation in more details can be found in  [an archived Microsoft KB article](https://jeffpar.github.io/kbarchive/kb/075/Q75634/).)_

Three things to know:

1.  The percent sign is used in batch files to represent command line parameters:  `%1`,  `%2`, ...
2.  Two percent signs with any characters in between them are interpreted as a variable:
    
    `echo %myvar%`
    
3.  Two percent signs  _without_  anything in between (in a batch file) are treated like a single percent sign in a command (not a batch file):  `%%f`

----------

Why's that?

For example, if we execute your (simplified) command line

```batch
FOR /f %f in ('dir /b .') DO somecommand %f

```

in a batch file,  _rule 2_  would try to interpret

```batch
%f in ('dir /b .') DO somecommand %

```

as a variable. In order to prevent that, you have to apply  _rule 3_  and escape the  `%`  with an second  `%`:

```batch
FOR /f %%f in ('dir /b .') DO somecommand %%f
```


## Repeat a command
```batch
SET CMD=dir
for /l %x in (1, 1, 100) do %CMD%
```

## get unique text file content
> NOTE: requires cygwin
> * cygiconv-2.dll
> * cygintl-8.dll
> * cygwin1.dll
> * cat.exe
> * uniq.exe

```batch
cat unique_Test.txt  |sort | uniq
```
or (using **uniq.exe**)

```batch
uniq -c myfile.txt
```

## assign the first line of  a text file to a variable
```batch
set /p var= <file.txt
```


## Process


### Kill a process

```batch
taskkill /F /IM process.exe
```

```batch
taskkill /PID PID /F 
```

### Query of Process running
```batch
wmic process get Caption,ParentProcessId,ProcessId
```

Given a parent PID you can list the  _immediate_  children with something like:

```batch
wmic process where (ParentProcessId=2480) get Caption,ProcessId
```


remove first line (header)
```batch
for /f "usebackq skip=1 tokens=*" %i in (%query%) get variableValue ^| findstr /r /v "^$"`) do @echo %i
```


**Example:**
```batch
for /f "usebackq skip=1 tokens=*" %i in (`wmic environment where ^(name^="PATH" and systemVariable^=FALSE^) get variableValue ^| findstr /r /v "^$"`) do @echo %i
```

**`tasklist` command**
```batch
tasklist /v /fo csv | findstr /i "mycmd"
```


## Iterate a text file
```batch
for /F "tokens=*" %%A in (myfile.txt) do [process] %%A
```
if text file lines have spaces:

```batch
for /F "usebackq tokens=*" %%A in ("my file.txt") do [process] %%A
```



## Convert paths and filenames

Considering `I` the variable:
```
In addition, substitution of FOR variable references has been enhanced.
You can now use the following optional syntax:

    %~I         - expands %I removing any surrounding quotes (")
    %~fI        - expands %I to a fully qualified path name
    %~dI        - expands %I to a drive letter only
    %~pI        - expands %I to a path only
    %~nI        - expands %I to a file name only
    %~xI        - expands %I to a file extension only
    %~sI        - expanded path contains short names only
    %~aI        - expands %I to file attributes of file
    %~tI        - expands %I to date/time of file
    %~zI        - expands %I to size of file
    %~$PATH:I   - searches the directories listed in the PATH
                   environment variable and expands %I to the
                   fully qualified name of the first one found.
                   If the environment variable name is not
                   defined or the file is not found by the
                   search, then this modifier expands to the
                   empty string

The modifiers can be combined to get compound results:

    %~dpI       - expands %I to a drive letter and path only
    %~nxI       - expands %I to a file name and extension only
    %~fsI       - expands %I to a full path name with short names only
    %~dp$PATH:I - searches the directories listed in the PATH
                   environment variable for %I and expands to the
                   drive letter and path of the first one found.
    %~ftzaI     - expands %I to a DIR like output line

In the above examples %I and PATH can be replaced by other valid
values.  The %~ syntax is terminated by a valid FOR variable name.
Picking upper case variable names like %I makes it more readable and
avoids confusion with the modifiers, which are not case sensitive.
```


## Print windows services list with path exe
```batch
wmic service get name, pathname
```


## Increment terminal buffer size
### temporaly (current terminal instance)
```batch
mode con lines=32766
```
32766= 2^15-2

OR
```batch
mode con:cols=140 lines=2500
```

### permently (Windows registry)
```batch
:: escape the environment variable in the key name
set mySysRoot=%%SystemRoot%%

:: 655294544 equals 9999 lines in the GUI
reg.exe add "HKCU\\Console\\%mySysRoot%_system32_cmd.exe" /v ScreenBufferSize /t REG_DWORD /d 655294544 /f

:: We also need to change the Window Height, 3276880 = 50 lines
reg.exe add "HKCU\\Console\\%mySysRoot%_system32_cmd.exe" /v WindowSize /t REG_DWORD /d 3276880 /f
```

## Current directory
```shell
SET PRQA_DIR="%~dp0."
```

## Convert string to lowercase or uppercase
```bash
REM functions for making string to lowercase/uppercase
set tolower=for /L %%n in (1 1 2) do if %%n==2 ( for %%# in (a b c d e f g h i j k l m n o p q r s t u v w x y z) do set "lowerstring=!lowerstring:%%#=%%#!") ELSE setlocal enableDelayedExpansion ^& set lowerstring=
set toupper=for /L %%n in (1 1 2) do if %%n==2 ( for %%# in (A B C D E F G H I J K L M N O P Q R S T U V W X Y Z) do set "UPPERSTRING=!UPPERSTRING:%%#=%%#!") ELSE setlocal enableDelayedExpansion ^& set UPPERSTRING=

SET string_lowercase=dario
SET string_uppercase=DARIO

%tolower%%string_uppercase%
%toupper%%string_lowercase%

echo %lowerstring%
echo %UPPERSTRING%
```

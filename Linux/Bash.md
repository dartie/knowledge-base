# Bash

## Mount network drive
### Mount with write permissions
```bash
sudo mount -t cifs -o username=dartie,uid=1000,nounix //nas/Public /mnt/nas
```

```bash
export servername=192.168.1.151
export sharename=Public
export user=dartie
export password=password
sudo mkdir -p /mnt/nas/public
sudo mount -t cifs -o user=${user} //${servername}/${sharename} /mnt/nas/${sharename}
```


## ls command
list

```
-rwxrw-r--    10    root   root 2048    Jan 13 07:11 afile.exe
?UUUGGGOOOS   00  UUUUUU GGGGGG ####    ^-- date stamp and file name are obvious ;-)
^ ^  ^  ^ ^    ^      ^      ^    ^
| |  |  | |    |      |      |    \\--- File Size
| |  |  | |    |      |      \\-------- Group Name (for example, Users, Administrators, etc)
| |  |  | |    |      \\--------------- Owner Acct
| |  |  | |    \\---------------------- Link count (what constitutes a "link" here varies)
| |  |  | \\--------------------------- Alternative Access (blank means none defined, anything else varies)
| \\--\\--\\----------------------------- Read, Write and Special access modes for [U]ser, [G]roup, and [O]thers (everyone else)
\\------------------------------------- File type flag
```

## Symbolic links
```shell
sudo ln -s /usr/bin/python3 /usr/bin/python
```
`python` is a link of `python3`

## grep
[How To Find Files by Content Under UNIX - nixCraft](https://www.cyberciti.biz/faq/unix-linux-finding-files-by-content/)
```bash
grep -rnw '/path/to/somewhere/' -e 'pattern'
```

```
-r or -R is recursive,
-n is line number, and
-w stands for match the whole word.
-l (lower-case L) can be added to just give the file name of matching files.
```
Along with these, `--exclude`, `--include`, `--exclude-dir` flags could be used for efficient searching:

* This will only search through those files which have `.c` or `.h` extensions:
```bash
grep --include=\\*.{c,h} -rnw '/path/to/somewhere/' -e "pattern"
```

* This will exclude searching all the files ending with `.o` extension:
```bash
grep --exclude=*.o -rnw '/path/to/somewhere/' -e "pattern"
```

* For directories it's possible to exclude a particular directory(ies) through --exclude-dir parameter. For example, this will exclude the dirs dir1/, dir2/ and all of them matching *.dst/:
```bash
grep --exclude-dir={dir1,dir2,*.dst} -rnw '/path/to/somewhere/' -e "pattern"
```


## sed
```shell
sed -i 's/original/new/g' file.txt
```

Explanation:
`sed` = Stream EDitor
`-i` = in-place (i.e. save back to the original file)

The command string:
`s` = the substitute command
`original` = a regular expression describing the word to replace (or just the word itself)
`new` = the text to replace it with
``g` = global (i.e. replace all and not just the first occurrence)
`file.txt` = the file name

Additional arguments:
`-r` = add regular expressions


* Reference: https://www.thegeekstuff.com/2009/09/unix-sed-tutorial-replace-text-inside-a-file-using-substitute-command/?utm_source=sitekickr&utm_medium=snip_button


## Manage services

### /etc/init.d/
```bash
# Start
sudo /etc/init.d/smbd start

# Stop
sudo /etc/init.d/smbd stop

# Restart
sudo /etc/init.d/smbd restart
```


### service
```bash
# Start
sudo service smbd start

# Stop
sudo service smbd stop

# Restart
sudo service smbd restart
```


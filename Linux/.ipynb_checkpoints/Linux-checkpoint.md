# Linux

## Add support for x32 bit to a x64 distro

```bash
sudo dpkg --add-architecture i386
sudo apt-get update
sudo apt-get install libc6:i386 libncurses5:i386 libstdc++6:i386
./file-name
```


## Change hostname

1. Change hostname in file `/etc/hostname`

   ```bash
   sudo vi /etc/hostname
   ```

2. Change hostname # [How to allow execution without prompting file `/etc/hosts`

   ```bash
   sudo vi /etc/hosts
   ```

3. Restart network service

   ```bash
   /etc/init.d/network restart
   ```

   ​

## How to allow execution without prompting for password using sudo
1. Run `sudo visudo`
2. At the end of the file, add
	```
	<yourusername> ALL=NOPASSWD: <command1>, <command2>
	```


## Cross compilation
**Requirements:** 
* `mingw32-cross-gcc`: https://software.opensuse.org/download.html?project=windows%3Amingw%3Awin32&package=mingw32-cross-gcc

1. Compile with mingw32-gcc
	32bit

	```bash
	i686-w64-mingw32-gcc -o test.exe test.c
	```

	64bit

	```bash
	x86_64-w64-mingw32-gcc -o test.exe test.c
	```

**Resources:** https://prognotes.net/2015/04/compile-c-programs-for-windows-and-linux/
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTg3MDM0MzM0MSwtMTg4MzQ2Nzg1NF19
-->

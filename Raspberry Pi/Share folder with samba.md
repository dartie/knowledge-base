# Share folder with samba

1. Install samba 
    ```bash
    sudo apt update
    sudo apt-get install samba
    ```

1. Configuring Samba editing the samba configuration file `/etc/samba/smb.conf` 
    ```bash
    sudo nano /etc/samba/smb.conf
    ```

1. Change the workgroup name to the name of your workgroup. To find out the workgroup name on Windows 7 PC go to `Control Panel → System`. On a system running Windows 10 you can find this on `Settings → System → About`
You can also enable your Raspberry Pi as a WINS server by changing the entry wins support to `yes`
    ```
    workgroup = MYWORKGROUP
    wins support = yes
    ```
    * Replace `MYWORKGROUP` with the name of your workgroup. Save and exit the file.

1. Create shared folder
    ```bash
    mkdir /home/pi/shared
    pi@raspberrypi:~ $ chmod 777 /home/pi/shared
    ```

1. Edit the `/etc/samba/smb.conf` file and add the following lines. These lines define the behaviour of the shared folder so you can call them share definition.
    ```
    [pishare]
        comment = Pi Shared Folder
        path = /home/pi/shared
        browsable = yes
        guest ok = yes
        writable = yes
    ```
1. Save and exit the file. You need to restart samba for the changed to take effect.
    ```bash
    sudo /etc/init.d/smbd restart
    # or sudo service smbd restart
    ```

The following table explains the meaning of each entry in the share definition.

| [pishare]                  | This is the name of the share                                |
| -------------------------- | ------------------------------------------------------------ |
| comment = Pi Shared Folder | The text Pi Shared FOlder is the text that is displayed as Comments in shares detail view |
| path = /home/pi/shared     | Specifies the folder that contains the files to be shared    |
| browsable = yes            | Set this share to be visible when you run the net view command and also when you browse the network shares. |
| writable = yes             | Allows user to add/modify files and folders in this share. By the default samba shares are readonly |
| guest ok = yes             | Allows non authenticated users access the share              |

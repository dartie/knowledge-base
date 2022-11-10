# WD extra

## Copy speed
* [Before you pack up your WD and return it, let's talk about Copying Speeds! - My Cloud - WD Community](https://community.wd.com/t/before-you-pack-up-your-wd-and-return-it-lets-talk-about-copying-speeds/91887)


## sw
[My Cloud EX2](https://support-en.wd.com/app/products/product-detail/p/129#WD_downloads)

## desktop apps - obsolete
* WD My Cloud Desktop for Windows: http://downloads.wdc.com/nas/WDMyCloud_win.exe
* WD My Cloud Desktop for Mac: http://downloads.wdc.com/nas/WDMyCloud_mac.dmg

## Community apps
[WD community](https://wdcommunity.com/)

## extra apps
* [Repository with software worked on v4 firmware - My Cloud - WD Community](https://community.wd.com/t/repository-with-software-worked-on-v4-firmware/94532)

* [INSTALL ENTWARE ON WD MY CLOUD HOME (SSH ACCESS, NFS SERVER, OPKG install packages) - My Cloud Home Ideas - WD Community](https://community.wd.com/t/install-entware-on-wd-my-cloud-home-ssh-access-nfs-server-opkg-install-packages/228591)
* [INSTALL ENTWARE ON WD MY CLOUD HOME (SSH ACCESS, NFS SERVER, OPKG install packages) - My Cloud Home Ideas - WD Community](https://community.wd.com/t/install-entware-on-wd-my-cloud-home-ssh-access-nfs-server-opkg-install-packages/228591/74)

### via ssh
Doing the qnap / optware route is an unnecessary headache.

Just search for docker images built for armhf or armv7 for example although nzbget is an available app, you can also install it this way from the docker hub which has thousands of arm images. It’s as simple as using ssh and then executing this command
```bash
docker run -d
–name nzbget
–restart always
-p 6789:6789
-v /shares/Downloads/:/downloads
-v /shares/Downloads/.nzbget:/config
adrienbrault/armhf-nzbget
```

Now you’ll have your share named Downloads as the download path for nzbget and the config folder .nzbget in that folder as well. It’ll automatically restart with your system. No conversion of packages necessary, from there it is also easy enough to build a WD app using the guides outlined in the developer API so that it can be installed via the web interface.

Any app you want to install simply google
```bash
[app_name] armhf docker
```

## SSH

```bash
ssh sshd@nas
```

While I completely agree with all warnings above, here’s a few tips for power users (on a unix OS).

* Use a static IP on your NAS. Don’t lose time searching for its IP address.
If you need to look up the IP address anyway and are too lazy to login to your router, just scan your network for a Western Digital network interface.
    ```bash
    sudo nmap -sn 192.168.0.0/24  | grep Western -B2
    Nmap scan report for mycloudnas (192.168.0.101)
    Host is up (-0.10s latency).
    MAC Address: 00:14:EE:02:BD:FF (Western Digital Technologies)
    ```

* Add your NAS to your ssh config, usually located at ~/.ssh/config. Add a section like this
    ```bash
    Host wdnas
        Hostname 192.168.0.101         # or use the name of your nas
        User root                      # no need to type the user all the time
        HostKeyAlgorithms +ssh-dss     # only use this if required
    ```
* Now you can login with this short command
    ```bash
    ssh wdnas
    ```
* You can also copy files from and to your NAS
    ```bash
    scp wdnas:/var/log/mycloud.log ~/Documents
    scp -r ~/Documents/somedir  wdnas:/shares/SomeShare
    ```
* Passwords are lame. Use login by public key instead. You never have to type your password no more.
If you did update your ssh config, installation of your public key is as simple as this.
    ```bash
    ssh-copy-id wdnas
    ```
To keep your authorized keys after reboot, use a persistent home directory, e.g. by installing Entware from www.wdcommunity.com 46…
Enjoy!

## Third party apps
### MC
1. cd `/mnt/HD/HD_a2/` 
1. Run 
    ```bash
    wget http://en.zaoios.ru/soft/mc-wd-my-cloud-ex2.tar.gz
    ```
1. Extract with
    ```bash
    tar xvzf mc-wd-my-cloud-ex2.tar.gz
    ```
1. Copy `system` content into `/system`
    ```bash
    cp -RTa system/ /system
    ```
    for avoiding `/system/xbin/mc.real: not found` error
1. Set `TERM` variable
    ```bash
    export TERM=xterm
    ```
    for avoiding `Error opening terminal: xterm-256color.` error
1. Run `MC` 
    ```bash
    /mnt/HD/HD_a2/mc/mc
    ```

### nzbget
1. Download the package from [WD community](https://wdcommunity.com/)
1. Install it via `Apps` menu
1. Access to http://nas:6789/
    ```
    user: nzbget
    pwd : tegbzn6789
    ```

### git client
1. download git from EX2 repository - http://downloads.wdc.com/apps/WDMyCloudEX2/git/WDMyCloudEX2_git_1.40.bin 466
1. open it in HEX editor 
1. change `4B 69 6E 67 73 43 61 5A` (KingsCaZ) to `47 72 61 6E 64 54 65 5A` (GrandTeZ) at first string
1. Save it, and then do install it over `Install an app manually` link in AppStore tab.


### git server
1. Create repo folder and make group writeable
1. Create a user and add to group
1. Update user account to point to user share folder
1. Create SSH Key and copy .pub to /shares/user/.ssh/authorized_keys
1. Set permissions 
    ```
    cd /shares/user; chown user . ; chmod 0755 . ; chown -R user .ssh ; chmod go-rw -R .ssh
    ```
1. Add to `/mnt/HD/HD_a2/Nas_Prog/git/start.sh`:
    ```
    sed -ir 's/(AllowUsers .*)/\\1 alice bob/' /etc/ssh/sshd_config
    kill -HUP cat /var/run/sshd.pid
    ```
1. restart device
1. `git clone user@remote/shares/GitRepoPath/repo`

#### To just use the NAS as a file based git remote:
```
cd repos/my-project
git clone --bare . \\\\MyNAS\\repos\\my-project
git remote add origin \\\\MyNAS\\repos\\my-project
git push --set-upstream origin master
```


## Hack
[WD MyCloud Gen2 - Enable apps install tab + Apps! - My Cloud - WD Community](https://community.wd.com/t/wd-mycloud-gen2-enable-apps-install-tab-apps/177885)
Yeah, its “dirty hack”, but works well.

All files on my website:

Fox-exe.ru 2.1k or Anionix.ddns.net 1.0k
Mirror on Drive.google.com 24
More apps from 4.1k @hashashin
Plex updates from 166 @LaMpiR
Some other software at GitHub/Machsix 44 and Bintray.com 38 suggested by @bahusoid

1. Go to web interface
1. In “URL” field (In your browser) type:
    ```
    javascript:APP_INSTALL_FUNCTION=1; APPS_EULA=1; check_app_eula();
    ```
1. Alternative way: 
    Press [ctrl] + [shift] + [i], open “Console” tab, put this and hit [enter]:
    ```
    APP_INSTALL_FUNCTION=1; APPS_EULA=1; check_app_eula();
    ```
1. Go to Apps tab and install “WD_Crack” app.
1. Refresh page and install any other apps.




## How to Make Persistent System Changes (crontab, etc)

[How to Make Persistent System Changes (crontab, etc) - My Cloud Pro Series - WD Community](https://community.wd.com/t/how-to-make-persistent-system-changes-crontab-etc/201268/3)

The config.xml file is used in many examples shown below. Changing other system files is beyond the scope of this guide.

Most NAS options are stored in a file called config.xml and this file is stored in several locations. The contents of the file can be viewed by executing either of the following commands.
```bash
cat /usr/local/modules/default/config.xml
cat /etc/NAS_CFG/config.xml
```
Note the differences between the two files, where `/usr/local/modules/default/config.xml` appears to be a default basic configuration, possibly used as a fallback.

The `config.xml` file is also stored in a RAM database controlled by a Linux program called xmldbc.
```bash
xmldbc -h
```

```
Usage: xmldbc version 2 [OPTIONS]
  -h                     show this help message.
  -H                     show version number.
  -v                     verbose mode.
  -i                     ignore external function (like runtime).
  -g {node path}         get value from {node path}.
  -s {node path} {value} set  {value} in {node path}.
  -d {node path}         delete {node path}.
  -l {XML file}          reload XML file to database.
  -D {XML file}          dump database to XML file.
  -S {unix socket}       specify unix socket name, default is /var/run/xmldb_sock
  -A {ephp file}         embeded php parse.
  -V {name=value}        variable for ephp.
  -x {command}           set extended get/set command.
  -t {tag:sec:command}   schedule a timer.
  -k {tag}               kill timers by tag.
  -X {node field}        sorting.
  -I {node field}        insert row.
  -p {node path} {file}  print node to file.
  -r {XML file}          read file and insert to XMLDB.
```

The contents of the xmldbc database can be dumped to an XML file by executing the following command. Any destination path and filename may be used, as long as they do not conflict with existing system files.

```bash
xmldbc -D /tmp/xmldbc_test.xml
```

At first, I thought xmldbc may have been the actual source that was used to revert system changes, but a detailed examination of the source code revealed that it was not.

Further investigation revealed a number of “hidden” system partitions which are stored in eMMC flash memory. The partitions aren’t actually “hidden” per-se, but they are not easy to find unless you know what to look for. All things considered, I think this is a good thing because it prevents inexperienced users from accidentally bricking their NAS. A list of all active partitions can be viewed by executing the following command.

```bash
cat /proc/partitions
```

Pay particular attention to the partitions with a **mmcblk** name prefix. These are eMMC flash partitions, and they are read/write, so USE EXTREME CAUTION at all times. A more detailed and meaningful list can be seen by executing the following command.

```bash
blkid -o list
```

```
device                                   fs_type         label            mount point            UUID
-------------------------------------------------------------------------------------------------------------------------------------
/dev/loop0                               squashfs                         (in use)
/dev/loop1                               ext4                             (in use)               94c1bc4e-98f8-4aa6-b699-9d02c4c8f43d
/dev/loop3                               squashfs                         /usr/local/modules
/dev/sda1                                linux_raid_member                (in use)               1bd71974-bf36-f39b-bb4b-d7932c0a2b97
/dev/sda2                                ext4                             /mnt/HD/HD_a2          27bd93dd-a6b4-49d7-af45-9cfc6a1eef61
/dev/sda4                                ext4                             /mnt/HD_a4             da63156e-198b-43bb-8b37-beac6d94f44b
/dev/sdb1                                linux_raid_member                (in use)               1bd71974-bf36-f39b-bb4b-d7932c0a2b97
/dev/sdb2                                ext4                             /mnt/HD/HD_b2          d23c5cac-b202-465a-ba32-325e99672a1f
/dev/sdb4                                ext4                             /mnt/HD_b4             9fad9dd3-ddff-4e4d-9149-fe61787cdb50
/dev/sdc1                                linux_raid_member                (in use)               1bd71974-bf36-f39b-bb4b-d7932c0a2b97
/dev/sdc2                                ext4                             /mnt/HD/HD_c2          c4669438-f2df-4a99-a29b-17e772e7ceaa
/dev/sdc4                                ext4                             /mnt/HD_c4             ed1be8c5-d51f-4c35-b115-53676f2def74
/dev/mmcblk0                                                              (not mounted)
/dev/mmcblk0p1                           vfat            wdnas_efi        (not mounted)          9FE2-0840
/dev/mmcblk0p2                           ext4            wdnas_kernel     (not mounted)          c5d6e030-df55-4731-99e4-cbb2e5b771e2
/dev/mmcblk0p3                           ext4            wdnas_initramfs  (not mounted)          6bab9bea-2650-4944-84ea-a6fc4ba3fdd0
/dev/mmcblk0p4                           ext4            wdnas_image.cfs  (not mounted)          00035529-6b69-4fca-a0fd-cde0cd805a00
/dev/mmcblk0p5                           ext4            wdnas_rescue_fw  (not mounted)          8c54a8c2-9055-407c-bab1-5985d107fb3a
/dev/mmcblk0p6                           ext4            wdnas_config     (not mounted)          43eafe4c-2503-401e-b288-6cba67952ac9
/dev/mmcblk0p9                           ext4            wdnas_backup     (not mounted)          46330f66-5c9f-4862-9053-6ba3461685be
/dev/md0                                 swap                             <swap>                 b66719fa-c34d-44c1-9f1d-98e48a95ce05
/dev/mapper/docker-8:2-81788934-pool     ext4                             (not mounted)          94c1bc4e-98f8-4aa6-b699-9d02c4c8f43d
```

The following is a list of named system (mmcblk) eMMC flash partitions, preceded by descriptions.
```
GRUB Bootloader           wdnas_efi
Linux Kernel              wdnas_kernel
Initial RAM Filesystem    wdnas_initramfs
Squashfs Filesystem       wdnas_image.cfs
Rescue Firmware           wdnas_rescue_fw
Configuration Files       wdnas_config
Backup Files              wdnas_backup
```

Note that the mount point for each of the mmcblk partitions indicates if they are mounted. A list of mounted partitions can be viewed by executing the following command.


```bash
cat /proc/mounts
```

Before one can interact with a partition, it must be mounted. If a partition is already mounted, one simply needs to change to the directory it’s mounted to. To mount one of the **mmcblk** partitions, execute the following sequence of commands, one at a time. Note that a temporary directory named `/tmp/eMMC_flash` is used to prevent conflicts with existing system directories. In the following example the `/dev/mmcblk0p9` eMMC flash partition is mounted, where the path corresponding to any partition of interest can be used instead.

```bash
cd /
mkdir /tmp/eMMC_flash
mount /dev/mmcblk0p9 /tmp/eMMC_flash
cd /tmp/eMMC_flash
ls -l
```

Too make persistent changes (adding cron jobs, etc) to the **config.xml** file, first mount the appropriate partitions (if required), then make two copies of the file. One copy (**config_backup.xml**) is simply a backup in case changes need to be reverted, and the second copy (**config_edit.xml**) will be used for making changes. Note: On my WD PR4100 NAS `/usr/local/tmp_wdnas_config` is mounted to the `/dev/mmcblk0p6` device on system startup, and the system configuration files are stored in a subfolder named config. Mount points and paths may vary, depending on the NAS model and firmware version.

```bash
cp -f /usr/local/tmp_wdnas_config/config/config.xml /shares/Public/config_backup.xml
cp -f /usr/local/tmp_wdnas_config/config/config.xml /shares/Public/config_edit.xml
```

In the example shown below, note that I’ve added a new cron job named **cron_test**. Within the **config.xml** file is a `<crond></crond>` section, which contains all cron jobs which are added to the **crontab** at system startup.

```
<crond>
	<list>
		<count>9</count>
		<name id="1">stime</name>
		<name id="2">wd_crontab</name>
		<name id="3">app_get_info</name>
		<name id="4">recycle_bin_clear</name>
		<name id="5">chk_wfs_download</name>
		<name id="6">random_check</name>
		<name id="7">user_expire_chk</name>
		<name id="8">fw_available</name>
		<name id="9">cron_test</name>
	</list>
	<stime>
		<count>1</count>
		<item id="1">
			<method>3</method>
			<1>30</1>
			<2>2</2>
			<3>*</3>
			<4>*</4>
			<5>*</5>
			<run>/usr/sbin/stime&amp;</run>
		</item>
	</stime>
	<wd_crontab>
		<count>1</count>
		<item id="1">
			<method>3</method>
			<1>0</1>
			<2>3</2>
			<3>*</3>
			<4>*</4>
			<5>*</5>
			<run>wd_crontab.sh&amp;</run>
		</item>
	</wd_crontab>
	<app_get_info>
		<count>1</count>
		<item id="1">
			<method>3</method>
			<1>0</1>
			<2>4</2>
			<3>*</3>
			<4>*</4>
			<5>*</5>
			<run>auto_fw -a -c&amp;</run>
		</item>
	</app_get_info>
	<recycle_bin_clear>
		<count>1</count>
		<item id="1">
			<method>3</method>
			<1>0</1>
			<2>0</2>
			<3>*</3>
			<4>*</4>
			<5>*</5>
			<run>auto_clear_recycle_bin.sh &amp;</run>
		</item>
	</recycle_bin_clear>
	<chk_wfs_download>
		<count>1</count>
		<item id="1">
			<method>3</method>
			<1>30</1>
			<2>3</2>
			<3>*</3>
			<4>*</4>
			<5>*</5>
			<run>/usr/sbin/chk_wfs_download&amp;</run>
		</item>
	</chk_wfs_download>
	<random_check>
		<item id="1">
			<method>3</method>
			<1>0</1>
			<2>0</2>
			<3>*</3>
			<4>*</4>
			<5>*</5>
			<run>random_check -s &amp;</run>
		</item>
	</random_check>
	<user_expire_chk>
		<item id="1">
			<method>3</method>
			<1>0</1>
			<2>0</2>
			<3>*</3>
			<4>*</4>
			<5>*</5>
			<run>expire.sh</run>
		</item>
	</user_expire_chk>
	<fw_available>
		<item id="1">
			<method>3</method>
			<1>52</1>
			<2>18</2>
			<3>*</3>
			<4>*</4>
			<5>*</5>
			<run>auto_fw -c 1 &amp;</run>
		</item>
	</fw_available>
	<cron_test>
		<item id="1">
			<method>3</method>
			<1>*</1>
			<2>*</2>
			<3>*</3>
			<4>*</4>
			<5>*</5>
			<run>date >> /shares/Public/test.txt &amp;</run>
		</item>
	</cron_test>
</crond>
```


To add a new cron job, first edit the `<list></list>` section as follows, using any name you want for the new cron job, as long as it’s unique. Note that the `id=""` attributes can only contain numbers, and each number must be unique. Also, the number within the `<count></count>` element should be changed to reflect the number of cron jobs contained in the `<list></list>` section. In this case, there are 9 cron jobs, so the count is 9.

```
<list>
	<count>9</count>
	<name id="1">stime</name>
	<name id="2">wd_crontab</name>
	<name id="3">app_get_info</name>
	<name id="4">recycle_bin_clear</name>
	<name id="5">chk_wfs_download</name>
	<name id="6">random_check</name>
	<name id="7">user_expire_chk</name>
	<name id="8">fw_available</name>
	<name id="9">cron_test</name>
</list>
```

Next, add a new section to the end of the <crond></crond> section as follows. Note that the outer element name must **EXACTLY** match the name element value used in the `<list></list>` section. In this case, the outer element name is `<cron_test></cron_test>`.

```
<cron_test>
	<item id="1">
		<method>3</method>
		<1>*</1>
		<2>*</2>
		<3>*</3>
		<4>*</4>
		<5>*</5>
		<run>date >> /shares/Public/test.txt &amp;</run>
	</item>
</cron_test>
```

The exact purpose of the <method></method> element is currently unknown. The numbered elements (`<1></1>`, `<2></2>`. etc) represent the 5 fields used by crontab for specifying time intervals. For more information about crontab time intervals, see: [[GUIDE] Crontab Demystified](https://community.wd.com/t/guide-crontab-demystified/201588)

In the examples shown above, the text within the `<run></run>` element is the command or script to be executed. The & (ampersand) character at the end of a shell command is known as job control. The & (ampersand) character informs the shell to put the command in the background, allowing parallel commands to be run. The & (ampersand) character is reserved as a special character in XML files, so it must be represented by `&amp;` at all times.

For example, the following command will append the current date to a text file in the “Public” share folder. The & (ampersand) character at the end of the line isn’t strictly necessary, but I’ve included it so I could explain it’s purpose and how to use it within XML files.

```bash
date >> /shares/Public/test.txt &
```

Shell scripts contained in text files, or even binary programs can also be executed by a cron job. However, they must be saved in a location which is not periodically refreshed along with the root filesystem. eMMC flash partitions can be used for this purpose, but one must be **EXTREMELY CAREFUL** to not overwrite any existing files.

For example, if the shell command in the examples shown above were contained in a text file, the resulting `<cron_test></cron_test>` XML `<run></run>` command line might resemble the following.

```
<run>/usr/local/tmp_wdnas_config/config/cron_test.sh &amp;</run>
```

When finished making changes, simply save the **config.xml** file, then copy it to the appropriate location, replacing the existing **config.xml** file.

```bash
cp -f /shares/Public/config_flash.xml /usr/local/tmp_wdnas_config/config/config.xml
```

One should be **ABSOLUTELY CERTAIN** that the **config.xml** file does not contain any typos or errors **BEFORE** replacing the existing **config.xml** file. Note that standard XML parsers or validation services may report the **config.xml** XML file as being malformed because the developers chose to use element names (`<1></1>`, `<2></2>`. etc) which violate the XML syntax rules. The NAS must be rebooted from the dashboard for changes to take effect.

After the NAS is finished rebooting, verify that the new cron job has been added to the **crontab** by executing the following command.

```bash
crontab -l
```

When finished, **ALWAYS UNMOUNT eMMC FLASH PARTITIONS**, as shown in the following example. Either the partition or the mount point may be used to unmount a partition. Note: Partitions mounted by the system should **NOT** be unmounted.

```bash
umount /tmp/eMMC_flash
```

Again, **USE EXTREME CAUTION** because making changes to any of the system files stored in the eMMC flash partitions can very easily **BRICK YOUR NAS**. You have been warned… multiple times.


## Left
- [ ] python3
- [ ] sonarr
- [ ] wake on lan
- [ ] 

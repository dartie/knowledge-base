# NSA320

## Install Debian
**Resources:**
* [serial instructions](http://mud-slide.blogspot.com/2013/12/installing-linux-on-zyxel-nsa-320-part_722.html)
* [cable](https://www.amazon.it/CMYKZONE-Programmazione-Facilmente-Connettori-Dispositivi/dp/B07LBD7C5D/ref=sr_1_2?__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=debug+cable&qid=1582275817&sr=8-2)
* [steps](https://forum.doozan.com/read.php?3,12381)
* [fix LEDs](https://forum.doozan.com/read.php?2,65899)
* [OMV on Zyxel NSA320 ? - My NAS Build - openmediavault](https://forum.openmediavault.org/index.php/Thread/4271-OMV-on-Zyxel-NSA320/?postID=77832#post77832)

## Steps
Basic Debian buster Kirkwood rootfs for most Kirwood plugs:

- tarball size: 209M
- install size: 536M
- The init system used in this rootfs is sysvinit . To boot with systemd, see note 2 below.
- Installed packages: nano, avahi, ntp, busybox-syslogd (log to RAM), htop, isc-dhcp-client, dialog, bzip2, nfs server/client, iperf, ethtool, sysvinit-core, sysvinit, sysvinit-utils, u-boot-tools, and mtd-utils.
- see LED controls in /etc/rc.local, and /etc/init.d/halt
- see some useful aliases in /root/.profile
- root password: root

1. Download at Dropbox: [Debian-5.2.9-kirkwood-tld-1-rootfs-bodhi.tar.bz2](https://www.dropbox.com/s/pa2cbg93qgcnp8w/Debian-5.2.9-kirkwood-tld-1-rootfs-bodhi.tar.bz2)
    ```
    md5:
    cd8ad170aa1a9fdc2a0a1c43ab1c0721
    sha256:
    8ccbbced367b4c2bf3728262e882f8232aff0fecd1c0c767219a0cab49a0b9bf
    ```

    And remember to check the hash of what you download, as always.

    Installation can be done on any Linux box, with a fresh USB drive (SD card or HDD would work fine too).

    > Note: all steps below must be done while logging in as **root** user (**not sudo**). If you are not the root user then don't continue, because the rootfs will not work.

1. Format a new USB drive with a single Ext3 partition, and label it `rootfs`. If you are running the latest U-Boot for Kirkwood then you can use Ext4.

2. Mount the drive on a Linux box. cd to top level directory and extract it. It is assuming the USB drive is mounted at `/media/sdb1`
    ```
    cd /media/sdb1 
    tar -xjf Debian-5.2.9-kirkwood-tld-1-rootfs-bodhi.tar.bz2
    ```
3. Adjust fstab (optional).

    Edit `/media/sdb1/etc/fstab` entry for root device to match the rootfstype of your rootfstype if you use Ext4 or Ext2. However, you can keep it as is without problem in booting since the kernel will figure out which file system the rootfs was formatted.
    ```
    LABEL=rootfs    /               ext3    noatime,errors=remount-ro 0 1
    ```
4. Create uImage with embedded DTB for booting with older u-boots (2012 or earlier). 
    > Do not do this step if you have installed [the latest U-Boot for Kirkwood](http://forum.doozan.com/read.php?3,12381) (or are installing this u-boot at the same time).

    Please replace **kirkwood-goflexnet.dtb** below with the correct DTB name for your box (see the folder `/media/sdb1/boot/dts` for the exact spelling of your Kirkwood box name).

    Generate the uImage with DTB embedded inside:
    ```
    cd /media/sdb1/boot
    cp -a zImage-5.2.9-kirkwood-tld-1  zImage.fdt
    cat dts/kirkwood-goflexnet.dtb  >> zImage.fdt
    mv uImage uImage.orig
    mkimage -A arm -O linux -T kernel -C none -a 0x00008000 -e 0x00008000 -n Linux-5.2.9-kirkwood-tld-1 -d zImage.fdt  uImage
    sync
    ```

    If your Linux box does not have mkimage, then install it
    ```bash
    apt-get install u-boot-tools
    ```
5. Done. Take this USB rootfs to your plug and cold start. After booted into Debian, see Note1 and Note2 below. It is very important that you do Note1 steps to secure your box.

### Note1:

After logging in this rootf the first time, remember to generate new SSH key to make it your own unique rootfs. And also update your rootfs to get the latest Debian package security updates:
```bash
rm /etc/ssh/ssh_host*
ssh-keygen -A

apt-get update
apt-get upgrade
```
> Warning: 

Watch the apt-get upgrade progress. If the apt-get upgrade results in a new initramfs, the log would shows this message:
```bash
update-initramfs: Generating /boot/initrd.img-5.2.9-kirkwood-tld-1
```

Then you need to regenerate the uInitrd boot file:
```bash
cd /boot
mkimage -A arm -O linux -T ramdisk -C gzip -a 0x00000000 -e 0x00000000 -n initramfs-5.2.9-kirkwood-tld-1 -d initrd.img-5.2.9-kirkwood-tld-1 uInitrd
```

### Note2:
To boot with systemd, add parameter `init=/bin/systemd` to your u-boot env bootargs (beware that in later Debian distribution, the location of systemd binary might have changed).

- For example,
    ```bash
    fw_setenv set_bootargs 'setenv bootargs console=ttyS0,115200 root=LABEL=rootfs rootdelay=10 $mtdparts init=/bin/systemd'
    ```
- Or, if you are booting with my [latest u-boot images](http://forum.doozan.com/read.php?3,12381) you can also use the uEnv.txt capability to do this. In the default envs, custom_params is a variable that allows you to add extra bootargs. So add the following line to uEnv.txt:

    ```bash
    custom_params=init=/bin/systemd
    ```

If that's still not possible to run systemd, you might want to install it again:
```bash
apt-get install systemd
```


## Troubleshooting
### Kernel panic
[Nsa320 Kernelpanic](https://forum.doozan.com/read.php?3,95709)

You should not do Step 4. It is for older uboot (2012 or earlier). You are booting the new u-boot now.

```
Quote

4. Create uImage with embedded DTB for booting with older u-boots (2012 or earlier). Do not do this step if you have installed the latest U-Boot for Kirkwood (or are installing this u-boot at the same time).

Please replace kirkwood-goflexnet.dtb below with the correct DTB name for your box (see the folder /media/sdb1/boot/dts for the exact spelling of your Kirkwood box name).

Generate the uImage with DTB embedded inside:
cd /media/sdb1/boot
cp -a zImage-5.2.9-kirkwood-tld-1 zImage.fdt
cat dts/kirkwood-goflexnet.dtb >> zImage.fdt
mv uImage uImage.orig
mkimage -A arm -O linux -T kernel -C none -a 0x00008000 -e 0x00008000 -n Linux-5.2.9-kirkwood-tld-1 -d zImage.fdt uImage
sync
```

So mount the USB rootfs on another Linux box. Assuming it is mounted at /media/sdb1.

```bash
cd /media/sdb1/boot
cp -a uImage uImage.nsa320_with_DTB
cp -a uImage.orig uImage
sync
```
And then bring it back to the NSA320. Boot again.




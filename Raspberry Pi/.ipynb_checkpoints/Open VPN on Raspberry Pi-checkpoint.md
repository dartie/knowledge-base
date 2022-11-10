# Open VPN on Raspberry Pi

## Install OpenVPN

### Enable internet and grant access to the main subnet to all vpn clients
```bash
# vpn clients ping main network clients
sudo iptables -t nat -D PREROUTING -s 10.8.0.0/24 -i eth0 -j MASQUERADE

# main network clients ping vpn clients
sudo iptables -A FORWARD -i tun0 -s 10.8.0.0/24 -d 192.168.1.0/24 -j ACCEPT
```

```bash
# vpn client can ping main network clients
sudo iptables -t nat -A POSTROUTING -s 10.8.0.0/24 ! -d 10.8.0.0/24 -j MASQUERADE
```

### enable forwarding in sysctl
```bash
sudo sysctl -w net.ipv4.ip_forward=1
```

## Configure via file
1. Edit file `/etc/openvpn/server.conf`
    ```bash
    sudo nano /etc/openvpn/server.conf
    ```



## Install the GUI

1. Run 
    ```bash
    sudo nano /etc/apt/sources.list
    ```
1. Add line:
    ```
	deb http://mirrordirector.raspbian.org/raspbian jessie main contrib non-free rpi
    ```
1. Run:
    ```bash
	sudo apt-get update
	sudo apt-get upgrade
	sudo apt-get install git apache2 php5 libapache2-mod-php5 php5-mcrypt expect geoip-bin
    ```
1. Edit `/etc/apache2/apache2.conf`
    ```bash
    sudo nano /etc/apache2/apache2.conf
    ```
1. Replace `${APACHE_RUN_USER}` and `${APACHE_RUN_GROUP}` with `pi`
1. Run the command:
    ```
    cd /var/www/html
    sudo chown pi:pi -R /var/www
    cd /var/www/html
    git clone https://github.com/AaronWPhillips/pivpn-gui
    ```


## Commands
```shell
systemctl status openvpn@server.service
```


## Troubleshooting
* Message `Job for openvpn@server.service failed because the control process exited with error code.`



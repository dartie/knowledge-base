# Maintainance


 - [pi-hole](#pi-hole)   
 - [qbittorrent](#qbittorrent)   
 - [pivpn](#pivpn)   
 - [iPynb](#ipynb)   
 - [motion](#motion)   
 - [sonarr](#sonarr)   
- [Overall info](#overall-info)  
 - [startup](#startup)   


## pi-hole
**Port:** 80


## qbittorrent
**Port:** 8101

```bash
sudo systemctl status qbittorrent
sudo systemctl start qbittorrent
sudo systemctl restart qbittorrent
sudo systemctl stop qbittorrent
```


## pivpn
**Port:** 1194

`/etc/openvpn/server.conf`

```bash
sudo service openvpn status
sudo service openvpn start
sudo service openvpn stop
```


## iPynb
**Port:** 8102

`/etc/systemd/system/jupyter.service`

```bash
sudo systemctl daemon-reload
sudo systemctl start jupyter.service
```

## motion
**Port: (  web )** 8110

**Port: (stream)** 8111

`/etc/motion/motion.conf`

```bash
sudo systemctl status motion
sudo systemctl start motion
sudo systemctl restart motion
sudo systemctl stop motion
```

## sonarr
**Port:** 8989
```bash
sudo mount -t cifs -o username=dartie,uid=1000,nounix //nas/Public/TVSeries /mnt/nas/tvseries
```


# Overall info
## startup
```
# Sonarr : map nas drive for tvseries
sudo mount -t cifs -o username=dartie,uid=1000,nounix //nas/Public/TVSeries /mnt/nas/tvseries

# pivpn : enable mask
sudo iptables -t nat -D PREROUTING -s 10.8.0.0/24 -i eth0 -j MASQUERADE
```

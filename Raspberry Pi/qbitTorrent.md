# qbitTorrent

## Prerequisites
* A Raspberry pi setup, with Raspian OS with Terminal and some text editor (nano etc.).

* Static IP Setup.

## Setup
1. Type the following to update your repo and install qbittorrent
    ```bash
    sudo apt-get update && sudo apt-get install qbittorrent-nox
    ```
1. Now let’s add a user
    ```bash
    sudo adduser qbtuser
    ```
1. Set a password for qbtuser

1. Let’s create the service file, Type (I’m using nano, you can use any text editor you like)
    ```bash
    sudo nano /etc/systemd/system/qbittorrent.service
    ```
1. Copy and paste the following into the file that we are creating:
    ```
    [Unit]
    Description=qBittorrent Daemon Service
    After=network.target

    [Service]
    User=qbtuser
    ExecStart=/usr/bin/qbittorrent-nox --webui-port=8080

    [Install]
    WantedBy=multi-user.target
    Save file and exit out of the editor.
    ```
1. Let’s check if everything is fine
    ```bash
    sudo systemctl daemon-reload
    sudo su qbtuser
    qbittorrent-nox
    ```
1. You should be able to point a web browser (on the same network) to the IP of your server: http://ip-of-server:8080 and log in with:
    ```
    User: admin
    Password: adminadmin
    ```
1. Press `Ctrl + C` to exit out.

1. Type `exit` to exit out of qbtuser.

1. Check the status of the service to make sure everything is working
    ```bash
    sudo systemctl start qbittorrent
    sudo systemctl status qbittorrent
    ```
1. Quit out of the above screen by pressing `q`.

1. Now to start the service to run every time on startup.
    ```
    sudo systemctl enable qbittorrent
    ```
    and you should see:
    ```
    Created symlink from /etc/systemd/system/multi-user.target.wants/qbittorrent.service to /etc/systemd/system/qbittorrent.service.
    ```

1. [OPTIONAL] Disable account login for SSH (for security reasons), this account will still be accessible locally.
    ```bash
    sudo usermod -s /usr/sbin/nologin qbtuser
    ```
    
## General commands
* Starting qBittorrent
    ```bash
    sudo systemctl start qbittorrent
    ```
* Stopping qBittorrent:
    ```bash
    sudo systemctl stop qbittorrent
    ```
* Check status:
    ```bash
    sudo systemctl status qbittorrent
    ```


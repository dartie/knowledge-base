# Sonarr

## Sonarr on Raspberry Pi 3

1. Update packages
    ```
    sudo apt-get update
    ```
1. Upgrade packages
    ```
    sudo apt-get upgrade -y
    ```

1. Install `libmono-cil-dev`
    ```
    sudo apt-get install libmono-cil-dev -y
    ```

> If you get a `libmono-cil-dev will not be installed you hold broken packages`, do this extra step
> 
> Lower the pin preference
> ```bash
> sudo nano /etc/apt/preferences
> ```
> Add these lines, if you are on wheezy replace `jessie` with `wheezy` or `buster` (use `lsb_release -a` for detecting the distro)
> ```
> Package: *
> Pin: release n=jessie
> Pin-Priority: 998
> ```
> Save with `Ctrl+X`, `Y` and Enter
> 
> Now update packages and install
> ```bash
> sudo apt-get update
> sudo apt-get install libmono-cil-dev -y
> ```


### Install Mono 3.10 Raspberry Pi armhf Package
1. Download the precompiled mono 3.10 arm deb package
    ```bash
    wget http://sourceforge.net/projects/bananapi/files/mono_3.10-armhf.deb
    ```
    > If Sourceforge is down you can use a mirror (thanks Hermi)
    > ```bash
    > wget http://www.frickelzeugs.de/mono_3.10-armhf.deb
    > ```
    > Here is yet another mono mirror
    > ```bash
    > wget https://www.dropbox.com/s/k6ff6s9bfe4mfid/mono_3.10-armhf.deb
    > ```

1. Install the Mono 3.10 package for Raspbian
    ```bash
    sudo dpkg -i mono_3.10-armhf.deb
    ```
    
1. You can check your mono version
    ```bash
    mono --version
    ```

It should read

```
Mono JIT compiler version 3.10.0 (mono-3.10.0-branch/ce003f4 Wed Nov 26 20:10:31 CET 2014)
Copyright (C) 2002-2014 Novell, Inc, Xamarin Inc and Contributors. www.mono-project.com
```

> Even if it doesn’t show 3.10.0 don’t worry, there is a workaround for the init.d script


### Install Sonarr Raspberry Pi
1. Enable apt-get to install from https sources or you will get this error
    ```
    The method driver `/usr/lib/apt/methods/https` could not be found.
    To solve it install the https package
    ```

    ```bash
    sudo apt-get install apt-transport-https -y --force-yes
    ```

1. Add sources to install Sonarr on Raspbian
    ```bash
    sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys FDA5DFFC
    echo "deb https://apt.sonarr.tv/ master main" | sudo tee -a /etc/apt/sources.list.d/sonarr.list
    ```

1. Update packages
    ```bash
    sudo apt-get update
    ```

1. Install Sonarr (NzbDrone)
    ```bash
    sudo apt-get install nzbdrone sqlite3-dev -y
    ```

1. Take ownership of the Sonarr installation so updates will work properly
    ```bash
    sudo chown -R pi:pi /opt/NzbDrone
    ```
    
### Autostart Sonarr
1. Create the `init.d` script file
    ```bash
    sudo nano /etc/init.d/nzbdrone
    ```
1. Paste this long code, change `DAEMON` to `DAEMON=/usr/local/bin/mono` if mono shows 3.2.8 instead of 3.10
    ```
    #! /bin/sh
    ### BEGIN INIT INFO
    # Provides: NzbDrone
    # Required-Start: $local_fs $network $remote_fs
    # Required-Stop: $local_fs $network $remote_fs
    # Should-Start: $NetworkManager
    # Should-Stop: $NetworkManager
    # Default-Start: 2 3 4 5
    # Default-Stop: 0 1 6
    # Short-Description: starts instance of NzbDrone
    # Description: starts instance of NzbDrone using start-stop-daemon
    ### END INIT INFO

    ############### EDIT ME ##################
    # path to app
    APP_PATH=/opt/NzbDrone

    # user
    RUN_AS=pi

    # path to mono bin
    DAEMON=$(which mono)

    # Path to store PID file
    PID_FILE=/var/run/nzbdrone/nzbdrone.pid
    PID_PATH=$(dirname $PID_FILE)

    # script name
    NAME=nzbdrone

    # app name
    DESC=NzbDrone

    # startup args
    EXENAME="NzbDrone.exe"
    DAEMON_OPTS=" "$EXENAME

    ############### END EDIT ME ##################

    NZBDRONE_PID=`ps auxf | grep NzbDrone.exe | grep -v grep | awk '{print $2}'`

    test -x $DAEMON || exit 0

    set -e

    #Look for PID and create if doesn't exist
    if [ ! -d $PID_PATH ]; then
    mkdir -p $PID_PATH
    chown $RUN_AS $PID_PATH
    fi

    if [ ! -d $DATA_DIR ]; then
    mkdir -p $DATA_DIR
    chown $RUN_AS $DATA_DIR
    fi

    if [ -e $PID_FILE ]; then
    PID=`cat $PID_FILE`
    if ! kill -0 $PID > /dev/null 2>&1; then
    echo "Removing stale $PID_FILE"
    rm $PID_FILE
    fi
    fi

    echo $NZBDRONE_PID > $PID_FILE

    case "$1" in
    start)
    if [ -z "${NZBDRONE_PID}" ]; then
    echo "Starting $DESC"
    rm -rf $PID_PATH || return 1
    install -d --mode=0755 -o $RUN_AS $PID_PATH || return 1
    start-stop-daemon -d $APP_PATH -c $RUN_AS --start --background --pidfile $PID_FILE --exec $DAEMON -- $DAEMON_OPTS
    else
    echo "NzbDrone already running."
    fi
    ;;
    stop)
    echo "Stopping $DESC"
    echo $NZBDRONE_PID > $PID_FILE
    start-stop-daemon --stop --pidfile $PID_FILE --retry 15
    ;;

    restart|force-reload)
    echo "Restarting $DESC"
    start-stop-daemon --stop --pidfile $PID_FILE --retry 15
    start-stop-daemon -d $APP_PATH -c $RUN_AS --start --background --pidfile $PID_FILE --exec $DAEMON -- $DAEMON_OPTS
    ;;
    status)
    # Use LSB function library if it exists
    if [ -f /lib/lsb/init-functions ]; then
    . /lib/lsb/init-functions
    if [ -e $PID_FILE ]; then
    status_of_proc -p $PID_FILE "$DAEMON" "$NAME" && exit 0 || exit $?
    else
    log_daemon_msg "$NAME is not running"
    exit 3
    fi

    else
    # Use basic functions
    if [ -e $PID_FILE ]; then
    PID=`cat $PID_FILE`
    if kill -0 $PID > /dev/null 2>&1; then
    echo " * $NAME is running"
    exit 0
    fi
    else
    echo " * $NAME is not running"
    exit 3
    fi
    fi
    ;;
    *)
    N=/etc/init.d/$NAME
    echo "Usage: $N {start|stop|restart|force-reload|status}" >&2
    exit 1
    ;;
    esac

    exit 0
    ```
    
    `Ctrl+X`, `Y` and `Enter` to save

1. Make the Sonarr `init.d` script executable
    ```bash
    sudo chmod +x /etc/init.d/nzbdrone
    ```
1. Update the Sonarr init.d to start on boot
    ```bash
    sudo update-rc.d /etc/init.d/nzbdrone defaults 98
    ```
    > If the above command gives an error try
    > ```
    > sudo update-rc.d nzbdrone defaults 98
    > ```
    
1. Reboot and then configure Sonarr.



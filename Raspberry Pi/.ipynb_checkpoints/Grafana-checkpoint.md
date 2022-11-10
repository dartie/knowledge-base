* https://techexpert.tips/grafana/grafana-monitoring-snmp-devices/
* http://codedemigod.com/posts/monitoring-my-servers/
* https://grafana.com/grafana/dashboards/928


# Influxdb
* https://pimylifeup.com/raspberry-pi-influxdb/
* https://www.circuits.dk/install-grafana-influxdb-raspberry/
* https://simonhearne.com/2020/pi-influx-grafana/
* https://docs.influxdata.com/influxdb/v1.7/write_protocols/line_protocol_tutorial

## Installation
```bash
wget https://dl.influxdata.com/influxdb/releases/influxdb_2.0.0-beta.7_linux_arm64.tar.gz
tar xvzf influxdb_2.0.0-beta.7_linux_arm64.tar.gz
sudo cp influxdb_2.0.0-beta.7_linux_arm64/{influx,influxd} /usr/local/bin/
```

```bash
sudo apt update
sudo apt upgrade -y
wget -qO- https://repos.influxdata.com/influxdb.key | sudo apt-key add -

echo "deb https://repos.influxdata.com/debian buster stable" | sudo tee /etc/apt/sources.list.d/influxdb.list

sudo apt update
sudo apt install influxdb
sudo systemctl unmask influxdb
sudo systemctl enable influxdb
sudo systemctl start influxdb
```

# Grafana

## Installation
https://grafana.com/docs/grafana/latest/installation/debian/#apt-repository

```bash
echo "deb https://packages.grafana.com/oss/deb stable main" | sudo tee -a /etc/apt/sources.list.d/grafana.list 
# or for beta: echo "deb https://packages.grafana.com/oss/deb beta main" | sudo tee -a /etc/apt/sources.list.d/grafana.list 

sudo apt-get install -y adduser libfontconfig1
wget https://dl.grafana.com/oss/release/grafana_6.7.1_armhf.deb
sudo dpkg -i grafana_6.7.1_armhf.deb

sudo systemctl daemon-reload
sudo systemctl start grafana-server
sudo systemctl status grafana-server
sudo systemctl enable grafana-server.service
```

> Start the server with init.d
> To start the service and verify that the service has started:
> ```bash
> sudo service grafana-server start
> sudo service grafana-server status
> ```

1. Configure the Grafana server to start at boot:
  ```bash
  sudo update-rc.d grafana-server defaults
  ```
  
## Troubleshooting

### Black page at login
The version installed is obsolete, delete it and install the latest with the official packages (see above)

### paste subprocess was killed by signal (Broken pipe)
```bash
sudo apt-get remove grafana-data
sudo apt-get purge grafana-data
```

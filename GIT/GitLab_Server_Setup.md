Link: https://linoxide.com/linux-how-to/install-gitlab-on-ubuntu-fedora-debian/

1. Run the terminal as ```su```
1. Run
```bash
# install required packages
apt-get install curl openssh-server ca-certificates postfix

# start the sshd and postfix services
systemctl start sshd postfix
systemctl enable sshd postfix
```

1. Download package from here: https://packages.gitlab.com/gitlab/gitlab-ee
1. Install package
```shell
dpkg -i gitlab-ee_9.5.9-ee.0_amd64.deb 
```

1. Configure Gitlab
```bash
gitlab-ctl reconfigure
```
1. Configure Firewall allowing port 80 (use **Firewalld** or **iptables** )

   * iptables
```shell
iptables -A INPUT -p tcp -m tcp --dport 80 -j ACCEPT
/etc/init.d/iptables save
```
   * Firewalld
```shell
firewall-cmd --permanent --add-service=http
firewall-cmd --reload
```
1. Access to GitLab via 127.0.0.1 and create the user 


# Enable SSL 
1. Generate Public key
````shell
ssh-keygen -t rsa -C "your.email@example.com" -b 4096
````
> ``` ssh-keygen -t rsa -C "dartie90@gmail.com" -b 4096```

1. Get the key content
````shell
cat ~/.ssh/id_rsa.pub
````

1. Open http://127.0.0.1/profile/keys

1. Paste the string into the **Key** box

1. Give a Title and **Add Key**

1, 



# Enable SSL
## link: 
* https://www.bonusbits.com/wiki/HowTo:Setup_HTTPS_for_Gitlab
* https://www.bonusbits.com/wiki/HowTo:Generate_Self-Signed_SSL_Certificate_with_OpenSSL

1. Edit file ````/etc/gitlab/gitlab.rb````
1. Change ````external_url````  in ````external_url 'https://gitlab.domain.com'````
> ``` external_url 'https://gitlab.dartie.com' ```


1. Add ````nginx['redirect_http_to_https'] = true````
1. Add ````ci_nginx['redirect_http_to_https'] = true````

1. Create Certificate Folder
````shell
sudo mkdir -p /etc/gitlab/ssl
sudo chmod 700 /etc/gitlab/ssl
````
1.  Create Private Key
```shell
sudo openssl genrsa -des3 -out /etc/gitlab/ssl/gitlab.domain.com.key 2048
```
> ````sudo openssl genrsa -des3 -out /etc/gitlab/ssl/gitlab.dartie.key 2048````

1. Enter **Pass phrase** and remember for later

1. Create a Certificate Request
````shell
sudo openssl req -new -key /etc/gitlab/ssl/gitlab.domain.com.key -out /etc/gitlab/ssl/gitlab.domain.com.csr
````
> ````sudo openssl req -new -key /etc/gitlab/ssl/gitlab.dartie.key -out /etc/gitlab/ssl/gitlab.dartie.csr````

1. Remove
````shell
sudo cp -v /etc/gitlab/ssl/gitlab.domain.com.{key,original}
sudo openssl rsa -in /etc/gitlab/ssl/gitlab.domain.com.original -out /etc/gitlab/ssl/gitlab.domain.com.key
sudo rm -v /etc/gitlab/ssl/gitlab.domain.com.original
````
> ````sudo cp -v /etc/gitlab/ssl/gitlab.dartie.{key,original}````
> ````sudo openssl rsa -in /etc/gitlab/ssl/gitlab.dartie.original -out /etc/gitlab/ssl/gitlab.dartie.key````
> ````sudo cp -v /etc/gitlab/ssl/gitlab.dartie.{key,original}````

1. Create Certificate
````shell
sudo openssl x509 -req -days 1460 -in /etc/gitlab/ssl/gitlab.domain.com.csr -signkey /etc/gitlab/ssl/gitlab.domain.com.key -out /etc/gitlab/ssl/gitlab.domain.com.crt
````
> ```` sudo openssl x509 -req -days 1460 -in /etc/gitlab/ssl/gitlab.dartie.csr -signkey /etc/gitlab/ssl/gitlab.dartie.key -out /etc/gitlab/ssl/gitlab.dartie.crt ````

1. Remove Certificate Request File
````shell
sudo rm -v /etc/gitlab/ssl/gitlab.domain.com.csr
````
> ```sudo rm -v /etc/gitlab/ssl/gitlab.dartie.csr```

1. Set file permissions
````shell
sudo chmod 600 /etc/gitlab/ssl/gitlab.domain.com.*
````
> ````sudo chmod 600 /etc/gitlab/ssl/gitlab.dartie.*````

1. Run Gitlab configuration
````shell
sudo gitlab-ctl reconfigure
````

1. Restart services
````shell
sudo gitlab-ctl restart
````

1. Allow port https (443)
````shell
iptables -A INPUT -p tcp -m tcp --dport 443 -m state --state NEW,ESTABLISHED -j ACCEPT
````

1. ​

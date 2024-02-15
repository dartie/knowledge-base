# Puppet

- [Puppet](#puppet)
  - [Download Puppet Enterprise](#download-puppet-enterprise)
  - [Requirements](#requirements)
    - [Open the required firewall ports](#open-the-required-firewall-ports)
  - [Installation](#installation)
- [Control Repo](#control-repo)
  - [Setup Control Repo](#setup-control-repo)
    - [1. Create a project for the Control Repo on your git server](#1-create-a-project-for-the-control-repo-on-your-git-server)
    - [2. Clone template Control Repo and push to your git server](#2-clone-template-control-repo-and-push-to-your-git-server)
    - [3. Setup SSH keys on the Puppet Enterprise server](#3-setup-ssh-keys-on-the-puppet-enterprise-server)
    - [4. Set a Deploy Key on the Control Repo](#4-set-a-deploy-key-on-the-control-repo)
    - [5. Enable Code Manager on Puppet Enterprise](#5-enable-code-manager-on-puppet-enterprise)
    - [6. Deploy the Control Repo to Puppet Enterprise](#6-deploy-the-control-repo-to-puppet-enterprise)
    - [7. Enable a webhook for auto sync of your Control Repo updates](#7-enable-a-webhook-for-auto-sync-of-your-control-repo-updates)
    - [8. Add some useful modules to your Puppet Enterprise installation](#8-add-some-useful-modules-to-your-puppet-enterprise-installation)


## Download Puppet Enterprise

1. Login to your CentOS VM (Referenced in [PE requirements](https://puppet-enterprise-guide.com/theory/pe-prequisites.html#1-puppet-enterprise)).
1. If you are not logged in as the root account, elevate to root.
    ```bash
    sudo -i
    ```
1. You’ll be using wget to download the Puppet Enterprise tarball so you’ll need to install it first.
    ```bash
    yum install -y wget
    ```
1. Now, use the following commands to download the latest available version for Enterprise Linux 7 (CentOS/RedHat).
    ```bash
    PE_VERSION=$(curl -s http://versions.puppet.com.s3-website-us-west-2.amazonaws.com/ | tail -n1)
    PE_SOURCE=puppet-enterprise-${PE_VERSION}-el-7-x86_64
    DOWNLOAD_URL=https://s3.amazonaws.com/pe-builds/released/${PE_VERSION}/${PE_SOURCE}.tar.gz
    wget --progress=bar ${DOWNLOAD_URL}
    ```


## Requirements

### Open the required firewall ports

1. Ensure the required firewall ports are open. If you’re not running a local firewall on the VM, you can skip this step.
    ```bash
    systemctl start firewalld
    ```

    ```bash
    systemctl enable firewalld
    firewall-cmd --zone=public --add-port=22/tcp --permanent
    firewall-cmd --zone=public --add-port=443/tcp --permanent
    firewall-cmd --zone=public --add-port=4433/tcp --permanent
    firewall-cmd --zone=public --add-port=5432/tcp --permanent
    firewall-cmd --zone=public --add-port=8081/tcp --permanent
    firewall-cmd --zone=public --add-port=8140/tcp --permanent
    firewall-cmd --zone=public --add-port=8142/tcp --permanent
    firewall-cmd --zone=public --add-port=8143/tcp --permanent
    firewall-cmd --zone=public --add-port=8170/tcp --permanent
    firewall-cmd --reload
    ```

## Installation 

1. Unpack the tar file.
    ```bash
    tar zxf ${PE_SOURCE}.tar.gz
    ```
1. Let’s start the installation! First, let’s make sure the system locale is set to English for the install.
    ```bash
    export LANG=en_US.UTF-8
    export LANGUAGE=en_US.UTF-8
    export LC_ALL=en_US.UTF-8
    ```
1. Next, run the installer.
    ```bash
    cd ${PE_SOURCE}
    ```

    ```bash
    ./puppet-enterprise-installer
    ```
1. At the prompt to “Proceed with the installation”, **type Y** and **press return**.

    The installer will take about 8-10 minutes to complete.

1. By default, Puppet will use the system’s fully qualified domain name (FQDN) during installation, and a number of services will be configured to connect to endpoints on this FQDN. If DNS name resolution fails to resolve your FQDN to the system’s IP address, you’ll experience unstable behavior. Make sure there is an entry in `/etc/hosts` for your FQDN. The following command is a quick way to accomplish that after the installer finishes:

    ```bash
    echo "$(facter ipaddress) $(puppet config print certname) $(hostname)" >> /etc/hosts
    ```

1. Now that the installer has finished, let’s set the password for the main **admin** user.
    ```bash
    puppet infrastructure console_password
    ```

    Follow the instructions on screen to set your password.

1. Finally, you’ll need to run the puppet agent twice to finish up the installation. Run the puppet agent as follows, and repeat it once more when finished.

    ```bash
    puppet agent -t
    ```

1. You can now access the Puppet Enterprise Web Console at https://\<IP address or FQDN> and login with username **admin** and the password you set earlier.

This lab installs Puppet Enterprise with all default settings. It means that no admin password was set during installation, and that defaults were used to generate the SSL certificates for the Web Console and all other services. As a result, the generated certificate for the Web Console is valid for the FQDN of the machine. The certificates for the TCP 8140 and TCP 8142 endpoints, to which Puppet Agents connect, are valid for both the FQDN of the machine, as well as the short name: **puppet**.

If you want to control these options (and more) at install time, you can create an installation answer file, as described [here](https://puppet.com/docs/pe/2021.2/installing_pe.html#configuration_parameters_and_the_pe.conf_file). An example answer file that sets the admin password and defines the valid names for the SSL certificates, looks like this:

**_pe.conf_**

```bash
"console_admin_password": "P@ssw0rd"
"puppet_enterprise::puppet_master_host": "puppet-01.company.local"
"pe_install::puppet_master_dnsaltnames": ["puppet-01.company.local","puppet.company.local"]
```

# Control Repo

Allows to store and use configurations within Puppet Enterprise.

## Setup Control Repo

### 1. Create a project for the Control Repo on your git server


### 2. Clone template Control Repo and push to your git server

```bash
# install git
sudo dnf install -y git

# ?? What's the full path? 
cd ~
mkdir code
cd code
git config --global user.name "Your Name"
git config --global user.email your.email@address.com

# clone the Control Repo locally
git clone https://github.com/puppetlabs/control-repo.git --branch production
cd control-repo

# Reconfigure the repo to point it to the git server:
git remote remove origin
git remote add origin http://<fqdn of your gitlab server>/puppet/control-repo.git

# push the repo to the git server 
# (this command will ask for your credentials to the git server)
git push origin production
```

Output:

```
Counting objects: 858, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (400/400), done.
Writing objects: 100% (858/858), 150.97 KiB | 0 bytes/s, done.
Total 858 (delta 364), reused 858 (delta 364)
remote: Resolving deltas: 100% (364/364), done.
To http://gitlab.company.local/puppet/control-repo.git
* [new branch]      production -> production
```


### 3. Setup SSH keys on the Puppet Enterprise server
Skip at moment, as I'll use the https public repo

### 4. Set a Deploy Key on the Control Repo

### 5. Enable Code Manager on Puppet Enterprise
Code Manager is the easiest way to configure Puppet Enterprise to import automation content from a git repository. In this step you’ll configure code manager to pull code from your Gitlab server.

1. Navigate to the Puppet Enterprise console.
1. On the navigation bar on the left, click on **Node groups**. Then click the **⊞** sign next to **PE Infrastructure** to expand that group.
1. Click on the **PE Master** group and on the page that opens, click the **Classes** tab.
1. Scroll down to the section called **Class: puppet_enterprise::profile::master**
1. Set the first parameter:
    1. Click on the **Parameter name** dropdown box, then find and click on `code_manager_auto_configure`.
    1. Set this parameter’s value to: `true`. Make sure this value is not surrounded by quotes.
    1. Click the **Add to node group** button to lock in this parameter.
1. Set the second parameter:
    1. Click on the **Parameter name** dropdown box, then find and click on `r10k_private_key`.
    1. Set this parameter’s value to:
        ```bash
        /etc/puppetlabs/puppetserver/ssh/id-control_repo.rsa
        ```       
    1. Click the **Add to node group** button to lock in this parameter.
1. Set the third parameter:
    1. Click on the **Parameter name** dropdown box, then find and click on `r10k_remote`.
    1. Set this parameter’s value to:
        ```bash
        git@<fqdn of your Gitlab server>:puppet/control-repo.git
        ```
    1. Click the **Add to node group** button to lock in this parameter.
Finally, on the bottom right hand corner of the page, click the button **Commit 3 changes** to save changes.
    1. Now you need to run the Puppet Agent on the Puppet Server to configure Code Manager with it’s new parameters. As this particular change will restart a number of Puppet Enterprise services, you should initiate this Puppet run from the terminal console of the Puppet Enterprise server:
        ```bash
        puppet agent -t
        ```

### 6. Deploy the Control Repo to Puppet Enterprise
Code Manager is now able to deploy the Control Repo directly from Gitlab to the Puppet Server. This means that the Control Repos content can be pulled down from source control to the Puppet Server for use in Puppet Enterprise. In this step, you’ll manually deploy the Control Repo using Code Manager for the first time.

1. Deploying code is a privileged action, so you first need to create an RBAC token to allow you to perform the action. Perform this on the terminal console of the Puppet Enterprise server:
    ```bash
    puppet access login --lifetime 1y
    ```

    Enter the credentials for the admin account when prompted. A token is now generated & saved to ~/.puppetlabs/token. This token will be used by default for the puppet commands you’ll use next.

1. Perform a Code Manager dry run to ensure everything is working properly:
    ```bash
    puppet code deploy --dry-run
    ```

    Output:
    ```
    --dry-run implies --all.
    --dry-run implies --wait.
    Dry-run deploying all environments.
    Found 1 environments.    
    ```
1. Now, perform the initial code deployment for the production environment:
    ```bash
    puppet code deploy production --wait
    ```
    Output:
    ```
    Found 1 environments.
    [
    {
        "deploy-signature": "882089207ccc0f326007c0dbdb415426f6e100f2",
        "environment": "production",
        "file-sync": {
        "code-commit": "81fc54f9a63336b241547b6e96e1d7a33d9a2bfb",
        "environment-commit": "d05e76a7f41608d5eb0756f9b533c9ad156a2f8d"
        },
        "id": 1,
        "status": "complete"
    }
    ]
    ```

Your code is now live on the Puppet Enterprise server, and can be used to manage systems. However, future updates you make to the control repo will have no effect until those updates are deployed to the Puppet Enterprise server again. You can do this manually each time, by re-running the puppet code deploy production `--wait` command, however this quickly becomes tedious. In the next step, you’ll configure a webhook to automate code deployment upon an update (commit) to the Control Repo. Alternatively, this could be automated via a CI/CD system, like Continuous Delivery for Puppet Enterprise (CD4PE).

### 7. Enable a webhook for auto sync of your Control Repo updates
Every time you make a change to your Control Repo on the git server, you will need to manually run `puppet code deploy` command to apply the changes. 
To avoid this, a webhook can be set up to automate this action.

1. First, you need to enable local webhooks within Gitlab. You can do this by navigating to 
    * **Admin** (the spanner icon in the top left) **->** 
    * **Settings ->**
    * **Network ->**
    * **Outbound Requests ->** 
    * **Allow requests to the local network from hooks and services**
2. Next, you need to get the value of the RBAC token, which will form part of the webhook. To get the value, run this command on the terminal console of the Puppet Enterprise server:
    ```bash
    cat ~/.puppetlabs/token
    ```
3. Copy the RBAC token string that is output to the clipboard (be careful to only copy the token).
4. Switch back to the Gitlab web interface, to the control-repo project, to add a Webhook:
    1. On the left navigation bar, click Settings → Webhooks.
    2. Set the URL - add the FQDN of your Puppet Server and your RBAC token to the URL below:
        ```bash
        https://<fqdn of your puppet server>:8170/code-manager/v1/webhook?type=gitlab&token=<paste RBAC token here>
        ```
        The URL should look something like this:
        ```bash
        https://puppetserver:8170/code-manager/v1/webhook?type=gitlab&token=0dY2SZHcaJEmFXJOYwBcAK4P0uklvdB0DWUjQvxI64M4
        ```
    3. Uncheck the checkbox in the **Enable SSL verification** option, as you’re using a self-signed certificate
    4. Click the green **Add webhook** button
5. A webhook will appear at the bottom of the page. Click the **Test** button, then select **Push events**. You should get an HTTP 200 result to indicate success.



### 8. Add some useful modules to your Puppet Enterprise installation

You now have your Control Repo set up and Code Manager configured, however, the Puppetfile is currently empty. Your Puppetfile is how you’ll express which automation modules you want to download for use within Puppet Enterprise. This step will give you an example Puppetfile that provides a list of modules for the most typical automation use cases on Linux and Windows.

1. Navigate the Gitlab web interface and click on the **control-repo** project.
1. Locate the **Puppetfile** in the root of the repository and click on it. On the page that comes up, click the blue **Edit** button.
1. Replace the content of the file with the following content:
    ```bash
    # Definition of where the modules come from, only used for backwards compatibility. Code Manager has its own settings for the Forge URL.
    forge 'https://forge.puppet.com'

    # Useful shared capabilities and common dependencies
    mod 'puppetlabs-stdlib',                      :latest
    mod 'puppetlabs-apt',                         :latest
    mod 'puppetlabs-concat',                      :latest
    mod 'puppetlabs-docker',                      :latest
    mod 'puppetlabs-exec',                        :latest
    mod 'puppetlabs-facts',                       :latest
    mod 'puppetlabs-hocon',                       :latest
    mod 'puppetlabs-inifile',                     :latest
    mod 'puppetlabs-mount_iso',                   :latest
    mod 'puppetlabs-powershell',                  :latest
    mod 'puppetlabs-pwshlib',                     :latest
    mod 'puppetlabs-reboot',                      :latest
    mod 'puppetlabs-resource_api',                :latest
    mod 'puppetlabs-transition',                  :latest
    mod 'puppetlabs-translate',                   :latest
    mod 'puppet-archive',                         :latest
    mod 'timidri-meltdown',                       :latest
    mod 'trlinkin-noop',                          :latest
    mod 'pcfens-static_custom_facts',             :latest

    # Modules for automation of Puppet Enterprise itself
    mod 'puppetlabs-bolt_shim',                   :latest
    mod 'puppetlabs-cd4pe',                       :latest
    mod 'puppetlabs-cd4pe_jobs',                  :latest
    mod 'puppetlabs-device_manager',              :latest
    mod 'puppetlabs-puppet_agent',                :latest
    mod 'puppetlabs-puppet_authorization',        :latest
    mod 'puppetlabs-puppet_conf',                 :latest
    mod 'puppetlabs-puppetserver_gem',            :latest

    # Modules for displaying Puppet metrics (optional)
    mod 'puppetlabs-puppet_metrics_dashboard',    :latest
    mod 'puppetlabs-puppet_metrics_collector',    :latest
    mod 'puppet-grafana',                         :latest
    mod 'puppet-telegraf',                        :latest

    # Modules for automating Linux operating systems
    mod 'puppetlabs-cron_core',                   :latest
    mod 'puppetlabs-host_core',                   :latest
    mod 'puppetlabs-k5login_core',                :latest
    mod 'puppetlabs-mailalias_core',              :latest
    mod 'puppetlabs-mount_core',                  :latest
    mod 'puppetlabs-selinux_core',                :latest
    mod 'puppetlabs-sshkeys_core',                :latest
    mod 'puppetlabs-yumrepo_core',                :latest
    mod 'puppetlabs-zfs_core',                    :latest
    mod 'puppetlabs-firewall',                    :latest
    mod 'puppetlabs-ntp',                         :latest
    mod 'puppet-alternatives',                    :latest
    mod 'puppet-epel',                            :latest
    mod 'puppet-logrotate',                       :latest
    mod 'herculesteam-augeasproviders_core',      :latest
    mod 'herculesteam-augeasproviders_grub',      :latest
    mod 'herculesteam-augeasproviders_ssh',       :latest
    mod 'herculesteam-augeasproviders_sysctl',    :latest
    mod 'herculesteam-augeasproviders_syslog',    :latest
    mod 'herculesteam-augeasproviders_shellvar',  :latest
    mod 'herculesteam-augeasproviders_pam',       :latest
    mod 'acjohnson-adcli',                        :latest
    mod 'saz-timezone',                           :latest
    mod 'sgnl05-sssd',                            :latest
    mod 'stm-debconf',                            :latest

    # Modules for automating Linux applications
    mod 'puppetlabs-apache',                      :latest
    mod 'puppetlabs-java',                        :latest
    mod 'puppetlabs-mysql',                       :latest
    mod 'puppet-nginx',                           :latest
    mod 'puppet-redis',                           :latest
    mod 'biemond-oradb',                          :latest
    mod 'biemond-wildfly',                        :latest
    mod 'jethrocarr-initfact',                    :latest
    mod 'saz-memcached',                          :latest

    # Modules for automating Windows operating systems
    mod 'puppetlabs-acl',                         :latest
    mod 'puppetlabs-chocolatey',                  :latest
    mod 'puppetlabs-dism',                        :latest
    mod 'puppetlabs-dsc_lite',                    :latest
    mod 'puppet-windows_firewall',                :latest
    mod 'puppetlabs-registry',                    :latest
    mod 'puppetlabs-scheduled_task',              :latest
    mod 'puppetlabs-windows_puppet_certificates', :latest
    mod 'puppetlabs-wsus_client',                 :latest
    mod 'puppet-download_file',                   :latest
    mod 'puppet-windows_env',                     :latest
    mod 'puppet-windowsfeature',                  :latest
    mod 'ayohrling-local_security_policy',        :latest
    mod 'encore-powershellmodule',                :latest
    mod 'fervid-auditpol',                        :latest
    mod 'karmafeast-windows_smb',                 :latest
    mod 'nekototori-winrmssl',                    :latest
    mod 'noma4i-windows_updates',                 :latest
    mod 'jpi-timezone_win',                       :latest
    mod 'tse-winntp',                             :latest

    # Modules for automating Windows applications
    mod 'puppetlabs-iis',                         :latest
    mod 'puppetlabs-sqlserver',                   :latest
    mod 'kreeuwijk-vmtools_win',                  :latest
    ```
1. Click the Commit changes button.
1. The commit will trigger the webhook, which signals to Code Manager to perform another synchronization of the automation content in your Control Repo. As you’re installing quite a few modules for the first time here, it can take a few minutes for this action to complete. If you want, you can view the progress of the code deployment on the Puppet Enterprise server with this command on the terminal console:
    ```bash
    tail -f /var/log/puppetlabs/puppetserver/puppetserver.log
    ```
1. When the log file above says the following, the deployment has finished:
    ```bash
    [deploy-pool-1] [p.c.core] Finished deploy attempt for environment 'production'.
    ```
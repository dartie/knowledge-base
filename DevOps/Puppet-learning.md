# Puppet

- [Puppet](#puppet)
- [Server installation](#server-installation)
- [Agent installation](#agent-installation)
  - [Linux agent installation](#linux-agent-installation)
    - [Run the agent installation script from the node’s command line.](#run-the-agent-installation-script-from-the-nodes-command-line)
  - [Windows agent installation](#windows-agent-installation)
    - [Install the agent from the PE console.](#install-the-agent-from-the-pe-console)
- [**Configure autosigning**](#configure-autosigning)
- [**Configure Puppet Enterprise to support additional agent platforms**](#configure-puppet-enterprise-to-support-additional-agent-platforms)
    - [Compile agent for unsupported platform](#compile-agent-for-unsupported-platform)
  - [Enable package data collection](#enable-package-data-collection)
  - [View and manage package inventory](#view-and-manage-package-inventory)
  - [Create a report of all packages installed in your environment](#create-a-report-of-all-packages-installed-in-your-environment)
  - [Create a report that lists the web servers (nodes that have the httpd package installed)](#create-a-report-that-lists-the-web-servers-nodes-that-have-the-httpd-package-installed)
  - [Uninstall puppet-agent from client](#uninstall-puppet-agent-from-client)
  - [Remove nodes from the primary server on Linux](#remove-nodes-from-the-primary-server-on-linux)
  - [Reinstall Linux agents with trusted facts and an autosign password](#reinstall-linux-agents-with-trusted-facts-and-an-autosign-password)
  - [Uninstall Windows agents](#uninstall-windows-agents)
  - [Remove the node from the primary server on Windows](#remove-the-node-from-the-primary-server-on-windows)
  - [Reinstall Windows agents with trusted facts and an autosign password](#reinstall-windows-agents-with-trusted-facts-and-an-autosign-password)


# Server installation

[**Install Puppet Enterprise**](https://www.notion.so/Install-Puppet-Enterprise-74302db4625740f9bf758395f9a4ead6?pvs=21)

```bash
# Download the installation package
curl -JLO 'https://pm.puppet.com/cgi-bin/download.cgi?dist=el&rel=9&arch=x86_64&ver=latest'

# Unpack the tarball
tar -xf puppet-enterprise-2023.5.0-el-9-x86_64.tar.gz

# Run the PE installer (as root!)
sudo ./puppet-enterprise-2023.5.0-el-9-x86_64/puppet-enterprise-installer -y

# Set the password for the PE console to puppetlabs
puppet infrastructure console_password --password=puppetlabs
# if puppet command is not found, point to the fullpath: 
# sudo /opt/puppetlabs/bin/puppet infrastructure console_password --password=puppetlabs 

# Run Puppet
puppet agent -t

# Complete post-configuration operations
puppet agent -t

# Check Puppet services
puppet infrastructure status
```

**Output**

```
Notice: Contacting services for status information...

Master: puppet.0priuh96bcnc.svc.cluster.local
  Activity Service: Running, checked via https://puppet.0priuh96bcnc.svc.cluster.local:4433/status/v1/services
  Agentless Catalog Executor Service: Running, checked via https://puppet.0priuh96bcnc.svc.cluster.local:44633/admin/status
  Bolt Service: Running, checked via https://puppet.0priuh96bcnc.svc.cluster.local:62658/admin/status
  Classifier: Running, checked via https://puppet.0priuh96bcnc.svc.cluster.local:4433/status/v1/services
  Orchestrator: Running, checked via https://puppet.0priuh96bcnc.svc.cluster.local:8143/status/v1/services
  PCP Broker: Running, checked via https://puppet.0priuh96bcnc.svc.cluster.local:8143/status/v1/services
  PCP Broker v2: Running, checked via https://puppet.0priuh96bcnc.svc.cluster.local:8143/status/v1/services
  PostgreSQL: Running, checked via postgresql://puppet.0priuh96bcnc.svc.cluster.local:5432/
  Puppet Server: Running, checked via https://puppet.0priuh96bcnc.svc.cluster.local:8140/status/v1/services
  PuppetDB: Running, checked via https://puppet.0priuh96bcnc.svc.cluster.local:8081/status/v1/services
  RBAC: Running, checked via https://puppet.0priuh96bcnc.svc.cluster.local:4433/status/v1/services

Status at 2023-11-15 15:07:11 +0000
11 of 11 services are fully operational.
```

Installation help

```
USAGE: puppet-enterprise-installer [-c CONF_FILE] [-D] [-h] [-q] [-V] [-y] [-p] [-s]

OPTIONS:

    -c <PATH_TO_FILE>
        Use pe.conf at <PATH_TO_FILE>.

        If you have a pre-existing pe.conf, the installer will overwrite it if you use this flag.
        Note that installer will create a backup of the pre-existing pe.conf before overwriting it.
    -D
        Display debugging information.
    -h
        Display this help.
    -q
        Run in quiet mode; the installation process is not displayed.
    -V
        Display very verbose debugging information.
    -y
        Assume yes/default and bypass any prompts for user input.
        Ensure that your pe.conf file is valid before using this flag.
    -p
        Prepare the system for future install.
        Will install packages and modules, but not run the final configure command.
    -s
    Skip any PostgreSQL checks, not recommended.
```

1. Connect to [https://127.0.0.1:80](https://127.0.0.1:80) and log in using username `admin` and password `puppetlabs`

# Agent installation

- **Method 1** (recommended best practice)
    
    *Local installation via the CLI using the agent install script with PE package management*
    
- **Method 2** (simplest and best for unattended installation)
    
    *Remote installation via the console using PE package management*
    
- **Method 3** (local package management)
    
*Local installation via the CLI using your own package management*

The agent installation script performs the following actions:

1. 1.Detects the operating system on which it's running.
2. 2.Downloads the appropriate agent package from the primary server.
3. 3.Installs the **`puppet-agent`** package.
4. 4.Creates a basic **`puppet.conf`** file.
5. 5.Kicks off a Puppet run.

## Linux agent installation

### Run the agent installation script from the node’s command line.

1. Log into the PE console with username `admin` and password `puppetlabs`.
2. From the console sidebar, navigate to the **Nodes** page.
3. In the upper-right corner, click **Add Nodes**.
4. On the **Add nodes to inventory** page, click **Install Agents**.
5. Copy the curl command shown in the ***nix nodes** field at the right of the console.
    
    💡 **Tip:** Select the text and right-click to copy.
    

🔀 Switch to the **Linux Agent** tab.

1. Paste and run the curl command.
    
    ✅ **Result:** This command installs the Puppet agent.
    

🔀 Switch back to the **PE Console** tab when the installation is complete.

1. Click the circular **Refresh** icon, located at the top right corner of the PE console:
    
    ![https://storage.googleapis.com/instruqt-images/refresh-icon.png](https://storage.googleapis.com/instruqt-images/refresh-icon.png)
    
2. Sign the agent's certificate. From the console sidebar, navigate to the **Certificates** page and click the **Unsigned certificates** tab.
3. In the list of nodes, find the node name starting with `nixagent`. Click the **Accept** button, located to the right of the node name.

🔀 Switch back to the **Linux Agent** tab.

1. Trigger a Puppet run:
    
    ```bash
    puppet agent -t
    ```
    

🔀 Switch back to the **PE Console** tab.

1. From the console sidebar, navigate to the **Nodes** page. Click the node name starting with `nixagent`.
2. On the **Facts** tab, inspect the facts about the `nixagent` node.

---

🎈 **Congratulations!**

You installed Puppet agents locally from the command line on Linux. Expand the drop-down section below to learn how to install the agent from the PE console using Windows.

## Windows agent installation

### Install the agent from the PE console.

🔀 Switch to the **PE Console** tab if needed.

1. From the console sidebar, navigate to the **Nodes** page. In the upper-right corner, click **Add Nodes**.
2. On the **Add nodes to inventory** page, click **Install Agents**.
3. From the **Transport method** list, select **WinRM**. Enter the following information:
    - WinRM hosts: `winagent`
    - User: `Administrator`
    - password: `Puppetlabs!`
    - Test connection: checked
4. Click **Add nodes**.
5. To check the status of the installation, navigate to the **Tasks** page, and then click the ID number of the **pe_bootstrap** task. When the installation is complete, you'll see a certname in the output at the bottom of the page.
    
    ✏️ **Note:** The installation might take a few minutes to complete. Don't move on until this step has finished.
    
6. When the certificate is ready to sign, a blue decoration is shown on the **Certificates** page link.
    
    💡 **Tip:** If the decoration isn't shown after the `pe_bootstrap` task has finished running, click the refresh icon at the top right of the PE console:
    
    ![https://storage.googleapis.com/instruqt-images/refresh-icon.png](https://storage.googleapis.com/instruqt-images/refresh-icon.png)
    
7. Sign the agent's certificate. Navigate to the **Certificates** page and click the **Unsigned certificates** tab.
8. In the list of nodes, find the node name containing `winagent` and click **Accept**.

🔀 Switch to the **Windows Agent** tab.

1. From the Windows Start Menu, click **Puppet**, and then click **Start Command Prompt with Puppet**. Then, trigger a Puppet run at the command prompt:
    
    ```bash
    puppet agent -t
    ```
    
2. Click the **PE Console** tab, and from the console sidebar, navigate to the **Nodes** page. Click the node name containing `winagent`.
3. On the **Facts** tab, inspect the facts about the `winagent` node.

---

🎈 **Congratulations!**

You installed Puppet agents remotely from the PE console on Windows.

To continue, click **Next**.

# **Configure autosigning**

- **Why do I have to accept the node's certificate?**
    
    All the traffic between the agents and the primary server is encrypted and uses X.509 certificates, which are validated by a certificate authority (CA) that runs on the primary server. Before the agent can receive configurations from the primary server, the CA must sign the agent's certificate. After it's signed, the server can't accept any new certificate with the same name.
    
    This security measure prevents rogue clients from impersonating an existing Puppet node.
    
- **Where are the SSL certificates stored?**
    
    On any node (agent, primary server, or CA server), all certificates are stored in the ssldirdirectory.
    
    - *nix: /etc/puppetlabs/puppet/ssl*
    
    Windows: *C:\ProgramData\PuppetLabs\puppet\etc*
    
    This directory isn't created during installation. It's created during the first Puppet run after installation.
    

1. On the **Primary Server** tab, navigate to:
    
    ```bash
    cd /etc/puppetlabs/puppet
    ```
    
2. Create and edit the `autosign.rb` script.
    
    ```bash
    vim autosign.rb
    ```
    
3. Copy the code below into `autosign.rb` file.
    
    💡 **Tip:** To do this, type `:set paste`, press **Enter**, and then press `i`. Click the code below to copy it, and paste it from the clipboard. Then, save and exit by pressing `ESC` and typing `:wq`.
    
    ```ruby
    #!/opt/puppetlabs/puppet/bin/ruby
    #
    # A note on logging:
    #   This script's stderr and stdout are only shown at the DEBUG level
    #   of the server's logs. This means you won't see the error messages
    #   in puppetserver.log by default. All you'll see is the exit code.
    #
    #   https://docs.puppet.com/puppet/latest/ssl_autosign.html#policy-executable-api
    #
    # Exit Codes:
    #   0 - A matching challengePassword was found.
    #   1 - No challengePassword was found.
    #   2 - The wrong challengePassword was found.
    #
    require 'puppet/ssl'
    
    csr = Puppet::SSL::CertificateRequest.from_s(STDIN.read)
    psk = File.read('/etc/puppetlabs/puppet/psk').chomp.strip
    
    if pass = csr.custom_attributes.find do |attribute|
            ['challengePassword', '1.2.840.113549.1.9.7'].include? attribute['oid']
        end
    else
        puts 'No challengePassword found. Rejecting certificate request.'
        exit 1
    end
    
    if pass['value'] == psk
        exit 0
    else
        puts "challengePassword does not match: #{pass['value']}"
        exit 2
    end
    
    ```
    
    💡 To learn more about autosigning certificate requests, visit the [Puppet docs](https://puppet.com/docs/puppet/6/ssl_autosign.html).
    
4. Make the script executable and set the owner/group to `pe-puppet:pe-puppet`.
    
    💡 **Tip:** To save time, click the code below to copy it, and then paste it on the command line:
    
    ```bash
    chmod 700 /etc/puppetlabs/puppet/autosign.rb
    ```
    
    then:
    
    ```bash
    chown pe-puppet:pe-puppet /etc/puppetlabs/puppet/autosign.rb
    ```
    
5. Create and edit the pre-shared key (PSK) file.
    
    ```bash
    vim psk
    ```
    
6. Copy the following pre-shared key into the file.
    
    💡 **Tip:** To do this, type `:set paste`, press **Enter**, and then press `i`. Click the code below to copy it, and paste it from the clipboard. Then, save and exit by pressing `ESC` and typing `:wq`.
    
    ```
    PASSWORD_FOR_AUTOSIGNER_SCRIPT
    ```
    
7. Lock down the key file permissions and set the owner/group to `pe-puppet:pe-puppet`.
    
    ```bash
    chmod 600 /etc/puppetlabs/puppet/psk
    ```
    
    then:
    
    ```bash
    chown pe-puppet:pe-puppet /etc/puppetlabs/puppet/psk
    ```
    
8. Configure the primary server to enable autosigning with `autosign.rb`.
    
    ```bash
    puppet config set autosign /etc/puppetlabs/puppet/autosign.rb --section server
    ```
    
9. Restart the primary server.
    
    ```bash
    service pe-puppetserver restart
    ```
    
    🔀 Switch to the **Linux Agent** tab.
    
10. Install the Puppet agent by using the installation script with the `custom_attributes:challengePassword` parameter.
    
    ```bash
    uri='https://puppet:8140/packages/current/install.bash'
    ```
    
    then:
    
    ```bash
    curl --insecure "$uri" | bash -s custom_attributes:challengePassword=PASSWORD_FOR_AUTOSIGNER_SCRIPT
    ```
    
    🔀 Switch back to the **PE Console** tab when the agent installation is complete.
    
11. Log in with username `admin` and password `puppetlabs`.
12. From the console sidebar, navigate to the **Nodes** page and confirm that the `nixagent` node is shown in the node list, which means that the agent's certificate was signed automatically and the node is now managed by PE.
13. Click the `nixagent` node, and on the **Facts** tab, explore the facts about the machine, such as OS version, number of CPUs, and so on.

---

🎈 **Congratulations!**

You installed the Puppet agent with autosigning enabled.

# **Configure Puppet Enterprise to support additional agent platforms**

1. On the Linux node, install an agent by running the installation script with the `custom_attributes:challengePassword` parameter:
    
    ```bash
    uri='https://puppet:8140/packages/current/install.bash'
    curl --insecure "$uri" | bash -s custom_attributes:challengePassword=PASSWORD_FOR_AUTOSIGNER_SCRIPT
    ```
    
    ✅ **Result:** The installation script will fail.
    
2. In the output, notice the failure message:
    
    ```
    The agent packages needed to support ubuntu-20.04-amd64 are not present are not present on your        primary  server. To add them, apply the pe_repo::platform::ubuntu_2004_amd64 class to your master node, and then run Puppet. The required agent packages should be retrieved when puppet runs on the master, after which you can run the install.bash script again.
    ```
    
    💭 **Why did the installation fail?**
    
    The Ubuntu 20.04 package isn't present on the primary server — the primary server isn't running Ubuntu. To ensure that the packages are present, you must add the `pe_repo::platform:<AGENT_OS_VERSION_ARCHITECTURE>` classes to the primary server.
    
    🔀 Switch to the **PE Console** tab.
    
3. Log in with username `admin` and password `puppetlabs`.
4. From the console sidebar, navigate to the **Node groups** page. Expand **PE Infrastructure** (click **+**) and then click **PE Master**.
5. Add the repository class for the agent node OS that you want to support.
    1. On the **Classes** tab, in the **Add new class** field, enter `pe_repo`.
    2. From the list of classes, select the `pe_repo::platform::ubuntu_2004_amd64` repo class.
    3. Click **Add class**.
6. Commit your change: Click **Commit** in the bottom right of the page.
    
    🔀 Switch to the **Primary Server** tab.
    
7. Run Puppet to manually trigger the download of the new agent package to the primary server:
    
    ```bash
    puppet agent -t
    ```
    
    🔀 Switch to the **Linux Agent** tab.
    
8. Install the agent on the Linux node by running the following installation script, which includes the `custom_attributes:challengePassword` parameter to autosign the agent certificate:
    
    ```bash
    uri='https://puppet:8140/packages/current/install.bash'
    curl --insecure "$uri" | sudo bash -s custom_attributes:challengePassword=PASSWORD_FOR_AUTOSIGNER_SCRIPT
    ```
    
    In the output, notice the success message. (You may need to scroll up).
    
    ```
    The following NEW packages will be installed: puppet-agent
    ```
    

🎈 **Congratulations!**

You configured Puppet Enterprise to support installing agents that run a different OS than the primary server.

- **Why did I run Puppet on the primary server?**
    
    The primary server has its own agent installed. This agent manages the primary server's configuration.
    
- **Where does the primary server download agent packages from?**
    
    When you reconfigure the primary server to host additional agent platform packages, the built-in PE configuration automatically downloads and stages packages via the internet from https://pm.puppetlabs.com.
    
- **Can I configure a proxy for the package download?**
    
    Yes, in a similar way: in the console, using the *pe_repo::http_proxy_host class*.
    
- **During a standard installation of a primary server, what agent package repositories are created?**
    - A platform package identical to the primary server’s platform.
    - windows_x86_64

[Fact](https://www.notion.so/Fact-7b9a43d420f248ae895ae90cc08469c1?pvs=21)

### Compile agent for unsupported platform

1. Install requirements
    
    ```bash
    sudo dnf install ruby  # Ruby
    gem install bundler    # bundler
    ```
    
2. Build [puppet-runtime](https://github.com/puppetlabs/puppet-runtime)
    
    ```bash
    git clone https://github.com/puppetlabs/puppet-runtime
    cd puppet-runtime
    bundle install
    ```
    
3. a

**Docker**

```bash
docker run -ti --name agent1 puppet/puppet-agent-ubuntu agent -t --server 192.168.1.33
```

## Enable package data collection

1. Log into the PE console with username `admin` and password `puppetlabs`.
2. From the console sidebar, navigate to the **Node groups** page, expand (click **+**) **PE Infrastructure**, and click the **PE Agent** node group.
3. On the **Classes** tab, notice that the `puppet_enterprise::profile::agent` class has already been added to this node group, along with a couple of class-specific parameters.
4. Enable package data collection.
    1. In the **Parameter name** list for the class, select the `package_inventory_enabled` parameter and set it to `true`.
    2. Click **Add to node group**.
    3. Commit your change by clicking **Commit** near the bottom of the page.
5. Run Puppet to apply the change to the nodes in the **PE Agent** node group.
    1. Click **Run > Puppet** near the upper-right corner of the page.
    2. Notice the node details, and leave the options with the default values shown.
    3. Click **Run job** near the bottom of the page.
✏️ **Note:** This might take a few moments to complete (monitor the job status near the upper-right corner of the page).
✅ **Result:** On this Puppet run, Puppet enables package inventory collection. On subsequent Puppet runs, Puppet collects package data and reports it on the **Packages** page.
6. To start collecting and reporting package data, run Puppet a second time.
    1. In the upper right of the **Job details** page, click **Run again > All nodes**.
    2. Click **Run job** to start the second Puppet agent run.
    3. Notice the job status near the upper-right corner of the page.

## View and manage package inventory

1. From the console sidebar, navigate to the **Packages** page.
2. For this scenario, you're trying to find the app servers, web servers, and load balancers by searching for the packages listed in the table below:
    1. Enter the name or partial name of a package in the **Filter by package name** field and click **Apply**.
    2. In the results list, click the package name, and notice which nodes have the package installed.
    3. Repeat this for all the packages in the table.Package NameServer RoleServer NameJava 8App server??httpdWeb server??nginxLoad balancer??

## Create a report of all packages installed in your environment

1. On the **Packages** page, remove any filters from the previous steps.
2. Right-click **Export Data** and click **Save link as**.
3. Download the CSV file to your local machine and review it.

## Create a report that lists the web servers (nodes that have the httpd package installed)

1. On the **Packages** page, in the **Filter by package name** field, enter **httpd** and click **Apply**.
2. In the results, click **httpd**.
3. Right-click **Export Data**, and then click **Save link as**.
4. Download the CSV file to your local machine and review it.

---

🎈 **Congratulations!**

You enabled package data collection and used the information to discover the roles of the nodes in your environment. To continue, click **Next**.

## Uninstall puppet-agent from client

⚠️ **Important:** The **Linux Agent 1** and **Linux Agent 2** tabs represent Linux nodes. Complete the following steps **on each Linux agent node**.

1. On each node, retrieve the node's `certname` by running the following command:
    
    ```bash
    puppet config print certname
    ```
    
    🏆 **Extra credit:** Alternatively, see if you can find the certnames in the **PE console**. Log in with user `admin` and password `puppetlabs`.
    
2. Copy each certname to a local text editor of your choice — you'll need them later in the lab.
3. Retire the nodes by running the *nix agent uninstall script on each node:
    
    ```bash
    /opt/puppetlabs/bin/puppet-enterprise-uninstaller -y -pd
    ```
    
4. Verify that the Puppet directory has been removed by running the following command on each node:
    
    ```bash
    ls /etc/puppetlabs
    ```
    
    ✅ **Result:** The output confirms that the agent no longer exists.
    
    ✏️ **Note:** Remember to complete these steps on each Linux agent node before continuing to the next section.
    

## Remove nodes from the primary server on Linux

💭 **Why do this?**

Uninstalling the agent from a node does not remove the node from management by the primary server. You must also purge the node.

🔀 Switch to the **Primary Server** tab to run commands on the primary server.

1. Purge both Linux nodes by running the following command **twice**, each time replacing `<CERTNAME>` with the certnames you gathered in the previous section:
    
    ```bash
    puppet node purge <CERTNAME>
    ```
    
    ✅ **Result:** In the output, notice the message: `Node <CERTNAME> was purged.`
    
    ✏️ **Note:** Remember to run this command for each Linux node before continuing to the next section.
    

## Reinstall Linux agents with trusted facts and an autosign password

Now, replace `<DATACENTER>` and `<ROLE>` in the script with the correct trusted fact for each node:

|  | Data center | Role |
| --- | --- | --- |
| Linux Agent 1 | dc-west | cmsweb |
| Linux Agent 2 | dc-west | cmsloadbalancer |
| Windows Agent | dc-east | ecommerce |

🔀 Switch to the **Linux Agent 1** tab.

1. Install an agent on the node by running the following installation script.
    
    ⚠️ **Important:** Remember to replace `<DATACENTER>` and `<ROLE>` with data from the table above.
    
    ```
    uri='https://puppet:8140/packages/current/install.bash'
    curl --insecure "$uri" | sudo bash -s custom_attributes:challengePassword=PASSWORD_FOR_AUTOSIGNER_SCRIPT extension_requests:pp_role=<ROLE> extension_requests:pp_datacenter=<DATACENTER>
    
    ```
    
2. 🔀 Switch to the **Linux Agent 2** tab and repeat step 1.
3. 🔀 Switch to the **PE Console** tab and click refresh inside the tab to see the attached nodes.
4. Click the Linux node names to view the trusted facts for each new node.

---

🎈 **Congratulations!**

You uninstalled the agent from your Linux nodes and purged them from the primary server so that you can reuse their node licenses. You then securely assigned each server's role and data center in your environment by installing the Puppet agent with trusted facts and provided an autosign password to enable certificate signing so that primary server can authenticate the agent.

## Uninstall Windows agents

1. 🔀 Switch to the **Windows Agent** tab.
2. Open a PowerShell terminal: **Start** —> **Windows PowerShell** —> **Windows PowerShell 5.1**
    💡 Make sure you are using the correct version of Windows PowerShell (version 5.1).

3. Retrieve the node's `certname` by running the following command:

    ```bash
    puppet config print certname
    ```

🏆 **Extra credit:** Alternatively, see if you can find the certname in the **PE Console**. Log in with user `admin` and password `puppetlabs`.

4. Copy the certname to a local text editor of your choice — you'll need it later in the lab.
5. Launch the **Windows Add or Remove Programs** interface by running the following command in PowerShell:

    ```powershell
    appwiz
    ```
    
6. Right-click **Puppet Agent (64-bit)**, select **Uninstall**, and follow the prompts to uninstall. Click OK on the dialog box that indicates a reboot is necessary, but do not reboot.    ✏️ **Note:** Uninstalling the agent removes the Puppet program directory, the agent service, and all related registry keys. This might take a couple of minutes. ⚠️ **Important:** The `data` directory remains intact, including all SSL keys. Completely remove the agent from the node in the next step.

7. In the PowerShell terminal, run the following command:

    ```powershell
    remove-item C:\ProgramData\PuppetLabs\puppet -Recurse -Confirm:$false
    ```

## Remove the node from the primary server on Windows

💭 **Why do this?**

Uninstalling the agent from a node does not remove the node from management by the primary server. You must also purge the node.

1. 🔀 Switch to the **Primary Server** tab to run commands on the primary server.
2. Purge the Windows node by running the following command, replacing `<CERTNAME>` with the certname you gathered in a previous step:
    
    ```bash
    puppet node purge <CERTNAME>    
    ```
    

✅ **Result:** In the output, notice the message: `Node <CERTNAME> was purged.`

## Reinstall Windows agents with trusted facts and an autosign password

Now, replace `<DATACENTER>` and `<ROLE>` in the script with the correct trusted fact for the Windows node:

|  | Data Center | Role |
| --- | --- | --- |
| Linux Agent 1 | dc-west | cmsweb |
| Linux Agent 2 | dc-west | cmsloadbalancer |
| Windows Agent | dc-east | ecommerce |

1. 🔀 Switch to the **Windows Agent** tab.
1. Install an agent by using the following installation script, passing in the corresponding role and data center for the last command. Run the following four commands one at a time:
    
    💡 Make sure you are using the correct version of Windows PowerShell (version 5.1).

    ```powershell
    # Command 1
    [Net.ServicePointManager]::ServerCertificateValidationCallback = {$true};
    ```
        
    ```powershell
    # Command 2
    $webClient = New-Object System.Net.WebClient;
    ```
        
    ```powershell
    # Command 3
    $webClient.DownloadFile('https://puppet:8140/packages/current/install.ps1', 'install.ps1');
    ```
        
    ```powershell
    # Command 4
    .\install.ps1 custom_attributes:challengePassword=PASSWORD_FOR_AUTOSIGNER_SCRIPT extension_requests:pp_role=<ROLE> extension_requests:pp_datacenter=<DATACENTER>
    ```
    
    :pencil: **Note:** A rescue command is built into the Windows image; as an alternative to running steps 1-3, you can run the following in a new PowerShell prompt:
    
    ```bash
    Get-PuppetInstallerScript
    ```
    
1. 🔀 Switch to the **PE Console** tab and log in with user `admin` and password `puppetlabs`.
1. On the **Nodes** page, click the Windows node name to view the trusted facts for the new node.

---

🎈 **Congratulations!**

You uninstalled the Puppet agent from your Windows node and purged it from the primary server so that you can reuse its node license. You securely assigned the server's role and data center in your environment by installing the agent with trusted facts and provided an autosign password to enable certificate signing so that primary server can authenticate the agent.
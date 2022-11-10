# My configuration

## Alias
```bash
echo 'alias update="sudo apt update && sudo apt upgrade -y"' >> ~/.bashrc
```

## Gnome

### Change folder colour
```bash
sudo add-apt-repository ppa:costales/yaru-colors-folder-color & sudo apt install -y folder-color yaru-colors-folder-color 
```

### Gnome Extensions from command line
```bash
# move to directory where you downloaded the extension.
cd ~/Downloads/
# Find UUID replace <extension zip file name> with your download zip file copy it
unzip -c <extension zip file name> metadata.json | grep uuid | cut -d \" -f4

# This command will return UUID copy it.
# Create extension directory in gnome-shell
# paste copied UUID instead of <UUID>
mkdir -p ~/.local/share/gnome-shell/extensions/<UUID>
# Now, Unzip extension in created directory.

# Do not forget to replace UUID
cd ~/.local/share/gnome-shell/extensions/<UUID>
unzip -q ~/Downloads/<extension zip file name> -d ~/.local/share/gnome-shell/extensions/<UUID>/

# Finally, Run this command with UUID to get extension in running mode.
# This command will enable your extension.

# Do not forget to replace UUID
gnome-shell-extension-tool -e <UUID>
```


### Gnome Extensions
#### Dash to Dock - Estensioni per GNOME Shell
https://extensions.gnome.org/extension/307/dash-to-dock/

#### Dynamic Top Bar - Estensioni per GNOME Shell
https://extensions.gnome.org/extension/885/dynamic-top-bar/

#### Pomodoro - Estensioni per GNOME Shell
https://extensions.gnome.org/extension/53/pomodoro/

#### Caffeine - Estensioni per GNOME Shell
https://extensions.gnome.org/extension/517/caffeine/

#### Workspaces to Dock - Estensioni per GNOME Shell
https://extensions.gnome.org/extension/427/workspaces-to-dock/

#### Refresh Wifi Connections - Estensioni per GNOME Shell
https://extensions.gnome.org/extension/905/refresh-wifi-connections/

#### Auto Move Windows - Estensioni per GNOME Shell
https://extensions.gnome.org/extension/16/auto-move-windows/

#### Drop Down Terminal - Estensioni per GNOME Shell
https://extensions.gnome.org/extension/442/drop-down-terminal/

#### EasyScreenCast - Estensioni per GNOME Shell
https://extensions.gnome.org/extension/690/easyscreencast/

#### GitHub - projecthamster/hamster-shell-extension: Shell extension for hamster
https://github.com/projecthamster/hamster-shell-extension

#### Activities Configurator - Estensioni per GNOME Shell
https://extensions.gnome.org/extension/358/activities-configurator/

#### NetSpeed - Estensioni per GNOME Shell
https://extensions.gnome.org/extension/104/netspeed/

#### Applications Menu - Estensioni per GNOME Shell
https://extensions.gnome.org/extension/6/applications-menu/

#### Todo.txt - Estensioni per GNOME Shell
https://extensions.gnome.org/extension/570/todotxt/

#### User Themes - Estensioni per GNOME Shell
https://extensions.gnome.org/extension/19/user-themes/

#### SerMon: Service Monitor - Estensioni per GNOME Shell
https://extensions.gnome.org/extension/1804/sermon/

#### GSConnect - Estensioni per GNOME Shell
https://extensions.gnome.org/extension/1319/gsconnect/

#### Screenshot Tool - Estensioni per GNOME Shell
https://extensions.gnome.org/extension/1112/screenshot-tool/

#### Dash to Panel - Estensioni per GNOME Shell
https://extensions.gnome.org/extension/1160/dash-to-panel/



## POP_OS
### Slack
```bash
sudo apt-get update
sudo apt-get upgrade slack-desktop
```

## Install Deepin software
```bash
sudo apt-get install ppa-purge
sudo add-apt-repository ppa:openarun/dde-dev
sudo apt install dde
sudo apt-get install dde-file-manager deepin-calculator deepin-gtk-theme deepin-movie deepin-image-viewer deepin-screen-recorder deepin-screenshot deepin-terminal deepin-voice-recorder deepin-gtk-theme
```
# Remove Wine
```shell
sudo apt-get --purge remove wine

rm -r "$HOME/.wine"
rm  $HOME/.config/menus/applications-merged/wine*
rm -r "$HOME/.local/share/applications/wine"
rm $HOME/.local/share/desktop-directories/wine*
rm $HOME/.local/share/icons/????_*.xpm

sudo apt-get remove --purge wine

sudo apt-get update
sudo apt-get autoclean
sudo apt-get clean
sudo apt-get autoremove
```

# Install Wine 2
* Ref: https://wiki.winehq.org/Ubuntu

```shell
sudo dpkg --add-architecture i386

wget -nc https://dl.winehq.org/wine-builds/Release.key
sudo apt-key add Release.key
sudo apt-add-repository https://dl.winehq.org/wine-builds/ubuntu/

sudo apt-get install --install-recommends winehq-stable
```

> On Linux Mint 17.x, the last line should be the following:
> sudo apt-add-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ trusty main'

> On Linux Mint 18.x, the last line should be the following:
> sudo apt-add-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ xenial main'

---
Created: 2021-06-15T16:56
tags:
  - Linux
  - Productivity
  - Tips
Last edited time: 2025-05-29T14:07
---
- [[#First Install]]
    - [[#Init Git SSH]]
    - [[#Setup Git Multiple Accounts]]
    - [[#Remove Leftover Boot Entries]]
- [[#Basic Monitoring]]
- [[#HDD won’t load]]
- [[#bluetooth arch linux]]
    - [[#Slow apt]]
  
## First Install
### Init Git SSH
```JavaScript
mkdir ~/.ssh/ && cd ~/.ssh/
ssh-keygen -t rsa
cat ~/.ssh/id_rsa.pub
ssh-add ~/.ssh/id_rsa
ssh -T git@github.com
```
### Setup Git Multiple Accounts
Without ssh: `git config credential.helper store`

> [!info] How To Work With Multiple Github Accounts on your PC  
> How To Work With Multiple Github Accounts on your PC · GitHub  
> [https://gist.github.com/rahularity/86da20fe3858e6b311de068201d279e3](https://gist.github.com/rahularity/86da20fe3858e6b311de068201d279e3)  
### Remove Leftover Boot Entries
[[Remove Leftover Boot Entries]]
  
## Basic Monitoring
[[Basic Monitoring]]
  
## HDD won’t load

> [!info] [SOLVED] Unable to mount external easystore hard drive from GUI file manager  
> Starting today, likely after a system update, attempting to mount and view the device’s content from either the Thunar file manager or External Drives icon on the desktop fails and provides this message Failed to mount "easystore".  
> [https://forum.endeavouros.com/t/solved-unable-to-mount-external-easystore-hard-drive-from-gui-file-manager/45766](https://forum.endeavouros.com/t/solved-unable-to-mount-external-easystore-hard-drive-from-gui-file-manager/45766)  
  
# bluetooth arch linux
```JavaScript
sudo pacman -S bluez
sudo pacman -S bluez-utils
sudo systemctl enable bluetooth.service 
```
## Slow apt

> [!info] Slow apt downloads? Try this solution to speed them up  
> In this post we explain a simple method to speed up apt downloads from the repositories available for Ubuntu and other distributions.  
> [https://en.ubunlog.com/slow-apt-downloads-solution/](https://en.ubunlog.com/slow-apt-downloads-solution/)
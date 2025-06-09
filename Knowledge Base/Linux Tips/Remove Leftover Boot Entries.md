If you have leftover boot entries from old OS installations (like Windows, another Linux distro, etc.), you can clean them up in Linux by following these steps:
---
### **1. Check Current Boot Entries**
Run the following command to list all available boot entries:
```Shell
sudo efibootmgr
```
You will see output like this:
```Plain
BootCurrent: 0001
BootOrder: 0001,0002,0003,0004
Boot0001* Ubuntu
Boot0002* Windows Boot Manager
Boot0003* Fedora
Boot0004* Manjaro
```
This shows all boot entries stored in your system’s **UEFI firmware**.
---
### **2. Remove Unwanted Boot Entries**
To remove a specific boot entry, use:
```Shell
sudo efibootmgr -b XXXX -B
```
Replace `XXXX` with the actual boot number. For example, to remove the Windows Boot Manager (Boot0002):
```Shell
sudo efibootmgr -b 0002 -B
```
---
### **3. Delete Leftover OS Files (If Necessary)**
If you previously installed another OS, its files might still be present in the EFI partition. To remove them:
### **Mount the EFI Partition**
First, check which partition is the EFI partition:
```Shell
lsblk
```
Typically, it's something like `/dev/sdX1` or `/dev/nvme0n1p1`. Mount it:
```Shell
sudo mount /dev/sdX1 /mnt
```
### **Delete Unused Boot Directories**
Navigate to the EFI boot folder:
```Shell
cd /mnt/EFI
ls
```
You might see folders like `Ubuntu`, `Microsoft`, `Fedora`, etc. If you want to remove, say, Fedora:
```Shell
sudo rm -rf Fedora
```
Then unmount:
```Shell
sudo umount /mnt
```
---
### **4. Update GRUB (If Using GRUB Bootloader)**
If the old OS still appears in GRUB but is no longer installed, update GRUB:
```Shell
sudo update-grub   # Debian/Ubuntu
sudo grub2-mkconfig -o /boot/grub2/grub.cfg   # RHEL/Fedora
```
---
### **5. (Optional) Reset Boot Order**
If your system still prioritizes an old OS in the boot order, you can change it:
```Shell
sudo efibootmgr -o 0001,0004  # Adjust based on your preferred order
```
---
### **Final Step: Reboot**
After everything, reboot your system:
```Shell
sudo reboot
```
Now your boot menu should be clean!
Let me know if you need further clarification. 🚀
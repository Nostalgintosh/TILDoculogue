# UPDATING IN OSTREE UPDATE
In Fedora Kinote in order to update the OS version you will need to uninstall the old version in order to install the newer version.
For example, we need to install Fedora 44 from Fedora 43 we need to install V44 then uninstalled V43

## Upgrading Fedora Kinoite with Conflicting Layers

**The Problem:** 
When upgrading an immutable OS (like Fedora Kinoite) to a new major version, previously layered repositories (e.g., RPM Fusion) hard-coded to the older OS version will cause a dependency failure and halt the upgrade.

**The Solution:** 
Execute an atomic transaction to strip the legacy dependencies at the exact moment the base image is swapped. This ensures the system compiles only one clean deployment tree and requires only one reboot.

**The Command:**
```powershell
rpm-ostree rebase fedora:fedora/44/x86_64/kinoite --uninstall=rpmfusion-free-release --uninstall=rpmfusion-nonfree-release
```
and enter the password. From then you will need to reboot your computer from there using the flowing command
```powershell
systemctl reboot
```

# UPDATING IN OSTREE UPDATE
In Fedora Kinote in order to update the OS version you will need to uninstall the old version in order to install the newer version.
For example, we need to install Fedora 44 from Fedora 43 we need to install V44 then uninstalled V43
```powershell
rpm-ostree rebase fedora:fedora/44/x86_64/kinoite --uninstall=rpmfusion-free-release --uninstall=rpmfusion-nonfree-release
```

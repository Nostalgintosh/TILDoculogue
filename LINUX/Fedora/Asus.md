# Fedora Kinoite Optimization Guide: ASUS ROG Zephyrus G14

This guide is specifically tailored for optimizing **Fedora Kinoite** (an atomic, KDE Plasma-based OS) on an ASUS ROG Zephyrus G14 (specifically the 2020 model with an NVIDIA GeForce RTX 2060 Max-Q).

Because Kinoite is an immutable operating system, we must layer packages using `rpm-ostree` rather than the standard `dnf` package manager, and carefully manage reboots to apply the new system images.

---

## 1. Add the Terra Repository (For ASUS Tools)
The Terra repository contains the essential `asusctl` and `supergfxctl` packages required to manage the hardware on ROG laptops (fan curves, keyboard RGB, battery charge limits, and GPU Mux switching). 

To add this repository correctly on an atomic Fedora system, use the following command to download the repository configuration file:

```bash
curl -fsSL https://github.com/terrapkg/subatomic-repos/raw/main/terra.repo | sudo tee /etc/yum.repos.d/terra.repo
```

## 2. Add RPM Fusion Repositories (For NVIDIA Drivers)
Fedora is completely open-source out of the box and does not include the proprietary NVIDIA drivers required for the RTX 2060. We must add the **RPM Fusion** repositories to access the `akmod-nvidia` packages.

Run this command to layer the repositories:

```bash
rpm-ostree install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
```

## 3. Reboot to Apply Repositories
Because `rpm-ostree` builds a new system image in the background, the system cannot see the newly added RPM Fusion repositories until you boot into that new image. 

Reboot your system:
```bash
reboot
```

## 4. Install the ASUS Tools and NVIDIA Drivers
Once logged back in, the system will now be able to locate all the necessary packages. We will install the hardware daemons, the GUI control center, and the proprietary NVIDIA drivers all in one go to save time.

Run the full installation command:
```bash
rpm-ostree install asusctl supergfxctl asusctl-rog-gui akmod-nvidia xorg-x11-drv-nvidia-cuda
```
*Note: This process will take several minutes as it compiles the new system image and kernel modules.*

## 5. Final Reboot
Once the terminal indicates that the new tree has been checked out and the installation is done, reboot the system to boot into your final optimized OS image.

```bash
reboot
```

## 6. Enable Hardware Services
After rebooting, you need to tell `systemd` to start the ASUS hardware controllers in the background so they run automatically on every startup. Open your terminal and run:

```bash
sudo systemctl enable --now asusd
sudo systemctl enable --now supergfxd
```

---

## What's Next?
You are now fully optimized! Here is how to use your new tools:

* **ROG Control Center:** Open your KDE application launcher and search for "ROG Control Center". Use this to limit your battery charging (e.g., to 60% or 80% if plugged in often) to save battery health, and to customize fan curves.
* **GPU Switching:** You can now switch your GPU modes using the ROG Control Center or via terminal (`supergfxctl -m Hybrid` or `supergfxctl -m Integrated`).
* **Power Profiles:** You can cycle through Fedora's built-in power profiles (Quiet, Balanced, Performance) using the native KDE battery widget in your system tray or by pressing `Fn + F5` on your keyboard.


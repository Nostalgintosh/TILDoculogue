## TIL: Fixing Flatpak "No remote refs found for flathub" on Fedora Kinoite

### Problem
When trying to install a Flatpak via the terminal (e.g., `flatpak install flathub com.visualstudio.code`) on a fresh Fedora Kinoite installation, the terminal returns an error:
`error: No remote refs found for 'flathub'`

### Cause
A fresh installation of Fedora Kinoite does not always have the external Flathub repository configured by default. The system has the flatpak utility, but it doesn't know where to look for the `flathub` remote target.

### Solution
Add the Flathub remote repository to the system before running the installation command.

1. **Add the Flathub remote:**
   ```bash
   flatpak remote-add --if-not-exists flathub [https://flathub.org/repo/flathub.flatpakrepo](https://flathub.org/repo/flathub.flatpakrepo)
   ```

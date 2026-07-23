# The bescis of COBOL

Make sure that you leave 7 lines blink, and on the 8th line most of the time write `INDENTIFICATION DIVISION.` on the 13th Collum.
- **NOTE:** ALL OF THE WRITING MUST BE ON Area B AND THE TWO NUMBERS MUST BE AT Area A.

The are reserve words like `READT`, `SET`, `DATA`, `END`, `FILE`, `UNTIL` & `IF` as example, so do not use the unless you `READY` to use them.
```cbl






            
            IDENTIFICATION DIVISION.
            PROGRAM-ID. INTEFER-EXAMPLE.

            DATA DIVISION.
            WORKING-STORAGE SECTION.
        01  WS-NUMBER        PIC 9(4) VALUE 0.

            PROCEDURE DIVISION.
                MOVE 42 TO WS-NUMBER
                DISPLAY "The number is: " WS-NUMBER
                STOP RUN.
```
# USING FEDORA KINOITE OS
Because Fedora Kinoite is an immutable (atomic) operating system, installing development tools directly onto your base system is generally discouraged. The cleanest, Fedora-recommended approach is to use **Toolbox** to create an isolated, mutable environment for your COBOL development.

YOU HAVE TWO CHOESE:

### Method 1: Using Toolbox (Recommended)

Toolbox comes pre-installed on Kinoite. Open **Konsole** and run:

1. **Create the container:**
Run `toolbox create` to generate a new Fedora container. Press **Enter** to accept the defaults if prompted.


2. **Enter the container:**
Run `toolbox enter`. Your terminal prompt will change (usually adding a diamond icon `⬢`) to indicate you are now inside the mutable container.


3. **Install GnuCOBOL:**
Run `sudo dnf install gnucobol`. (Inside a toolbox, `sudo` does not require a password).


4. **Verify the installation:**
Run `cobc -version` to confirm the compiler is installed and ready to use.


---

### Method 2: Layering on the Host System

If you absolutely must have COBOL installed on the host OS itself, you will need to layer the package using `rpm-ostree`. This modifies your base image and requires a reboot.

1. **Install the package:** Run `rpm-ostree install gnucobol` in Konsole.
2. **Reboot:** Run `systemctl reboot` to apply the new system image.
3. **Verify:** Open Konsole again and run `cobc -version`.

> **Expert Note:** GnuCOBOL is the modern standard open-source COBOL compiler. Once installed, you compile COBOL files in the terminal using the `cobc` command. To compile a source file into an executable, use the `-x` flag: `cobc -x yourprogram.cob`.

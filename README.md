# sudo-keepassxc
Using KeepassXC and Sudo together

script: inve  
used as an alternative to envoking a venv

Script: sudo  
this script is to be put on an earlier search path, so that it gets called instead on /usr/bin/sudo
it sets up the SUDO_ASKPASS environment variable.

kpxcsudo source dir  
the Python program to ask for a the KeepassXC password and searches for an entry matching the current user and hostname.
it then returns the password to stdout

script: kpxcsudo/clear-build  
removes Nuitka's build artifacts

script: kpxcsudo/build-by-nuitka  
building with Nuitka avoids the need to organise virtual environments.

program: kpxcsudo/kpxcsudo.bin  
this the program SUDO_ASKPASS uses, this:-  
SUDO_ASKPASS="</Absolute-Path-To>/scripts/kpxcsudo.bin" /usr/bin/sudo -A "$@"


Other Apps  
https://github.com/Frederick888/git-credential-keepassxc  
https://kpcli.sourceforge.io  
I think the above use the browser extension and protocol, whereas I wanted a pure command-line version for a headless server

keepassxc-cli  
which comes with the GUI installed version has a dependency on Qt5 or Qt6

Deprecated  
https://github.com/rebkwok/kpcli


//June2026

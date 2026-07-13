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


//June2026

How to implement the script into a virtual machine.

Disclaimer: the current script was written for Ubuntu 16.04, as long as the OS uses the bash shell however, it should work
as intended.

Start up the Ubuntu virtual machine, make sure not to run any updates, as this script checks for three only things:
1. password policies
2. general updates
3. security updates

First you must login as root.
Next you will copy the file into the /usr/local/bin directory. From here, you will run the following commands:
$ chmod a-uw

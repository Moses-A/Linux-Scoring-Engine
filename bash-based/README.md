# How to implement the script into a virtual machine.

Disclaimer: the current script was written for Ubuntu 16.04, as long as the OS uses the bash shell however, it should work
as intended.

Start up the Ubuntu virtual machine, make sure not to run any updates, as this script checks for three only things:
1. password policies
2. general updates
3. security updates

First you must login as root.
Next, you will copy the file into the /usr/local/bin directory. From here, you will run the following commands:
            chmod 111 /usr/local/bin/scoring.bash

Next, you will create cron job for the script to run every 30 seconds:
            crontab -e

Then insert the following line at the end of the file :
            */30 * * * * /usr/local/bin/scoring.bash

Finally save the file and exit.

# Acknowledgements

 This scoring engine was created on the behalf of both Holmes and Business Careers
 
 Cyber Patriot High School teams and created for their use. This code is avaliable 
 
 for resditribution and modification of any kind, please refer to the MIT License.


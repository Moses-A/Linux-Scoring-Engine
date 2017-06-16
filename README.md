# Linux Scoring Engine

This scoring engine has a modular aspect to it, in the sense that it can, through a few edits, can be applied
to almost any Linux image, even none Debian based distributions.


At the moment, their are two versions, the terminal based and the web interface version, which interacts
with HTML files in order to display both the score and points earned.

This project is still under production and is not expected for completion until late July of 2017.

My recommendation for setting up web based interface engine:

1. Have the "bad image" already created, for simplicity sake. (Recommend having Apache2 installed)

2. Copy the engine.py file to the root directory, remove all read and write permissions.

3. Create a symbolic link to the file in another directory, preferably /var/www/html

4. From here, edit the root user's crontab (# crontab -e) and place the line:

                * *  * * * python /directory/of/symboliclink

5. Finally wait a few minutes than check 127.0.0.1 and make sure the points are displaying.


My recommendation for setting up terminal based engine:

1. Have the "bad image" already created

2. copy the engine.py file to somewhere accessible by the recipient

3. run the script to check the score:

           $ sudo python /directory/list/here/engine.py



#Acknowledgements

 This scoring engine was created on the behalf of both Holmes and Business Careers
 
 Cyber Patriot High School teams and created for their use. This code is avaliable 
 
 for resditribution and modification of any kind, please refer to the MIT License.
 
 

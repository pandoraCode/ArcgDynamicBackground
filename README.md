# ArcgDynamicBackground

This script works as a dynamic background changer, it changes the background screen of your desktop every 4 hours

## To run
 - Make sure you have python installed on your machine
 - Run the install.sh file to install the needed python packages :
 
`requests
shutil 
os
subprocess
 pathlib`


- You can either run it using `python dynamic-bg.py &` on boot
- Or if you're using systemd, place the project in user/bin then place dynamic-db.service in /lib/systemd/system/

`  sudo systemctl enable dynamic-db.service ||
   sudo systemctl start dynamic-db.service 
`

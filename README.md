README


Here's some things to know about getting this project to work. This was put together on a Raspbery Pi Model B+. 

1. First, install the fswebcam package: sudo apt-get install fswebcam
2. Make sure you have at least Python version 3.4.2 or above installed. 
3. Use pip to install the python Azure-Storage module: sudo pip3.4 install Azure-Storage
4. Set up your Raspberry Pi to run the uploadtoblob.py script on boot. I followed this guide http://www.raspberrypi-spy.co.uk/2015/02/how-to-autorun-a-python-script-on-raspberry-pi-boot/

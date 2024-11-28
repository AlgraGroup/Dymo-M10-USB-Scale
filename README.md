# Dymo-M10-USB-Scale
Python code to read the weight from a Dymo M10 USB scale. Works under Linux


On a Raspberry pi with Raspberry pi OS:
In order to run the code as a regular user, the following line needs to be added to the file 
/etc/udev/rules.d/50-usb-perms.rules:

SUBSYSTEM=="usb", ATTRS{idVendor}=="0922", ATTRS{idProduct}=="8003", GROUP="plugdev", MODE="0666"

then the rules need to be applied by running

sudo udevadm control --reload ; sudo udevadm trigger

Now the script can be run without sudo

TOXIC Transmission Operating boX's Integrated Client
====================================================

Transmission client for raspberry pi with support for lcd

Dependancies

python transmission-fluid transmission transmission-daemon git

Steps to setup

1) configure lcd.py (line 57): change the pins to your setup 

   note  : pin numbers are GPIO pin numbers and not physical pin numbers 

   refer : <http://www.adafruit.com/adablog/wp-content/uploads/2013/02/Leaf_R2.png> 

 
2) change login details in toxic.py(line 23) : replace all caps words with respective values 

   note  : initialize to blank for localhost without authentication 

	client = Transmission() 

  
3) Enable web client of transmission-daemon to desired values 

 
4) append line : "sudo python /location/of/toxic.py"

	in file /etc/rc.local 
	> sudo nano /etc/rc.local 

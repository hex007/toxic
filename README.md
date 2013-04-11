TOXIC
=====

Transmission client for raspberry pi with support for lcd

Steps to setup

1) configure lcd.py : change the pins to your setup 

   note  : pin numbers are GPIO pin numbers and not physical pin numbers 

   refer : <http://www.adafruit.com/adablog/wp-content/uploads/2013/02/Leaf_R2.png> 

 
2) change login details in toxic.py : replace all caps words with respective values 

   note  : initialize to blank for localhost without authentication 

	ie client = Transmission() 

  
3) Enable web client of transmission-daemon to desired values 

 
4) append line : > sudo python /location/of/toxic.py 
	to file /etc/rc.local 
	command > sudo nano /etc/rc.local 

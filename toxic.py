# Torrent Operating boX's Integrated Client (TOXIC)

from os import system as sys
from time import sleep
from transmission import Transmission
import lcd


lcd = lcd.lcd()
lcd.begin(16,2)
lcd.clear()

lcd.message("    Starting    \n  Transmission  ")
sys("service transmission-daemon start")
lcd.clear()
lcd.message("Booting to TOXIC\n   seconds left ")
for i in range(9,0,-1):
	lcd.setCursor(0,1)
	lcd.message(str(i).rjust(2))
	sleep(1)

# Enter specific details here
client = Transmission(host='IP_ADDRESS', port=PORT, username='USER', password='PASS')
lcd.clear()
lcd.message("TOX: __d __s __p\nUp:____|Dwn:____")

def adjust(speed):
	speed = int(speed)/1024
	if speed < 1000 :
		speed = str(str(speed)+'K').rjust(4)
	else :
		speed = str(float(speed)/1024)
		speed = str(speed[0:speed.find('.')-1]+'M').rjust(4)
	return speed

try :
	while True :
		request = client('session-stats',fields=['downloadSpeed'])
		response=client('torrent-get',fields=['status'])
		downSpeed = adjust(request['downloadSpeed'])
		upSpeed   = adjust(request['uploadSpeed'])
		down = str(len([a for a in response['torrents'] if a['status']==4])).rjust(2)
		seed = str(len([b for b in response['torrents'] if b['status']==6])).rjust(2)
		pause = str(len([c for c in response['torrents'] if c['status']==0])).rjust(2)
		lcd.setCursor(5,0)
		lcd.message(down)
		lcd.setCursor(9,0)
		lcd.message(seed)
		lcd.setCursor(13,0)
		lcd.message(pause)
		lcd.setCursor(3,1)
		lcd.message(upSpeed)
		lcd.setCursor(12,1)
		lcd.message(downSpeed)
		sleep(1)
finally :
	lcd.clear()
	lcd.message("Toxic goodbye :(\nSystem halted!!!")

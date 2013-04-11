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

client = Transmission(host='IP_ADDRESS', port=PORT, username='USER', password='PASS') # empty args to connect to localhost without auth
lcd.clear()
lcd.message("TOXIC: __dw __se\nUp:____|Dwn:____")

try :
        while True :
                request = client('session-stats',fields=['downloadSpeed'])
                response=client('torrent-get',fields=['status'])
                downSpeed = str(str(request['downloadSpeed']/1024)+'K').rjust(4)
                upSpeed   = str(str(request['uploadSpeed']/1024)+'K').rjust(4)
                down = str(len([a for a in response['torrents'] if a['status']==4])).rjust(2)
                seed = str(len([b for b in response['torrents'] if b['status']==6])).rjust(2)
                lcd.setCursor(7,0)
                lcd.message(down)
                lcd.setCursor(12,0)
                lcd.message(seed)
                lcd.setCursor(3,1)
                lcd.message(upSpeed)
                lcd.setCursor(12,1)
                lcd.message(downSpeed)
                sleep(1)
finally :
        lcd.clear()
        lcd.message("Toxic goodbye :(\nSystem halted!!!")

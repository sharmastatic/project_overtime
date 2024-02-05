import os
import sys
import time
import sevseg
import requests

url = "https://api.sunrisesunset.io/json?lat=43.651070&lng=-79.347015"
response = requests.get(url)
data = response.json()
sunrise = data["results"]["sunrise"]
sunset =  data["results"]["sunset"]

def time_split(time_str):
    tt, label = map(str, time_str.split())
    return tt, label

sunrise_time = time_split(sunrise)[0]
sunrise_label = time_split(sunrise)[1]

def time_to_num(time_str):
    hh, mm, ss = map(str, time_str.split(':'))
    return hh, mm, ss

sunrise_hh = time_to_num(sunrise_time)[0]
sunrise_mm = time_to_num(sunrise_time)[1]
sunrise_ss = time_to_num(sunrise_time)[2]

sunrise_tot = int(sunrise_hh)*3600 + int(sunrise_mm)*60 + int(sunrise_ss)

sunset_time = time_split(sunset)[0]
sunset_label = time_split(sunset)[1]

sunset_hh = time_to_num(sunset_time)[0]
sunset_mm = time_to_num(sunset_time)[1]
sunset_ss = time_to_num(sunset_time)[2]

sunset_tot = (int(sunset_hh)+12)*3600  + int(sunset_mm)*60 + int(sunset_ss)

try:
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # clear the console
        currentTime=time.localtime()        #local time
        totalseconds = (currentTime.tm_hour*3600)+(currentTime.tm_min*60)+(currentTime.tm_sec) 

        if (totalseconds>=sunrise_tot):
        
            currenttotalseconds = abs(totalseconds - sunrise_tot)

            Gmins = currenttotalseconds/24                     #According to dimensional analysis, we're doing (sec)/(sec/min) = mins 
            Ghours = Gmins/60                           #According to dimensional analysis, we're doing (mins)/(min/hour) = hour
            Ghours_actual = int(Ghours)                 #whole number is the actual hour
            Gmins_actual= (int((float(Ghours) - int(Ghours))*60))       #decimal value multiplied by 60 is actual minutes
            Gsec_actual = currenttotalseconds-((Ghours_actual*1440)+(Gmins_actual*24))     #remaining seconds from total seconds are current time seconds
           
            hDigits=sevseg.getSevSegStr(Ghours_actual,2)                        #sevseg display for updated hh:mm:ss
            hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()

            mDigits=sevseg.getSevSegStr(Gmins_actual,2)
            mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()

            sDigits=sevseg.getSevSegStr(Gsec_actual,2)
            sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()

            print (hTopRow + '      ' + mTopRow + '     ' + sTopRow)            #sevseg display printed
            print (hMiddleRow + '      ' + mMiddleRow + '     ' + sMiddleRow)
            print (hBottomRow + '      ' + mBottomRow + '     ' + sBottomRow)
            print()

            #below is the line of code to print time in str 
            print(str(Ghours_actual)+':' + str(Gmins_actual) + ':' + str(Gsec_actual))
            print(f'Sunrise: {sunrise_time}')
            print(f'Sunrise: {sunset_time}')
        elif (totalseconds<sunrise_tot):
            currenttotalseconds = (86400 - sunrise_tot)+ totalseconds #24 hours is 86400 seconds. logic is actually a day minus the sunrise time = rest of the day until midnight; which is added to 00:01 until its next day sunrise. 

            Gmins = currenttotalseconds/24                     #According to dimensional analysis, we're doing (sec)/(sec/min) = mins 
            Ghours = Gmins/60                           #According to dimensional analysis, we're doing (mins)/(min/hour) = hour
            Ghours_actual = int(Ghours)                 #whole number is the actual hour
            Gmins_actual= (int((float(Ghours) - int(Ghours))*60))       #decimal value multiplied by 60 is actual minutes
            Gsec_actual = currenttotalseconds-((Ghours_actual*1440)+(Gmins_actual*24))     #remaining seconds from total seconds are current time seconds
           
            hDigits=sevseg.getSevSegStr(Ghours_actual,2)                        #sevseg display for updated hh:mm:ss
            hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()

            mDigits=sevseg.getSevSegStr(Gmins_actual,2)
            mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()

            sDigits=sevseg.getSevSegStr(Gsec_actual,2)
            sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()

            print (hTopRow + '      ' + mTopRow + '     ' + sTopRow)            #sevseg display printed
            print (hMiddleRow + '      ' + mMiddleRow + '     ' + sMiddleRow)
            print (hBottomRow + '      ' + mBottomRow + '     ' + sBottomRow)
            print()

            #below is the line of code to print time in str 
            print(str(Ghours_actual)+':' + str(Gmins_actual) + ':' + str(Gsec_actual))
            print(f'Sunrise: {sunrise_time}')
            print(f'Sunrise: {sunset_time}')
            
        while True: 
            time.sleep(0.01)
            if time.localtime().tm_sec != currentTime.tm_sec:
                break

except KeyboardInterrupt:
    sys.exit()              #when ctrl c is pressed

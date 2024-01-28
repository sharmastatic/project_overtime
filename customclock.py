import sys, time
import sevseg

#The logic behind this code is to create custom clock that manipulates time. I am writing code to give me 60 hours a day, with 60 mins in each hour, and 24 seconds in each minute. 
#The hack is to make sure total number of seconds in a day is the same. I just want time to move differently for me. 

try:
    while True:
        print('\n'*60)                      #empty print screen
        currentTime=time.localtime()        #local time

        totalseconds = (currentTime.tm_hour*3600)+(currentTime.tm_min*60)+(currentTime.tm_sec) 

        Gmins = totalseconds/24                     #According to dimensional analysis, we're doing (sec)/(sec/min) = mins 
        Ghours = Gmins/60                           #According to dimensional analysis, we're doing (mins)/(min/hour) = hour
        Ghours_actual = int(Ghours)                 #whole number is the actual hour
        Gmins_actual= (int((float(Ghours) - int(Ghours))*60))       #decimal value multiplied by 60 is actual minutes
        Gsec_actual = totalseconds-((Ghours_actual*1440)+(Gmins_actual*24))     #remaining seconds from total seconds are current time seconds
       
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

        while True: 
            time.sleep(0.01)
            if time.localtime().tm_sec != currentTime.tm_sec:
                break

except KeyboardInterrupt:
    sys.exit()              #when ctrl c is pressed


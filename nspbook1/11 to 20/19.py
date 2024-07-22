import sys, time
import sevseg

try:
    while True:
        print('\n' * 60)
        currentTime= time.localtime()
        hours = str(currentTime.tm_hour % 12)
        if hours == '0':
            hours = '12'
        minutes = str(currentTime.tm_min)
        seconds = str(currentTime.tm_sec)

        hdigits = sevseg.getSevSegStr(hours, 2)
        hTopRow, hMiddleRow, hBottomRow = hdigits.splitlines()

        mdigits = sevseg.getSevSegStr(minutes, 2)
        mTopRow, mMiddleRow, mBottomRow = mdigits.splitlines()

        Sdigits = sevseg.getSevSegStr(seconds, 2)
        sTopRow, sMiddleRow, sBottomRow = Sdigits.splitlines()

        print(hTopRow    + '     ' + mTopRow    + '     ' + sTopRow)
        print(hMiddleRow + '  *  ' + mMiddleRow + '  *  ' + sMiddleRow)
        print(hBottomRow + '  *  ' + mBottomRow + '  *  ' + sBottomRow)
        print()
        print('Press Ctrl-C to quit.')

        while True:
            time.sleep(0.01)
            if time.localtime().tm_sec != currentTime.tm_sec:
                break
except KeyboardInterrupt:
    print('\n')
    print('Digital clock. by Al sweigart.')
    sys.exit()
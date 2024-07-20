import sys, time
import sevseg

flag_valid = False
while not flag_valid:
    try:
        respone = input('Please enter a number for the countdown.\n> ')
        secondsleft = int(respone)
        assert secondsleft > 0
        flag_valid = True
    except ValueError:
        print('Please enter a integer')
    except:
        print('Input number must be greater than zero.')

try:
    while True:
        print('\n' * 60)

        hours =str(secondsleft // 3600)
        minutes = str((secondsleft % 3600) // 60)
        seconds = str(secondsleft % 60)

        hdigits = sevseg.getSevSegStr(hours, 2)
        hToprow, hMiddlerow, hbottomRow = hdigits.splitlines()

        mdigits = sevseg.getSevSegStr(minutes, 2)
        mTopRow, mMiddleRow, mBottomRow = mdigits.splitlines()

        sdigits = sevseg.getSevSegStr(seconds, 2)
        sTopRow, sMiddleRow, sBottomRow = sdigits.splitlines()

        print(hToprow    + '     ' + mTopRow    + '     ' + sTopRow)
        print(hMiddlerow + '  *  ' + mMiddleRow + '  *  ' + sMiddleRow)
        print(hbottomRow + '  *  ' + mBottomRow + '  *  ' + sBottomRow)
        if secondsleft == 0:
            print()
            print('    * * * * BOOM * * * *')
            break
        print()
        print('Press Ctrl-C to quit.')

        time.sleep(1)
        secondsleft -= 1
except KeyboardInterrupt:
     print('ountd - BOOMBAMM!!! ')
     sys.exit()
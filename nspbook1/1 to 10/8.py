'''calender'''

import datetime

DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 
        'Friday', 'Saturday')

MONTHS = ('January', 'February', 'March', 'April', 'May', 'June'
          ,'July', 'August', 'September', 'October', 'November', 'December')

print('Calender maker')

while True:
    print('Enter the year for the calender.')
    response = input('> ')
    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break

    print('Please enter a numeric year, like 2024.')
    continue

while True:
    print('Enter the month for the calender, 1-12:')
    response = input('> ')

    if not response.isdecimal():
        print('Please enter a numeric month, like 3 for March.')
        continue

    month = int(response)
    if 1 <= month <= 12:
        break

    print('Please enter a number from 1 to 12.')

def getCalenderFor(year, month):
    calText = ''

    calText += (' ' * 34) + MONTHS[month - 1]  + ' ' + str(year) +'\n'

    calText +=  '...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday.....Saturday..\n'

    weekseparator = ('+----------' * 7) + '+\n'

    blankRow = ('|          '*7) +'|\n'

    currentDate = datetime.date(year, month, 1)

    while currentDate.weekday() != 6:
        currentDate -= datetime.timedelta(days=1)

    while True:
        calText += weekseparator

        dayNumberRow = ''
        for i in range(7):
            dayNumberLabel = str(currentDate.day).rjust(2)
            dayNumberRow += '|' + dayNumberLabel +(' '*8)
            currentDate += datetime.timedelta(days=1)
        dayNumberRow +='|\n'

        calText += dayNumberRow
        for i in range(3):
            calText += blankRow
        
        if currentDate.month != month:
            break


    calText+=weekseparator
    return calText

calText = getCalenderFor(year, month)
print(calText)

# calenderFilename = 'calender_{}_{}.txt'.format(year, month)
# with open(calenderFilename, 'w')as fileObj:
#     fileObj.write(calText)

# print('Saved to '+ calenderFilename)
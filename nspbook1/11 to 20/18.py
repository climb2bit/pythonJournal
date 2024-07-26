import random, sys

print('''Dice roller, by mango

Enter what kind and how many dice to roll. The format is the number of 
dice, followed by "d", followed by the number of sides the dice have.
You can also add a plus or minus adjustment. Press QUIT to exit.''')

while True:
    try:
        diceStr = input('> ')
        if diceStr.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        diceStr = diceStr.lower().replace(' ', '')

        dIndex = diceStr.find('d')
        if dIndex == -1:
            raise Exception('Missing the "d" character.')
        
        numberOfDice = diceStr[:dIndex]
        if not numberOfDice.isdecimal():
            raise Exception('Missing the number of dice.')
        numberOfDice = int(numberOfDice)

        modIndex = diceStr.find('+')
        if modIndex == -1:
            modIndex = diceStr.find('-')
        
        if modIndex == -1:
            numberOfsides = diceStr[dIndex + 1 :]
        else:
            numberOfsides = diceStr[dIndex + 1 : modIndex]
        if not numberOfsides.isdecimal():
            raise Exception('Missing number of sides.')
        numberOfsides = int(numberOfsides)

        if modIndex == -1:
            modAmount = 0
        else:
            modAmount = int(diceStr[modIndex + 1 :])
            if diceStr[modIndex] == '-':
                modamount= -modAmount
        
        rollllls = []
        for i in range(numberOfDice):
            rollresult = random.randint(1 ,numberOfsides)
            rollllls.append(rollresult)

        print('Total:', sum(rollllls) + modAmount, '(Each die:', end = '')

        for i, roll, in enumerate(rollllls):
            rollllls[i] = str(roll)
        print(', '.join(rollllls), end = '')

        if modAmount != 0:
            modSign = diceStr[modIndex]
            print(', {}{}'.format(modSign, abs(modAmount), end = ''))
        print(')')

    except Exception as esc:
        print('Invalid input. Enter something like 3d6 or 1d10+2.')
        print('Input was invalid because: ' + str(esc))
        continue
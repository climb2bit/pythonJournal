import random, sys
print('dice, in case you forgot to bring.')
while True:
    print('do you want to roll?')
    response = input('> ')

    if response.lower()  == 'yes': 
        print('roll, roll, roll!')
        dice = random.randint(1, 6)
        print(dice)
        continue
    elif response.lower() == 'no':
        print('Thanks for using!')
        sys.exit()
    else:
        print('Please enter yes or no.')

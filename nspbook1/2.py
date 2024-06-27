"""Birthday paradox"""

import datetime, random

def get_Birthdays(number_of_birthdays):
    birthdays = [] 
    for i in range(number_of_birthdays):
        start_of_year = datetime.date(2001,1,1)
        random_number_of_days = datetime.timedelta(random.randint(0,364))
        birthday = start_of_year + random_number_of_days
        birthdays.append(birthday)
    return birthdays

def get_Match(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None
    for a, BirthdayA in enumerate(birthdays):
        for b, BirthdayB in enumerate(birthdays[a+1:]):
            if BirthdayA == BirthdayB:
                return BirthdayA
            
print('''Birthday Paradox
      
The Birthday Paradox shows us that in a group of N people, the odds
that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation to explore this concept.
      
(It's not actually a paradox, it's just a surprising result!)
''')

MONTHS = ('Jan','Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:
    print('How many birthdays shall I generate? ( Max 100 )')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numBdays = int(response)
        break
print()

print('Here are', numBdays, 'birthdays:')
birthdays = get_Birthdays(numBdays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(', ', end = '')
    monthName = MONTHS[birthday.month - 1]
    dateText = '{} {}'.format(monthName, birthday.day)
    print(dateText, end = '')
print()
print()

match = get_Match(birthdays)

print('In this simulation, ', end = '')
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = '{} {}'.format(monthName, match.day)
    print('multiple people have a matching birthday on', dateText)
else:
    print('There are no matching birthdays.')
print()

print('Gererating', numBdays, 'random birthdays 100,000 times...')
input('Press Enter to begin...')

print('Let\'s run another 100,000 simulations.')
simMatch = 0
for i in range(100_000):
    if i % 10_000 == 0:
        print(i, 'simulations run...')
    birthdays = get_Birthdays(numBdays)
    if get_Match(birthdays) != None:
        simMatch = simMatch + 1
print('100,000 simulations run.')

probability = round(simMatch / 100_000 * 100,2)
print('Out of 100,000 simulations of', numBdays, 'people, there was a')
print('matching birthday in that group', simMatch, 'times. This means')
print('that', numBdays, 'people have a',probability, '% chance of')
print('having a matching birthday in their group.')
print('That\'s probably more than you would think!')
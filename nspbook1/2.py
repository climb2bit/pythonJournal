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
      
(It's not actually a paradox, it's just a surprising result)
''')

MONTHS = ('Jan','Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
from tkinter import Tk, Canvas
from datetime import date, datetime
def get_events():
    list_events = []
    with open('events.txt')as file:
        for line in file:
            line = line.rstrip('\n')
            current_event = line.split(',')
            event_date= datetime.strptime(current_event[1].strip(), '%d/%m/%y').date()
            current_event[1] = event_date
            list_events.append(current_event)
    return list_events

def days_between(date1, date2):
    timegap = date1 - date2
    return timegap.days
    # if (timegap.days >= 0):
        # time_between = str(date1 - date2)
        # number_of_days = time_between.split(' ')
        # return number_of_days[0]
    
root = Tk()
c = Canvas(root, width=800,height= 800,bg = 'black')
c.pack()
c.create_text(100, 50, anchor = 'w', fill = 'orange',\
font = 'Arial 18 bold underline', text= 'My Countdown Calender')
events = get_events()
today = date.today()
v_s = 100
events.sort(key= lambda x: x[1])
for event in events:
    event_name = event[0]
    days_until = days_between(event[1], today)
    if days_until > 0:
        display = 'It is %i days until %s' % (days_until, event_name)
        if (int(days_until) <= 7):
            text_col= 'red'
        else: 
            text_col = 'lightblue'
        c.create_text(100,v_s,anchor='w', fill=text_col, font= 'Arial 18 bold', text=display)
        v_s = v_s + 30
#    else:
#        display = 'It is %i days passed since %s' % (abs(days_until), event_name)
#        c.create_text(100,v_s,anchor='w', fill="green", font= 'Arial 18 bold', text=display)
#        v_s = v_s + 30
root.mainloop()

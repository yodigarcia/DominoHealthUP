import datetime
from pytz import timezone

def get_time():
    a = datetime.datetime.now().day
    b = datetime.datetime.now().month
    if b == 1:
        b = "January"
    elif b == 2:
        b = "February"
    elif b == 3:
        b = "March"
    elif b == 4:
        b = "April"
    elif b == 5:
        b = "May"
    elif b == 6:
        b = "June"
    elif b == 7:
        b = "July"
    elif b == 8:
        b = "August"
    elif b == 9:
        b = "September"
    elif b == 10:
        b = "October"
    elif b == 11:
        b = "November"
    elif b == 12:
        b = "December"

    c = datetime.datetime.now().hour
    d = datetime.datetime.now().minute
    e = datetime.datetime.now().second
    return print("%i %s at %i:%i:%i " %(a,b,c,d,e))

# get_time()

x =123123123123
print(len(x))
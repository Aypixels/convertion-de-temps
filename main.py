from datetime import datetime
from math import floor
import sched, time 

s = sched.scheduler(time.time, time.sleep) 

def do_something(sc): 

    date1 = datetime.now()
    date2 = datetime(2022, 8, 20, 0, 0, 0, 0)

    def convert (date1, date2):

        diff = date2 - date1

        day = floor(diff.seconds / 60 / 60 / 24)
        hour = floor((diff.seconds / 60 / 60) % 24)
        minutes = floor((diff.seconds / 60) % 60)
        seconds = floor((diff.seconds) % 60)

        return {'days': day, 'hours': hour, 'minutes': minutes, 'seconds': seconds}

    convertion = convert(date1, date2)

    print(convertion.get('days'), 'jours\n', convertion.get('hours'), 'heures\n', convertion.get("minutes"), 'minutes &', convertion.get('seconds'), 'secondes')
    # do your stuff 
    sc.enter(1, 1, do_something, (sc,)) 

s.enter(1, 1, do_something, (s,))
s.run()



# print(convertion.get('days'), 'jours\n', convertion.get('hours'), 'heures\n', convertion.get("minutes"), 'minutes &', convertion.get('seconds'), 'secondes')
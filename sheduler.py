import threading
import datetime
import time


class Sheduler:

    tasks = 0

    class delay:

        @classmethod
        def __init__(cls, date="0000 00 00 00 00"):
            cls.year = int(date.split(' ')[0])
            cls.month = int(date.split(' ')[1])
            cls.day = int(date.split(' ')[2])
            cls.hour = int(date.split(' ')[3])
            cls.minutes = int(date.split(' ')[4])

        @classmethod
        def do(cls, func, deamon=True, *args, **kwargs):

            def task():

                Sheduler.tasks += 1
                
                while True:

                    waiting_date = datetime.datetime.strftime(datetime.datetime(
                        cls.year, cls.month, cls.day, cls.hour, cls.minutes
                    ), "%y.%m.%d %H:%M")
                    current_date = datetime.datetime.strftime(datetime.datetime.now(), "%y.%m.%d %H:%M")

                    if waiting_date == current_date:

                        func(*args, **kwargs)
                        break

                    elif datetime.datetime.now() >= datetime.datetime(cls.year, cls.month, cls.day, cls.hour, cls.minutes):

                        func(*args, **kwargs)
                        break

                    else:

                        time.sleep(1)

                Sheduler.tasks -= 1

            thread = threading.Thread(target=task, daemon=deamon)
            thread.start()

    class every:

        @classmethod
        def __init__(cls, times):
            cls.times = times

        @classmethod
        def seconds(cls):
            cls.type = "seconds"
            return cls

        @classmethod
        def minutes(cls):
            cls.type = "minutes"
            return cls

        @classmethod
        def hours(cls):
            cls.type = "hours"
            return cls

        @classmethod
        def days(cls):
            cls.type = "days"
            return cls

        @classmethod
        def do(cls, func, deamon=True, *args, **kwargs):

            def task():

                Sheduler.tasks += 1
                
                while True:
            
                    if cls.type == "seconds": time.sleep(cls.times)

                    elif cls.type == "minutes": time.sleep(cls.times*60)

                    elif cls.type == "hours": time.sleep((cls.times*60)*60)

                    elif cls.type == "days": time.sleep(((cls.times*60)*60)*24)

                    if func(*args, **kwargs) == "BREAK_SHEDULER": break

                Sheduler.tasks -= 1

            thread = threading.Thread(target=task, daemon=deamon)
            thread.start()

    class once:

        @classmethod
        def __init__(cls, times):
            cls.times = times

        @classmethod
        def seconds(cls):
            cls.type = "seconds"
            return cls

        @classmethod
        def minutes(cls):
            cls.type = "minutes"
            return cls

        @classmethod
        def hours(cls):
            cls.type = "hours"
            return cls

        @classmethod
        def days(cls):
            cls.type = "days"
            return cls

        @classmethod
        def do(cls, func, deamon=True, *args, **kwargs):

            def task():

                Sheduler.tasks += 1 
                
                while True:
            
                    if cls.type == "seconds": time.sleep(cls.times)

                    elif cls.type == "minutes": time.sleep(cls.times*60)

                    elif cls.type == "hours": time.sleep((cls.times*60)*60)

                    elif cls.type == "days": time.sleep(((cls.times*60)*60)*24)

                    func(*args, **kwargs)
                    break
                
                Sheduler.tasks -= 1

            thread = threading.Thread(target=task, daemon=deamon)
            thread.start()

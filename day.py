from appt import Appt

class Day(Appt):
    def __init__(self, month, date, year, desc):
        super().__init__(month, date, year, desc)

    def occursOn(appts, day, month, year):
        matching_appts = []
        for appt in appts:
            if appt.day == day:
                matching_appts.append(appt)
        return matching_appts

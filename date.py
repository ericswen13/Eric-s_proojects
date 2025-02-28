from appt import Appt

class Date(Appt):
    def occursOn(appts, day, month, year):
        matching_appts = []
        for appt in appts:
            if appt.day == day and appt.month == month and appt.year == year:
                matching_appts.append(appt)
        return matching_appts

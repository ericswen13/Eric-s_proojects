from appt import Appt

class Month(Appt):
    def occursOn(appts, day, month, year):
        matching_appts = []
        for appt in appts:
            if appt.month == month:
                matching_appts.append(appt)
        return matching_appts

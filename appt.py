class Appt:
    def __init__(self, month, day, year, desc):
        self.month = month
        self.day = day
        self.year = year
        self.desc = desc

    def __str__(self):
        return f'{self.month}/{self.day}/{self.year}: {self.desc}'

    def OccursOn(appt, month, day, year):
        matching_appts = []
        for appts in appt:
            if month == appts.month and day == appts.day and year == appts.year:
                matching_appts.append(appts)
        return matching_appts

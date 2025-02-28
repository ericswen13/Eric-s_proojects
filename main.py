from appt import Appt
from month import Month
from day import Day
from date import Date

appt1 = Appt('10', '25', '2022', 'Teeth cleaning')
appt2 = Month('10', '24', '2023', 'Braces adjustment')
appt3 = Day('11', '25', '2023', 'Fillings and Restorations')
appt4 = Date('10', '25', '2023', 'Root Canal')

appts = [appt1, appt2, appt3, appt4]

m, d, y = input('Enter date in order mm dd yyyy: ').split(' ')
second = input("Would you like to check it by: Day, Month, Date: ")

if second == 'Month':
    o = Month.occursOn(appts, d, m, y)
    print("Appointments in month:")
    for appt in o:
        print(appt)
elif second == 'Day':
    x = Day.occursOn(appts, d, m, y)
    print("Appointments in day:")
    for appt in x:
        print(appt)
elif second == 'Date':
    print(d, m, y)
    u = Date.occursOn(appts, d, m, y)
    print("Appointments in date:")
    for appt in u:
        print(appt)
else:
    print('Please enter a valid option, remember that the first letter must be uppercase')

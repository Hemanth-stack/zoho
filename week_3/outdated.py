month_names = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    s = input('Date: ')
    try:
        month,day,year = s.split('/')
        print(year,month,day,sep='-')
    except:
        pass
    try:
        month,day,year = s.split(' ')
        print(year,month_names.index(month),day[:-1],sep='-')
    except:
        pass
months = [
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
    input_date = input("Date: ").strip()
    if '/' in input_date:
        month, day, year = input_date.split('/')
        if month.isalpha:
            continue
        month = int(month)
        day = int(day)
    elif input_date.split(" ")[0] in months:
        if ',' not in input_date:
            
        txt_month, day, year = input_date.split(" ")
        month = months.index(txt_month) + 1
        day = int(day.strip(','))
    else:
        continue

    if day > 31 or month > 12:
        continue
    break
print(f'{year}-{int(month):02}-{int(day):02}')

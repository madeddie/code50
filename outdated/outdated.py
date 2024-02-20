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

input_date = input("Date: ")
while True:
    if '/' in input_date:
        month, day, year = input_date.split('/')
    elif input_date.split(" ")[0] in months:
        txt_month, day, year = input_date.split(" ")
        month = months.index(txt_month) + 1
        print(f'{year}-{month:02}-{int(day.strip(",")):02}')

print(f'{year}-{int(month):02}-{int(day):02}')

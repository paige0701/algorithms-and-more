from datetime import date


def find_day(num):

    days = ['MON','TUE','WED',"THU",'FRI','SAT','SUN']

    return days[num]

def find_day_with_date(a,b):
    return find_day(date(2016,a,b).weekday())


def main():
    print(find_day_with_date(5,24))

if __name__ == '__main__':
    main()


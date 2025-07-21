#problem 19

def time_difference(time1, time2):
    hour1, minute1 = map(int, time1.split(":"))
    hour2, minute2 = map(int, time2.split(":"))

    total1 = hour1 * 60 + minute1
    total2 = hour2 * 60 + minute2

    return abs(total1 - total2)

time1 = input("Enter first time (HH:MM): ")
time2 = input("Enter second time (HH:MM): ")
print("Difference in minutes:", time_difference(time1, time2))

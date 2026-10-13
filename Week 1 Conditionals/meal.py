def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    calculate_time = hours + minutes / 60
    return calculate_time


def hours_time(time):
    if 7.0 <= time <= 8.0 :
        print('breakfast time')

    elif 12.0 <= time <=13.0 :
        print('lunch time')

    elif 18.0 <= time <= 19.0:
        print('dinner time')





def main():
    time = input('Whats hours is now? ').strip()
    converted_time = convert(time)
    hours_time(converted_time)



if __name__ == "__main__":
    main()





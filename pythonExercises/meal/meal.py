def main():
    question=input("What time is it? ")
    hour=convert(question)
    if hour>=7.0 and hour<=8.0:
        print("breakfast time")
    elif hour>=12.0 and hour<=13.0:
        print("lunch time")
    elif hour>=18.0 and hour<=19.0:
        print("dinner time")


def convert(time):
    hour,minute=time.split(":")
    new_hour=float(hour)
    new_minute=float(minute)/60.0
    return new_hour+new_minute



if __name__ == "__main__":
    main()
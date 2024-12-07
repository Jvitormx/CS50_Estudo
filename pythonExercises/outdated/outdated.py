months=[
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

def change_date(date_change):
    date_change1=date_change.split("/")
    temp=date_change1[0]
    date_change1[0]=date_change1[2]
    date_change1[2]=date_change1[1]
    date_change1[1]=temp
    return date_change1

def main():
    while(True):
        date=input("Date: ").strip()
        if " " in date and "," in date:
            date1=date.split(" ")
            try:
                day=int(date1[1].replace(",", ""))
            except ValueError:
                continue
            if day<=31:
                month=months.index(date1[0])+1
                print(f"{date1[2]}-{month:02}-{day:02}")
                break
            else:
                continue


        if "/" in date:
            date1=change_date(date)
            try:
                month=int(date1[1])
            except ValueError:
                continue
            day=int(date1[2])
            if month<=12 and day<=31:
                print(f"{date1[0]}-{month:02}-{day:02}")
                break
            else:
                continue
main()

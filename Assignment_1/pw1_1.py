def calcGross(hours,rate):
    print("Gross pay: " + str(hours * rate))

if __name__ == "__main__":
    hours = float(input("Enter hours: "))
    rate = float(input("Enter rate: "))
    calcGross(hours,rate)

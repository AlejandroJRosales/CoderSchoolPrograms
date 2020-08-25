import datetime


website = input("What website are is this for: ")
sport = input("What is your favorite sport: ")
hobby = input("What is a hobby of yours? ")

first = website[0:2]
second = sport[0:2]
third = hobby[0:2]
year = str(datetime.date.today().year)
print(first + second + third + year)

import datetime


answers = []
website = input("What website are is this for: ")
answers.append(website)
sport = input("What is your favorite sport: ")
answers.append(sport)
hobby = input("What is a hobby of yours? ")
answers.append(hobby)

password = ""
for answer in answers:
    password += answer[0:2]
year = str(datetime.date.today().year)
print(password + year)

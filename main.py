#First we input the age
age = input("What is your current age?\n")
# we then convert the age to intigers
age = int(age)
# System guesses at random how long a user lives
pridicted_age = random.randint(age,110)
# we calculate the years one has left
year_left = pridicted_age - age
# the months one has left
months_left = (year_left * 12)
# weeks one has left
weeks_left = (year_left * 52)
# days one has left
days_left = (year_left * 365)
# we use f-string to print the output
print(f"You have {days_left} days,{weeks_left} weeks, {months_left} months and {year_left} years left.")
input("press enter to EXIT!")

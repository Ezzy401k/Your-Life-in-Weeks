import random

#First we input the age
age = input("What is your current age?\n")
# we then convert the age to intigers
age = int(age)
last_year = int(random.random() * 100)
#System guesses at random how long a user lives
pridicted_age = random.randint(age,last_year)
# we calculate the years one has left
year_left = pridicted_age - age
# the months one has left
months_left = (year_left * 12)
# weeks one has left
weeks_left = (year_left * 52)
# days one has left
days_left = (year_left * 365)
# we use f-string to print the output
print(f"You have {days_left} in days,{weeks_left} in weeks, {months_left} in months and {year_left} in years left.")
input("press enter to EXIT!")
# print(type(last_year))

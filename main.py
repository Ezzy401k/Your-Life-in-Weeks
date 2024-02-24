#First we input the age
age = input("What is your current age?\n")
# we then convert the age to intigers
age = int(age)
# we calculate the years one has left
year_left = 90 - age
# the months one has left
months_left = (year_left * 12)
# weeks one has left
weeks_left = (year_left * 52)
# days one has left
days_left = (year_left * 365)
# we use f-string to print the output
print(f"You have {days_left} left,{weeks_left} left, and {months_left} months left")

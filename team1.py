"""
File: team1.py
Author: Joshua Ellis

Purpose: Ask and answer questions. Print the info onto the screen in a specific way.

Above and Beyond completed.
"""
print("Please enter the following information: \n")
fname = input("First Name: ")
lname = input("Last Name: ")
hair = input("Hair Color: ")
eye = input("Eye Color: ")
email = input("Email Address: ")
phone = input("Phone Number: ")
job = input("Job Title: ")
whenstart = input("When Did You Start: ")
training = input("Did You Complete Advanced Training: ")
id = input("ID Number: ")

print("The ID card is: \n ------------------------------------------\n")
print(f"{lname.capitalize()}, {fname.capitalize()}\n{job.title()}\nID: {id}\n\n{email}\n{phone}\n\n")
print(f"Hair: {hair.capitalize():15}\t\tEyes: {eye.capitalize()}\nMonth: {whenstart.capitalize():14}\t\tTraining: {training.capitalize()}")
def ask(question):
    answer = input(question)
    return answer
age = int(ask("\nHow old are you? "))
print(f"On your next birthday, you will be {age+1}.\n")

cartons = int(ask("How many egg cartons do you have? "))
eggs = cartons*12
print(f"You have {eggs} eggs.\n")

cookies = int(ask("How many cookies do you have? "))
people = int(ask("How many people are there? "))
cookiesPerPerson = cookies / people
print(f"Each person may have {cookiesPerPerson} cookies.\n")
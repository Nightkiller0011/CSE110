"""
File: team10.py
Author: Joshua Ellis

Purpose: Read and sort through a file.

Above and Beyond completed.
"""

def main():
    file_data = []
    file = None
    name_data = []
    name = None
    id_data = []
    id = None
    job_data = []
    job = None
    salary_data = []
    salary = None

    with open("hr_system.txt") as data:
        for x in data:
            file = x.strip()
            file_data.append(file)
        for x in file_data:
            information = x.split()
            name = information[0]
            name_data.append(name)
            id = information[1]
            id_data.append(id)
            job = information[2]
            job_data.append(job)
            salary = int(information[3])
            if job == 'Engineer':
                salary += 24000
                salary_data.append(salary)
            else:
                salary_data.append(salary)
            print(f"{name} (ID: {id}), Title: {job} - ${salary/24:.2f}")


main()
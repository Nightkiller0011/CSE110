"""
File: assignment11and12.py
Author: Joshua Ellis

Purpose: .

# Above and Beyond completed.
"""
def main():    
    year_of_interest = int(input(f"\nEnter Year of Interest: "))

    file_data = []
    file = None
    country_data = []
    country = None
    abv_data = []
    abv = None
    year_data = []
    year = None
    rate_data = []
    rate = None
    lnumber = 0
    spnumber = 100
    z = 0
    lplace = None
    lyear = None
    spplace = None
    spyear = None
    ylplace = None
    ylnumber = 0
    yspplace = None
    yspnumber = 100
    average = 0
    sum = 0
    count = 0
    with open("life-expectancy.csv") as data:
        for x in data:
            if z == 0:
                print()
            else:
                file = x.strip()
                file_data.append(file)
            z += 1
        i = 0
        for x in file_data:
            information = x.split(",")
            country = information[0]
            country_data.append(country)
            abv = information[1]
            abv_data.append(abv)
            year = int(information[2])
            year_data.append(year)
            rate = information[3]
            rate_data.append(rate)
            number = float(rate)
            if year == year_of_interest:
                count += 1
                if number > ylnumber:
                    ylnumber = number
                    ylplace = country
                if number > 0 and number < yspnumber:
                    yspnumber = number
                    yspplace = country
                sum += number
                average = sum / count
            if number > lnumber:
                lnumber = number
                lplace = country
                lyear = year
            if number > 0 and number < spnumber:
                spnumber = number
                spplace = country
                spyear = year
    print(f"The overall max life expectancy is: {lnumber} from {lplace} in {lyear}.")
    print(f"The overall min life expectancy is: {spnumber} from {spplace} in {spyear}.\n")
    print(f"For the year {year_of_interest}: \nThe average life expectancy across all countries was {average:.2f}")
    print(f"The max life expectancy was: {ylnumber} from {ylplace}.")
    print(f"The min life expectancy was: {yspnumber} from {yspplace}.\n")


main()
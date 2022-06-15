"""
File: team11.py
Author: Joshua Ellis

Purpose: Read through a file and present it in a certain order.

Above and Beyond completed.
"""
def main():
    file_data = []
    file = None
    book_data = []
    book = None
    scripture_data = []
    scripture = None
    chapter_data = []
    chapter = None
    largestchapter = 0
    largestbook = None
    print(f"\nNew Testament, Old Testament, Book of Mormon, Doctrine and Covenants, Pearl of Great Price, All\n")
    chosen = input(f"Which volume of scriptures would you like to select? ")
    with open("books_and_chapters.txt") as data:
        for x in data:
            file = x.strip()
            file_data.append(file)
        for x in file_data:
            information = x.split(":")
            scripture = information[2]
            if scripture.lower() == chosen.lower() or chosen.lower() == "all":
                scripture_data.append(scripture)
                book = information[0]
                book_data.append(book)
                chapter = int(information[1])
                chapter_data.append(chapter)
                if chapter > largestchapter:
                    largestchapter = chapter
                    largestbook = book
                print(f"Scripture: {scripture}, Book: {book}, Chapters: {chapter}")
        print()
        if chosen.lower() == "all":
            print(f"The Largest Book in all of the scriptures recorded here is {largestbook} with {largestchapter} Chapters.\n")
        elif chosen.lower() == "new testament" or chosen.lower() == "old testament" or chosen.lower() == "book of mormon" or chosen.lower() == "doctrine and covenants" or chosen.lower() == "pearl of great price":
            print(f"The Largest Book in this scripture is {largestbook} with {largestchapter} Chapters.\n")
        else:
            print(f"You chose something that is not a book we have recorded. Please try again.\n")

def program_loop():
    again = 'y'
    while again == "y":
        main()
        again = input(f"Would you like to try again?(y/n) ")
        
program_loop()
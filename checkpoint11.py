with open("books.txt") as data:
    for x in data:
        book = x.strip()
        print(book)

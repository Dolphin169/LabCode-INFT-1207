import csv


# Function to add a book to the reading list
def add_book(title, author, year):
    with open('books.csv', mode='a', newline='') as file:
        if title != "":
            writer = csv.writer(file)
        else:
            return "Error: No title"
        if author != "":
            writer = csv.writer(file)
        else:
            return "Error: No author"
        if year.isnumeric():
            writer = csv.writer(file)
        else:
            return "Error: Not a numeric date"
        writer.writerow([title, author, year])


# Function to list all books
def list_books():
    with open('books.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(f'Title: {row[0]}, Author: {row[1]}, Year: {row[2]}')


# Function to search for a book by title
def search_book(title):
    with open('books.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0].lower() == title.lower():
                return f'Found: Title: {row[0]}, Author: {row[1]}, Year: {row[2]}'

        print('Book not found')

'''def delete_book(title,author,year):
    with open('books.csv', mode='r') as file:
        rows = csv.reader(file)
        new_rows = []
        for row in rows:
            if row[0].lower() != title.lower() or row[1].lower() != author.lower() or row[2].lower() != year.lower():
                new_rows.append(row)

        with open('books.csv', mode='w') as file1:
            writer = csv.writer(file1)
            print(new_rows)
            for row in new_rows:
                writer.writerow()'''


def delete_book(title):
    found = False
    rows = []

    # Read all rows from the CSV and keep those that don't match the title
    with open('books.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0].lower() != title.lower():
                rows.append(row)
            else:
                found = True

    # If the book was found, rewrite the CSV without it
    if found:
        with open('books.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print(f'Book "{title}" has been deleted.')
    else:
        print('Book not found, nothing to delete.')


# Menu loop
def menu():
    while True:
        print("\n1. Add Book\n2. List Books\n3. Search Book\n4. Delete Book\n5. Quit")
        choice = input("Select an option: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            year = input("Enter year of publication: ")
            add_book(title, author, year)
        elif choice == '2':
            list_books()
        elif choice == '3':
            title = input("Enter book title to search: ")
            print(search_book(title))
        elif choice == '4':
            title = input("Enter book title: ")
            #author = input("Enter author name: ")
            #year = input("Enter year of publication: ")
            delete_book(title)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")


# Run the program
if __name__ == "__main__":
    menu()

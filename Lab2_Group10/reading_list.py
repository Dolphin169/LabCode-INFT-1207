import csv


# Function to add a book to the reading list
def add_book(title, author, year):
    with open('books.csv', mode='a', newline='') as file:
        if title != "":
            writer = csv.writer(file)
        else:
            print("Error: No title")
            return "Error: No title"
        if author != "":
            writer = csv.writer(file)
        else:
            print("Error: No author")
            return "Error: No author"
        if year.isnumeric():
            writer = csv.writer(file)
        else:
            print("Error: Not a numeric date")
            return "Error: Not a numeric date"
        writer.writerow([title, author, year])


# Function to list all books
def list_books():
    with open('books.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(f'Title: {row[0]}, Author: {row[1]}, Year: {row[2]}')
            return


# Function to search for a book by title
def search_book(title):
    with open('books.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0].lower() == title.lower():
                return f'Found: Title: {row[0]}, Author: {row[1]}, Year: {row[2]}'

        print('Book not found')

def delete_book(title,author,year):
    #set the book were going to delete to false
    delete = False
    #make an empty array to add the books to keep
    rows = []
    #read the file to see what books are there
    with open("books.csv", mode="r") as file:
        #make a variable named reader that is the csv format for reading a file
        reader = csv.reader(file)
        #for each row in the read file in csv format
        for row in reader:
            #check if said row does not contain the correct title, author, and date that we want to delete
            if row[0].lower() != title.lower() and row[1].lower() != author.lower() and row[2].lower() != year.lower():
                #if it does not then put it in the array we made
                rows.append(row)
            else:
                #if it is the book we want to delete then turn delete to true
                delete = True

    #if it is found and the for loop is done
    if delete:
        #write the file
        with open("books.csv", mode="w", newline="") as file:
            #makes a writer format for csv
            writer = csv.writer(file)
            #writes the books.csv with rows
            writer.writerows(rows)
        #prints what book has been deleted
        print(f"Book '{title}, {author}, {year}' has been deleted")
        return f"Book '{title}, {author}, {year}' has been deleted"
    else:
        #if the book cant be found write this message
        print("Nothing to delete, Book not in list")
        return "Nothing to delete, Book not in list"


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
            author = input("Enter author name: ")
            year = input("Enter year of publication: ")
            delete_book(title,author,year)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")


# Run the program
if __name__ == "__main__":
    menu()

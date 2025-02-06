import unittest
import csv
from reading_list import add_book, list_books, search_book, delete_book


class TestReadingList(unittest.TestCase):
    def test_add_book(self):
        """Test adding a book."""
        add_book("Test Book", "Author Name", "2022")
        with open("books.csv", "r") as file:
            reader = csv.reader(file)
            rows = list(reader)
        #self.assertIn(["Test Book", "Author Name", "2022"], rows)

        output = add_book("Feafae", "Feafaef", "asdf")
        self.assertEqual(output, "Error: Not a numeric date")

    def test_search_book(self):
        """Test searching for an existing book."""
        output_result = search_book("Test Book")  # Now it returns a value
        expected_output = "Found: Title: Test Book, Author: Author Name, Year: 2022"
        self.assertEqual(output_result, expected_output, "search_book did not return the expected output.")

        output_result = search_book("1Q84")  # Now it returns a value
        expected_output = "Found: Title: 1Q84, Author: Haruki Murakami, Year: 2009"
        self.assertEqual(output_result, expected_output, "search_book did not return the expected output.")

    def test_delete_book(self):
        result = delete_book("Life is a Book","Kevin Thomas","2025")
        expected = "Book 'Life is a Book, Kevin Thomas, 2025' has been deleted"
        self.assertEqual(result, expected, "delete_book did not return expected output")

    def test_list_books(self):
        result = list_books()
        expected = "Title: Title, Author: Author, Year: Year Title: 1Q84, Author: Haruki Murakami, Year: 2009 Title: Test Book, Author: Author Name, Year: 2022 Title: The Picture of Dorian Gray, Author: Oscar Wilde, Year: 1890 Title: Test Book, Author: Author Name, Year: 2022 Title: Test Book, Author: Author Name, Year: 2022"
        self.assertEqual(result, expected, "list_books() did not return expected output")

if __name__ == '__main__':
    unittest.main()
def delete_duplicate_entries(books):
  # Create a set to store the unique books
  unique_books = set()

  # Iterate through the books and add the unique books to the set
  for book in books:
    unique_books.add(book)

  # Convert the set back to a list and return the list
  return list(unique_books)

def sort_books_by_cost(books):
  # Sort the books by cost
  sorted_books = sorted(books, key=lambda x: x[1])

  # Print the sorted books
  for book in sorted_books:
    print(book[0], book[1])

def count_books_with_cost_more_than_500(books):
  # Count the number of books with cost more than 500
  count = 0
  for book in books:
    if book[1] > 500:
      count += 1

  return count

# Main function
def main():
  # Get input from the user
  num_books = int(input("Enter the number of books: "))
  books = []
  for i in range(num_books):
    name = input("Enter the name of the book: ")
    cost = int(input("Enter the cost of the book: "))
    books.append((name, cost))

  # Delete the duplicate entries
  unique_books = delete_duplicate_entries(books)
  print("After deleting the duplicate entries:", unique_books)

  # Display the books in ascending order based on cost
  print("Books in ascending order based on cost:")
  sort_books_by_cost(unique_books)

  # Count the number of books with cost more than 500
  count = count_books_with_cost_more_than_500(unique_books)
  print("Number of books with cost more than 500:", count)

# Call the main function
main()

def selection_sort(arr):
  # Selection sort algorithm
  for i in range(len(arr) - 1):
    min_index = i
    for j in range(i + 1, len(arr)):
      if arr[j] < arr[min_index]:
        min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

def bubble_sort(arr):
  # Bubble sort algorithm
  for i in range(len(arr) - 1):
    for j in range(len(arr) - 1 - i):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]

def display_top_five_scores(arr):
  # Display the top five scores
  for i in range(5):
    print(arr[i])

# Main function
def main():
  # Get input from the user
  num_students = int(input("Enter the number of students: "))
  percentages = []
  for i in range(num_students):
    percentage = float(input("Enter the percentage of student {}: ".format(i + 1)))
    percentages.append(percentage)

  # Sort the array using selection sort
  print("After sorting the array using selection sort:")
  selection_sort(percentages)
  display_top_five_scores(percentages)


  # Sort the array using bubble sort
  print("After sorting the array using bubble sort:")
  bubble_sort(percentages)
  display_top_five_scores(percentages)

  #top five scorers
  print("Top Five Scorers: ")
  display_top_five_scores(percentages)

# Call the main function
main()

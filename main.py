from sort_functions import functions as sort_fn
import random

# Generate a list of 10000 random numbers
list_10000 = [random.randint(0, 100000) for _ in range(10000)]

# Generate a list of 50000 random numbers
list_50000 = [random.randint(0, 100000) for _ in range(50000)]

# Generate a list of 100000 random numbers
list_100000 = [random.randint(0, 100000) for _ in range(100000)]

while True:
  print("Select an option:")
  print("1. Bubble Sort")
  print("2. Quick Sort")
  print("3. Selection Sort")
  print("4. Heap Sort")
  print("5. Insertion Sort")
  print("6. Merge Sort")
  print("7. Exit")

  choice = int(input("Enter your choice: "))

  match choice:
    case 1:
        sort_fn.bubble_sort(list_10000.copy())
        sort_fn.bubble_sort(list_50000.copy())
        sort_fn.bubble_sort(list_100000.copy())
    case 2:
        sort_fn.quick_sort(list_10000.copy(), 0, len(list_10000) - 1)
        sort_fn.quick_sort(list_50000.copy(), 0, len(list_50000) - 1)
        sort_fn.quick_sort(list_100000.copy(), 0, len(list_100000) - 1)
    case 3:

        sort_fn.selection_sort(list_10000.copy())
        sort_fn.selection_sort(list_50000.copy())
        sort_fn.selection_sort(list_100000.copy())
    case 4:

        sort_fn.heap_sort(list_10000.copy())
        sort_fn.heap_sort(list_50000.copy())
        sort_fn.heap_sort(list_100000.copy())
    case 5:

        sort_fn.insertion_sort(list_10000.copy())
        sort_fn.insertion_sort(list_50000.copy())
        sort_fn.insertion_sort(list_100000.copy())
    case 6:

        sort_fn.merge_sort(list_10000.copy())
        sort_fn.merge_sort(list_50000.copy())
        sort_fn.merge_sort(list_100000.copy())
    case 7:

      break
    case _:
      print("Invalid choice")
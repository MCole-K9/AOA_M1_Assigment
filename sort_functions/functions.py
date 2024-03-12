import time


def timer(func):
  """
  A decorator function that measures the execution time of the given function and logs the size of the list argument.
  """

  def wrapper(*args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    list_size = len(
        args[0]) if len(args) > 0 and isinstance(args[0], list) else 0
    print(
        f"Function '{func.__name__}' took {end - start:.4f} seconds to run on a list of size {list_size}."
    )
    return result

  return wrapper


@timer
def bubble_sort(arr: list[int]) -> list[int]:
  n = len(arr)
  # optimize code, so if the array is already sorted, it doesn't need
  # to go through the entire process
  swapped: bool = False
  # Traverse through all array elements
  for i in range(n - 1):
    # range(n) also work but outer loop will
    # repeat one time more than needed.
    # Last i elements are already in place
    for j in range(0, n - i - 1):
      # traverse the array from 0 to n-i-1
      # Swap if the element found is greater
      # than the next element
      if arr[j] > arr[j + 1]:
        swapped = True
        arr[j], arr[j + 1] = arr[j + 1], arr[j]

    if not swapped:
      # if we haven't needed to make a single swap, we
      # can just exit the main loop.
      break

    #return sorted array
  return arr




# function to find the partition position in quick sort function

def partition(array:list[int], low: int, high:int):

  # choose the rightmost element as pivot
  pivot: int = array[high]

  # pointer for greater element
  i: int = low - 1

  # traverse through all elements
  # compare each element with pivot
  for j in range(low, high):
    if array[j] <= pivot:
      # if element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1

      # swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])

  # swap the pivot element with the greater element specified by i
  (array[i + 1], array[high]) = (array[high], array[i + 1])

  # return the position from where partition is done
  return i + 1

# function to perform quicksort
@timer
def quick_sort(array: list[int], low: int, high: int) -> list[int]:
  quick_sort_fn(array, low, high)
  return array



def quick_sort_fn(array:list[int], low: int, high: int):



  if low < high:

    # find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pi = partition(array, low, high)

    # recursive call on the left of pivot
    quick_sort_fn(array, low, pi - 1)

    # recursive call on the right of pivot
    quick_sort_fn(array, pi + 1, high)



# Heap Sort 
def heapify(arr, n, i):
    # Find largest among root and children
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
          largest = r

    # If root is not largest, swap with largest and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

@timer
def heap_sort(arr):
    n = len(arr)

    # Build max heap
    for i in range(n//2, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        # Swap
        arr[i], arr[0] = arr[0], arr[i]

        # Heapify root element
        heapify(arr, i, 0)

# Selection sort 

@timer
def selection_sort(array):
    size = len(array)
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):

            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i

        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])

@timer
def insertion_sort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        # Place key at after the element just smaller than it.
        array[j + 1] = key


# MergeSort 

@timer
def mergeSort(array):
    if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1
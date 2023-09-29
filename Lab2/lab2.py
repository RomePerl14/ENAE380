"""
This is your template for lab2. Implement all questions in the appropriate
function. You are encouraged to implement helper functions as needed with
a short (one-line) description of their purpose.
"""

import time, random

# Function to generate a random array of size n, with the limit being 0 -> n
def random_array_generator(n : int):
    random_array = [] # Define an array
    for i in range(n): # Iterate the length of n
        random_array.append(random.randint(0, n)) # add a random number to the array
    return random_array # Return the bad boy for operator use

# Function to linearly search an array. In this case, it's the random arrays
def linear_searcher(k : int, array : list):
    start_time = time.time() # Save the time we started at
    indicies = [] # Create an index to account for the possibility of multiple numbers at different indicies
    print_display = False # Switch to see if we should print the display or not
    result_string = "Found the number '" + str(k) + "' at the following indicies: " # text to display string
    # print("Input list: " + str(array))

    # Iterate through the length of the input array, search for the desired value, and return information accordingly
    for i in range(len(array)): # Look through entire array
        if array[i] == k: # Check if the element matches our values
            indicies.append(i) # If it does, save the index
    if len(indicies) == 0: # If we have no values, then the number does not exist in the input array
        print("the number '" + str(k) + "' was not found in the list!")
    else:
        print_display = True
        for i in range(len(indicies)):
            result_string = result_string + str(indicies[i])  + ", " 
    if print_display == True:
        print(result_string)
        end_time = (time.time() - start_time)
        print("Elapsed time: " + str(end_time) + " seconds\n")
        return indicies
    else:
        end_time = (time.time() - start_time)
        print("Elapsed time: " + str(end_time) + " seconds\n")
        return

def array_sorter(n : int): # Creates a sorted array from a given length
    sorted_list = []
    for i in range(n):
        sorted_list.append(i)
    return sorted_list

def binary_searcher(k : int, array : list): # Searches for a value "k" through a sorted array
    looping = True
    middle_check = 0
    bottom_check = 0
    top_check = len(array) - 1
    start_time = time.time()
    while(looping):
        middle_check = int((top_check+bottom_check)/2) # Get the midpoint of the array 
        if k > array[middle_check]: # Check if our value is greater than the middle value
            bottom_check = middle_check + 1 # If it is, change out middle value to be the new bottome value
        elif k < array[middle_check]: # Check if our value is less than the middle value
            top_check = middle_check - 1 # If it is, change out top value to be the new middle value (Subtract one to account for 0 indexing)
        else: # The only other option should be that our search values is the middle point
            print("Found value '" + str(k) + "' at index '" + str(middle_check) + "'!" )
            print("Elapsed time: " + str(time.time()-start_time) + " seconds\n")
            return middle_check
        if middle_check == len(array)-1 or middle_check == 0:
            print("Element was not found in the inputted array! Are you sure it should be there?") # If we reach here, then the element was not present
            print("Elapsed time: " + str(time.time()-start_time) + " seconds\n")
            return
 
    
    



class Lab2(object):
    def bubble_sort(self, my_list):
        """

        Parameters
        ----------
        my_list: list of elements to sort

        Returns
        -------
        list: sorted list in ascending order

        """

        initial_length = len(my_list) # Get the inital array length
        switch_em = False # Create a switch so we can immediately exit the loop if we don't need to swap anything

        # Swapping loops
        for i in range(initial_length-1): # Iterate through the "full" length of the array
            for j in range(0, initial_length-i-1): # Now, iterate through the length of the array minus our current index - 1
                if my_list[j] > my_list[j + 1]: # if the current value is less than the next value swap them
                    switch_em = True # Flip the switch
                    my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j] # Swapping operation
            if switch_em == False: # Catch if we haven't needed to swap
                print("Array was already sorted!\n")
                list = my_list
                return list
        list = my_list
        print("Array has been sorted!")
        return list

    def selection_sort(self, my_list):
        """

        Parameters
        ----------
        my_list : list of elements to sort

        Returns
        -------
        list : sorted list in ascending order
        """
        pass

    def insertion_sort(self, my_list):
        """

        Parameters
        ----------

        my_list : list(int)
            list of elements to sort


        Returns
        -------
        list
            sorted list in ascending order
        """
        pass

    def mergeSort(self, alist):
        """

        Parameters
        ----------

        my_list : list(int)
            list of elements to sort


        Returns
        -------
        list
            sorted list in ascending order
        """
        pass
        

    def readFile(self, filename):
        """
        Insert descriptions here. Make sure to comment this code thoroughly.
        """

        openedFile = open("testNumbers.txt", "r")
        pass

    def vigenere(self):
        """
        Insert descriptions here. Make sure to comment this code thoroughly.
        """
        pass

    def decrypt(self):
        """
        Insert descriptions here. Make sure to comment this code thoroughly.
        """
        pass

class Animal:
    """ implement this class below with appropriate function descriptors """
    pass

class Runner(Animal):
    """ implement this class below with appropriate function descriptors """
    pass



def main():
    ### RANDOM NUMBER GENERATOR ###
    print("\nRandom Number Array Generator:")
    print(random_array_generator(10))

    ### LINEAR SEARCH PROGRAM ###
    print("\nLinear Search Program:")
    
    start_time = time.time() # Get the start time
    search_number = 124 # Number to search for

    # Generate a bunch of random arrays, and search for our search number in them
    linear_searcher(search_number, random_array_generator(10))
    linear_searcher(search_number, random_array_generator(100))
    linear_searcher(search_number, random_array_generator(500))
    linear_searcher(search_number, random_array_generator(1000))
    linear_searcher(search_number, random_array_generator(5000))

    print("Linear Search Total Elapsed time: " + str(time.time()-start_time) + " seconds\n")

    ### BINARY SEARCH PROGRAM ###
    print("\nBinary Search Program:")
    start_time = time.time() # Get the start time

    # Create the sorted arrays and search through em
    sorted_array = array_sorter(10) # Create a sorted array
    search_number = int(len(sorted_array)/3) # Random search number
    binary_searcher(search_number, sorted_array) # Binary search it
    
    sorted_array = array_sorter(100) # Create a sorted array
    search_number = int(len(sorted_array)/3) # Random search number
    binary_searcher(search_number, sorted_array) # Binary search it
    
    sorted_array = array_sorter(500) # Create a sorted array
    search_number = int(len(sorted_array)/3) # Random search number
    binary_searcher(search_number, sorted_array) # Binary search it

    sorted_array = array_sorter(1000) # Create a sorted array
    search_number = int(len(sorted_array)/3) # Random search number
    binary_searcher(search_number, sorted_array) # Binary search it

    sorted_array = array_sorter(5000) # Create a sorted array
    search_number = int(len(sorted_array)/3) # Random search number
    binary_searcher(search_number, sorted_array) # Binary search it

    print("Binary Search Total Elapsed Time: " + str(time.time()-start_time) + " seconds\n")

    ### BUBBLE SORT PROGRAM ###
    print("\nBubble Sort Program")

    ar = random_array_generator(10)
    obj = Lab2()
    obj.bubble_sort(ar)



if __name__ == '__main__':
    main()
    # l = Lab2()
    # l.mergeSort([1, 7, 3, 5, 8, 3])


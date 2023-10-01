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
        print_display = True # Flip the switch
        for i in range(len(indicies)): # Go through the entire array
            result_string = result_string + str(indicies[i])  + ", " # Create the result string
    if print_display == True: # If we found stuff, lets print it
        print(result_string)
        end_time = (time.time() - start_time)
        print("Elapsed time: " + str(end_time) + " seconds\n")
        return indicies # Return what we found
    else: # If we didn't find anything, let the user still know the time
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
        

def merger(a, l, m, r): # Merges two subarray's into one
    '''
    INPUT:
        a : an array of length n
        l : current index value of the main array
        m : value obtained through two expression comparisons
        r : value obtained through two expression comparisons

    OUTPUT:
        nada! (uses pass by reference)
    '''
    # Set iteration length values
    n1 = m - l + 1
    n2 = r - m

    # Create 0 arrays the size of our length values
    L = [0] * n1 
    R = [0] * n2

    # Iterate through both of the newly create arrays, and stuff them with actual values from out main array
    for i in range(0, n1):
        L[i] = a[l + i]
    for i in range(0, n2):
        R[i] = a[m + i + 1]

    # Get iteration indicies for the sub arrays, and save our main index for the main array
    i, j, k = 0, 0, l
    while i < n1 and j < n2:
        if L[i] <= R[j]: # If they are equal, shove the L value into A at our current index in the main array
            a[k] = L[i]
            i += 1 # Iterate up the L index
        else: # If it's the other way around, do that
            a[k] = R[j]
            j += 1 # Iterate up the R index
        k += 1 # Iterate up the main array index

    # If we're still less than our interation lengths, keep going to refill the array with our new values
    while i < n1:
        a[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        a[k] = R[j]
        j += 1
        k += 1

'''
SOURCE: https://www.geeksforgeeks.org/iterative-merge-sort/
'''
           

class Lab2(object):
    def bubble_sort(self, my_list):
        """

        Parameters
        ----------
        my_list : list of elements to sort

        Returns
        -------
        list : sorted list in ascending order

        """

        start_time = time.time()
        initial_length = len(my_list) # Get the inital array length
        switch_em = False # Create a switch so we can immediately exit the loop if we don't need to swap anything

        # Swapping loops
        for i in range(initial_length-1): # Iterate through the "full" length of the array
            for ii in range(0, initial_length-i-1): # Now, iterate through the length of the array minus our current index - 1
                if my_list[ii] > my_list[ii + 1]: # if the current value is less than the next value swap them
                    switch_em = True # Flip the switch
                    my_list[ii], my_list[ii + 1] = my_list[ii + 1], my_list[ii] # Swapping operation
            if switch_em == False: # Catch if we haven't needed to swap
                print("Input array was already sorted!")
                list = my_list
                print("Elapsed time: " + str(time.time()-start_time) + " seconds\n")
                return list
        list = my_list
        print("Array is now sorted!")
        print("Elapsed time: " + str(time.time()-start_time) + " seconds\n")
        file = open("timeFile.csv", "a")
        file.write("," + str(time.time()-start_time))
        return list
    
        '''
        SOURCE: https://www.geeksforgeeks.org/python-program-for-bubble-sort/
        '''

    def selection_sort(self, my_list):
        """

        Parameters
        ----------
        my_list : list of elements to sort

        Returns
        -------
        list : sorted list in ascending order
        """

        start_time = time.time()
        for i in range(len(my_list)):
            grabbed_index = i # Set the desired index per iteration
            for ii in range(i + 1, len(my_list)): # Iterate through the list again (but this time, start at the current index + 1) - starts at 1 (not 0), and keeps going up to account for us slinking down the array
                if my_list[ii] < my_list[grabbed_index]: # If the current value is less than the grabbed index, change the grabbed index
                    grabbed_index = ii # Update our index so we know what number we're swapping with our current value
            my_list[i] = my_list[grabbed_index] # Swap the values of where we are and our grabbed index
            my_list[grabbed_index] = my_list[i]
        
        print("Array is now sorted!")
        print("Elapsed time: " + str(time.time()-start_time) + " seconds\n")
        file = open("timeFile.csv", "a")
        file.write("," + str(time.time()-start_time))
        file.close()
        list = my_list
        return list
    
        '''
        SOURCE: https://www.geeksforgeeks.org/python-program-for-selection-sort/#
        '''
                
    def insertion_sort(self, my_list):
        """

        Parameters
        ----------
        my_list : list of elements to sort

        Returns
        ----------
        list : sorted list in ascending order
        """      

        start_time = time.time()
        if len(my_list) <= 1: # Check to see if the list length is larger than 1, or at least larger than 0. If not, you can't sort a list of 1! so return
            print("The inputted list is already sorted!")
            print("Elapsed time: " + str(time.time()-start_time) + " seconds\n")
            return
    
        # Start looking through the length of the array, to make sure
        for i in range(1, len(my_list)):   # Look through the array, starting from index 1
            current_value = my_list[i]  # store the current value that we are looking at (INDEX = 1)
            ii = i-1 # Create a second indexer, this one being the current index minus 1 (INDEX = 0)
            while ii >= 0 and current_value < my_list[ii]: # If ii is greater than (or equal to) 0 (so always), AND the current_value less than the previous value, do something
                my_list[ii+1] = my_list[ii]  # Set the current index i to be the value of index ii (i = ii + 1) (INDEX 1 now equals INDEX 0)
                ii = ii - 1 # Step back the ii index by 1 value, so that the next line works (INDEX -1)
            my_list[ii+1] = current_value  # Insert the key in the correct position (INDEX 0 now equals INDEX 1)
        print("Array is now sorted!")
        print("Elapsed time: " + str(time.time()-start_time) + " seconds\n")
        file = open("timeFile.csv", "a")
        file.write("," + str(time.time()-start_time))
        file.close()
        list = my_list
        return list

        '''
        SOURCE: https://www.geeksforgeeks.org/python-program-for-insertion-sort/
        '''

    def merge_sort(self, my_list):
        """

        Parameters
        ----------
        my_list : list of elements to sort

        Returns
        -------
        list : sorted list in ascending order
        """

        start_time = time.time()
        a = my_list # Temporarily save the list into a separate variable
        width = 1 # Set a starting array width (2^0) = 1
        n = len(a) # Get the length of the array                                     
        while (width < n): # While our index is less than the length of the array
            l=0 # For each iteration, start from the Oth index (always)
            while (l < n): # While our index is less than the length of the array
                r = min(l+(width*2-1), n-1) # Compare the two expressions (current_index + (current_array_width*2)-1), array_length - 1
                m = min(l+width-1,n-1) # Compare the two expressions (current_index + current_array_width-1), array_length -1       
                merger(a, l, m, r) # Send the values to the merge functions
                l += width*2 # Up our l value for the next iteration
            width *= 2 # Upon next full iteration, we're looking at a bigger array, so, account for it (power of twos, people)
        print("Array is now sorted!")
        print("Elapsed time: " + str(time.time()-start_time) + " seconds\n")
        file = open("timeFile.csv", "a")
        file.write("," + str(time.time()-start_time))
        file.close()
        list = a
        return list
    
        '''
        SOURCE: https://www.geeksforgeeks.org/iterative-merge-sort/
        '''
   
    def readFile(self, filename):
        """
        Parameters
        ----------
        filename : The file path (relative or absolute) to the file being looked at

        Returns
        ----------
        Nothing (Creates a new file)

        """

        lines = open(filename, "r").readlines()
        header = False # Start off by assuming there is no header value
        return_list = []
        try:
            int(lines[0]) # Assuming that there will not be more than 1 line of text in the file, we check to see if there's a header or not
        except:
            header = True # If we caught an exception, theres a header, so set it equal to true
        
        if header == True:
            writeFile = open("sortedNumbers.txt", "w")
            writeFile.write("Sorted Numbers\n")
            for i in range(1,len(lines)): return_list.append(int(lines[i]))
            return_list = self.merge_sort(return_list)
            for i in range(len(return_list)): writeFile.write(str(return_list[i]) + "\n")
            writeFile.close()
        elif header == False:
            for i in range(1,len(lines)): return_list.append(int(lines[i]))
            return_list = self.merge_sort(return_list)
            for i in range(len(return_list)): writeFile.write(str(return_list[i]) + "\n")
            writeFile.close()
        
        print("Done sorting test Numbers file!")

    def vigenere(self, plaintxt = None, key = None):
        """
        Parameters
        ----------
        plaintxt : A string of text to be encrypted
        key : The key used to encrypt the text

        Returns
        ----------
        Nothing (prints encrypted text)
        """
        print("\n")
        if plaintxt == None:
            print("You didn't input a string to encrypt. Please do so now:")
            plaintxt = input()
        if key == None:
            print("You didn't input a keyword. Please do so now:")
            key = input()
        plaintxt = str(plaintxt)
        crpyt_key = str(plaintxt)
        
        # IDK why we can't use regex since that would make this 10x more useful but whateves - gonna remake regex then
        letters_list = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25}
        # letters_list_upper = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9,"K":10,"L":11,"M":12,"N":13,"O":14,"P":15,"Q":16,"R":17,"S":18,"T":19,"U":20,"V":21,"W":22,"X":23,"Y":24,"Z":25}

        # Because there is no reason to keep the word capitalized, and because I'm not going to go through the effort of doing multiple branches of if statements to check if its UPPER or LOWER case, do this:
        plaintxt = plaintxt.lower()
        crpyt_key = crpyt_key.lower()

        key_counter = 0
        for i in range(len(plaintxt)):
            if plaintxt[i] in letters_list.keys():
                




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

    print("\n----------------------------------------")
    ### LINEAR SEARCH PROGRAM ###
    print("\nLinear Search Program\n--------------------")
    
    start_time = time.time() # Get the start time
    search_number = 124 # Number to search for

    # Generate a bunch of random arrays, and search for our search number in them
    linear_searcher(search_number, random_array_generator(10))
    linear_searcher(search_number, random_array_generator(100))
    linear_searcher(search_number, random_array_generator(500))
    linear_searcher(search_number, random_array_generator(1000))
    linear_searcher(search_number, random_array_generator(5000))

    print("Linear Search Total Elapsed time: " + str(time.time()-start_time) + " seconds\n")

    print("\n----------------------------------------")
    ### BINARY SEARCH PROGRAM ###
    print("\nBinary Search Program\n--------------------")
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

    ## Object Declaration ##
    obj = Lab2()

    # ### -- SORTING ALGORITHMS -- ###
    # # Create a new file to write our time information too
    # timeFile = open("timeFile.csv", "w")
    # timeFile.write("\n")
    # timeFile.write(",SORTING ALGORITHM APPROXIMATE TIME-LENGTH\n,(Each iteration uses a new random array - each sorting algorithm is tested on the same array)\n,\n")
    # timeFile.write(",,,SORT TYPE and TIME (seconds)\n")
    # timeFile.write(",,,BUBBLE,,,,,SELECTION,,,,,INSERTION,,,,,MERGE,,,,,\n")
    # timeFile.write(",,SIZE,8,200,500,1000,10000,8,200,500,1000,10000,8,200,500,1000,10000,8,200,500,1000,10000,\n")
    # timeFile.write(",ITERATION")

    # for i in range(10):

    #     timeFile = open("timeFile.csv", "a")
    #     timeFile.write("," + str(i+1))
    #     timeFile.close()
    #     # Get random arrays:
    #     ran_array_8 = random_array_generator(8)
    #     ran_array_200 = random_array_generator(200)
    #     ran_array_500 = random_array_generator(500)
    #     ran_array_1000 = random_array_generator(1000)
    #     ran_array_10000 = random_array_generator(10000)

    #     # length 8 random array
    #     obj.bubble_sort(ran_array_8)
    #     obj.bubble_sort(ran_array_200)
    #     obj.bubble_sort(ran_array_500)
    #     obj.bubble_sort(ran_array_1000)
    #     obj.bubble_sort(ran_array_10000)

    #     obj.selection_sort(ran_array_8)
    #     obj.selection_sort(ran_array_200)
    #     obj.selection_sort(ran_array_500)
    #     obj.selection_sort(ran_array_1000)
    #     obj.selection_sort(ran_array_10000)

    #     obj.insertion_sort(ran_array_8)
    #     obj.insertion_sort(ran_array_200)
    #     obj.insertion_sort(ran_array_500)
    #     obj.insertion_sort(ran_array_1000)
    #     obj.insertion_sort(ran_array_10000)

    #     obj.merge_sort(ran_array_8)
    #     obj.merge_sort(ran_array_200)
    #     obj.merge_sort(ran_array_500)
    #     obj.merge_sort(ran_array_1000)
    #     obj.merge_sort(ran_array_10000)

    #     timeFile = open("timeFile.csv", "a")
    #     timeFile.write("\n,")
    #     timeFile.close()
    
    ### -- READ AND WRITER -- ###
    obj.readFile("testNumbers.txt")

    ### -- VIgenere -- ###
    obj.vigenere("I like balls", "PIPEBOMB")

if __name__ == '__main__':
    main()
    # l = Lab2()
    # l.mergeSort([1, 7, 3, 5, 8, 3])


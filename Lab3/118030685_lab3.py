"""
This is your template for lab3. Implement all questions in the appropriate 
function. Implement helper functions as needed with
a short (one-line) description of their purpose.
"""
# ROMEO PERLSTEIN
# SECTION: 0102

class Logic():
    def __init__(self):
        pass

    def AND_gate(self, bit1 : bool, bit2 : bool):
        '''
        Description
        ----------
        A classic AND logic gate

        Parameters
        ----------
            bit1: The first input bit
            bit2: The second input bit

        Returns
        ----------
            True or False, depending on what the deal is
        '''

        if bit1 and bit2: # If both True
            return True
        else: # Any other case
            return False
        
        
    def OR_gate(self, bit1 : bool, bit2 : bool):
        '''
        Description
        ----------
        A classic OR logic gate

        Parameters
        ----------
            bit1: The first input bit
            bit2: The second input bit

        Returns
        ----------
            True or False, depending on what the deal is
        '''

        if bit1 or bit2: # IF one of the inputs are True
            return True
        else: # Anything else
            return False
        
    def XOR_gate(self, bit1 : bool, bit2 : bool):
        '''
        Description
        ----------
        A classic XOR logic gate

        Parameters
        ----------
            bit1: The first input bit
            bit2: The second input bit

        Returns
        ----------
            True or False, depending on what the deal is
        '''

        if bit1 and not bit2: # If one is true and the other is false
            return True
        elif not bit1 and bit2: # Reverse case, if the other is true and the other is false
            return True
        else: # Anything else
            return False
        
    def NOT_gate(self, bit : bool):
        '''
        Description
        ----------
        A classic NOT logic gate

        Parameters
        ----------
            bit: A boolean input

        Returns
        ----------
            True or False, depending on what the deal is
        '''

        return not bit # Simply return the flipped bit
    
    def NAND_gate(self, bit1 : bool, bit2 : bool):
        '''
        Description
        ----------
        A classic NAND logic gate

        Parameters
        ----------
            bit1: The first input bit
            bit2: The second input bit

        Returns
        ----------
            True or False, depending on what the deal is
        '''

        return not self.AND_gate(bit1, bit2) # Call the AND gate and then flip it
        
    def NOR_gate(self, bit1 : bool, bit2 : bool):
        '''
        Description
        ----------
        A classic NOR logic gate

        Parameters
        ----------
            bit1: The first input bit
            bit2: The second input bit

        Returns
        ----------
            True or False, depending on what the deal is
        '''
        return not self.OR_gate(bit1, bit2) # Call the OR gate and then flip it
        
    def XNOR_gate(self, bit1 : bool, bit2 : bool):
        '''
        Description
        ----------
        A classic XNOR logic gate

        Parameters
        ----------
            bit1: The first input bit
            bit2: The second input bit

        Returns
        ----------
            True or False, depending on what the deal is
        '''

        if bit1 and bit2: # If both inputs are True
            return True
        elif not bit1 and not bit2: # If both inputs are False
            return True
        else: # Anything else
            return False
    # END CLASS
        
def four_bit_logic_circuit(bit_inputs : list) -> list:
    '''
    Description
    ----------
    A four bit logic gate that takes four bits as an input and spits out a four bit output, depending on the input

    Parameters
    ----------
        bit_inputs: a list of integer bits

    Returns
    ----------
    returns a list of four integers, 1 or 0, acting like bits
    '''
    print("\n-- FOUR BIT LOGIC CIRCUIT -- ")

    if len(bit_inputs) != 4: # Make sure the input is the correct length (four)
        print("\nIncorrect about of bits inputted! 4 bits required, only " + str(len(bit_inputs)) + " inputted!")
        return
    
    for i in range(len(bit_inputs)): # Check to make sure it's able to be an integer, and that its either 1 or 0
        try:
            bit_inputs[i] = int(bit_inputs[i]) # Catch if it's not able to be converted to an integer (booleans can, and so can strings of numbers, and so can floats)
        except:
            print("\nOne of your inputted bits is not a bit! Bit in question: " + str(bit_inputs[i]))
            return
        if bit_inputs[i] == 1 or bit_inputs[i] == 0: # Check if our bit is either a 1 or a 0
            pass
        else: # If it's not a 1 or a 0, throw an error
            print("\nOne of your inputted bits is not 1 or 0, that's literally what a bit is?? What are you doing??\nBit in question: " + str(bit_inputs[i]))
            return
    
    # Start doing the logic
    l = Logic()
    output1 = l.NAND_gate(bit_inputs[0], bit_inputs[1]) # Get the output of the first NAND gate
    output2 = l.XOR_gate(bit_inputs[1], bit_inputs[2]) # Get the output of the first XOR gate
    final_output1 = l.OR_gate(output1, output2) # Get the output for the top most OR gate
    final_output2 = output2 # The final output for the 2nd bit is equal to the output of the first XOR gate
    output3 = l.NOR_gate(bit_inputs[2], bit_inputs[3]) # Get the output of the first NOR gate
    output4 = l.XNOR_gate(bit_inputs[2], bit_inputs[3]) # Get the output of the first XNOR gate
    final_output3 = l.AND_gate(output3, l.NOT_gate(output4)) # Get the output of the left-most AND gate
    final_output4 = l.NOT_gate(output4) # The final output for the 4th bit is the NOT of the output from the bottom most XNOR gate

    print("INPUT:")
    print(bit_inputs)
    print("OUTPUT:")
    output = [int(final_output1), int(final_output2), int(final_output3), int(final_output4)] # Save the output as integers
    print(output)
    print()
    return(output)
        
def two_bit(list1 : list, list2 : list) -> list:
    """
    Description
    ----------
    A two bit multiplier, takes in a two 2-bit values and multiplies them together
    
    Parameters
    ----------
        list1: list(bits)
        list2: list(bits)

    Returns
    -------
        list: A list of four integer values 
    """
    print("\n-- 2-BIT Multiplier --")
    print("First input:")
    print(list1)
    if len(list1) != 2: # Make sure the input is the correct length (four)
        print("\nIncorrect about of bits inputted! 2 bits required, " + str(len(list1)) + " inputted!")
        return
    for i in range(len(list1)): # Check to make sure it's able to be an integer, and that its either 1 or 0
        try:
            list1[i] = int(list1[i]) # Check to make sure we can convert the input into an integer (so it must be a bool, double, or a string of a number)
        except:
            print("\nOne of your inputted bits is not a bit! Bit in question: " + str(list1[i]))
            return
        if list1[i] == 1 or list1[i] == 0: # Make sure that our inputs are either a 1 or a 0
            pass
        else: # If not, throw and error
            print("\nOne of your inputted bits is not 1 or 0, that's literally what a bit is?? What are you doing??\nBit in question: " + str(list1[i]))
            return
    print("Second input:")
    print(list2)
    if len(list2) != 2: # Make sure the input is the correct length (four)
        print("\nIncorrect about of bits inputted! 2 bits required, " + str(len(list2)) + " inputted!")
        return
    for i in range(len(list2)): # Check to make sure it's able to be an integer, and that its either 1 or 0
        try:
            list2[i] = int(list2[i]) # Check to make sure we can convert the input into an integer (so it must be a bool, double, or a string of a number)
        except:
            print("\nOne of your inputted bits is not a bit! Bit in question: " + str(list2[i]))
            return
        if list2[i] == 1 or list2[i] == 0: # Make sure that our inputs are either a 1 or a 0
            pass
        else: # If not, throw and error
            print("\nOne of your inputted bits is not 1 or 0, that's literally what a bit is?? What are you doing??\nBit in question: " + str(list2[i]))
            return
    
    # Start the logicing
    l = Logic()
    ANDgate1_output = l.AND_gate(list1[0], list2[1])
    ANDgate2_output = l.AND_gate(list1[0], list2[0])
    ANDgate3_output = l.AND_gate(list1[1], list2[0])
    ANDgate4_output = l.AND_gate(list1[1], list2[1])
    
    # Get the first 2 final outputs
    final_output1 = int(ANDgate2_output) # The 0th index of the output
    final_output2 = int(l.XOR_gate(ANDgate1_output, ANDgate3_output)) # The 1st index ofthe output

    # Continue with the rest of the logic
    ANDgate_middle_output = l.AND_gate(ANDgate1_output, ANDgate3_output)
    final_output4 = int(l.AND_gate(ANDgate_middle_output, ANDgate4_output))
    final_output3 = int(l.XOR_gate(ANDgate_middle_output, ANDgate4_output))

    print("OUTPUT:")
    output = [final_output1, final_output2, final_output3, final_output4]
    print(output)
    print()
    return output

def conversion():
    """
    Description
    ----------
    Converts an integer to a binary number, or a binary number to an integer
    
    Parameters
    ----------
        none, however prompts for inputs
        bits: The inputted bits (if inputted) - using HSB notation
        integer: The inputted integer (if inputted)

    Returns
    -------
        Nothing, but outputs either a 4 bit binary number, or an integer
    """
    # Prompt the user to either input a binary number or an integer
    converting = True
    while(converting):
        print("Would you like to convert an integer to a binary number, or a binary number to an integer? (int/bin)")
        checking1 = True
        while(checking1):
            answer = input()
            if answer == "int":
                print("Okay! Preparing to convert an integer")
                what_convert = True
                checking1 = False
            elif answer == "bin":
                print("Okay! Preparing to convert a binary number")
                what_convert = False
                checking1 = False
            else:
                print("Didn't recognize the input, please try again! (inputs should be 'int' or 'bin')")
        
        checking2 = True # Start the next loop to convert the binary/integer number
        if what_convert == True: # This means we are going to convert an integer to a binary number
            while(checking2):
                print("\nPlease input an integer value:")
                integer = input()
                binary = [0,0,0,0] # Initialize our binary number
                try:
                    integer = int(integer) # Make sure it's an integer, or something that can be made into a number at least
                except:
                    print("\n\tYou didn't input an integer! Inputted value: " + str(integer))
                    print("\tSending you back to the beginning as punishment...\n")
                    break
                if integer == 0: # If it's zero, we can just skip the rest of the stuff and break the loop now
                    checking2 = False
                    break
                negative = False
                if integer < 0: # CHeck if the number is negative
                    negative = True
                    integer = integer*-1 # If it is, make it positive
                
                count = 0 # start a counter 
                res = integer # save our integer into a result variable that we can modify without losing the original value
                failed = False # set a switch incase we fail
                while res != 0:
                    binary[count] = res % 2 # get the remaider of the result modulo 2
                    res = int(res/2) # get the integer value of the actual result / 2 (this is our next divide value)
                    count = count + 1 # count up
                    if count == 4 and res != 0: # If we've passed 4 counts and our result is still not 0
                        print("The number you inputted is too big! Please try again. We are only able to convert 4 bit numbers here!!")
                        res = 0 # reset the result to break the loop
                        failed = True # Let the loop know we failed
                    
                if failed == False: # If we didn't fail the previous step, continue on converting
                    if negative == True: # If our number was negative, convert back to make sure it is returned negative
                        # Copy the contents of our "binary" list into 3 separate variables
                        sign_magnitude_bits = binary.copy() # copy the array over to another variable
                        one_comp_bits = binary.copy() # copy the array over to another variable
                        two_comp_bits = binary.copy() # copy the array over to another variable

                        # Get the sign-magnitude version
                        if sign_magnitude_bits[3] == 0: # since our input is automatically converted to a positive integer, we can only convert back to negative IF our current number's MSB is 0
                            sign_magnitude_bits[3] = 1 # Make the MSB 1 to signifiy it's negative
                            sign_magnitude = str(sign_magnitude_bits[3]) + str(sign_magnitude_bits[2]) + str(sign_magnitude_bits[1]) + str(sign_magnitude_bits[0]) # Create the output string in MSB format
                        else: # If the current MSB is 1, then our original number is already too big 
                            sign_magnitude = "overflow"
                        
                        # Get the one's compliment version
                        if one_comp_bits[3] == 0: # since our input is automatically converted to a positive integer, we can only convert back to negative IF our current number's MSB is 0
                            for i in range(len(one_comp_bits)): # Go through the rest of the numbers, and flip their bits (as is ones compliment convention)
                                if one_comp_bits[i] == 1: # If the bit is 1, flip it to 0
                                    one_comp_bits[i] = 0
                                elif one_comp_bits[i] == 0: # If the bit is 0, flip it to 1
                                    one_comp_bits[i] = 1
                            one_comp = str(one_comp_bits[3]) + str(one_comp_bits[2]) + str(one_comp_bits[1]) + str(one_comp_bits[0]) # Create the output string in MSB format
                        else: # If our MSB is 1, then we've parsed a number to big for out 4 bit output
                            one_comp = "overflow"

                        # Get the two's compliment version
                        if two_comp_bits[3] == 0:
                            print(two_comp_bits)
                            for i in range(len(two_comp_bits)): # Go through the rest of the numbers, and flip their bits (as is twos compliment convention)
                                if two_comp_bits[i] == 1: # If the bit is 1, flip it to 0
                                    two_comp_bits[i] = 0
                                elif two_comp_bits[i] == 0: # If the bit is 0, flip it to 1
                                    two_comp_bits[i] = 1
                            adding = True
                            count = 0
                            print(two_comp_bits)
                            while(adding): # Now that we've flipped the bits, we're going to go through and add 1
                                if two_comp_bits[count] == 0: # If our current bit is 0, simply add a one, and stop trying to add 
                                    two_comp_bits[count] = 1
                                    adding = False # Stop the loop
                                elif two_comp_bits[count] == 1: # If out current bit is 1, then we have to move over to the next bit and see if that one is 1 or 0. For the current bit, make it 0
                                    two_comp_bits[count] = 0
                                count = count + 1 # up our count
                            two_comp = str(two_comp_bits[3]) + str(two_comp_bits[2]) + str(two_comp_bits[1]) + str(two_comp_bits[0]) # Create the output string in MSB format
                        else:
                            two_comp = "overflow"
                    
                    # Do stuff if the number isn't negative
                    else:
                        # Copy the contents of our "binary" list into 3 separate variables
                        sign_magnitude_bits = binary.copy() # copy the array over to another variable
                        one_comp_bits = binary.copy() # copy the array over to another variable
                        two_comp_bits = binary.copy() # copy the array over to another variable

                        # check if the binary number is an overflow
                        if sign_magnitude_bits[3] == 1: # since our input is automatically converted to a positive integer, we can only convert back to negative IF our current number's MSB is 0
                            sign_magnitude = "overflow"
                        else: # If our number isn't overflowing, then we can just print the output
                            sign_magnitude = str(sign_magnitude_bits[3]) + str(sign_magnitude_bits[2]) + str(sign_magnitude_bits[1]) + str(sign_magnitude_bits[0]) # Create the output string in MSB format
                        if one_comp_bits[3] == 1: # since our input is automatically converted to a positive integer, we can only convert back to negative IF our current number's MSB is 0
                            one_comp = "overflow"
                        else: # If our number isn't overflowing, then we can just print the output 
                            one_comp = str(one_comp_bits[3]) + str(one_comp_bits[2]) + str(one_comp_bits[1]) + str(one_comp_bits[0]) # Create the output string in MSB format
                        if two_comp_bits[3] == 1: # since our input is automatically converted to a positive integer, we can only convert back to negative IF our current number's MSB is 0
                            two_comp = "overflow"
                        else: # If our number isn't overflowing, then we can just print the output 
                            two_comp = str(two_comp_bits[3]) + str(two_comp_bits[2]) + str(two_comp_bits[1]) + str(two_comp_bits[0]) # Create the output string in MSB format
                    if negative == True and integer == 8: # Twos compliment check case
                        two_comp = "1000"
                    elif negative == True and integer == 1:
                        two_comp = "1111"

                    if sign_magnitude == "overflow" and one_comp == "overflow" and two_comp == "overflow": # Check if all of the numbers overflow, and if so, prompt for another input
                        print("The inputted number is too big! All outputs have overflowed, please input another (smaller) number!")
                    else: # If we're all good, print the output to the screen!
                        print("\tOUTPUTS ARE IN MSB (most significant bit) FORMAT\n\taka, 0001 = 1, 0100 = 4\n")
                        print("\tsign-magnitude:  \t" + sign_magnitude)
                        print("\tone's compliment:\t" + one_comp)
                        print("\ttwo's compliment:\t" + two_comp)
                        print("\nDo you want to convert another number? (Input 'y' for yes, input any key to stop)")
                        answer = input() # Ask if the user wants to continue, and if so, continue
                        if answer == "y" or answer == "Y": # if its a y or a Y as the input
                            checking2 = False # Stop the current integer loop, and go back to the beginning
                        else: # If they don't want to continue, we gotta turn off all of our loops 
                            checking1 = False 
                            checking2 = False
                            converting = False
        elif what_convert == False: # Case for integer to binary
            while(checking2):
                print("\nPlease input an 4-bit binary number value in MSB format (as in, 0001 = 1, 0100 = 4):")
                binary = str(input())
                failed = False
                if len(binary) != 4: # If our length is bigger or less than 4 (or, in layman terms, if it's not 4), throw an error
                    print("You didn't input a 4-bit binary number! Your input was " + str(len(binary)) + " bits")
                    print("Inputted binary number: " + binary)
                    failed = True # Flip the switch so we know we failed
                else:
                    for bit in binary:
                        try: # Check to make sure the bit is actually an integer
                            int(bit)
                        except: # If it's not an integer, throw an error!
                            print("One of your inputted bits is not a 1 or a 0! That's all it can be, what gives?!")
                            print("Inputted binary number: " + binary)
                            print("Bit in question: " + bit)
                            failed = True # Flip the switch so we know we failed
                            break
                        if int(bit) == 1 or int(bit) == 0: # If our current bit is either 1 or 0, then we're good
                            pass
                        else: # If it's not 1 or 0, then we need to throw an error!
                            print("One of your inputted bits is not a 1 or a 0! That's all it can be, what gives?!")
                            print("Inputted binary number: " + binary)
                            print("Bit in question: " + bit)
                            failed = True # Flip the switch so we know we failed
                            break
                if failed == False: # If we haven't already failed, then we can continue
                    binary_bits = [int(binary[0]), int(binary[1]), int(binary[2]), int(binary[3])]
                    if binary_bits[0] == 1: # If our MSB is 1, then we are working with a negative number!
                        # Get the sign magnitude integer
                        res = 0 # Start with a 0 value
                        for i in range(1, len(binary_bits)): # Iterate through the binary number, 1->3
                            res = 2*res + binary_bits[i] # multiple the result by 2, and add the current binary number (1 or 0)
                        sign_magnitude = res*-1 # Multiply by -1

                        # Get the ones compliment integer
                        one_comp_bits = binary_bits.copy()
                        for i in range(len(one_comp_bits)): # Go through the rest of the numbers, and flip their bits (as is ones compliment convention)
                                if one_comp_bits[i] == 1: # If the bit is 1, flip it to 0
                                    one_comp_bits[i] = 0
                                elif one_comp_bits[i] == 0: # If the bit is 0, flip it to 1
                                    one_comp_bits[i] = 1

                        # Now that we've inverted all of the bits, we can find the value
                        res = 0 # Start with a 0 value
                        for i in range(1, len(one_comp_bits)): # Iterate through the binary number, 1->3
                            res = 2*res + one_comp_bits[i] # multiple the result by 2, and add the current binary number (1 or 0)
                        one_comp = res*-1 # Multiply by -1

                        # Get the twos compliment integer
                        if binary == "1111": # Catch case for if it's -1
                            two_comp = -1
                        elif binary == "1000": # Catch case for its -8
                            two_comp = -8
                        else:
                            two_comp_bits = [binary_bits[3],binary_bits[2],binary_bits[1],binary_bits[0]] # Reverse the order to LSB for minusing 1 
                            count = 0
                            while(True):
                                if two_comp_bits[count] == 1: # If our current bit is 1, then we need to "subtract"
                                    two_comp_bits[count] = 0 # make this bit 0
                                    if count != 0: # If we're at the very first, then we can't make the previous bit 1, its just nothing
                                        two_comp_bits[count-1] = 1 # If we're not at the first bit, then replace the previous bit with a 1
                                    break
                                count = count + 1
                            two_comp_bits = [two_comp_bits[3],two_comp_bits[2],two_comp_bits[1],two_comp_bits[0]] # Re-reverse the order to MSB so we can convert to an integer easier
                            # Go through the rest of the numbers, and flip their bits (as is twos compliment convention)
                            for i in range(len(two_comp_bits)): 
                                if two_comp_bits[i] == 1: # If the bit is 1, flip it to 0
                                    two_comp_bits[i] = 0
                                elif two_comp_bits[i] == 0: # If the bit is 0, flip it to 1
                                    two_comp_bits[i] = 1
                            
                            # Now that we've flipped the bits, we can add up the number
                            res = 0
                            for i in range(1, len(two_comp_bits)): # Iterate through the binary number, 1->3
                                res = 2*res + two_comp_bits[i] # multiple the result by 2, and add the current binary number (1 or 0)
                            two_comp = res*-1 # Multiply by -1
                        
                    else: # If we are not working with a negative number, the binary to integer is not different for each algorithm!
                        res = 0 # Start with a 0 value
                        for i in range(1, len(binary_bits)): # Iterate through the binary number, 1->3
                            res = 2*res + binary_bits[i] # multiple the result by 2, and add the current binary number (1 or 0)
                        # The value for each is just the result from above, so set them all equal to that value
                        sign_magnitude = res # Save the result
                        one_comp = res # Save the result
                        two_comp = res # Save the result

                    print("\tOUTPUTS:\n")
                    print("\tsign-magnitude:  \t" + str(sign_magnitude))
                    print("\tone's compliment:\t" + str(one_comp))
                    print("\ttwo's compliment:\t" + str(two_comp))
                    print("\nDo you want to convert another number? (Input 'y' for yes, input any key to stop)")
                    answer = input() # Ask if the user wants to continue, and if so, continue
                    if answer == "y" or answer == "Y": # if its a y or a Y as the input
                        checking2 = False # Stop the current integer loop, and go back to the beginning
                    else: # If they don't want to continue, we gotta turn off all of our loops 
                        checking1 = False 
                        checking2 = False
                        converting = False
                        
def two2dec():
    """
    Description
    ----------
    Converts an 8-bit binary number to a decimal using two's compliment
    
    Parameters
    ----------
        none, however prompts for an input
        bits: the 8-bit binary number provided by the user

    Returns
    -------
        Nothing, but outputs adecimal converted from the 8-bit binary number input
    """
    converting = True
    while(converting):
        print("\nPlease input an 8-bit binary number value in MSB format (as in, 0001 = 1, 0100 = 4):")
        bits = str(input())
        failed = False
        if len(bits) != 8: # If our length is bigger or less than 4 (or, in layman terms, if it's not 4), throw an error
            print("You didn't input a 8-bit binary number! Your input was " + str(len(bits)) + " bits")
            print("Inputted binary number: " + bits)
            failed = True
        else:
            for bit in bits:
                try: # Check to make sure the bit is actually an integer
                    int(bit)
                except: # If it's not an integer, throw an error!
                    print("One of your inputted bits is not a 1 or a 0! That's all it can be, what gives?!")
                    print("Inputted binary number: " + bits)
                    print("Bit in question: " + bit)
                    failed = True
                    break
                if int(bit) == 1 or int(bit) == 0: # If our current bit is either 1 or 0, then we're good
                    pass
                else: # If it's not 1 or 0, then we need to throw an error!
                    print("One of your inputted bits is not a 1 or a 0! That's all it can be, what gives?!")
                    print("Inputted binary number: " + bits)
                    print("Bit in question: " + bit)
                    failed = True
                    break
        if failed == False: # If we haven't failed, lets continue
            if int(bits[0]) == 1:
                # Get the negative twos compliment decimal
                if bits == "11111111": # Catch case for if it's -1
                    two_comp = -1
                elif bits == "10000000": # Catch case for its -8
                    two_comp = -128
                else:
                    two_comp_bits = [int(bits[7]),int(bits[6]),int(bits[5]),int(bits[4]),int(bits[3]),int(bits[2]),int(bits[1]),int(bits[0])] # Reverse the order to LSB for minusing 1 
                    count = 0
                    while(True):
                        if two_comp_bits[count] == 1: # If our current bit is 1, then we need to "subtract"
                            two_comp_bits[count] = 0 # make this bit 0
                            if count != 0: # If we're at the very first, then we can't make the previous bit 1, its just nothing
                                two_comp_bits[count-1] = 1 # If we're not at the first bit, then replace the previous bit with a 1
                            break
                        count = count + 1
                    two_comp_bits = [two_comp_bits[7],two_comp_bits[6],two_comp_bits[5],two_comp_bits[4],two_comp_bits[3],two_comp_bits[2],two_comp_bits[1],two_comp_bits[0]] # Re-reverse the order to MSB so we can convert to an integer easier
                    # Go through the rest of the numbers, and flip their bits (as is twos compliment convention)
                    for i in range(len(two_comp_bits)): 
                        if two_comp_bits[i] == 1: # If the bit is 1, flip it to 0
                            two_comp_bits[i] = 0
                        elif two_comp_bits[i] == 0: # If the bit is 0, flip it to 1
                            two_comp_bits[i] = 1
                    
                    # Now that we've flipped the bits, we can add up the number
                    res = 0
                    for i in range(1, len(two_comp_bits)): # Iterate through the binary number, 1->3
                        res = 2*res + two_comp_bits[i] # multiple the result by 2, and add the current binary number (1 or 0)
                    two_comp = res*-1 # Multiply by -1
            else:
                two_comp_bits = [int(bits[0]),int(bits[1]),int(bits[2]),int(bits[3]),int(bits[4]),int(bits[5]),int(bits[6]),int(bits[7])] # save the input into an array
                res = 0 # get a starting value
                for i in range(1, len(two_comp_bits)): # Iterate through the binary number, 1->3
                    res = 2*res + two_comp_bits[i] # multiple the result by 2, and add the current binary number (1 or 0)
                two_comp = res

            print("\n\tOUTPUTS:\n")
            print("\ttwo's compliment decimal:\t" + str(two_comp))
            print("\nDo you want to convert another number? (Input 'y' for yes, input any key to stop)")
            answer = input() # Ask if the user wants to continue, and if so, continue
            if answer == "y" or answer == "Y": # if its a y or a Y as the input
                pass # Do nothing
            else: # If they don't want to continue, we gotta turn off all of our loops 
                converting = False



def dec2float():
    """
    Description
    ----------
    Converts an decimal input to a 8-bit binary float
    
    Parameters
    ----------
        none, however prompts for an input
        dec: The inputted decimal by the user

    Returns
    -------
        Nothing, but outputs the binary float converted from the inputted decimal
    """
    print("\n-- DECIMAL TO 8-BIT BINARY FLOATING POINT --\n-- Finicky with large numbers --")
    converting = True
    while(converting):
        failed = False # A switch to see if the input was bad
        negative = False # A switch to see if we are dealing with a negative number
        print("\nEnter 'end' to stop")
        print("Please input a number to convert to binary (Can be an int or float):")
        dec = input() # Get the user input
        if dec.lower() == "end":
            converting = False
            break
        try: # See if we can convert the inputted number to a float - if so, we are good to go
            dec = float(dec)
        except: # If not, they must've inputted an unsable character
            print("\nThe inputted value was not able to convert to a number! Input: " + str(dec))
            failed = True # Flip the switch

        if failed == False: # If we haven't failed yet, we can continue
            if dec < 0: # if our number is negative, convert it to positive and store the data that it's negative
                negative = True # Flip the switch
                dec = dec*-1

            # Initialize some data containers
            binary_decimal = [] # Holds the numbers to the right of the decimal
            binary_number = [] # Holds numbers to the left of the decimal
            binary = "" # Holds the final number

            # Get the values to the right of the decimal point
            res = dec % 1 # Get the decimal value
            only_int = False # Make a switch
            if res == 0.0: # If we don't have any decimals, we need to remember that for later down the line
                only_int = True # Flip the switch
            while(res != 0): # Go through an algorithm until we equal 0
                res = res*2 # First, muliply the current value (which is the original decimal) by 2
                binary_decimal.append(int(res)) # Get the either 1 or 0 value from multiplying that decimal by 2. A decimal multiplied by 2 will never be greater than 2, so we are guaranteed either a 1 or a 0. Add the number to our array
                res = res % 1 # Our new value is the decimal of the number we just found (if it's greater than 1) This will equal 0 if our number is on, or it'll be the next fraction we look at
            
            # Get the binary output of the whole number part
            res = int(dec) # Convert the float to an integer (squash the decimals)
            only_dec = False # Create a switch
            if res != 0: # if our current result from converting dec to an in is not automatically 0, we can do things
                while res != 0: # While our number isn't 0, computer an algorithm
                        binary_number.append(res % 2) # Add the remainder of the current value/2 to our binary number array - should either be a 0 or a 1
                        res = int(res/2) # Divide our current number by 2, and ditch the decimals
            else:
                only_dec = True # If it is, that means we only have decimals, so we need to note this for later

            # Create a string that represents our binary number in MSB format
            for i in range(len(binary_number)-1, -1, -1): # Iterate downward from the final index to 0
                binary = binary + str(binary_number[i]) # Save the binary number into MSB form from LSB form - The integer part of our binary number
            for i in range(len(binary_decimal)): # For every bit in the decimal part of our binary number, save it into the final string
                binary = binary + str(binary_decimal[i]) # build the string

            # Check if we have decimals
            if only_int: 
                binary = binary + "0" # If we are only rocking with integers, we need to add a padding .0 to make this a float
            if len(binary) != 5: # If our current value does not equal 5, we've messed up somewhere
                print("overflow error! The number you entered is too big, please input another number")
            else: # If we haven't overflowed
                for ii in range(len(binary)): # A loop to make sure our first value is not 0
                    if binary[0] == "0":
                        binary = binary[1:len(binary)] + "0"
                mantissa = binary[len(binary)-4:len(binary)] # Get the mantissa, the last 4 bits in 8-bit number
                if only_dec == True: # If we are only dealing with decimal values
                    count = 0 # start a counter
                    while(True): # Start looping
                        if binary_decimal[count] != 0: # count how long it takes to get to a number that's not 0
                            break # Once we reach it, stop looping
                        count = count + 1 # Keep counting until we get there
                    count = count + 1 # Once we've reached it, add 1 more to the final number so it is correct
                    exponent = (count*-1) + 3 # Our exponent is the count number (how many zero's we were away from the decimal on the right) - use this formula to get the exponent
                else:
                    exponent = len(binary_number)-1 + 3 # If we are not only dealing with decimals, our exponent is the length of our integer number
                res = exponent # Save the exponent value into a res variable for use below
                exponent_temp = [] # create a temp array
                count = 0 # Start another counter
                while count != 3: # While our counter isn't greater than 3
                    exponent_temp.append(res % 2) # convert our exponent integer number to binary form - add the remainder from our current value / 2 to our array (should be 1 or 0)
                    res = int(res/2) # divide our current number by 2, and ditch the decimals to use next iteration
                    count = count + 1 # Count up, because we only want to do this 3 times
                exponent = "" # rewrite the exponent value to be a string
                for i in range(len(exponent_temp)-1, -1, -1): # Iterate backwards to convert the binary number from LSB to MSB
                    exponent = exponent + str(exponent_temp[i])
                
                # Print out results!
                if negative == True: # If we were negative, we just flip the MSB to 1
                    print("\n\tYour floating point number is:")
                    print("\t" + "1" + exponent + mantissa)
                else: # If we weren't negative, our MSB is 0
                    print("\n\tYour floating point number is:")
                    print("\t" + "0" + exponent + mantissa)

def float2dec():
    """
    Description
    ----------
    Converts an 8-bit binary float to a decimal   
    
    Parameters
    ----------
        none, however prompts for an input
        dec: The inputted binary by the user

    Returns
    -------
        Nothing, but outputs the binary float converted from the inputted decimal
    """
    print("\n-- 8-BIT BINARY FLOAT TO DECIMAL --\n")
    converting = True
    while(converting):
        print("enter 'end' to stop")
        print("Please input an 8-bit binary number:")
        binary = str(input())
        if binary.lower() == "end":
            print()
            converting = False
            break
        failed = False
        if len(binary) != 8:
            print("\nYou didn't input an 8 bit binary number!\n\tInputted number size: " + str(len(binary)) + "\n\tInput: " + binary + "\n")
            failed = True
        else:
            for bit in binary:
                try:
                    int(bit)
                    if int(bit) == 1 or int(bit) == 0:
                        pass
                    else:
                        print("\none of your bits is not a 1 or 0, they need to be either 1 or 0!!!")
                        print("\n\tBit in question: " + str(bit))
                        print("\ttInput: " + binary)
                        failed = True
                except:
                    print("\nOne of the bits in your input was not a 1 or 0! What gives?\n\tBit in question: " + str(bit) + "\n\tInput: " + binary + "\n") 
                    break

        # Start actually doing the things
        if failed == False:
            sign = binary[0]
            exponent = [int(binary[1]), int(binary[2]), int(binary[3])]
            mantissa = binary[4:len(binary)]

            # Convert the exponent back to a number
            count = len(exponent)-1 # Our exponent value
            result = 0 # Since we're going to do a sum, let's set our inital sum value
            for i in range(len(exponent)): # Iterate through the entire exponent
                result = result + exponent[i]*(2**count) # Sum of the binary number multiplied by 2 to the power of the current index of the binary number (index starting at 0)
                count = count - 1 # Iterate down the index
            number_of_moves = result-3 # Get the exponent
            mantissa = "1" + mantissa # Get the original binary number 
            result = 0 # start a result tracker
            for i in range(len(mantissa)): # For the entire mantissa value (the binary number)
                result = result + int(mantissa[i])*(2**number_of_moves) # Convert the binary to an integer and sum it with the last value, and multiply it by the our current number of moves (being used as an exponent, after we pass the decimal, it becomes negative, so it makes a decimal number)
                number_of_moves = number_of_moves - 1 # Subtract our number of moves to get out new exponent
            if sign == "1": # If our fist bit was 1, then our nunmber is negative
                final_number = result*-1
            elif sign == "0": # If it was 0, our number is positive
                final_number = result
            # Print out results!
            print("\n\tYour floating point number is:")
            print("\t" + str(final_number) + "\n")

def main():

    logical = Logic()

    check1 = True
    check2 = False

    print("\nbit1: " + str(check1) + "\tbit2: " + str(check2))

    print("AND " + str(logical.AND_gate(check1, check2)))
    print("OR " + str(logical.OR_gate(check1, check2)))
    print("XOR " + str(logical.XOR_gate(check1, check2)))
    print("NOT " + str(logical.NOT_gate(check1)))
    print("NAND " + str(logical.NAND_gate(check1, check2)))
    print("NOR " + str(logical.NOR_gate(check1, check2)))
    print("XNOR " + str(logical.XNOR_gate(check1, check2)))

    four_bit_logic_circuit([0,1,0,0])
    four_bit_logic_circuit([1,1,1,0])
    four_bit_logic_circuit([0,0,0,1])

    # multiply 2 and 3
    two_bit([1,1], [0,1]) 

    # conversion() function
    conversion()

    # # two2dec() function
    two2dec()

    # dec2float() function
    dec2float()

    # float2dec function
    float2dec()


if __name__=="__main__":
    main()

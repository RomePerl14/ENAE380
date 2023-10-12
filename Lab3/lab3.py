"""
This is your template for lab3. Implement all questions in the appropriate 
function. Implement helper functions as needed with
a short (one-line) description of their purpose.
"""

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
    print("Would you like to convert an integer to a binary number, or a binary number to an integer? (int/bin)")
    checking = True
    while(checking):
        answer = input()
        if answer == "int":
            print("Okay! Preparing to convert an integer")
            what_convert = True
            checking = False
        elif answer == "bin":
            print("Okay! Preparing to convert a binary number")
            what_convert = False
            checking = False
        else:
            print("Didn't recognize the input, please try again! (inputs should be 'int' or 'bin')")
    
    checking = True
    if what_convert == True: # Converting an integer to a binary number
        while(checking):
            print("\nPlease input an integer value:")
            integer = input()
            try:
                integer = int(integer)
            except:
                print("You didn't input an integer! Input: " + str(integer))
                


    

def two2dec():
    """
    
    """
    # replace the line below with your implementation
    pass

def dec2float():
    """
    
    """
    # replace the line below with your implementation
    pass

def float2dec():
    """
    
    """
    # replace the line below with your implementation
    pass


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


if __name__=="__main__":
    main()

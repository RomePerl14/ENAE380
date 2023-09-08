# Romeo Perlstein
# Lab deliverable 2, ENME480 section 0102

# Sieve of Eratosthenes script


def main():
    print("\n")
    print("\tplease input the range you'd like to find all prime numbers in (default is 1000):")
    usr_input = input()
    if usr_input == "" or usr_input == None:
        usr_input = 1000
    int(usr_input)
    list_of_booleans = []
    list_of_primes = []
    for i in range(usr_input+1):
        list_of_booleans.append(True)
    p = 2

    ## Accidentally wrote a loop to find all odd numbers, leaving it here cause I thought it was neat
    # loop = True 
    # ii = 1
    # while(loop):
    #     if ii*p == usr_input:
    #         list_of_numbers.remove(ii*p)
    #         loop = False
    #         break
    #     print(int(ii*p))
    #     list_of_numbers.remove(int(ii*p))
    #     ii = ii + 1
    # print(list_of_numbers)
    # print(len(list_of_numbers))

    while(p*p <= usr_input): # Make sure that we are not overrunning out array
        if list_of_booleans[p] == True: # Default case
            for i in range(p*p, usr_input+1, p): # iterate through p*p to the usr_input, with a step of p
                list_of_booleans[i] = False # get rid of anywhere that there is non-prime numbers
        p = p+1 # iterate up

    for ii in range(2, usr_input+1): # Go through the boolean list to see where there are prime numbers and not prime numbers
        if list_of_booleans[ii] == True: # If there is a prime number, save it
            list_of_primes.append(ii) ## append it
    print(list_of_primes)
    print("There are " + str(len(list_of_primes)) + " prime numbers from 1 to " + str(usr_input))

        
    
if __name__ == "__main__":
    main()
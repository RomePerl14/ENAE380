# ROMEO PERLSTEIN
# SECTION: 0102

import random, time # Used for selecting a random card, and use for sleeping

def main():
    print("\n\t-- HEXADECIMAL BLACK JACK --")
    
    # Initialize some useful strings
    dealer = "---\t--- [DEALER] " # Dealer prompt
    dealers_hand = "---\t--- [DEALERS HAND] " # dealers hand prompt
    your_hand = "---\t--- [YOUR HAND] " # Your hand prompt
    dealt_card = "---\t--- --- [New Card]: " # New card
    secret_card = "---\t--- --- [New Card]: 0x--" # New card (dealer)
    secret_card_name = "0x--"
    round_prompt = "\n---\t[Dealer] Would you like another card? (hit = y, hold = n)" # New card prompt
    deck = {"0x00":0, "0x01":2,"0x02":2,"0x03":3,"0x04":4,"0x05":5,"0x06":6,"0x07":7,"0x08":8,"0x09":9,"0x0a":10,"0x0b":11,"0x0c":12,"0x0d":13,"0x0e":14,"0x0f":15} # Dictionary containing all of the cards and their values
    deck_names = list(deck.keys()) # Deck of card names

    # Start the game
    playing = True # Playing switch
    while(playing):
        dealers_current_hand = [] # initializer for dealers current hand (to display to the player)
        dealers_real_current_hand = [] # Initializer for the dealers actual hand
        your_current_hand = [] # Players actual hand    
        print("\n\t--- RULES ---\n\t- Dealer and Player both start with two cards\n\t- Card values: " + str(deck) + "\n\t- Dealer draws until deck value is greater than 28\n\t- First to 31 wins")
        print("\n---\tWould you like to start a new game? (y/n)") # Ask the user if they want to play
        answer = input()
        if answer.lower() == "n": # If the answer is no, say bye
            print("\n---\tThanks for playing, goodbye!\n")
            playing = False # Make sure we don't loop again
        elif answer.lower() == "y": # Continue if the answer is yes
            print("\n---\tAlright, lets play!")

            # Get your first card
            print(dealer + "Here is your first card: ")
            new_card_index = random.randint(0,14) # Get a random index from 0->14
            print(dealt_card + deck_names[new_card_index]) # Print out the dealt card
            your_current_hand.append(deck_names[new_card_index]) # Add it your the list for your hand
            print(your_hand + str(your_current_hand)) # Print out your current hand
            print() # padding print for readability
            time.sleep(1) # Sleep

            # Get the dealers first card
            print(dealer + "Dealers first card: ")
            new_card_index = random.randint(0,14) # Get another random index to pick a card from
            print(dealt_card + deck_names[new_card_index]) # Print out the dealt card
            dealers_current_hand.append(deck_names[new_card_index]) # save the current card into the dealers hand
            dealers_real_current_hand.append(deck_names[new_card_index]) # Save the dealers current hand into a non-displayed list (to keep their second card a secret until we've finished hitting)
            print(dealers_hand + str(dealers_current_hand)) # Print out the dealers current deck
            print()
            time.sleep(1) # Sleep

            '''
            The next two blocks of code repeat the same process, see above comments for indepth explanation
            '''

            # Get your second card
            print(dealer + "Here is your second card: ")
            new_card_index = random.randint(0,14)
            print(dealt_card + deck_names[new_card_index])
            your_current_hand.append(deck_names[new_card_index])
            print(your_hand + str(your_current_hand))
            print()
            time.sleep(1)

            # Get the dealers second card
            print(dealer + "Dealers second card: ")
            new_card_index = random.randint(0,14)
            print(secret_card) # The only difference is that we're keeping the dealers second card a secret
            dealers_current_hand.append(secret_card_name) # add the secret card to the dealers displayed hand for printing
            dealers_real_current_hand.append(deck_names[new_card_index]) # Add the real drawn card to the dealers real hand
            print(dealers_hand + str(dealers_current_hand)) # Print the dispaly version of the dealers hand
            print()
            time.sleep(1)

            # Give the player their chance to get more cards
            game_end = False # switch incase the game ends "early"
            hitting = True # loop for us to keep adding cards
            while(hitting):
                # Sum up your current hand
                your_hand_amount = 0 # Save your starting amount
                for i in range(len(your_current_hand)):
                    your_hand_amount = your_hand_amount + deck[your_current_hand[i]] # Add the current value of your hand plus the value of the next card, using the deck dictionary
                print()

                # Display your hand and the dealers hand
                print(your_hand + "Your current hand: " + str(your_current_hand))
                print(your_hand + "Your current hands value: " + str(your_hand_amount))
                print("---\t---")
                print(dealer + "Dealers current hand: " + str(dealers_current_hand))
                print(dealer + "Dealers current hands value: ???")
                if your_hand_amount > 31: # If we continue to hit, and our card value is over 31, we've automatically lost
                    print("\n" + dealer + "Bust, better luck next time!")
                    print("---\t--- YOU LOSE --- ")
                    print("--------------------------------------------------\n")
                    time.sleep(7.5)
                    game_end = True # Make sure to not contiue after we break this loop
                    hitting = False # flip the loop off
                    break # break the loop

                print(round_prompt) # Print the prompt to as the user if they want to hit or hold
                answer = input()
                if answer.lower() == "y": # If we hit, add another card
                    # same method as above, get a random integer, save the card at that index, and then print the hand
                    print(dealer + "Here is your next card: ")
                    new_card_index = random.randint(0,14)
                    print(dealt_card + deck_names[new_card_index])
                    your_current_hand.append(deck_names[new_card_index])
                    print(your_hand + str(your_current_hand))
                    print()
                    time.sleep(1)
                elif answer.lower() == "n": # If we haven't let's move on
                    print(dealer + "Gotcha, revealing my hand now")
                    print()
                    hitting = False # Stop the loop
                else:
                    print("---\tI didn't understand your input, could you try again?") # If you said something funky, prompt again
            
            if game_end == False:
                # Let the dealer get their cards
                holding = True # Looping variable
                print("---\t--- REVEALING DEALERS CARD:") # reveal the dealers second card
                print(dealers_hand + str(dealers_real_current_hand)) # print the dealers second card
                time.sleep(5) # sleep so the player can see the hand
                while(holding):
                    dealers_hand_amount = 0 # set this value to 0 every time so we sum the deck correctly every loop
                    for i in range(len(dealers_real_current_hand)):
                        dealers_hand_amount = dealers_hand_amount + deck[dealers_real_current_hand[i]] # Add the current value of dealers hand to the next card in the hand, using the deck dictionary

                    # Print out the hands of the dealer and the player
                    print(your_hand + "Your current hand: " + str(your_current_hand))
                    print(your_hand + "Your current hands value: " + str(your_hand_amount))
                    print("---\t---")
                    print(dealer + "Dealers current hand: " + str(dealers_real_current_hand))
                    print(dealer + "Dealers current hands value: " + str(dealers_hand_amount))
                    print()
                    if dealers_hand_amount > 31: # If we've gone over 31, the dealer LOST (get OWNED DEALER)
                        print("\n" + dealer + "House Busts, congrats!")
                        print("---\t--- YOU WIN --- ")
                        print("--------------------------------------------------\n")
                        time.sleep(7.5)
                        game_end = True
                        holding = False
                        break
                    if dealers_hand_amount > 28: # If the dealer has gone over 28, stop getting more cards
                        break
                    time.sleep(5)

                    # Again, same thing as above, get a new random int, find the card in the deck, add it to the hand, and then print the new hand and new card
                    print("---\t--- ---------------")
                    print(dealer + "Dealers new card: ")
                    new_card_index = random.randint(0,14)
                    print(dealt_card + deck_names[new_card_index])
                    dealers_real_current_hand.append(deck_names[new_card_index])
                    print(dealers_hand + str(dealers_real_current_hand))
                    print()
            
            # If we haven't premanturely ended the game
            if game_end == False:
                print()

                # Figure out who has the higher hand
                print(dealer + "Alright, lets see who's closer to 31")
                time.sleep(1)
                # Print out the value of each hand
                print(your_hand + "Your hand amount: " + str(your_hand_amount))
                print(dealer + "Dealers hand amount: " + str(dealers_hand_amount))
                time.sleep(5)

                # Compare the values
                if your_hand_amount > dealers_hand_amount: # If our value is greater, we win
                    print(dealer + "Looks like you win, congrats!")
                    print("---\t--- YOU WIN --- ")
                    print("--------------------------------------------------\n")
                    time.sleep(7.5)
                elif your_hand_amount < dealers_hand_amount: # If the dealers value is greater, we lose
                    print(dealer + "Looks like the House wins, better luck next time.")
                    print("---\t--- YOU LOSE --- ")
                    print("--------------------------------------------------\n")
                    time.sleep(7.5)
                elif your_hand_amount == dealers_hand_amount: # IF we tie, it's just as bad as losing
                    print(dealer + "Looks like we've tied. Better luck next time")
                    print("---\t--- TIE (just as bad as a loss) --- ")
                    print("--------------------------------------------------\n")
                    time.sleep(7.5) 
                else: # catch something that should never ever happen
                    print("---\t--- This isn't supposed to happend, what gives?")
                    print("---\t--- WAIT, WHAT? --- ")
                    print("--------------------------------------------------\n")
                    time.sleep(7.5) 

        else: # Catch bad inputs
            print("---\tI didn't understand your input, could you try again?")


if __name__ == "__main__":
    main()
"""
This is your template for lab1. Implement all questions in the appropriate 
function. You are encouraged to implement helper functions as needed with
a short (one-line) description of their purpose.
"""

# Romeo Perlstein, section 0102
# Hopefully this code is fun to read!

import time, textstat

class Lab1(object):
	def average(self, input_number1=None, input_number2=None): # Usr inputs, with default values
		"""
		Finds the average of two numbers.


		Parameters
		----------
		input_number1 : float
			First input from user

		input_number2 : float
			Second input from user


		Returns
		-------
		result: float
			the average of the two numbers input by user
		"""

		#Replace the line below with your implementation.
		print("\n\t--NUMBER AVERAGE FINDER--\n   Finds the average between two numbers\n") # intro to the method

		## Could implement some try-catch statements, but I'm lazy ##

		# Check to see if the user inputted numbers in the function
		if input_number1 == None: # If they haven't, get an input
			print("First number input not detected, please input desired first number: ")
			input_number1 = float(input())
		else: # If there is an input, make it a float (because)
			input_number1 = float(input_number1)

		# Do the same thing as above except for the 
		if input_number2 == None:
			print("Second number input not detected, please input desired first number: ")
			input_number2 = float(input())
		else:
			input_number2 = float(input_number2)
		
		result = (input_number1+input_number2)/2 # hardcoding the number two because it only takes in two numbers anyway
		print("The average between " + str(input_number1) + " and " + str(input_number2) + " is " + str(result))
		return result # return the result for use outside of the class
	

	def money(self, amount=None):
		"""
		Write your function descriptor here.
		
		Returns change for the given input amount, attempting to maximize the amount of large denominations
		and minimizing the amount of 1's and 4's 

		Parameters
		----------
		amount : int

		Returns
		----------
		change : dict
		A dictionay containing the amount of coins per each denomination
		Key - the denomination (15, 4, 1)
		Value - the amount of said denomination
	
		"""
		print("\n\t--- CHANGE MAKER ---\nReturns change for the inputted amount of money\n")

		if amount == None:
			print("No input detected, please input the amount of money you would like change for:")
			amount = input() # Get the input if there is none
			try: # Check if it's an integer
				amount = int(amount)
			except: # If it's not, check what it is
				try: # If it's a float, yell at the user, and then prompt again
					float(amount)
					print("You inputted a float, I only take EXACT change!")
					print("\nPlease input the amount of money you would like change for (Exact change only):")
					amount = input()
					try: # If their second try fails, then kick em out of the program
						amount = int(amount)
					except:
						print("Thats it, you're done! No change for you!")
						return
				except: # if it's not a float, yell again at the user and prompt for an input
					print("You didn't even input a number! What gives?")
					print("\nPlease input the amount of money you would like change for (Exact change, and a NUMBER please):")
					amount = input()
					try: # If their second try fails, then kick em out of the program
						amount = int(amount)
					except:
						print("Thats it, you're done! No change for you!")
						return
		else: # Do the exact same thing as above, but this case checks for inputted values
			try:
				amount = int(amount)
			except:
				try:
					float(amount)
					print("You inputted a float, I only take EXACT change!")
					print("\nPlease input the amount of money you would like change for (Exact change only):")
					amount = input()
					try:
						amount = int(amount)
					except:
						print("Thats it, you're done! No change for you!")
						return
				except:
					print("You didn't even input a number! What gives?")
					print("\nPlease input the amount of money you would like change for (Exact change, and a NUMBER please):")
					amount = input()
					try:
						amount = int(amount)
					except:
						print("Thats it, you're done! No change for you!")
						return

		print("\n\tInputted amount of coins: " + str(amount) + " cents")
		print("\tNow counting change...\n")

		# Initialize
		loop = True
		amount_15 = 0 
		amount_4 = 0
		amount_1 = 0

		# Subtract by 15 until we get below 0
		while(loop):
			amount = amount - 15
			if amount < 0: # If we get below 0, break the while loop
				loop = False
				amount = amount + 15
				break
			else:
				amount_15 = amount_15 + 1 # count up how many times we could subtract 15

		# do the same techinque for 4 and 1 cent coins
		loop = True
		while(loop):
			amount = amount - 4
			if amount < 0:
				loop = False
				amount = amount + 4
				break
			else:
				amount_4 = amount_4 + 1
		loop = True
		while(loop):
			amount = amount - 1
			if amount < 0:
				loop = False
				amount = amount + 1
				break
			else:
				amount_1 = amount_1 + 1

		# Create the dictionary we want to return for use outside of the class
		change = {}
		change["15 cent coins"] = amount_15
		change["4 cent coins"] = amount_4
		change["1 cent coins"] = amount_1

		time.sleep(2) # Sleep for dramatic effect
		print("Amount of 15 cent coins: " + str(change["15 cent coins"]))
		time.sleep(1)
		print("Amount of 4 cent coins: " + str(change["4 cent coins"]))
		time.sleep(1)
		print("Amount of 1 cent coins: " + str(change["1 cent coins"]))
		time.sleep(1)
		print("\n\tEnjoy your change!\n")
		return change

	def lyrics(self):
		"""
		Function that displays lyrics to a specific song by specific bands? 


		Parameters
		----------
		nada!

		Returns
		----------
		display output to terminal

		"""
		musicians = {}
		musicians["Lake Street Dive"] = """
		
		Hypothetically
Obviously, we're at the beginning of something
I don't expect you to know how it's gonna go
But I believe we might be onto something
And I just thought maybe you should know

I've been playing out a lot of hypotheticals in my mind
I've been writing your name down next to mine
Been imagining all the things you and I could do
I've seen all the posibilities in my dreams
You're alone when you should be livin' next to me
Baby, let's not wait and see

Immediate action is unnecessary
It's a fatal attraction, it's a little scary
But I got a plan of attack
And I'll get us there someday soon, I know it
I got a Plan A, and I got a Plan B
And if it's absolutely necessary, we'll go to Plan C
Whatever I gotta do to be with you

I've been playing out a lot of hypotheticals in my mind
I've been writing your name down next to mine
Been imagining all the things you and I could do
I've seen all the posibilities in my dreams
You're alone when you should be livin' next to me
Baby, let's not wait and see

Nobody can see into the future
Even the weatherman gets caught in the rain sometimes
But I see something in you that I've never seen before
And I can't be sure, no, maybe not
But I think it's worth a shot

Hypothtically, yes
Theoretically, forever
We'll see what happens
But I hope we will never be apart
Hypothetically, yes
Theoretically, forever
We'll see what happens
But I hope we will never be apart

Oh, hypothetically, yes
Theoretically, forever
We'll see what happens
But I hope we will never be apart
Oh, hypothetically, yes
Theoretically, forever
We'll see what happens
But I hope we will never be apart

I've been playing out a lot of hypotheticals in my mind
(Playing out a lot of hypotheticals)
I've been writing your name down next to mine
(I've been writing your name down next to mine)
Been imagining all the things you and I could do
I've seen all the possibilities in my dreams (all the possibilities)
You're alone when you should be livin' next to me (oh, yeah)
Baby, let's not wait and see
"""

		musicians["Bob Dylan"] = """

		Knocking on Heavens Door
Mama, take this badge off of me
I can’t use it anymore
It’s gettin’ dark, too dark for me to see
I feel like I’m knockin’ on heaven’s door

Knock, knock, knockin’ on heaven’s door
Knock, knock, knockin’ on heaven’s door
Knock, knock, knockin’ on heaven’s door
Knock, knock, knockin’ on heaven’s door

Mama, put my guns in the ground
I can’t shoot them anymore
That long black cloud is comin’ down
I feel like I’m knockin’ on heaven’s door

Knock, knock, knockin’ on heaven’s door
Knock, knock, knockin’ on heaven’s door
Knock, knock, knockin’ on heaven’s door
Knock, knock, knockin’ on heaven’s door
"""
		musicians["Taylor Swift"] = """

		Love Story
We were both young when I first saw you
I close my eyes and the flashback starts
I'm standin' there
On a balcony in summer air
See the lights, see the party, the ball gowns
See you make your way through the crowd
And say, "Hello"
Little did I know

That you were Romeo, you were throwin' pebbles
And my daddy said, "Stay away from Juliet"
And I was cryin' on the staircase
Beggin' you, "Please don't go, " and I said

Romeo, take me somewhere we can be alone
I'll be waiting, all there's left to do is run
You'll be the prince and I'll be the princess
It's a love story, baby, just say, "Yes"

So I sneak out to the garden to see you
We keep quiet, 'cause we're dead if they knew
So close your eyes
Escape this town for a little while, oh oh

'Cause you were Romeo, I was a scarlet letter
And my daddy said, "Stay away from Juliet"
But you were everything to me
I was beggin' you, "Please don't go, " and I said

Romeo, take me somewhere we can be alone
I'll be waiting, all there's left to do is run
You'll be the prince and I'll be the princess
It's a love story, baby, just say, "Yes"
Romeo, save me, they're tryna tell me how to feel
This love is difficult, but it's real
Don't be afraid, we'll make it out of this mess
It's a love story, baby, just say, "Yes"
Oh, oh

I got tired of waiting
Wonderin' if you were ever comin' around
My faith in you was fading
When I met you on the outskirts of town, and I said

Romeo, save me, I've been feeling so alone
I keep waiting for you, but you never come
Is this in my head? I don't know what to think
He knelt to the ground and pulled out a ring
And said, "Marry me, Juliet
You'll never have to be alone
I love you and that's all I really know
I talked to your dad, go pick out a white dress
It's a love story, baby, just say, "Yes"
Oh, oh, oh
Oh, oh, oh, oh
'Cause we were both young when I first saw you
"""
		musicians["George Gershwin"] = """

		Summertime
And the livin' is easy
Fish are jumpin'
And the cotton is high
Oh, your daddy's rich
And your ma is good-lookin'
So hush, little baby
Don't you cry

One of these mornings
You're going to rise up singing
Then you'll spread your wings
And you'll take the sky
But 'til that morning
There's a'nothing can harm you
With daddy and mammy standing by

[Instrumental]

One of these mornings
You're going to rise up singing
Then you'll spread your wings
And you'll take the sky
But 'til that morning
There's a'nothing can harm you
With daddy and mammy standing by
"""
		musicians["Paul McCartney"] = """

		Maybe I'm amazed
Maybe I'm amazed at the way you love me all the time
Maybe I'm afraid of the way I love you
Maybe I'm amazed at the the way you pulled me out of time
You hung me on a line
Maybe I'm amazed at the way I really need you

Maybe I'm a man, maybe I'm a lonely man
Who's in the middle of something
That he doesn't really understand

Maybe I'm a man and maybe you're the only woman
Who could ever help me
Baby, won't you help me to understand? Ooh

Maybe I'm a man, maybe I'm a lonely man
Who's in the middle of something
That he doesn't really understand

Maybe I'm a man and maybe you're the only woman
Who could ever help me
Baby, won't you help me to understand? Ooh-ooh-ooh, ah

Maybe I'm amazed at the way you're with me all the time
Maybe I'm afraid of the way I leave you
Maybe I'm amazed at the way you help me sing my song
Right me when I'm wrong
Maybe I'm amazed at the way I really need you

Oh, oh, oh
Hey-ey-hey
Oh, oh, oh, ooh-ooh-ooh
Yeah, yeah, yeah
Ooh
"""
		# print(musicians["Lake Street Drive"])
		# print(musicians["Bob Dylan"])
		# print(musicians["Taylor Swift"])
		# print(musicians["George Gershwin"])
		# print(musicians["Paul McCartney"])

		print("Lake Street Dive " + str(textstat.textstat.flesch_reading_ease(musicians["Lake Street Dive"])) + " " + str(textstat.textstat.flesch_kincaid_grade(musicians["Lake Street Dive"])))
		print("Bob Dylan " + str(textstat.textstat.flesch_reading_ease(musicians["Bob Dylan"])) + " " + str(textstat.textstat.flesch_kincaid_grade(musicians["Bob Dylan"])))
		print("Taylor Swift " + str(textstat.textstat.flesch_reading_ease(musicians["Taylor Swift"])) + " " + str(textstat.textstat.flesch_kincaid_grade(musicians["Taylor Swift"])))
		print("George Gershwin " + str(textstat.textstat.flesch_reading_ease(musicians["George Gershwin"])) + " " + str(textstat.textstat.flesch_kincaid_grade(musicians["George Gershwin"])))
		print("Paul McCartney " + str(textstat.textstat.flesch_reading_ease(musicians["Paul McCartney"])) + " " + str(textstat.textstat.flesch_kincaid_grade(musicians["Paul McCartney"])))


	def interest(self, prinicpal_amount=None, interest_rate=None, years_of_investment=None, compound_frequency=None):
		"""
		Calculates the compound interest of an investment for a certain period of time, at a certain frequency

		Parameters
		----------
		principal_amount : the inputted starting amount, in dollars
		interest_rate : The compound interest's interest rate
		years_of_investment : The planned length of investment time
		compound_frequency : the time that the interest rate is applied in

		Returns
		----------
		amount_earned : the amount of money earned

		"""
		print("\n\t--- INTEREST CALCULATOR ---")
		print(" Calculates the interest of a principal input\n")

		if prinicpal_amount == None: # If no prinicple amount inputted, make em input it
			print("No prinicpal amount inputted, please input a principal amount: ")
			prinicpal_amount = float(input())
		else:
			prinicpal_amount = float(prinicpal_amount) # If there is, save it (and make sure it's a float)
		if interest_rate == None: # If no interest rate, make em input one
			print("No interest rate detected, please input an interest rate (in decimal form, 5% = 0.05): ")
			interest_rate = float(input())
		else:
			interest_rate = float(interest_rate) # IF there is an input, save it (and make it a float)
		if years_of_investment == None: # If no inputted years of investment, make em input it
			print("No length of investment input detected, please input the desired length of investment (in years): ")
			years_of_investment = int(input())
		else:
			years_of_investment = int(years_of_investment) # If inputted, save the sucker
		if compound_frequency == None: # if no compound frequency, get the input
			print("No compound frequency detected please input the desired compound frequency (1 == annually, 12 = monthly, etc): ")
			compound_frequency = int(input())
		else:
			compound_frequency = int(compound_frequency) # Else, save it

		amount_earned = prinicpal_amount*(1+(.05/compound_frequency))**(compound_frequency*years_of_investment) # Do math
		amount_earned = round(amount_earned, 2) # Round the math to two decimal places, since it's currency
		
		# Print the information to the user
		print("\n\tTotal amount of interest earned after " + str(years_of_investment) + " years: ")
		print("\t" + str(amount_earned) + " dollars")
		print("\tinterested applied on every " + str(1/compound_frequency) + " year(s)\n")
		return(amount_earned)

	def coffee(self):
		"""
		Tries to guess the users coffee order through a series of questions


		Parameters
		----------
		None!

		"""
		print("\n\t--- AUTOMATIC COFFEE ORDERER ---") # Top print statement to signify code running
		print("Picks a coffee order based on a questionaire") # Descrpition of code to output to user

		# - local variable definitions - #
		self.error_statement = "\n---\nI'm not quite sure what you said, could you try answering again?\n---\n" # Generic Error Statement
		self.good_guess = False # Loop switch to see if the user liked out guess or not
		self.start = True # Loop to continually run the program if the user is unsatisfied
		self.on_off_switch = False # Switch to restart the questionaire

		while(self.start): # Main loop
			# Turn our switches "on" so that we can go through the process like normal
			self.good_guess = True
			self.on_off_switch = True
			print("-- ORDER START --")
			self.__coffee_prompter() # Start the prompting

		print("Thank you for using the Automatic Coffee Order!\n") # Goodbye statement to the user


	def __coffee_prompter(self): # A function to prompt the user for their first question
		print("\nIs it hot or cold out?") # First question
		self.__hot_or_cold() # Get the response, and move on
	
	def __hot_or_cold(self): # Function to read in the reponse of the user from the previous question, and then move the user forward
		response = input() # Get a response
		if "cold" == response.lower(): # If they said anything with the word cold, it's cold out
			print("\nOk, good to know that it's cold out (hopefully you are bundled up!)")
			while(self.on_off_switch): # Loop the next questionaire incase the make a mistake here
				print("Is is currently morning or evening?")
				self.__morning_evening2() # Call the morning evening input for the cold branch
		elif "hot" == response.lower():
			print("\nOk, good to know it's hot out!")
			while(self.on_off_switch):# Loop to the next questionaire
				print("Is it currently morning or evening?")
				self.__morning_evening() # Call the morning evening input for the hot branch
		else:
			print(self.error_statement) # Catch an error input
			print("Try typing:\n\thot\n\tcold\n\n")
			return
	
	## ------ HOT BRANCH ------ ##
	def __morning_evening(self): # Function to check if it's morning of evening for the hot branch, and then ask the next question
		reponse = input() # get the input
		if "morning" == reponse.lower(): # check for the word morning in the response
			print("\nI see, good morning then!")
			while(self.on_off_switch): # start another loop to make sure this question can be repeated upon mistake
				print("Ok, have you been yawning a lot?") # New question
				self.__yawning() # Get the yawning input
		elif "evening" == reponse.lower(): # check for the word evening in the response
			print("\nI see, good evening then! (like a vampire would say)")
			while(self.on_off_switch):
				print("Do you happen to be carrying your laptop, or a lot of books?") # New question
				self.__books_n_stuff() # Get the input from the new question
		else:
			print(self.error_statement) # IF they said something silly, return and reloop
			print("Try typing:\n\tmorning\n\tevening\n")
			return

	### -- MORNING BRANCH -- ###
	def __yawning(self): # Function to check if the user is yawning and then ask the next question
		response = input() # Get the input
		if "yes" == response.lower(): # if any affirmation in the input, punch it
			print("\nAh jeez, well hopefully some coffee will fix that right up! (Or sleep)")
			while(self.on_off_switch): # Start looping the new question
				print("Do you have younger kids at home? Or did you just come back from a workout? OR, are you just plain tired?") # New question
				self.__parent_workout_tired() # Get the input for the new question
		elif "no" == response.lower(): # if no is at all in the response, punch it this way
			print("\nThat's good to here, maybe you don't need coffee after all!")
			while(self.on_off_switch): # Start looping the new question
				print("Would you like the coffee for here or to go?") # new question
				self.__togo_or_dinein() # Get the input for the new question
		else:
			print(self.error_statement) # catch an error input and return the sucker to try again
			print("Try typing:\n\tyes\n\tno\n")
			return
		
	def __parent_workout_tired(self): # Function to ask if why the user is tired, and then suggest an order
		response = input() # Get the input
		if "i have kids" == response.lower() or "toddlers" in response.lower() or "younger" in response.lower(): # If kids, toddlers, or younger in the input, start the statement
			print("\nAh I see, the young folk got you tired! Well no worries, heres my suggestions:")
			print("\n\tYou should try a Double Shot Iced Latte, WITH a straw!\n") # Suggestion
			while(self.good_guess): # Start the loop to see if they like our suggestion
				print("Do you like my suggestion?") # New question
				self.__good_suggestion() # Loop
		elif "i was working out" == response.lower(): # If work is in the response, we go this way
			print("\nAh, well glad you got a work out in! If you keep it up you probably won't even need coffee! Here's my suggestion:")
			print("\n\tYou should try a Cold Brew!\n") # program response
			while(self.good_guess): # Start the loop for a new question
				print("Do you like my suggestion?") # New question
				self.__good_suggestion() # Get the input for the new question
		elif "i'm tired" == response.lower(): # Same as above
			print("\nI see, well no worries! We'll get you up and ready for the day (maybe try getting some sleep though ;D). Here's my suggestion:")
			print("\n\tI recommend trying a Double Espresso!\n")
			while(self.good_guess):
				print("Do you like my suggestion?")
				self.__good_suggestion()
		else:
			print(self.error_statement) # Catch an error and rerun the loop
			print("Try typing:\n\tI have kids\n\tI was working out\n\tI'm tired\n")
			return

	def __togo_or_dinein(self): # Function to check if the user would like to have the coffee for here or to go, and provide an order guess
		response = input() # Get the input
		if "here" == response.lower(): # if here or dine are in the response somewhere, we say that they're dining in
			while(self.on_off_switch): # loop for a new question
				print("\nDid you get a chance to alert the barista about the sugar being out?") # New question
				self.__let_barista_know() # Get the input for the new question
		elif "to go" == response.lower() or "togo" == response.lower(): # If to, togo, or go are in the response, we are giving them coffee to go
			print("\n\tI recommened a large Iced Latte!\n")
			while(self.good_guess): # loop for a new question
				print("Do you like my suggestion?") # New question
				self.__good_suggestion() # Get the response for the new question
		else:
			print(self.error_statement)
			print("Try typing:\n\there\n\tto go\n")
			return

	def __let_barista_know(self): # Function to check if the user let the barista know about sugar being out, and then ask the next question
		response = input() # Input acquiring
		if "yes" == response.lower(): # If yes is in response
			print("\n\tIn that case, I recommend getting an Iced Mocha!\n")
			while(self.good_guess): # Ask if it was a good guess
				print("Do you like my suggestion?")
				self.__good_suggestion() # Check to see if they liked the guess
		elif "no" == response.lower():
			print("\n\tIn that case, I recommend getting a Cappuccino!\n")
			while(self.good_guess): # Ask if they liked my guess
				print("did you like my suggestion?") 
				self.__good_suggestion() # Check to see if they did like it
		else:
			print(self.error_statement)
			print("Try typing:\n\tyes\n\tno\n")
			return
		
	### -- EVENING BRANCH -- ###

	def __books_n_stuff(self): # Function to see if the user is holding a lot of books, and then ask the next question
		response = input() # Get the input to the previous question
		if "yes" == response.lower():
			print("\n\tIn that case, I recommend an Iced Vanilla Red Eye\n")
			while(self.good_guess): # Ask if we made a good guess
				print("did you like my suggestion?")
				self.__good_suggestion() # check
		elif "no" == response.lower():
			print("\n\tIn that case, I recommend an Iced Chai Latte\n")
			while(self.good_guess): # Ask
				print("did you like my suggestion?")
				self.__good_suggestion() # Check
		else:
			print(self.error_statement)
			print("Try typing:\n\tyes\n\tno\n") # Catch
			return

	## ------- COLD BRANCH ------- ##
	# Note to reviewer: Everything below is the same type of model as above, ask a question, loop until they provide a good answer,
	# Then move on to the next question and loop again, etc etc... until we get to a guess

	def __morning_evening2(self): # Function to see if it's morning or evening for the cold branch, and then ask the next question
			morning_evening = input()
			if "morning" == morning_evening.lower():
				print("\nI see, good morning then!")
				while(self.on_off_switch):
					print("Ok, (for context, we are in New York, New York) are you visiting NYC, or do you live here?")
					self.__nyc()
			elif "evening" == morning_evening.lower():
				print("\nI see, good evening then! (like a vampire would say)")
				while(self.on_off_switch):
					print("Do you happen to be carrying your laptop, or a lot of books?")
					self.__books_n_stuff2()
			else:
				print(self.error_statement)
				print("Try typing:\n\tevening\n\tmorning\n")
				return
	
	### -- EVENING BRANCH -- ###
	def __books_n_stuff2(self): # Function to ask if the user is holding a lot of books, and then recommend a coffee
		response = input()
		if "yes" == response.lower():
			print("\n\tIn that case, I recommend a Larged Latte or Cappuccino!\n")
			while(self.good_guess):
				print("did you like my suggestion?")
				self.__good_suggestion()
		elif "no" == response.lower():
			print("\n\tIn that case, I recommend Herbal Tea or Hot Chocolate!\n")
			while(self.good_guess):
				print("did you like my suggestion?")
				self.__good_suggestion()
		else:
			print(self.error_statement)
			print("Try typing:\n\tyes\n\tno\n")
			return
		
	### -- MORNING BRANCH -- ###
	def __nyc(self): # Function to see if the user is from NYC (what?), and then ask the next question
		response = input()
		if "i live here" == response.lower():
			print("\nAh I see, a local. Well welcome back presumably!")
			while(self.on_off_switch):
				print("(For context, we apparently have a board of rotating specialty coffees)")
				print("Do you normally check out our board of rotating specialty coffees?")
				self.__did_you_even_look()
		elif "visiting" == response.lower():
			print("Welcome tourist!")
			print("\n\tI would recommend getting a classic Coffee with Cream and Sugar!\n")
			while(self.good_guess):
				print("did you like my suggestion?")
				self.__good_suggestion()
		else:
			print(self.error_statement)
			print("Try typing:\n\tI live here\n\tvisiting\n")
			return

	def __did_you_even_look(self): # Function to see if the user looked at the specials, and then ask a new question
		response = input()
		if "sometimes" == response.lower():
			print("\n\tIn that case, I recommended getting a Soy Latte!\n")
			while(self.good_guess):
				print("did you like my suggestion?")
				self.__good_suggestion()
		elif "what is that?" == response.lower() or "what is that" == response.lower():
			print("\nOh, it's a board where we display our different specialty coffees!")
			print("\n\tIn that case I would recommend you get the Bodega Drip Coffee!\n")
			while(self.good_guess):
				print("did you like my suggestion?")
				self.__good_suggestion()
		elif "of course" == response.lower() or "of course!" == response.lower():
			print("\nThanks for checking out our specials, glad to know someone is actually looking at them :)")
			while(self.on_off_switch):
				print("Would you happen to be a smoker, by any chance?")
				self.__do_I_smoke()
		else:
			print(self.error_statement)
			print("Try saying: \n\tSometimes\n\tWhat is that?\n\tOf course!\n")
			return
		
	def __do_I_smoke(self): # Function to see if the user is a cringe smoker (cringe), and then ask a new question
		response = input()
		if "yes" == response.lower():
			print("\nAh, well I would remcommend dropping that habit!")
			print("\n\tIn that case though, I would recommend getting an Americano!\n")
			while(self.good_guess):
				print("did you like my suggestion?")
				self.__good_suggestion()
		elif "no" == response.lower():
			print("\nThats great to hear! Smoking is no good")
			while(self.on_off_switch == True):
				print("Would you consider yourself a \"millenial?\"")
				self.__millenial_falcon()
		else:
			print(self.error_statement)
			print("Try saying\n\tyes\n\tno\n")
			return
		
	def __millenial_falcon(self): # Function to see if the user thinks they are a millenial, and then ask the next question
		response = input()
		if "yes" == response.lower():
			print("\n\tIn that case, I recommend you get the Flat White!\n")
			while(self.good_guess):
				print("did you like my suggestion?")
				self.__good_suggestion()
		elif "no" == response.lower():
			print("\n\t In that case, I recommend you get the Cortado!\n")
			while(self.good_guess):
				print("did you like my suggestion?")
				self.__good_suggestion()
		else:
			print(self.error_statement)
			print("Try typing:\n\tyes\n\tno\n")
			return

	def __good_suggestion(self): # Function to see if we made a good suggestion or not
		response = input()
		if "yes" == response.lower(): # If we did, turn off all of the switches so we can end the prorgam
			print("\nAwesome! Enjoy your coffee :)\n\n")
			self.good_guess = False # Turn off this switch so that we don't loop again
			self.on_off_switch = False # Turn all every switch to that we don't loop them
			self.start = False # We are going to loop at the very top, so turn off the while loop so we skip the next iteration
			return
		elif "no" == response.lower(): # If we did bad, reset the switches to false, and then when we begin the main loop, they will be set back to true
			print("\nDang! Sorry about my bad guess, let's run through it again and see if I can do better!\n\n")
			self.good_guess = False # Set this to false so we don't repeat it
			self.on_off_switch = False # Set this to false so that every previous function doesn't get called again
			return
		else:
			print(self.error_statement) # Throw an error statement
			print("Try typing:\n\tyes\n\tno\n")
			return


#If you want to test your methods within this code, first, create an object of the class Lab1
#Then, call the function that you want to test. Below, we instantiate the class Lab1, and then call
#the method "average" from that instantiation. You can do this for any of the methods that you write. 

obj_name = Lab1()
print("\t-- COFFEE PROMPTER --\n\n")
obj_name.coffee()
print("\n\n\n\n\t-- LYRICS CHECKER --\n\n")
obj_name.lyrics()
print("\n\n\n\n\t-- INTEREST CALCULATOR -- \n\n")
obj_name.money()
print("\n\n\n\n\t-- AVERAGE CALCULATOR --\n\n")
obj_name.average()
print("\n\n-- END LAB1 --\n\n")



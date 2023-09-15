"""
This is your template for lab1. Implement all questions in the appropriate 
function. You are encouraged to implement helper functions as needed with
a short (one-line) description of their purpose.
"""
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
		
		result = (input_number1*input_number2)/2 # hardcoding the number two because it only takes in two numbers anyway
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
			try:
				amount = int(input())
			except:
				raise ImportError("You didn't input a number! WHY???")
		else:
			int(amount)

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

		if prinicpal_amount == None:
			print("No prinicpal amount inputted, please input a principal amount: ")
			prinicpal_amount = float(input())
		else:
			prinicpal_amount = float(prinicpal_amount)
		if interest_rate == None:
			print("No interest rate detected, please input an interest rate (in decimal form, 5% = 0.05): ")
			interest_rate = float(input())
		else:
			interest_rate = float(interest_rate)
		if years_of_investment == None:
			print("No length of investment input detected, please input the desired length of investment (in years): ")
			years_of_investment = int(input())
		else:
			years_of_investment = int(years_of_investment)
		if compound_frequency == None:
			print("No compound frequency detected please input the desired compound frequency (1 == annually, 12 = monthly, etc): ")
			compound_frequency = int(input())
		else:
			compound_frequency = int(compound_frequency)

		amount_earned = prinicpal_amount*(1+(.05/compound_frequency))**(compound_frequency*years_of_investment)
		amount_earned = round(amount_earned, 2)
		
		print("\n\tTotal amount of interest earned after " + str(years_of_investment) + " years: ")
		print("\t" + str(amount_earned) + " dollars")
		print("\tinterested applied on every " + str(1/compound_frequency) + " year(s)\n")
		return(amount_earned)

	def coffee(self):
		"""
		Write your function descriptor here.


		Parameters
		----------
		None!

		"""
		print("\n\t--- AUTOMATIC COFFEE ORDERER ---")
		print("Picks a coffee order based on you inputs")
		self.error_statement = "\n---\nI'm not quite sure what you said, could you try answering again?\n---\n"
		self.looping = True

		while(True):
			self.__coffee_prompter()


	def __coffee_prompter(self):
		while(True):
			print("\nIs it hot or cold out?")
			self.__hot_or_cold()
	
	def __hot_or_cold(self):
		hot_or_cold = input()
		if "cold" in hot_or_cold.lower():
			print("cold")
		elif "hot" in hot_or_cold.lower():
			print("\nOk, good to know it's hot out!")
			while(True):
				print("Is it currently morning or evening?")
				self.__morning_evening()
		else:
			print(self.error_statement)
			return
		
	def __morning_evening(self):
		morning_evening = input()
		if "morning" in morning_evening.lower():
			print("\nI see, good morning then!")
			while(True):
				print("Ok, have you been yawning a lot?")
				self.__yawning()
		elif "evening" in morning_evening.lower():
			print("evening")
		else:
			print(self.error_statement)
			return

	### -- MORNING BRANCH -- ###
	def __yawning(self):
		yawning = input()
		if "yes" in yawning.lower() or "yea" in yawning.lower():
			print("\nAh jeez, well hopefully some coffee will fix that right up! (Or sleep)")
			while(True):
				print("Do you have younger kids at home? Or did you just come back from a workout? OR, are you just plain tired?")
				self.__parent_workout_tired()
		elif "no" in yawning.lower():
			print("That's good to here, maybe you don't need coffee after all!")
			while(True):
				
		else:
			print(self.error_statement)
			return
	def __parent_workout_tired(self):
		response = input()
		if "kids" in response.lower() or "toddlers" in response.lower() or "younger" in response.lower():
			print("Ah I see, the young folk got you tired! Well no worries, heres my suggestions:")
			print("\n\tYou should try a Double Shot Iced Latte, WITH a straw!\n")
			while(self.looping):
				print("Do you like my suggestion?")
				self.__good_suggestion()
		elif "work" in response.lower():
			print("Ah, well glad you got a work out in! If you keep it up you probably won't even need coffee! Here's my suggestion:")
			print("\n\tYou should try a Cold Brew!\n")
			while(self.looping):
				print("Do you like my suggestion?")
				self.__good_suggestion()
		elif "tired" in response.lower():
			print("I see, well no worries! We'll get you up and ready for the day (maybe try getting some sleep though ;D). Here's my suggestion:")
			print("\n\tI recommend trying a Double Espresso!\n")
			while(self.looping):
				print("Do you like my suggestion?")
				self.__good_suggestion()
		else:
			self.error_statement
			return

	def __togo_or_dinein(self):
		pass


	def __good_suggestion(self):
		response = input()
		if "yes" in response.lower() or "yea" in response.lower():
			print("\nAwesome! Enjoy your coffee :)\n\n")
			self.looping = False
			return
		elif "no" in response.lower():
			print("\nDang! Sorry about my bad guess, let's run through it again and see if I can do better!\n\n")
			self.looping = False
			return
		else:
			print(self.error_statement)
			return



	





#If you want to test your methods within this code, first, create an object of the class Lab1
#Then, call the function that you want to test. Below, we instantiate the class Lab1, and then call
#the method "average" from that instantiation. You can do this for any of the methods that you write. 

obj_name = Lab1()
# obj_name.coffee()
obj_name.coffee()
# obj_name.lyrics()
# obj_name.money(223895)
# obj_name.average(input_number2=2023)



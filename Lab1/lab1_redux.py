import textstat

'''
Romeo Perlstein, section 0102


LAB 1 resubmission for lyrics()
'''

 # Creating a temp class

class Lab1Redux():
        
    '''
    Only changes made from the inital submission were the selection of lyrics chosen.
    I original choose to do the full song for goofs but it unfortunately let to my 
    numbers from the textstat function being less that 0 (which, on textstat's website
    isn't possible? At least from what I read). Rather than the whole song, I reduced
    the section to only be two stanzas (I think that's what they're called). 

    Even though the results are better, I'm still somewhat confused at what the textstat
    functions actually look for. I've tried adding periods, removing "\n" or enters, 
    getting rid of or adding back the title, but nothing seems to make it get a better or 
    worse score. As far as I can tell, the only thing that changed was the amount of text
    the function was looking through!
    '''
    def lyrics(self):
        """
        Description
        ----------
        Function that displays lyrics to a specific song by specific bands? 

        Parameters
        ----------
            nada!

        Returns
        ----------
            display output to terminal

        """
        musicians = {} # initialize the dictionary

        # First song
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

"""
        # Second song
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

"""
        # Third Song
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

"""
        # Fourth song
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

"""
        # 5th song
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

        # Print the name, and then the scores dat they got
        print("Lake Street Dive \t" + str(textstat.textstat.flesch_reading_ease(musicians["Lake Street Dive"])) + " \t" + str(textstat.textstat.flesch_kincaid_grade(musicians["Lake Street Dive"])))
        print("Bob Dylan \t\t" + str(textstat.textstat.flesch_reading_ease(musicians["Bob Dylan"])) + " \t" + str(textstat.textstat.flesch_kincaid_grade(musicians["Bob Dylan"])))
        print("Taylor Swift \t\t" + str(textstat.textstat.flesch_reading_ease(musicians["Taylor Swift"])) + " \t" + str(textstat.textstat.flesch_kincaid_grade(musicians["Taylor Swift"])))
        print("George Gershwin \t" + str(textstat.textstat.flesch_reading_ease(musicians["George Gershwin"])) + " \t" + str(textstat.textstat.flesch_kincaid_grade(musicians["George Gershwin"])))
        print("Paul McCartney \t\t" + str(textstat.textstat.flesch_reading_ease(musicians["Paul McCartney"])) + " \t" + str(textstat.textstat.flesch_kincaid_grade(musicians["Paul McCartney"])))


def main():
    redux = Lab1Redux()
    redux.lyrics()



if __name__ == "__main__":
    main()
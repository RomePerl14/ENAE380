"""
This is your template for lab5. Implement all questions in the appropriate
function. You are encouraged to implement helper functions as needed with
a short (one-line) description of their purpose.

Romeo Perlstein
Section 0102
"""

import cv2
import time

class Lab5():

    def calculate_spectrum(self, filePath, hide_output=False):
        """
        Reports the total intensity of each of the three colors of an image

        Parameters
        ----------
        filePath : str
            path to original image file
        hide_output : bool = False
            a flag to turn the text output on or off

        Returns
        -------
        result : (int, int, int)
            total intesities in each of the BGR color channels respectively

        """  
        read_image = cv2.imread(filePath)
        b = read_image[:,:,0]
        g = read_image[:,:,1]
        r = read_image[:,:,2]

        bluesum, greensum, redsum = 0, 0, 0
        # each r,g,b array is an array of arrays, with the first index representing a row of the image (height), and the second index representing a column of the image (width)
        for i in range(len(b)): # Iterate through every row of the image
            for ii in range(len(b[i])): # now iterate through every column of the current row we are on
                bluesum = b[i][ii] + bluesum # Add the intensities of the blue value at this specific pixel, in a summation sort of way
        
        # Do the same thing as above, except for the the G and R color channels of the image
        for i in range(len(g)):
            for ii in range(len(g[i])):
                greensum = g[i][ii] + greensum
        for i in range(len(r)):
            for ii in range(len(r[i])):
                redsum = r[i][ii] + redsum

        result = (bluesum, greensum, redsum) # Save the tuple
        # Print the result
        if (hide_output == False):
            print("Intensity of colors in B,G,R (summation of color intensity at each pixel)\n\tB: " + str(result[0]) + "\n\tG: " + str(result[1]) + "\n\tR: " + str(result[2]))
        return result

    def get_dominant_color(self, filePath, hide_output=False):
        """
        Outputs the most dominant color of an image

        Parameters
        ----------
        filePath : str
            path to original image file, stored as a string
        hide_output : bool = False
            a flag to turn the text output on or off

        Returns
        -------
        int
            0 for Blue, 1 for Green, 2 for Red

        """
        res = self.calculate_spectrum(filePath, hide_output=True)
        max_val = max(res)

        # Save a dictionary for color indicies
        colors = {0 : "Blue", 1: "Green", 2: "Red", -1: "Error"}
        looping = True
        count = 0
        while looping: # Iterate through the res tuple to find the first instance of the largest value
            if max_val == res[count]: # If the index value is the same as our found max value, save it
                color_index = count # save the color index
                looping = False # stop the loop
            count = count + 1 # Iterate up
            if count == len(res): # If we're at the length, just stop
                if looping != False: # If we're at length but we've already found the largest value, don't send an error
                    looping = False # If we're at length but we haven't stopped, then say we ran into an error (and stop)
                    color_index = -1
        if (hide_output == False): # Hides the output 
            print("Color with the highest intensity is: " + str(color_index) + " (Which is " + colors[color_index] + ")\n")
        return color_index
        

    def measure_runtime_numpy(self):
        """
        Measures the time it takes to run timing_numpy() on 'test_image.png'

        Returns
        -------
        float
            time taken to run timing_numpy
        """
        start_time = time.time() # Get the starting time
        self.timing_numpy("test_image.png") # run the timing_numpy() function
        elapsed_time = time.time()-start_time # Get the elapsed time in seconds
        
        # Print the elapsed time
        print("time elapsed for timing_numpy(): \n\t" + str(elapsed_time) + " seconds")

        # Return the value
        return elapsed_time


    def measure_runtime_python(self):
        """
        Calculates the time it takes to run timing_python() on on 'test_image.png'

        Returns
        -------
        float
            time taken to run timing_python

        """
        start_time = time.time() # Get the starting time
        self.timing_python("test_image.png") # run the timing_numpy() function
        elapsed_time = time.time()-start_time # Get the elapsed time in seconds
        
        # Print the elapsed time
        print("time elapsed for timing_python(): \n\t" + str(elapsed_time) + " seconds")

        # Return the value
        return elapsed_time


    def timing_numpy(self, filePath):
        """ Accesses each pixel of an image via numpy. Do not modify this function. """
        IMG=cv2.imread(filePath)
        info=IMG.shape
        for row in range(0,info[0]):
            for col in range(0,info[1]):
                Blue_pixel=IMG.item(row,col,0)
                Green_pixel=IMG.item(row,col,1)
                Red_pixel=IMG.item(row,col,2)


    def timing_python(self, filePath):
        """ Accesses each pixel of an image via python lists. Do not modify this function. """
        IMG=cv2.imread(filePath)
        info=IMG.shape
        for row in range(0,info[0]):
            for col in range(0,info[1]):
                Blue_pixel=IMG[row][col][0]
                Green_pixel=IMG[row][col][1]
                Red_pixel=IMG[row][col][2]

    def blur_image(self, filePath):
        """
        Blurs the input image using a Guassian filter.
        Note that the function takes a file path, not a loaded image, as input,
        per the Piazza discussion.

        Parameters
        ----------
        filePath : str
            path to original image file

        Returns
        -------
        numpy.ndarray
            the newly generated image

        """

        read_image = cv2.imread(filePath) # read the file 
        
        # Since we want to use the gaussian kernal, we can just call the gaussian blur function in opencv
        blurred_image = cv2.GaussianBlur(read_image, (5,5), 25) # Going with a 5x5 kernal size, because, well, I feel like it I guess. Also, sigmaX and sigmaY are 25 because I liked the blur result they provided, and setting it higher didn't change much
        return blurred_image

    def findoutlines(self, filePath):
        """
        Outputs and writes an image outlining the shapes contained in the input image

        Parameters
        ----------
        filePath : str
            path to original image file

        Returns
        -------
        numpy.ndarray
            the newly generated image
        """
        # read the file
        read_image = cv2.imread(filePath) 
        b = read_image[:,:,0] # Save the color, just in case
        g = read_image[:,:,1]
        r = read_image[:,:,2]

        # Set the image to greyscale
        greyscale = cv2.cvtColor(read_image, cv2.COLOR_BGR2GRAY)

        # Apply a threshold so we can get the binary image 
        res, thres = cv2.threshold(greyscale, 19, 225, 0) # Found that 20 worked best through experimentation

        # Now get the contours of the image
        contours, tree = cv2.findContours(thres, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # using RETR_TREE cause apparently it's the best one

        # Draw the contours
        cont_img = cv2.drawContours(read_image, contours, -1, (255,255,255), 1) # Draw the contours from the result, and make the outline white with a px width of 1 (or change it to whatever size you want)
        
        # Note, function works well with solid colors (like BlurMe.png and BlueSquare.png) but does not hold itself well against an image like tiger2.jpeg
        cv2.imwrite("PERLSTEIN_2b.png", cont_img)


def main():
    l = Lab5()
    # l.calculate_spectrum("test_image.png")
    # l.get_dominant_color("test_image.png")
    # l.measure_runtime_numpy()
    # l.measure_runtime_python()
    # l.blur_image("BlurMe.png")
    # l.findoutlines("BlueSquare.png")


if __name__ == "__main__":
    main()
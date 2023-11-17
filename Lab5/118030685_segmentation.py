import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

from matplotlib import colors
from mpl_toolkits.mplot3d import Axes3D  # noqa
from matplotlib.colors import hsv_to_rgb

# To get a list of all the possible colour conversions

flags = [i for i in dir(cv2) if i.startswith("COLOR_")]
print(len(flags), "flags total:")

print(flags[48])

# Let's look at our fish image

# nemo = cv2.imread("nemo/nemo0.jpg")
# plt.imshow(nemo)
# plt.show()

# # OpenCV by default opens images in BGR color space

# nemo = cv2.cvtColor(nemo, cv2.COLOR_BGR2RGB)

# plt.imshow(nemo)
# plt.show()

# # Plotting the image on 3D plot

# r, g, b = cv2.split(nemo)

# fig = plt.figure()
# axis = fig.add_subplot(1, 1, 1, projection="3d")
# pixel_colors = nemo.reshape((np.shape(nemo)[0] * np.shape(nemo)[1], 3))
# norm = colors.Normalize(vmin=-1.0, vmax=1.0)
# norm.autoscale(pixel_colors)
# pixel_colors = norm(pixel_colors).tolist()

# axis.scatter(
#     r.flatten(), g.flatten(), b.flatten(), facecolors=pixel_colors, marker="."
# )
# axis.set_xlabel("Red")
# axis.set_ylabel("Green")
# axis.set_zlabel("Blue")
# plt.show()

# hsv_nemo = cv2.cvtColor(nemo, cv2.COLOR_RGB2HSV)

# h, s, v = cv2.split(hsv_nemo)

# fig = plt.figure()
# axis = fig.add_subplot(1, 1, 1, projection="3d")

# axis.scatter(
#     h.flatten(), s.flatten(), v.flatten(), facecolors=pixel_colors, marker="."
# )
# axis.set_xlabel("Hue")
# axis.set_ylabel("Saturation")
# axis.set_zlabel("Value")
# plt.show()

# light_orange = (1, 190, 200)
# dark_orange = (18, 255, 255)

# # Normalise to 0 - 1 range for viewing

# lo_square = np.full((10, 10, 3), light_orange, dtype=np.uint8) / 255.0
# do_square = np.full((10, 10, 3), dark_orange, dtype=np.uint8) / 255.0

# plt.subplot(1, 2, 1)
# plt.imshow(hsv_to_rgb(do_square))
# plt.subplot(1, 2, 2)
# plt.imshow(hsv_to_rgb(lo_square))
# plt.show()

# # Segment Nemo using inRange() function

# mask = cv2.inRange(hsv_nemo, light_orange, dark_orange)

# # Bitwise-AND mask and original image

# result = cv2.bitwise_and(nemo, nemo, mask=mask)

# # Convert back to RGB in order to plot using `matplotlib.pyplot`

# plt.subplot(1, 2, 1)
# plt.imshow(mask, cmap="gray")
# plt.subplot(1, 2, 2)
# plt.imshow(result)
# plt.show()

# light_white = (0, 0, 200)
# dark_white = (145, 60, 255)

# lw_square = np.full((10, 10, 3), light_white, dtype=np.uint8) / 255.0
# dw_square = np.full((10, 10, 3), dark_white, dtype=np.uint8) / 255.0

# plt.subplot(1, 2, 1)
# plt.imshow(hsv_to_rgb(lw_square))
# plt.subplot(1, 2, 2)
# plt.imshow(hsv_to_rgb(dw_square))
# plt.show()

# mask_white = cv2.inRange(hsv_nemo, light_white, dark_white)
# result_white = cv2.bitwise_and(nemo, nemo, mask=mask_white)

# plt.subplot(1, 2, 1)
# plt.imshow(mask_white, cmap="gray")
# plt.subplot(1, 2, 2)
# plt.imshow(result_white)
# plt.show()

# final_mask = mask + mask_white

# final_result = cv2.bitwise_and(nemo, nemo, mask=final_mask)

# plt.subplot(1, 2, 1)
# plt.imshow(final_mask, cmap="gray")
# plt.subplot(1, 2, 2)
# plt.imshow(final_result)
# plt.show()

# blur = cv2.GaussianBlur(final_result, (7, 7), 0)

# plt.imshow(blur)
# plt.show()

# # Generalising the segmentation

# path = "nemo/nemo"

# nemos_friends = []
# for i in range(6):
#     friend = cv2.cvtColor(cv2.imread(path + str(i) + ".jpg"), cv2.COLOR_BGR2RGB)
#     nemos_friends.append(friend)


# def segment_fish(image):
#     """Attempts to segment the clown fish out of the provided image."""
#     hsv_image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
#     light_orange = (1, 190, 200)
#     dark_orange = (18, 255, 255)
#     mask = cv2.inRange(hsv_image, light_orange, dark_orange)
#     light_white = (0, 0, 200)
#     dark_white = (145, 60, 255)
#     mask_white = cv2.inRange(hsv_image, light_white, dark_white)
#     final_mask = mask + mask_white
#     result = cv2.bitwise_and(image, image, mask=final_mask)
#     result = cv2.GaussianBlur(result, (7, 7), 0)
#     return result

# results = [segment_fish(friend) for friend in nemos_friends]

# for i in range(1, 6):
#     plt.subplot(1, 2, 1)
#     plt.imshow(nemos_friends[i])
#     plt.subplot(1, 2, 2)
#     plt.imshow(results[i])
#     plt.show()

'''
Romeo's Code section
Romeo Perlstein
section 0102
'''

# We do a little copying and pasting (it said I can use as MUCH of the code as I want and dog gonit I will)

# Get the path to the tiger images folder:
print("\nPlease provide the path to the tigerimages folder! (abs or relative):\nPossible flags for ease of use:\n\t -here : flag for if the tiger images are in the cwd\n\t -next : flag for if the tigerimages/ folder is in the current working directory")
path = str(input()) # Get the folder path

# Check if a flag was uses, and then overwrite the file_path if so - this only happens if a flag is called. If not, we can use the one previously defined
if path == "-here": # The here flag, represents if the file is in the cwd
    path = ""
elif path == "-next": # The next flag, represents if the tigerimages/ folder is in the cwd
    path = "tigerimages"
elif not os.path.exists(path): # Check if the folder exists
    print("Path does not exists! Cmon now!!!")
    raise ImportError("Agony")

# Build the path
file_path = os.path.join(path, "tiger1.jpeg")

# Read in the file, and show it
tiger = cv2.imread(file_path) # Displayed with blue colors because it is matplotlib reads RGB, not BGR, so red and blues are swapped here
# plt.imshow(tiger)
# plt.show()

# Convert the image to RGB for matplotlib, and to swap color layers back around
tiger_rgb = cv2.cvtColor(tiger, cv2.COLOR_BGR2RGB) # Convert the image to RGB
# plt.imshow(tiger_rgb)
# plt.show() # Show it

# Prepare and plot the image on a 3d plot
r, g, b = cv2.split(tiger_rgb)

# fig = plt.figure() # create a figure
# axis = fig.add_subplot(1, 1, 1, projection="3d") # add the 3 axis and make it look 3d
# pixel_colors = tiger_rgb.reshape((np.shape(tiger_rgb)[0] * np.shape(tiger_rgb)[1], 3)) # get the color of each pixel
# norm = colors.Normalize(vmin=-1.0, vmax=1.0) # get a norm value
# norm.autoscale(pixel_colors) # autoscale the norm to match the size of our pixel color data
# pixel_colors = norm(pixel_colors).tolist() # Make it into a list
# axis.scatter(r.flatten(), g.flatten(), b.flatten(), facecolors=pixel_colors, marker=".") # Make a scatter plot
# axis.set_xlabel("Red") # label the axis
# axis.set_ylabel("Green")
# axis.set_zlabel("Blue")
# plt.show() # Show it

# # Convert the rgb image to HSV for easier analysis
tiger_hsv = cv2.cvtColor(tiger_rgb, cv2.COLOR_RGB2HSV) # Convert it
h, s, v = cv2.split(tiger_hsv) # Get the separate channels

# # Plot the HSV spectrum
# fig = plt.figure() # Make a new figure
# axis = fig.add_subplot(1, 1, 1, projection="3d") # Make the figure 3d
# axis.scatter(h.flatten(), s.flatten(), v.flatten(), facecolors=pixel_colors, marker=".") # Make a scatter plot of the data
# axis.set_xlabel("Hue") # Label the axises
# axis.set_ylabel("Saturation")
# axis.set_zlabel("Value")
# plt.show() # Show it

# Get some preliminary color thresholds to test with
light_orange = (15, 190, 255)
dark_orange = (8, 230, 255)

# Normalise to 0 - 1 range for viewing
lo_square = np.full((10, 10, 3), light_orange, dtype=np.uint8) / 255.0
do_square = np.full((10, 10, 3), dark_orange, dtype=np.uint8) / 255.0

# Create a subplot of the two color squares to see their colors
plt.subplot(1, 2, 1)
plt.imshow(hsv_to_rgb(do_square))
plt.subplot(1, 2, 2)
plt.imshow(hsv_to_rgb(lo_square))
plt.show() # Show it

# Segment the tiger using inRange() function
mask = cv2.inRange(tiger_hsv, light_orange, dark_orange)

# Bitwise-AND mask and original image

result = cv2.bitwise_and(tiger_rgb, tiger_rgb, mask=mask)

# Convert back to RGB in order to plot using `matplotlib.pyplot`

plt.subplot(1, 2, 1)
plt.imshow(mask, cmap="gray")
plt.subplot(1, 2, 2)
plt.imshow(result)
plt.show()

light_white = (0, 0, 200)
dark_white = (145, 60, 255)

lw_square = np.full((10, 10, 3), light_white, dtype=np.uint8) / 255.0
dw_square = np.full((10, 10, 3), dark_white, dtype=np.uint8) / 255.0

plt.subplot(1, 2, 1)
plt.imshow(hsv_to_rgb(lw_square))
plt.subplot(1, 2, 2)
plt.imshow(hsv_to_rgb(dw_square))
plt.show()

mask_white = cv2.inRange(tiger_hsv, light_white, dark_white)
result_white = cv2.bitwise_and(tiger_rgb, tiger_rgb, mask=mask_white)

plt.subplot(1, 2, 1)
plt.imshow(mask_white, cmap="gray")
plt.subplot(1, 2, 2)
plt.imshow(result_white)
plt.show()

final_mask = mask + mask_white

final_result = cv2.bitwise_and(tiger_rgb, tiger_rgb, mask=final_mask)

plt.subplot(1, 2, 1)
plt.imshow(final_mask, cmap="gray")
plt.subplot(1, 2, 2)
plt.imshow(final_result)
plt.show()

blur = cv2.GaussianBlur(final_result, (7, 7), 0)

plt.imshow(blur)
plt.show()

# Generalising the segmentation


tigers = []
for i in range(2,5):
    new_path = os.path.join(path, "tiger" + str(i) + ".jpeg")
    print(new_path)
    friend = cv2.cvtColor(cv2.imread(new_path), cv2.COLOR_BGR2RGB)
    tigers.append(friend)


def segment_fish(image):
    """Attempts to segment the clown fish out of the provided image."""
    hsv_image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    light_orange = (1, 190, 200)
    dark_orange = (18, 255, 255)
    mask = cv2.inRange(hsv_image, light_orange, dark_orange)
    light_white = (0, 0, 200)
    dark_white = (145, 60, 255)
    mask_white = cv2.inRange(hsv_image, light_white, dark_white)
    final_mask = mask + mask_white
    result = cv2.bitwise_and(image, image, mask=final_mask)
    result = cv2.GaussianBlur(result, (7, 7), 0)
    return result

results = [segment_fish(friend) for friend in tigers]

for i in range(1, 6):
    plt.subplot(1, 2, 1)
    plt.imshow(tigers[i])
    plt.subplot(1, 2, 2)
    plt.imshow(results[i])
    plt.show()
    
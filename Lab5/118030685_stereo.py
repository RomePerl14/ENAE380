import numpy as np
import matplotlib.pyplot as plt
import skimage, skimage.io 



def display(img, colorbar=False):
    "Displays an image."
    plt.figure(figsize=(10, 10))
    if len(img.shape) == 2:
        i = skimage.io.imshow(img, cmap='gray')
    else:
        i = skimage.io.imshow(img)
    if colorbar:
        plt.colorbar(i, shrink=0.5, label='depth')
    plt.tight_layout()
    plt.show()


def make_pattern(shape=(16, 16), levels=64):
    "Creates a pattern from gray values."
    return np.random.randint(0, levels - 1, shape) / levels

def create_circular_depthmap(shape=(600, 800), center=None, radius=100):
    "Creates a circular depthmap, centered on the image. "
    depthmap = np.zeros(shape, dtype=float)
    r = np.arange(depthmap.shape[0])
    c = np.arange(depthmap.shape[1])
    R, C = np.meshgrid(r, c, indexing='ij')
    if center is None:
        center = np.array([r.max() / 2, c.max() / 2])
    d = np.sqrt((R - center[0])**2 + (C - center[1])**2)
    depthmap += (d < radius)
    return depthmap        

def normalize(depthmap):
    "Normalizes values of depthmap to [0, 1] range."
    if depthmap.max() > depthmap.min():
        return (depthmap - depthmap.min()) / (depthmap.max() - depthmap.min())
    else:
        return depthmap

def make_autostereogram(depthmap, pattern, shift_amplitude=0.1, invert=False):
    "Creates an autostereogram from depthmap and pattern."
    depthmap = normalize(depthmap)
    if invert:
        depthmap = 1 - depthmap
    autostereogram = np.zeros_like(depthmap, dtype=pattern.dtype)
    for r in np.arange(autostereogram.shape[0]):
        for c in np.arange(autostereogram.shape[1]):
            if c < pattern.shape[1]:
                autostereogram[r, c] = pattern[r % pattern.shape[0], c]
            else:
                shift = int(depthmap[r, c] * shift_amplitude * pattern.shape[1])
                autostereogram[r, c] = autostereogram[r, c - pattern.shape[1] + shift]
    return autostereogram


# pattern = make_pattern(shape=(128,64))
# display(pattern)

# depthmap = create_circular_depthmap(radius=150)
# display(depthmap, colorbar=True)

# autostereogram = make_autostereogram(depthmap, pattern, invert=True)
# display(autostereogram)

# depthmap = create_circular_depthmap(center=(200, 300), radius=100) + \
#            create_circular_depthmap(center=(450, 500), radius=100) + \
#            create_circular_depthmap(center=(200, 550), radius=150)
# depthmap = normalize(depthmap)
# display(depthmap, colorbar=True)
# autostereogram = make_autostereogram(depthmap, pattern)
# display(autostereogram)

'''
Romeos Code
Romeo Perlstein
section 0102
'''
# make a noise pattern using the noise function
pattern = make_pattern((64,64)) # make our noise 64x64
display(pattern) # display the pattern

# Create a depth map with silly little circles (didn't want to make another function to draw a different shape, its due soon)
d_map = create_circular_depthmap(center=(150, 300), radius=75) + \
           create_circular_depthmap(center=(350, 575), radius=125) + \
           create_circular_depthmap(center=(200, 400), radius=150) + \
           create_circular_depthmap(center=(250, 250), radius=100)+ \
           create_circular_depthmap(center=(115, 115), radius=115)+ \
           create_circular_depthmap(radius=200) # I made a few here because I wanted to make something different enough. The final depth map looks pretty sweet!
d_map = normalize(d_map) # Normalize the depth maps with each other
display(d_map, colorbar=True) # display them

# Create an autostereogram using the autosereogram function
autoster = make_autostereogram(d_map, pattern) # Use our pattern and d_map
display(autoster) # display it



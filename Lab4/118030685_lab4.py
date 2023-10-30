import wave
import struct
import matplotlib.pyplot as plt
import numpy as np
import scipy
import os


def sine():
    # frequency is the number of times a wave repeats a second
    frequency = 1000
    num_samples = 48000
 
    # The sampling rate of the analog to digital convert
    sampling_rate = 48000.0
    amplitude = 16000
    file = "test.wav"

    sine_wave = [np.sin(2 * np.pi * frequency * x/sampling_rate) for x in range(num_samples)]

    nframes=num_samples
    comptype="NONE"
    compname="not compressed"
    nchannels=1
    sampwidth=2

    wav_file=wave.open(file, 'w')
    wav_file.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))

    for s in sine_wave:
        wav_file.writeframes(struct.pack('h', int(s*amplitude)))

    wav_file.close() # Added - Close the file to properly save it


def get_freq():
    frame_rate = 48000.0
    infile = "test.wav"
    num_samples = 48000
    wav_file = wave.open(infile, 'r')
    data = wav_file.readframes(num_samples)
    wav_file.close()

    data = struct.unpack('{n}h'.format(n=num_samples), data)

    data = np.array(data)

    data_fft = np.fft.fft(data)

    frequencies = np.abs(data_fft)

    print("The frequency is {} Hz".format(np.argmax(frequencies)))

    plt.subplot(2,1,1)
    plt.plot(data[:300])
    plt.title("Original audio wave")
    plt.subplot(2,1,2)
    plt.plot(frequencies)
    plt.title("Frequencies found")
    plt.xlim(0,1200)
    plt.show()

def noisy():
    # frequency is the number of times a wave repeats a second
    main_frequency = 1000
    noise_frequency = 50
    num_samples = 48000
 
    # The sampling rate of the analog to digital convert
    sampling_rate = 48000.0
    amplitude = 16000

    # Make sine waves, but use the amplitude given
    main_sine_wave = [amplitude*np.sin(2 * np.pi * main_frequency * x/sampling_rate) for x in range(num_samples)]
    noise_sine_wave = [amplitude*np.sin(2 * np.pi * noise_frequency * x/sampling_rate) for x in range(num_samples)]

    n_main_sin_wave = np.array(main_sine_wave)
    n_noise_sine_wave = np.array(noise_sine_wave)

   # Using subplot2grid because I like it more
    sin_plot = plt.subplot2grid((3,1), (0,0)) # Create the 1khz sine plot
    noise_plot = plt.subplot2grid((3,1), (1,0)) # Create the 50hz sin plot
    combined_plot = plt.subplot2grid((3,1), (2,0)) # Create the combined plot
    plt.tight_layout()

    # Plot all of the graphs we just made (from 0->1200 (a factor of 48000), so that we can actually visualize it)
    sin_plot.plot(n_main_sin_wave[:1200]) # Plot the sine wave
    sin_plot.set_title("1kHz Sine Wave") # Set the title of the sine plot
    sin_plot.set_xlabel("Samples")
    sin_plot.set_ylabel("Amplitude")
    noise_plot.plot(n_noise_sine_wave[:1200]) # Plot the noise wave
    noise_plot.set_title("50Hz Sine wave (used to generate noise)") # Set the title of the noise plot
    noise_plot.set_xlabel("Samples")
    noise_plot.set_ylabel("Amplitude")
    
    # Plot the combined plot
    combined_plot.plot(n_noise_sine_wave[:1200], label="Noise") # first, plot the noise wave
    combined_plot.plot(n_main_sin_wave[:1200], label="1kHz Wave") # Then, plot the sine wave
    combined_plot.set_title("Combined 1kHz Sine Wave and 50Hz Sine Wave") # Set the title of the combined plot
    combined_plot.set_xlabel("Samples")
    combined_plot.set_ylabel("Amplitude")
    combined_plot.legend()
    
    # Plot the actual combined wave that we want to see
    combined_data = (n_noise_sine_wave + n_main_sin_wave) # Add the waves together to get the noise
    plt.figure() # Make a new figure
    plt.plot(combined_data[:1200]) # Plot the combined wave
    plt.title("1kHz Sine Wave With Noise (50Hz noise)") # Set the title of the graph
    plt.xlabel("Samples")
    plt.ylabel("Amplitude")

    # Now do a Fourier transform thingy on it to convert form the time domain to the frequency domain
    frequencies_nonabs = (np.fft.fft(combined_data))
    frequencies = abs(np.fft.fft(combined_data)) # Get the absolute value of the FFT to pull actually useful data from it
    plt.figure() # Create a new figure
    plt.plot(frequencies) # Plot the frequencies
    plt.xlim(0,1100) # limit the x-axis to be 0->1500
    plt.title("Found frequencies of combined Sine Waves using FFT")
    plt.xlabel("Frequencies (Hz)")
    plt.ylabel("Found-ness")
    
    filtered_frequencies = np.zeros(48000)
    filtered_frequencies_nonabs = filtered_frequencies
    filtered_frequencies_nonabs[500:1500] = frequencies_nonabs[500:1500]
    filtered_frequencies[500:1500] = frequencies[500:1500] # "filter" the frequencies, but literally just cutting out anything that's no around 1000 Hz
    plt.figure() # Make a new figure
    plt.plot(filtered_frequencies) # Plot it
    plt.title("Plot of Frequencies of Filtered Sine Wave") # Title
    plt.xlim(0, 1100) # limit the X axis so we can see the data better
    plt.xlabel("Frequencies (Hz)")
    plt.ylabel("Found-ness")

    converted_back_sine = np.fft.ifft(filtered_frequencies_nonabs) # do the inverse fourier transform to convert back from the frequencey plane to time frame 
    plt.figure() # Plot the figure
    plt.tight_layout() # Tight layout so we can actually see the x and y labels
    converted_back = plt.subplot2grid((2,1), (0,0)) # Create subplot object containing two plots. Make the first plot
    final_combined = plt.subplot2grid((2,1), (1,0)) # Make the second plot
    converted_back.plot(converted_back_sine[:1200]) # Fill the first subplot object with the plot
    converted_back.set_title("1kHz Plot Converted From Filtered Frequency")
    converted_back.set_xlabel("Samples")
    converted_back.set_ylabel("Amplitude")

    final_combined.plot(converted_back_sine[:1200], label="Converted Sine Wave") # Fill the second subplot with plot info from the converted plot
    final_combined.plot(main_sine_wave[:1200], label="1kHz Sine Wave") # Plot the original sine wave 
    final_combined.plot(combined_data[:1200], label="Noisy Since Wave") # Plot the noisy sine wave
    final_combined.set_title("Final Set of Combined Graphs")
    final_combined.set_xlabel("Samples")
    final_combined.set_ylabel("Amplitude")
    final_combined.legend()

    plt.show() # Show all of the plots we made

def pitch():
    infile = "trumpet.wav"
    wav_file = wave.open(infile, "r")

    nchannels = wav_file.getnchannels()
    nframes = wav_file.getnframes()
    sampwidth = wav_file.getsampwidth()

    data = wav_file.readframes(nframes)

    wav_file.close()

    dtype_map = {1: np.int8, 2: np.int16, 3: "special", 4: np.int32}
    if sampwidth not in dtype_map:
        raise ValueError("sampwidth %d unknown" % sampwidth)

    if sampwidth == 3:
        xs = np.fromstring(data, dtype=np.int8).astype(np.int32)
        ys = (xs[2::3] * 256 + xs[1::3]) * 256 + xs[0::3]
    else:
        ys = np.frombuffer(data, dtype=dtype_map[sampwidth])

    # if it's in stereo, just pull out the first channel
    if nchannels == 2:
        ys = ys[::2]
    
    #plot full signal
    plt.plot(ys)
    plt.title("Plot of sound waves of a trumpet audio file (1st channel)")
    plt.xlabel("Samples")
    plt.ylabel("Amplitude")
    
    #plot segment of signal
    segment= ys[:48000]
    plt.plot(segment) # plot the segment ontop of the 
    plt.figure() # Make a new figure to separately plot the segment
    plt.plot(ys[:48000]) # Replot the segment of the plot
    plt.title("Segmented sample of the trumpet audio")
    plt.xlabel("Samples")
    plt.ylabel("Amplitude")

    #FFT of segment
    frequency_of_segment = abs(np.fft.fft(segment))
    frequency_of_segment_nonabs = (np.fft.fft(segment))
    plt.figure()
    plt.plot(frequency_of_segment)
    plt.title("Frequncies in selected segment")
    plt.xlabel("Frequencies (Hz)")
    plt.ylabel("Found-ness")
    
    # Find three highest peaks and their frequencies
    first = 0 # First highest
    second = 0 # Second highest
    third = 0 # Third highest
    prev_value = -1
    current_value = 0 # Initialize our current value
    for i in range(len(frequency_of_segment)): # For the entire length of the array
        current_value = frequency_of_segment[i] # Get our current value
        if prev_value < current_value: # if our current value is greater than our last saved highest
            prev_value = current_value # Update our lasted saved highest
            first = i
        elif prev_value > current_value: # If our last saved highest is greater than our current value
            pass # do nothing

    # Get the second highest
    prev_value = -1
    for i in range(len(frequency_of_segment)):
        current_value = frequency_of_segment[i]
        if prev_value < current_value:
            if current_value < frequency_of_segment[first]: # Do everything the same as above except if its bigger than the first value don't update
                prev_value = current_value
                second = i
        elif prev_value > current_value:
            pass

    # Get the third highest
    prev_value = -1
    for i in range(len(frequency_of_segment)):
        current_value = frequency_of_segment[i]
        if prev_value < current_value:
            if current_value < frequency_of_segment[second]: # Literally the same thing as above again except if it's greater than the second value don't update it
                prev_value = current_value
                third = i
        elif prev_value > current_value:
            pass
    print("\nFirst most frequency found: " + str(first) + " Hz\nSecond most frequency found: " + str(second) + " Hz\nThird most frequency found: " + str(third) + " Hz\n")
    
    # Get the three highest in the 16000Hz range
    ## Literally do exactly the same as above, except with a smaller range of data
    first = 0 # First highest
    second = 0 # Second highest
    third = 0 # Third highest
    prev_value = -1
    current_value = 0 # Initialize our current value
    for i in range(len(frequency_of_segment[:16000])): # For the entire length of the array
        current_value = frequency_of_segment[i] # Get our current value
        if prev_value < current_value: # if our current value is greater than our last saved highest
            prev_value = current_value # Update our lasted saved highest
            first = i
        elif prev_value > current_value: # If our last saved highest is greater than our current value
            pass # do nothing

    # Get the second highest
    prev_value = -1
    for i in range(len(frequency_of_segment[:16000])):
        current_value = frequency_of_segment[i]
        if prev_value < current_value:
            if current_value < frequency_of_segment[first]: # Do everything the same as above except if its bigger than the first value don't update
                prev_value = current_value
                second = i
        elif prev_value > current_value:
            pass

    # Get the third highest
    prev_value = -1
    for i in range(len(frequency_of_segment[:16000])):
        current_value = frequency_of_segment[i]
        if prev_value < current_value:
            if current_value < frequency_of_segment[second]: # Literally the same thing as above again except if it's greater than the second value don't update it
                prev_value = current_value
                third = i
        elif prev_value > current_value:
            pass
    print("\nFirst most frequency found: " + str(first) + " Hz\nSecond most frequency found: " + str(second) + " Hz\nThird most frequency found: " + str(third) + " Hz\n")
    


    #Filter out highest frequencies
    filtered_freq = np.zeros(48000) # Create a new empty array so that we can filter out the high frequencies
    filtered_freq_non_abs = np.zeros(48000) # Do the same as above
    filtered_freq[:8000] = frequency_of_segment[:8000] # Ditch anything past a frequency of 8000 Hz
    filtered_freq_non_abs = frequency_of_segment_nonabs # Ditch anything past a frequency of 8000 Hz
    plt.figure() # Create a new figure
    plt.plot(filtered_freq) # Plot the frequencies
    plt.title("Plot of Frequencies found from 0 -> 16000 Hz")
    plt.xlabel("Frequencies (Hz)")
    plt.ylabel("Found-ness")
    
    #Plot inverse signal
    plt.figure() # Create a new figure
    inverse_freq = np.fft.ifft(filtered_freq_non_abs) # Get the inverse of our filtered frequency
    plt.plot(inverse_freq) # Plot the inversed frequency
    plt.title("Inverse Fourier Transform of the segment selected")
    plt.xlabel("Samples")
    plt.ylabel("Amplitude")

    #Save original segment and filtered segment to wave files 
    segment_file = wave.open("segment.wav", "w")
    segment_file.setparams((1, sampwidth, 48000, nframes, "NONE", "not compressed"))
    for i in range(len(segment)):
        segment_file.writeframes(segment[i])
    segment_file.close()

    filtered_file = wave.open("segment_filter.wav", "w")
    filtered_file.setparams((1, sampwidth, 48000, nframes, "NONE", "not compressed"))
    for i in range(len(inverse_freq)):
        filtered_file.writeframes(inverse_freq[i])
    filtered_file.close()

    plt.show()

def mix_signals(): 
    # Copy from sine() and get_freq() functions above. See above for more comments
    # frequency is the number of times a wave repeats a second
    frequency1 = 1000 # First frequency
    frequency2 = 300 # Second frequency
    frequency3 = 500 # Third Frequency

    num_samples = 48000
 
    # The sampling rate of the analog to digital convert
    sampling_rate = 48000.0
    amplitude = 10000
    file = "multi-wave.wav"

    sine_wave1 = [np.sin(2 * np.pi * frequency1 * x/sampling_rate) for x in range(num_samples)] # Make the first sine wave
    sine_wave2 = [np.sin(2 * np.pi * frequency2 * x/sampling_rate) for x in range(num_samples)] # Make the second sine wave
    sine_wave3 = [np.sin(2 * np.pi * frequency3 * x/sampling_rate) for x in range(num_samples)] # Make the third sine wave

    # Make the sine waves numpy arrays
    sine_wave1 = np.array(sine_wave1)
    sine_wave2 = np.array(sine_wave2)    
    sine_wave3 = np.array(sine_wave3)    
    sine_wave = sine_wave1 + sine_wave2 + sine_wave3 # Add them all together

    # Stolen from sine()
    nframes=num_samples
    comptype="NONE"
    compname="not compressed"
    nchannels=1
    sampwidth=2

    wav_file=wave.open(file, 'w') # Make a new file
    wav_file.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname)) # Set the file

    for s in sine_wave: 
        wav_file.writeframes(struct.pack('l', int(s*amplitude))) # Write the data to a wave file

    wav_file.close() # Added - Close the file to properly save it

    # Stolen from get_freq() function
    num_samples = 48000
    wav_file = wave.open(file, 'r')
    data = wav_file.readframes(num_samples)
    wav_file.close()

    data = struct.unpack('{n}h'.format(n=num_samples), data)

    data = np.array(data)

    data_fft = np.fft.fft(data)

    frequencies = np.abs(data_fft)

    plt.subplot(2,1,1)
    plt.plot(data[:1000])
    plt.title("Original audio wave")
    plt.subplot(2,1,2)
    plt.plot(frequencies)
    plt.title("Frequencies found")
    plt.xlim(0,1200)
    plt.show()

def stretch(input, factor): 
    if not os.path.exists(input):
        print("Inputted WAV file does not exist!")
        return
    
    # Stolen from pitch()
    wav_file = wave.open(input, "r")
    factor = float(factor)

    nchannels = wav_file.getnchannels()
    nframes = wav_file.getnframes()
    sampwidth = wav_file.getsampwidth()

    data = wav_file.readframes(nframes)

    wav_file.close()

    dtype_map = {1: np.int8, 2: np.int16, 3: "special", 4: np.int32}
    if sampwidth not in dtype_map:
        raise ValueError("sampwidth %d unknown" % sampwidth)

    if sampwidth == 3:
        xs = np.fromstring(data, dtype=np.int8).astype(np.int32)
        ys = (xs[2::3] * 256 + xs[1::3]) * 256 + xs[0::3]
    else:
        ys = np.frombuffer(data, dtype=dtype_map[sampwidth])

    # if it's in stereo, just pull out the first channel
    if nchannels == 2:
        ys = ys[::2]

    mod_wave = wave.open("modified_wave.wav", "w")
    mod_wave.setparams((1, sampwidth, int(48000*factor), nframes, "NONE", "not compressed"))
    for i in range(len(ys)):
        mod_wave.writeframes(ys[i])
    mod_wave.close()
    


def sampling(): 
    freq1 = 5.0      # freq in Hz
    freq2 = 1.0      # freq in Hz
    samp  = 1000.0   # sampling rate in Hz

    t = np.arange(0,1,1/samp)  # time (1s of data)
    N = len(t)                 # store the number of time points

    x = np.cos(2*np.pi*freq1*t) + .5*np.cos(2*np.pi*freq2*t)    # the signal equation

    # Continue the function here
    signal_plot = plt.subplot2grid((2,1), (0,0)) # Create subplot object containing two plots. Make the first plot
    freq_plot = plt.subplot2grid((2,1), (1,0))
    signal_plot.plot(x) # Plot the signal
    signal_plot.set_title("Plot of Signal")
    freq_plot.plot(abs(np.fft.fft(x))) # Plot the fast Fourier transform
    freq_plot.set_title("Plot of Frequencies (Hz)")
    freq_plot.set_xlabel("Frequencies (Hz)")

    # Sub-sample
    new_sample_rate = 5 # Starting with this as the example
    grabber = int(samp/new_sample_rate)
    F = []
    for i in range(0,len(x),grabber):
        F.append(x[i])
    
    plt.figure()
    signal_plot = plt.subplot2grid((2,1), (0,0)) # Create subplot object containing two plots. Make the first plot
    freq_plot = plt.subplot2grid((2,1), (1,0))
    signal_plot.plot(F) # Plot the signal
    signal_plot.set_title("Plot of Signal")
    freq_plot.plot(abs(np.fft.fft(F))) # Plot the fast Fourier transform
    freq_plot.set_title("Plot of Frequencies (Hz)")
    freq_plot.set_xlabel("Frequencies (Hz)")
    plt.show()

    # Signal starts to degrade when we start sampling at around less than 10x the highest sampling rate of the original data


def main():
    # sine()
    # get_freq()
    # noisy()
    # pitch()
    # mix_signals()
    # stretch("multi-wave.wav", 2)
    sampling()


if __name__ == "__main__":
    main()

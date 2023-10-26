import wave
import struct
import matplotlib.pyplot as plt
import numpy as np
import scipy


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
    frequencies = abs(np.fft.fft(combined_data)) # Get the absolute value of the FFT to pull actually useful data from it
    plt.figure() # Create a new figure
    plt.plot(frequencies) # Plot the frequencies
    plt.xlim(0,1100) # limit the x-axis to be 0->1500
    plt.title("Found frequencies of combined Sine Waves using FFT")
    plt.xlabel("Frequencies (Hz)")
    plt.ylabel("Found-ness")
    
    filtered_frequencies = np.zeros(48000) # Make an array of zeros
    filtered_frequencies[500:1500] = frequencies[500:1500] # "filter" the frequencies, but literally just cutting out anything that's no around 1000 Hz
    plt.figure() # Make a new figure
    plt.plot(filtered_frequencies) # Plot it
    plt.title("Plot of Frequencies of Filtered Sine Wave") # Title
    plt.xlim(0, 1100) # limit the X axis so we can see the data better
    plt.xlabel("Frequencies (Hz)")
    plt.ylabel("Found-ness")

    converted_back_sine = np.fft.ifft(filtered_frequencies)
    plt.figure()
    plt.tight_layout()
    converted_back = plt.subplot2grid((2,1), (0,0))
    final_combined = plt.subplot2grid((2,1), (1,0))
    converted_back.plot(converted_back_sine[:1200])
    converted_back.set_title("1kHz Plot Converted From Filtered Frequency")
    converted_back.set_xlabel("Samples")
    converted_back.set_ylabel("Amplitude")

    final_combined.plot(converted_back_sine[:1200], label="Converted Sine Wave")
    final_combined.plot(main_sine_wave[:1200], label="1kHz Sine Wave")
    final_combined.plot(combined_data[:1200], label="Noisy Since Wave")
    final_combined.legend()

    plt.show()




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
    
    #plot segment of signal
    
    #FFT of segment
    
    #Find three highest peaks and their frequencies
    
    #Filter out highest frequencies
    
    #Plot inverse signal
    
    #Save original segment and filtered segment to wave files 

def mix_signals(): 
    pass 

def stretch(input, factor): 
    pass 

def sampling(): 
    freq1 = 5.0      # freq in Hz
    freq2 = 1.0      # freq in Hz
    samp  = 1000.0   # sampling rate in Hz

    t = np.arange(0,1,1/samp)  # time (1s of data)
    N = len(t)                 # store the number of time points

    x = np.cos(2*np.pi*freq1*t) + .5*np.cos(2*np.pi*freq2*t)    # the signal equation

    # Continue the function here

def main():
    # sine()
    # get_freq()
    noisy()


if __name__ == "__main__":
    main()

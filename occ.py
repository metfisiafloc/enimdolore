import time

# Define the sampling frequency in Hz
sampling_frequency = 100  # Hz

# Calculate the sampling interval in seconds
sampling_interval = 1 / sampling_frequency

# Initialize the timer loop
while True:
    start_time = time.time()

    # Perform signal sampling or processing here

    # Calculate the time elapsed for the sampling process
    elapsed_time = time.time() - start_time

    # Add a delay to maintain the desired sampling frequency
    time.sleep(max(0, sampling_interval - elapsed_time))

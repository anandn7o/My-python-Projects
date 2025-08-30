import time

def stopwatch():
    input("Press Enter to start the stopwatch...")
    start_time = time.time()
    print("Stopwatch started. Press Enter to stop.")
    input()
    end_time = time.time()
    elapsed_time = end_time - start_time

    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    milliseconds = int((elapsed_time - int(elapsed_time)) * 1000)

    print(f"Elapsed Time: {minutes:02d}:{seconds:02d}.{milliseconds:03d}")

# Run the stopwatch
stopwatch()

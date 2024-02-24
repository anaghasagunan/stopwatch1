import time

def stopwatch():
    input("\n\nPress Enter to start the STOPWATCH!!\n\n")
    start_time = time.time()
    print("Press Ctrl + C to STOP\n\n")
    
    try:
        while True:
            elapsed_time = time.time() - start_time
            formatted_time = format_time(elapsed_time)
            print(f"\rTIME PASSED : {formatted_time}", end="")
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\n\nSTOPWATCH STOPPED.....\n\n")

        pass
def format_time(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "{:02}:{:02}:{:05.2f}".format(int(hours), int(minutes), seconds)
    

stopwatch()c
import os
import time

def shutdown_pc(minutes):
    seconds = minutes * 60
    time.sleep(seconds)
    os.system("shutdown /s /t 1")

def main():
    print("Welcome to the PC Shutdown Bot!")
    print("Enter the number of minutes after which you want your PC to shut down:")
    minutes = int(input("> "))
    print(f"The PC will shut down after {minutes} minutes.")

    shutdown_pc(minutes)

if __name__ == "__main__":
    main()

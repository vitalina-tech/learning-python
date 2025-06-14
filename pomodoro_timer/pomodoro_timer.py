import time
def countdown(minutes):
    total_seconds=minutes*60
    while total_seconds>0:
        mins=total_seconds//60
        secs=total_seconds%60
        print(f'Time left:{mins:02d}:{secs:02d}',end='\r')
        time.sleep(1)
        total_seconds-=1
    else:
        print("Time's up!        ")
if __name__=='__main__':
    try:
        user_input=int(input('Enter time in minutes: ').strip())
        if user_input>0:
            countdown(user_input)
        else:
            print("Please enter a positive number.")
    except:
        print("Invalid input. Please enter a number.")
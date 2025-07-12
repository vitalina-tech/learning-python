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
def pomodoro(focus_minutes, break_minutes, intervals):
    for i in range(intervals):
        print(f'\nSession {i+1}\nTime to focus!')
        countdown(focus_minutes)
        if i<intervals - 1:
            print('Break time!')
            countdown(break_minutes)
    print('\nPomodoro session complete!')
if __name__=='__main__':
    try:
        intervals=int(input('How many focus sessions? ').strip())
        focus=int(input('Minutes per focus session: ').strip())
        brk=int(input('Minutes per break: ').strip())
        if intervals>0 and focus>0 and brk>0:
            pomodoro(focus, brk, intervals)
        else:
            print("Please enter a positive number.")
    except:
        print("Invalid input. Please enter a number.")
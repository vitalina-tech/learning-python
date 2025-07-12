import time

def format_time(seconds):
    minutes, sec=divmod(int(seconds), 60)
    return f"{minutes:02d}:{sec:02d}"

def durations(start_time, end_time):
    return [end - start for start, end in zip(start_time, end_time)]

def get_input(starts, message):
    user_input=input(message)
    current_time=time.time()
    starts.append(current_time)
    if user_input.lower() == 'q':
        return False
    return True

print('Welcome to the flowtimer!')

focus_starts = []
break_starts = []
print("Press ENTER to start and stop each interval. Type 'q' then ENTER to quit.\n")
while True:
    if get_input(focus_starts, "Press ENTER to begin focus (or 'q' to quit): ") is False:
        break
    if get_input(break_starts, "Press ENTER to begin break (or 'q' to quit): ") is False:
        break

focus_durations = durations(focus_starts, break_starts)
break_durations = durations(break_starts, focus_starts[1:])

print("\nAll durations:\n")

for i in range(len(focus_durations)):
    print(f"Focus time: {format_time(focus_durations[i])}")
    if i < len(break_durations):
        print(f"Break time: {format_time(break_durations[i])}")
 

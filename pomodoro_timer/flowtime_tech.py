import time
print('Hey! Ready to dive into work?')
focus_intervals=[]
break_intervals=[]
focus_TIME=[]
break_TIME=[]
print("Press ENTER to start and stop each interval. Type 'q' tnen ENTER to quit.\n")
while True:
    focus_input=input("Time to focus(Press ENTER to start or 'q' to quit):")
    if focus_input.lower()=='q':
        stop_time=time.time()
        break_TIME.append(stop_time)
        break
    focus_time=time.time()
    focus_TIME.append(focus_time)
    if focus_input.lower()=='q':
        stop_time=time.time()
        break_TIME.append(stop_time)
        break
    break_input=input("Time for a break (Press ENTER to start or 'q' to quit): ")
    break_time=time.time()
    break_TIME.append(break_time)
    if break_input.lower()=='q':
        break
print("\nAll intervals:")
if len(break_TIME)>len(focus_TIME):
    del break_TIME[-1]
for i in range(len(focus_TIME)):
    focus_intervals.append(break_TIME[i]-focus_TIME[i])
    if focus_TIME[i]==focus_TIME[-1]:
        break
    break_intervals.append(focus_TIME[i+1]-break_TIME[i])
break_intervals.append(0)
for i, f, b in zip(range(len(focus_intervals)),focus_intervals, break_intervals):
    print(f"Focus: {f:.2f} seconds")
    if i==len(focus_intervals)-1:
        break
    print(f"Break: {b:.2f} seconds")


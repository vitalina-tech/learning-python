import time
print('Hey! Ready to dive into work?')
intervals=[]
print("Press ENTER to start and stop each interval. Type 'q' tnen ENTER to quit.\n")
while True:
    start_input=input("Start timing (or 'q' to quit):")
    if start_input.lower()=='q':
        break
    start_time=time.time()
    stop_input=input("Stop timing: ")
    elapsed=time.time()-start_time
    intervals.append(elapsed)
    print(f"Interval recorded: {elapsed:.2f}seconds\n")
    if stop_input.lower()=='q':
        break
print("\nAll intervals:")
for i, t in enumerate(intervals,1):
    print(f"Interval {i}: {t:.2f} seconds")

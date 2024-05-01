import random

#======= Question 1 =======

# Task 1 : 

moods = ["happy", "sad", "energetic", "calm"]
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

for i in range(14):
    print(f"On {days[i%len(days)]} you were feeling {random.choice(moods)}")


#======= Question 2 =======

# Task 2 :

times = ["morning", "afternoon", "evening"]

for day in days:
    for time in times:
        print(f"On {day} {time} you were feeling {random.choice(moods)}")
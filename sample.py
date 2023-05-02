import random

stay = 0
switch = 0

def monty_hall(trial):
    global stay
    global switch

    stay_percent = stay / trial * 100
    switch_percent = switch / trial * 100
    
    return stay_percent, switch_percent

num_trials = 100

for _ in range(num_trials):
    doors = [0, 0, 1]
    random.shuffle(doors)
    user_choice = doors.pop()
    if user_choice == 1:
        stay += 1
    else:
        switch += 1

stay_percent, switch_percent = monty_hall(num_trials)

print(f"Stay won {stay_percent}% of the time.")
print(f"Switch won {switch_percent}% of the time.")

import random

def result(user_choice): # user_choice 를 받아와서 stay, switch를 반환할 수 있도록 함수 정의
    global stay
    global switch        # global 변수 선언
    if user_choice == 1 :
        stay += 1
    else :
        switch += 1

    return stay, switch
    
    
def monty_hall(trial):
    global stay
    global switch

    stay_percent = stay / trial * 100
    switch_percent = switch / trial * 100
    
    return stay_percent, switch_percent



stay = 0                        # stay와 switch의 결과값 비교를 위한 initialize
switch = 0
trial =  int(input(" 반복하고 싶은 횟수를 입력하세요. "))

for _ in range(trial):		# 반복할 횟수는 일단 100으로.
    doors = [0, 0, 1] 		# 편의상 0은 염소, 1은 스포츠카로.
    random.shuffle(doors)		# doors 리스트 내의 요소들을 마구 섞어주기
    user_choice = doors.pop()	# 나의 선택과 동시에 doors에서는 해당 요소 제거 ## 사용자가 선택할 수 있도록 함수화

    stay, switch = result(user_choice) # result 함수로 반환된 user_choice 를 stay, switch 로 반환

stay_percent, switch_percent = monty_hall(trial)

print(f"Stay won {stay_percent}% of the time.")
print(f"Switch won {switch_percent}% of the time.")
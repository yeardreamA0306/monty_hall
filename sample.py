import random


stay = 0			# stay와 switch의 결과값 비교를 위한 initialize
switch = 0
trial = 100         # 반복 횟수를 사용자가 입력할 수 있도록 함수화

for _ in range(trial):		# 반복할 횟수는 일단 100으로.
  doors = [0, 0, 1] 		# 편의상 0은 염소, 1은 스포츠카로.
  random.shuffle(doors)		# doors 리스트 내의 요소들을 마구 섞어주기
  user_choice = doors.pop()	# 나의 선택과 동시에 doors에서는 해당 요소 제거 ## 사용자가 선택할 수 있도록 함수화
  if user_choice == 1:  # user_choice를 받아와서 stay, switch를 반환할 수 있도록 함수화
    stay += 1			# 처음 선택에 머물렀을 때 스포츠카를 탄 것이므로 stay 경우의 수를 1 더해주기
  else:
    switch += 1			# 선택을 바꾸었어야 하므로 switch의 경우의 수를 1 더해준다.

print(stay/trial*100, switch/trial*100) # stay, switch, trail을 받아와서 백분율 값을 리턴하도록 함수화

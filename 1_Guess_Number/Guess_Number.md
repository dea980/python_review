**설명:**

컴퓨터가 1부터 10까지의 랜덤한 숫자를 생성하고, 플레이어가 이를 맞추는 프로그램을 만들기.

**요구사항:**

- 컴퓨터는 랜덤 숫자를 생성. (1 ~10 의 랜덤한 숫자 만들어야함)
- 플레이어는 숫자를 입력하고 "크다" 또는 "작다" 힌트를 받음. (player 에게 hint 메세지를 추측이 틀렸을시 기존 컴퓨터가 생성한 수와 비교하여 알려주기)
- 플레이어가 숫자를 맞출 때까지 반복. (condition 을 true and false 로 활용해 만드는 while 이 필요할듯?)

** 생각해야할 것 **
- 만일 플레이어가 1~ 10 이외를 기입했을떄? (try? )
- 일정 조건문들 생각해보기 (작다 , 크다 ..)

**입출력 예시:**

```python
1과 10 사이의 숫자를 하나 정했습니다.
이 숫자는 무엇일까요?
예상 숫자: 5
너무 큽니다. 다시 입력하세요.
예상 숫자: 3
정답입니다!
```

** 추가 요구사항 **
- restart 를 요구 (while loop의 일부 로직 변경 필요)
## 이 요구사항을 바탕으로 sudo code 를 짜기


``` sudo
import random as rd (# random 함수를 쓰기위해 필요)
import numpy as np (## just in case 혹시 나 ..?)
def guess_number():
    nums = rd.randint(1,10) ## print( 1... 10 의 임의 숫자 생성
    ## trials
    attempt = 0
    ## game start
    while < attempt:
      ## 아마 여기에 player가 기입해야할듯?
      ## 아마 만일? 의 경우  
      player = int(input("random 1~10")
      try:  ## player

        if  player's num <1 or player's num > 10:
            print("please enter random number between 1~ 10:)

      except ValeuError: ## case that player type any other things other than int
            print("please type integer!)
      ## 프로그램의 함수 여기에 기입...
      if player's num < nums:
        print("num is larger")
      if player's num > nums:
          pint("num is smaller")
      else:
        print("you win!")

    ## while loop 이기에 ...! 
      attempt +=1
      ## 추가 사항 ...
      restart = input("Do you want to play again?? (y/n): ")
      if restart = y:
          attempt = 0 (restart)
      else:
        print("Good try")

```
*** 개선했던것들

- 이 번에는 주로 type과 input ... 을 신경씀
- 3번의 trial이 있는 프로그램으로 만들고 싶어 trials 를 3으로 지정
- 처음에 restart가 안되기에 .strip().lower()을 사용해 Y,y, N,n 인식 만듬
- restart = > input("Do you want to play again?? (y/n): ").strip().lower()



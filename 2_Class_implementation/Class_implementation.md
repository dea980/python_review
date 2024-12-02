

`Person` 클래스를 만들어 사용자 정보를 입력받고 출력하는 프로그램입니다.

**요구사항:**

- **클래스 정의:** `Person`
    - **멤버 변수:** `name`, `gender`, `age`
    - **생성자:** `__init__(name, gender, age)`
    - **메서드:** `display()`, `greeting()` 정보 출력.


### 입력:

1. **이름** (`name`): 문자열 형태의 유효한 이름 (예: "Alice").
2. **성별** (`gender`): "male", "female", "Male", "Female" 중 하나.
3. **나이** (`age`): 정수형의 유효한 나이 값.

### 출력:

1. 유효성을 검증한 이름, 성별, 나이 출력.
2. 연령대에 따라 맞춤형 인사말 제공:
    - **13세 미만:** "Hello, [Name]! What's up, kid!"
    - **13~19세:** "Hi, [Name]! What's up, Stu!"
    - **20~59세:** "Hello, [Name]! What's up brah!"
    - **60세 이상:** "Greetings, [Name]! Nice to meet you, Sir!"
**입출력 예시:**


```python
나이: 28
이름: 페이커
성별: male
이름: 페이커, 성별: male
나이: 28
## Greeting message will be added
```

**추가 설정:**

1. 성별 입력 검증 (`male` 또는 `female` 제한).
2. 나이대에 맞는 메시지를 출력하는 `greet()` 메서드 추가.

** Step 1 : 
Class 정의가 필요 
class 안에는 
-  input 들인 
    - name (str)
    - gender (str)
    - age (int)
그러므로 일단 생성자 즉 (__init__)에 name, gender, age를 매개변수로 저장 필요

display(), greeting() 또한 구현이 필요.

```sudo
class Person:
    ## __init__ 을 사용해 사용자 정보를 자동으로 초기화시킬수 있으므로 이렇게 정의
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
    ## display() 구현
    if self.name.type() == str:
        print(self.name)
    else:
        print("Please enter correct type for the name! it only accept string type")
    if self.gender.type() == str && (self.gender == 'Female' || self.gender == 'Male') ## lower and upper case need to check
        print(self.gender)
    else:
        print("please enter only Male or Female for your gender.")
    if self.age.type() == int:
        print(self.age)
    else:
        print("Please enter integer for age input")

    ## greet() 구현
    def greet(self): ## self가 꼭 들어가야함!
        if self.age <13:
            message = print("Hello, {self.name}! What's up, kid!")
        elif 13 <= self.age < 20:
            message = print("Hi, {self.name}! What's up, Stu!")
        elif 20 <= self.age < 60:
            message = print("Hello, {self.name}! What's up brah!")
        else:
            message = print("Greetings, {self.name}! Nice to meet you, Sir!")
    print(message)
## input 설정 ...
name = input("Please enter your name:")
gender = input("Please enter your gender:")
age = input("please enter your age:")
## Class 불러오기
## person으로 class 지정후 부름.
person = Person(name, gender, age)


## method 호춮 ...
person.display()
person.greet()
```

### Sudo code 로 짠후 개선점들 ... 
- 이후 type() 이 인식이 안되어, isinstance() 라는 함수를 사용해서 condition 작성
- greet() 함수의 message 의 변수에 지정 print() 를 하나의 print 로 output 설정
- self.gender 에서 M, F, f, m 을 그냥 다 설정.
  

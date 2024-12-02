## input : Name, Gender, Age
## output: Name, Gender , Age
## class Name = Person
## instances : Name, Gender, Age
# name: 이름을 저장하는 변수 (문자열)
# gender: 성별을 저장하는 변수 (문자열, "male" 또는 "female")
# age: 나이를 저장하는 변수 (정수형)

class Person:
  def __init__(self, name, gender, age):
    self.name = name
    self.gender = gender
    self.age = age

  def display(self): ## 1st trial with type() but in python it does not works so I change in to isinstance()
    ## Name Validation
    if isinstance(self.name, str):
      print(f"Name: {self.name}")
    else:
      print("Error: Name needs to be a string type.")

    # Gender validation
    ## I bet there is function for the normalize upper and lower case ... but I am too lazy ... I will just add the condition there.
    if isinstance(self.gender, str) and (self.gender == 'male' or self.gender == 'female' or self.gender == 'Male' or self.gender == 'Female'):
      print(f"Gender: {self.gender}")
    else:
      print("Error: Gender must be 'male' or 'female' as a string.")

    # Age validation
    if isinstance(self.age, int):
      print(f"Age: {self.age}")
    else:
      print("Error: Age needs to be an integer type.")
  def greet(self):
    if self.age < 13:
        message = f"Hello, {self.name}! You're a kid!"
    elif 13 <= self.age < 20:
        message = f"Hi, {self.name}! You're a teenager!"
    elif 20 <= self.age < 60:
        message = f"Hello, {self.name}! You're an adult!"
    else:
        message = f"Greetings, {self.name}! You're a senior citizen!"
    print(message)
        
    



name = input("Please type the name: ")
gender = input("Please type the gender, is it Male or Female?\nGender: ")
age = int(input("Please type the age: "))


person = Person(name, gender, age)
person.display()
person.greet()

## tested with 

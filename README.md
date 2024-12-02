This Repository is a Personal practical folder  for **"Python & Python Library"**. 
It includes basic Python functions and analysis skills.
---

## 🗂 Directory structure.

```

├── 1_Guess_Number
│   ├── Guess_Number.py      # 숫자 맞추기 게임 코드
│   └── Guess_Number.md
├── 2_Class_implementation
│   ├── Class_implementation.py              # Person 클래스를 활용한 프로그램 코드
│   └── Class_implementation.md            
├── 3_Data_Analysis_with_python
│   ├── Data_Analysis_with_python.py        # Pandas와 Numpy를 활용한 데이터 분석 코드
│   ├── Data_Analysis_with_python.md        
│   ├── 관서별_5대범죄_발생_및_검거.xlsx # 경찰서별 5대 범죄 데이터
│   └── pop_kor.csv                  # 인구 데이터
├── LICENSE                          # 프로젝트 라이선스
└── README.md                        # 프로젝트 소개 및 과제 설명
```

---

## 💡 

### 1. Guess Number

**Explanation:**

- It is a game in which a computer produces a random integer from 1 ~ to 10 and guesses it.
- It gives the hint ("Number is smaller or larger")
- 3 trials.

**Character:**

- Need to check the input range.
- Check to the trials and restart or end the game.

**Run:**

```bash
cd 1_Guess_Number
python Guess_Number.py
```

---

2️. Utilize Class() and Function()

**Explanation:**

- Define the `Person` class for input|output the user ID.

**Implementation:**

- Initialize **name**, **gender**, and **age** using the constructor (`__init__`).
- Validate input values for correctness and use a greet() method to display a personalized message.

**Run:**

```bash
cd 2_Class_implementation
python Class_implementation.py
```

### 3. Data analysis with Python library

**Explain:**

- Utilize Pandas and Numpy for Data analysis with this given data. `관서별_5대범죄_발생_및_검거.xlsx`, `pop_kor.csv`).

**Agenda:**

1. Import and output data to DataFrame.
2. Map police stations into distinctions and add `구별` columns.
3. Total calculation after changing the data by government office to distinction data with `pivot_table`.
4. Delete line `구 없음`.
5. Calculate arrest rates by crime and add columns.
6. Delete unnecessary columns.
7. Intuitively renaming the column.
8. Scale analysis by merging with population data.

**run:**

```bash
cd 3_Data_Analysis
python data_analysis_quiz.py
```

---

## 🛠 used skillset

- **Python**: Language and data analytics environments.
- **Pandas**: Data processing and analysis.
- **Numpy**: Calculating figures.
- **Random**: Random number generation for number matching game.

## 🚀 실행 방법

1. Repository cloning
    
    ```bash
    git clone https://github.com/dea980/python-library-assignment.git
    cd python-library-assignment
    ```
    
2. Run each directory:
    - **Guess_Number:** `1_Guess_Number/Guess_Number.py`
    - **Class and Function Implementation:** `2_Class_implementation/Class_implementation.py`
    - **Data analysis:** `3_Data_Analysis_with_python/Data_Analysis_with_python.py`

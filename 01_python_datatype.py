# 1. 주석
# python의 주석 : 1줄 주석은 => #
# 여러줄 주석은 """  """
"""
여기는 몽땅
주석이예요!!
"""
"""이것도 주석이에요!! 여기도 주석"""

# 2. Python의 keyword
# import keyword
# print(keyword.kwlist)
# control s 저장
# run
# 어떤 키워드를 사용할 수 있는지 확인해보아요!!

# 3. 변수의 생성과 삭제
# my_var = 100
# print(my_var)
# menu 첫번쨰

# 4. 변수를 삭제할 수 있어요!
# del my_var
# print(my_var)



# Python의 데이터 타입(data type)
# python의 built-in data type (이미 정의되있는 데이터 타입)
# - Numeric(숫자)
# - Text Sequence (문자열)
# - Sequence
# - Set
# - Mapping
# - Bool

# Numeric Data Type (숫자형)
# int(정수)
# float(실수)
# complex(복소수)

# a = 100 # 정수
# b = 3.14159265358979 # 실수
# c = 1 + 2j
# d = 0o34    # int (8진수)
# e = 0xAB    # int (16진수)

# 데이터타입을 알고싶어요!
# print(type(a))  # class int
# print(type(b))  # class flaot
# print(type(c))  # class complex
# control / 한꺼번에 주석

# my_result = 3 / 4   # 0이 아니라 0.75
# print(my_result)

# my_result = 10 % 3     # 나머지 연산자
# print(my_result)

# my_result = 10 // 3     # 몫 연산자
# print(my_result)

#######################################

# 2. Text Sequence Type(str)

# 다른 언어는 문자와 문자열을 구분
# 문자는 한글자, 문자열은 두글자 이상으로 구성
# 문자를 표현할때 다른 언어는 ''
# 문자열을 표현할 때 다른 언어는 ""
# Python은 문자열을 표현할 때 ('', "")
# a = "Hello"
# b = "K"
# c = 'python'

# 문자열 연산
# first = "haha"
# second = "hoho"

# print(first + second)   # hahahoho
# print(first + str(10))  # haha10
# print(first + str(10))   # haha10
# print(first * 3) # hahahahahaha

# indexing
# my_var = "Hello"
# print(my_var[1])

# slicing
# my_var = "Hello"
# print(my_var[0:3])

# my_var = "이것은 소리없는 아우성"
# print(my_var[0:3]
# print(my_var[0:])
# print(my_var[:])

# in , not in 연산자
# myStr = "This is a sample Text"
# print("sample" in myStr)
# print("sample" not in myStr)

# formatting
# num_of_apple = 10
# myStr = "나는 사과를 %d개 가지고 있어요!" % num_of_apple
# print(myStr)

# 문자열 formatting은 아래의 표현을 주로 사용해요!!
# num_of_apple = 10
# myStr = "나는 사과를 {}개, 바나나 {}개 가지고 있어요!".format(num_of_apple,20)
# print(myStr)

# 문자열 method를 이용해서 문자열 처리를 할 수 있어요!!!
# myStr = "cocacola"

# 문자열의 길이를 알고 싶으면??
# print(len(myStr))     # len() 함수를 이용
#
# print(myStr.count('c'))  # str의  method인 count()를 이용
# print(myStr.find('o'))  #
# myStr = "   my Hobby"
# print(myStr.upper())
# print(myStr.lower())
# print(myStr.strip())

# 3. Sequence type
# list
# 임의의 객체(데이터)를 순서대로 저장하는 집합 자료형
# Java의 ArrayList와 유사..
# list는 literal로 표현할 때 [] (대괄호로 표현)
# my_list = []
# print(type(my_list))
# my_list = list()
# my_list = [1, 2, 3]
# my_list = [1, 2, 3.14, "Hello"]
# my_list = [1, 2, 3.14, "Hello", [5, 6, 7], 100]

# indexing과  Slicing을 할 수 있어요!
# print(my_list[1])   # 2
# print(my_list[-2])   # [5, 6, 7]
# print(my_list[4:5])   # [5, 6, 7]
# print(my_list[4][1])
# print(my_list[0:2])  # [1, 2]

# list 연산
# a = [1, 2, 3]
# b = [4, 5, 6]
#
# print(a + b)
# print(a * 3)

# a = [1, 2, 3]
# a[0] = 5
# print(a)
# a[0] = [7, 8, 9]  #
# print(a)
# a[0:1] = [7, 8, 9]  #
# print(a)

# a = [1, 2, 3]
# # a.append(4)
# a.append([5, 6, 7])
# print(a)   # [1, 2, 3, [5, 6, 7]]

# my_list = ["홍길동", "아이유", "강감찬", "신사임당", "Kim"]
# result = my_list.sort() # 리스트를 오름차순으로 정렬
# print(result)
#my_list.sort()
#print(my_list)

##################################################

# Python
# Data type
# Built-in data type
# 1. Numeric ( int, float, complex )
# 2. Text Sequence Type(str) : 문자열
# 3. Sequence ( list, tuple, range )
# 4. Mapping( dict )

# Sequence type ( tuple )
# list는 []로 표현, tuple은 ()로 표현
# a = (1, 2, 3)    # tuple
# tuple은 일단 만들어지면 내용 변경이 안되요!!
# a[0] = 100
# a = (3,)   # 요소가 1개만 존재하는 tuple
# a = (1, 2, 3)  # 일반적인 Tuple
# a = 1, 2, 3
# print(type(a))
# a = (1, 2, 3)
# b = (5, 6, 7)
# print(a + b)

# a = (1, 2, 3)   # [1, 2, 3]
# my_list = list(a)
# print(my_list)
#
# my_tuple = tuple(my_list)
# print(my_tuple)

# range
# 주로 for문에서 사용
# 같은 데이터를 적은양의 데이터로 표현이 가능
# my_range = range(10)
# print(type(my_range))
# print(my_range)
# print(7 in my_range)
# print(my_range[1:4])
# my_range = range(1, 10, 3)

# Dictionary는 key와 value로 데이터를 저장하는 구조
# { }로 표현해요!!
# a = {"name": "홍길동", "age": 40}
# # print(type(a))
# print(a["name"])
# a["address"] = "서울"
# print(a)
# print(a.get("age"))

# dict에서 많이 사용하는 대표적인 method 3개
# a = {"name": "홍길동", "age": 40, "address": "서울"}
# print(list(a.keys()))    # ["name", "age", "address"]
# print(a.values())    # ["홍길동", 40, "서울"]
# print(a.items())

#########################################################

# Bool data type => Boolean(True, False)
# 사용하는 연산자 => and, or, not 연산자를 사용할 수 있어요
#                  & , | , ~  연산자를 이용해 비트연산을 해요!

# 다음의 경우는 Python에서 False로 간주
# 1. 빈 문자열은 False로 간주 => "", ''
# 2. 빈 리스트는 False로 간주 => []
# 3. 빈 tuple도 False로 간주 => ()
# 4. 빈 dict도 False로 간주 => {}
# 5. 숫자 0은 False로 간주
# 6. None은 당연히 False로 간주

# a = 5
# b = 0

# print(a and b)
# print(a & b)   # & :  bitwise 연산
               # 0101 & 0000 => 0000

# print(a | b)   # | :  bitwise 연산
               # 0101 | 0000 => 0101

#############################################

# Set data type
# 집합 자료형이고 중복을 허용하지 않아요!
# 순서가 존재하지 않는 자료형

# {} => dict => { "key": "value" }
# {} => set  => { 1, 2, 3 }
# my_set = {1, 2, 3, 4, 1, 2}
# print(my_set)

# my_list = [1, 2, 3, 4, 1, 2]
# my_set = set(my_list)
# print(my_set)

# my_str = "Hello"
# my_set = set(my_str)
# print(my_set)

# set에서 사용하는 연산자
# 합집합(union : |), 교집합(intersection : &), 차집합(difference: -)

# s1 = {1, 2, 3, 4}
# s2 = {3, 4, 5, 6}
#
# print(s1 | s2)   # union
# print(s1 & s2)   # intersection
# print(s1 - s2)   # difference

###############################################

# 추가적으로 날짜관련 사항도 알아보아요!!
# date와 datetime에 대해서 알아보아요!

# from datetime import date, datetime
#
# today = date.today()
# print(today)      # 2020-07-15
# # 오늘 날짜는 : 2020년 07월 15일 입니다.
#
# my_str = "오늘 날짜는 : {}년 {}월 {}일 입니다."
# my_str = my_str.format(today.year, today.month, today.day)
# print(my_str)
#
# my_datetime = datetime.today()
# print(my_datetime)
#
# print("현재시간은 : {}시 입니다.".format(my_datetime.hour))
# print("현재시간은 : {}시 {}분 입니다.".format(my_datetime.hour,my_datetime.minute))

# 오늘이 07월 15일이예요.
# 내일의 날짜는 07월 16일이예요.   => 이건 쉬워요!

# 오늘이 01월 31일이예요.
# 내일의 날짜는 02월 1일이예요.   => 그래도 할만해요

# 오늘이 03월 01일이예요.
# 어제의 날짜는 02월 29일이예요.   => 할게 아니예요..

## 결론은 날짜 연산은 처리하기가 너무 힘들어서 계산을 통해 처리하는게
## 아니라 delta를 이용해서 처리해요!

from datetime import date, datetime, timedelta

# today = date.today()  # 오늘 날짜를 구해요!
# days = timedelta(days=-1)
#
# print(today + days)

# today = datetime.today()
# hours = timedelta(hours=-5)
# print(today + hours)

# 1달전 날짜를 알아보아요!
# 예) 오늘 날짜가 3월 31일 => 1달전 날짜는 2월 28일

# 연도와 월에 대한 timedelta는 존재하지 않아요!
# 그래서 새로운 외부 module을 또 사용해야 해요!
# from datetime import date
# from dateutil.relativedelta import relativedelta
#
# today = date.today()
# months = relativedelta(months=-1)
#
# print(today + months)

# 현재날짜와 시간만 하고 있어요!!
# 문자열로 되어 있는 날짜를 진짜 날짜로 변환해서 연산을 하고 싶어요!

# from datetime import datetime
# from dateutil.parser import parse
# my_date = parse("2019-01-30")
# print(my_date)
# my_date = datetime(2019, 1, 30)
# print(my_date)

##########################################################

# Python의 Data type은 여기까지 정리해보아요!!








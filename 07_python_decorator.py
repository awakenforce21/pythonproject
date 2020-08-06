# Decorator

# Decorator의 사전적 의미는 장식가, 도배업자
# Python에서 Decorator는 기존의 코드에 여러가지 기능을 추가하는
# python구문이라고 이해하면 편해요!

# Closure
# first class에 대해서 알아보았어요!
# first class function(일급함수) : 파이썬은 일급함수를 지원하는 언어
# 1. 파이썬의 함수는 변수에 저장할 수 있어요!
# 2. 함수의 인자로 함수를 이용할 수 있어요! ==> Decorator
# 3. 함수의 결과값(리턴값)으로 함수를 이용할 수 있어요! ==> Closure

# def my_outer_func(func):
#     def my_inner_func():
#         func()
#     return my_inner_func
#
# def my_func():
#     print("my_func() 함수가 호출되었어요!!")
#
# decorated_my_func = my_outer_func(my_func)
# decorated_my_func()
#
# my_func()
#




# import time
# def my_outer_func(func):
#
#     def my_inner_func():
#         print("{} 함수 수행 시간을 계산합니다.".format(func.__name__))
#         start = time.time()  # 1970년 1월1일 0시0분0초 0
#         func()
#         end = time.time()
#         print("함수 수행 시간은 {}입니다.".format(start-end))
#
#     return my_inner_func
#
# @my_outer_func
# def my_func():
#     print("my_func() 함수가 호출되었어요!!")
#
# #decorated_my_func = my_outer_func(my_func)
# #decorated_my_func()
# my_func()

#####################################################

# def print_user_name(*args):   # 인자로 들어온 사람의 이름을 출력
#     # args는 tuple로 받아요!
#     for name in args:
#         print(name)
#
# print_user_name("홍길동","신사임당")   # 이렇게도 가능
# print_user_name("홍길동","신사임당","유관순")   # 이렇게도 가능

# def print_user_name(**kwargs):   # 인자로 들어온 사람의 이름을 출력
#     # kwargs는 dict로 받아요!
#     for key in kwargs.keys():
#         print(kwargs.get(key))
#
# # { "name1" : "홍길동", "name2" : "신사임당" }
# print_user_name(name1="홍길동",name2="신사임당")

# Decorator에 대해서 한가지 더 알아보아요!!

def my_outer(func):

    def my_inner(*args,**kwargs):
        print("데코레이터!! 시작")
        func(*args,**kwargs)
        print("데코레이터!! 끝!!")

    return my_inner

@my_outer
def my_func():
    print("이것은 소리없는 아우성!!")

@my_outer
def my_add(x,y):
    print("두 수의 합은 : {}".format(x+y))

#my_func()
my_add(10,20)
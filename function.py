# def test():
#     print('hello function')
#     #pass executes the func
#
# test()

# def user(name):
#     print(f'your name is {name}')
#
# user('ram')

# def user(name,age):
#     print(f'your name is {name}')
#     print(f'your age is {age}')
#
# user('ram',20)

# simple interest nikalni
# def take_value():
#     pass
# def calc():
#     pass
# def display():
#     pass

#
# def test():
#     z=10
# #     y=20
# return[z,y]

# simple interest

# def takevalue():
#     p = float(input('enter the value of principle'))
#     t = float(input('enter the value of time'))
#     r = float(input('enter the value of rate'))
#     return [p, t, r]
#
#
# def calc():
#     data = takevalue()
#     p = data[0]
#     t = data[1]
#     r = data[2]
#     return p * t * r / 100
#
#
# def display():
#     print(f'the interest is {calc()}')
#
#
# display()

# second no.
# def info(name,age):
#     x=0
#     while x<age:
#         print(name)
#         x+=1
# info('alisha',10)


# def students():
#     '''this is students function'''
#     return "hello"
# print(students) #memory location dincha and function execute huncha
# print(students())
# print(students.__doc__)  #documentation print garcha

# def students():
#     print('hello')
#
# print(students())

# def students(name,age):
#     print(f'ur name is {name}')
#     print(age)
# students('ram',20)


# def students(name, age=0):
#     print(f'ur name is {name}')
#     if age > 0:
#         print(age)
#
#
# students('ram', 20)


# def students(*name):
#     print(name)
# students('madan','gita','hari')

# **age is keyword argument
# *name is array argument

#endless parameter  pass method
# def students(*name,**age):
#     print(name)
#     print(age)
# students('madan','gita','hari',name='ram',age=20)

# x=10
# def data():
#     global x
#     x=x*2      #x=local and multiplied is global
#     print(x)
#     pass
# data()


# def pr(name):
#     print(name)
#
# pr('hello')


# def get_type(data):
#     print(type(data))
# x=10
# get_type(x)

#function decorator read

# def get_doc(function):
#     def test():
#         # print(function.__doc__)
#          return f'{function.__name__}'
#
#
#     return test
#
# @get_doc
# def users(name):
#     """hello user function"""
#     pass
#
# users()


# def division(function):
#     def test(x,y):
#         if x == 0 or y == 0:
#             print(f'value must not be zero')
#             return
#         return function(x,y)
#     return test
#
# @division
# def users(x, y):
#     return y/x
#     pass
# print(users(10, 7))

#virtual env
#pip list
#cd desktop
#cd test
#python -m venv project_env
#project_env\scripts\activate
#pip list
#project_env\scripts\deactivate.bat
#pip install request
#pip freeze>requirement.txt

# data=[1,2,3]
# print(dir(data))
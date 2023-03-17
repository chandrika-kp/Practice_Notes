# First program
'''
print("hello")
# Multiplication
x = int(input("multiplier = "))
multiply = int(input("multiplicand = "))
for i in range(1, multiply+1):
    z = x*i
# print(z)
    print(x, ' x ', i, ' = ', z) '''
#
# # list of people
# '''name = " poorna chandrika "
# first_name = name.split()[0]
# print(first_name)'''
#
# x = int(input("enter no. of people = "))
# for Names in range(x+1):
#     Names = input(" name = ")
#     list = list[Names]
#     print(list)
#     new_list = list.append
#     print(new_list)
# '''first_name = Names.split()[0]
# print(first_name)# for Names in new_list)
#
#         #print(first_name)
#     #else
# last_name = Names.split()[1]
# print(last_name)#for Names in new_list)'''
#
# print('Please enter an option')
# z=input('Your choice:b/w 1 to 5 ')
# print('\n')
# print('Please enter the first number')
# a=float(input('First number: '))
# print('Please enter the second number')
# b=float(input('Second number: '))
# print('\n')#if/elif statements to compute the chosen operation
# if z=='1':
#         c= a+b
#         print('1: Add two numbers')
#         print('a+b=',c)
# elif z=='2':
#         c=a-b
#         print('2: Subtract two numbers')# your code goes here
#         print('a-b=',c)
# elif z=='3':
#         c=a*b
#         print('3: Multiply two numbers')# your code goes here
#         print('a*b=',c)
# elif z=='4':
#         print('4: Divide two numbers')
#         if b==0:
#             print('Illegal division -- denominator equals zero')
# # el:
# #         c=a/b# your code goes here
# #         print('a/b=',c)
# #     elif z=='5':
# #         c=a**b
# #         print('a**B',c)
# # else:
# #     print('Invalid entry')
# print("Bye Bye")

#inval=float(input('Input a number greater than zero and less than or equal to 10: '))
# your code goes here
#endval = float(input("max value: "))
# if 0<inval<=float(10):
#     sum=inval
#     while sum<=endval:
#         sum += inval
#     print(sum)
#

# else:
#     print('You did not enter a value between 0 and 10')
# In order to ensure an exact match with the answer checker, please use the following
# code in the event that the user enters an invalid value:
#          print('You did not enter a value between 0 and 10')
#
# for i in range(0,5):
#     for j in range(0,4):
#         print('i =',i,' j=',j, ' i*j=',i*j)
# flag=0
# while flag==0:
#     z=float(input('Enter a number between 0 and 10: '))
#     print()
#     if z>=0 and z<=10:
#         flag=1
#     else:
#         print('Input error -- please try again')
#         print()
# print('Explain what the while loop is doing.')
# avalue = 3.14
# bvalue = 35
# if not(avalue <= 20) or (bvalue < 20):
# print('Thank you')
# print('Did the code within the if statement execute?')
#
# def months_days(month_name,number_of_days):
#     print(str(month_name)+" has "+ str(number_of_days)+" days")
# months_days("june",30)
# months_days("july",31)
# def lucky_number(name):
#   number = len(name) * 9
#   print("Hello " + name + ". Your lucky number is " + str(number))
# lucky_number("Kay")
# lucky_number("Cameron")
# 1) Complete the function to return the result of the conversion

# def convert_distance(miles):
#     km = miles*1.6
#     return km
# my_trip_miles = 55
# # In this blank, we have to convert my_trip_miles to kilometers by calling the above defined function
# my_trip_km = convert_distance(my_trip_miles)
# # Here, we are printing the result after the conversion
# print("The distance in kilometers is " + str(my_trip_km))
# # Here, we are calculating the number of kilometers in round trip by doubling the above result.
# print("The round-trip in kilometers is " + str(my_trip_km*2))


# def format_name(first_name,last_name):
#     if first_name == "":
#         print('"'"Name:",last_name,'"')
#     elif last_name == "":
#         print('"'"Name:",first_name,'"')
#     elif first_name != "" and last_name!="":
#         print('"'"Name:",first_name,',',last_name,'"')
#     else:
#         print("' '")
# print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

#format_name("", "Madonna")
# Should return the string "Name: Madonna"

#print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

#print(format_name("", ""))
# # Should return an empty string
#
# #def sum(x, y):
#  #       return(x+y)
# #print(sum(sum(1,2), sum(3,4)))
#
# # if ((10 >= 5*2) and (10 <= 5*2)):
# #     print("true")
# # else :
# #     print
#
# # def factorial(n):
# #     result = 1
# #     for x in range(1,n+1):
# #         result = result*x
# #         return result
# #     for n in range(0,x+1):
# #         print(n, factorial(n + 1))
# #
# #for x in range(1, 10, 3):
#  #   print(x)
# # for x in range(10):
# #     for y in range(x):
# #         print(y)
#
# # names=['aa xy','bb aa','cc bb','cc dd','pq aa','oo bb','mn cc','ij cc']
# # first=[]
# # second=[]
# # for i in names:
# #     d=i.split()
# #     first.append(d[0])
# #     second.append(d[1])
# # a=input("Enter name :")
# # b=input('enter ur choice (parent/sibling): ')
# # if b=="parent":
# #     if a in first:
# #         print("checking in first names list......")
# #         print(a, " is parent ")
# #         #x=first.index(a)
# #         #print(x)
# #         list_of_parents=[]
# #         list_of_indexp=[]
# #         for p,q in enumerate(first):
# #             print(p,q)
# #             if q==a:
# #                 list_of_indexp.append(p)
# #         print(list_of_indexp)
# #         for k in list_of_indexp:
# #             list_of_parents.append(names[k])
# #         print("any one in the below list  can be a parent of given name")
# #         print(list_of_parents)
# # elif b=="sibling":
# #     if a in second:
# #         print("checking in last names list....")
# #         print(a,"has siblings")
# #         list_of_siblings=[]
# #         list_of_index=[]
# #         for index,elem in enumerate(second):
# #             print(index,elem)
# #             if elem==a:
# #                 list_of_index.append(index)
# #         print(list_of_index)
# #         for j in list_of_index:
# #             list_of_siblings.append(names[j])
# #         print(list_of_siblings)
#
#
# # a = [1, 2, 3, 4]
# # b = ['a', 'b', 'c']
# # print(a[-1])
# # b.pop()
# # print(b)
# # c=str(len(a)+len(b))
# # print("sum of lengths of two lists " + c)
# # print(a+b)
#
# # t = [1, 2, 3, 4, 5]
# # def add_all(t):
# #     total = 0
# #     for x in t:
# #         total += x
# #     return total
# # print(add_all(t))
# # #
# # # #print(sum(t))
# #
# # s=[1,2,3,4,5,6]
# # y=s[:3]
# # z=s[3:]
# # print(y)
# # print(z)
# # print(y+z)
# # y[0]=6
# # print(y)
#
# a=2
# b=3
# alist_examp =[1,3.4,'asdf',96, True, 9.6,'zxcv',False, 2>5,a+b]
# print(alist_examp)
# print(type(alist_examp))
# print('This list contains ', len(alist_examp), ' elements')
# tmp=alist_examp
# print(tmp)
# print(alist_examp)
# tmp[3]='vbnm'
# print(tmp)
# print(alist_examp)
# tmp=alist_examp.copy()
# print(tmp)
# print(alist_examp)
# tmp[3]='vbnm'
# print(tmp)
# print(alist_examp)
# print()
# c=3 + alist_examp[1]
# alist_examp[1]= c +alist_examp[0]
# print(c)
# print(alist_examp)
# for i in range(len(alist_examp)):
#     print('Element',i, '= ', alist_examp[i])
# x=[3,4,5.5,6,7.9]
# y=[-300,3.14]
# z=[x , y, 3.45678]
# print()
# print(z)
# print()
# print('The list z contains ', len(z),' elements')
# print()
# for i in range(len(z)):
#     print('Element with index ',i,' = ',z[i])
# print(z[0][2])
# print(z[1][0])
# for j in range(len(x)):
#     print(z[0][j])
# for value in z:
#     print(value)
#
# my_string="this is a string"
# dir(my_string)
# print(my_string.capitalize())
# print(type(my_string))
# print(my_string[:])
# my_string="i like %s"% "python"
# print(my_string)
# python="programming"
# my_string="i like %s"% python
# print(my_string)
# my_string="i like %s and %s"% ("python",python)
# print(my_string)
# my_string="%i + %i= %i"%(1,2,3)
# print(my_string)
# my_string="%.2f"%2.345678
# print(my_string)
# print("%(lang)s %(lang)s %(lang)s is fun!"%{"lang":"python"})
# print("%(x)i + %(y).2f = %(z)s" %{"x":1,"y":3,"z":"sum"})
# print("python is as simple as {0},{1},{2}".format("c","C++","java"))
# xy={"x":0,"y":1}
# print("graph a point at where {x} and {y}".format(**xy))
#
# #LISTS
#
#
# my_list=[]
# my_list=list()
# my_list=[1,2,3]
# my_list1=["a","b","c"]
# my_nested_list=[my_list,my_list1]
# print(my_nested_list)
# print(my_list)
# new_list=[]
# my_list3=[4,5]
# my_list.extend(my_list3) #we cannnot assign to variable orelse it gives none in str methods
# print(my_list)
# my_combo_list=my_list1+my_list
# print(my_combo_list)
# sort_list=[40,30,60,10,100]
# sort_list.sort()  #we cannnot assign to variable orelse it gives none in str methods
# print(sort_list)
# sort_list2=[12,45,21,36,1,8,759,123]
# sort_list2.sort()
# print(sort_list2)
#
# #tuple
# my_tuple=()
# print(my_tuple)
# empty_tuple=tuple()
# print(empty_tuple)
# another_tuple=tuple([1,2,3])
# print(another_tuple)
# print(another_tuple[0:2])
#
# #Dictonaries
#
# my_dic={} #empty dictonary
# another_empty_dic=dict()
# dict1={"name":"chandu","Dob":"16th"}
# print(dict1)
# print(dict1["name"])
# print(dict1.keys())
# print("name" in dict1)
# print("name" in dict1.keys())  #run slower than above
# print("age" in dict1)
#
# x=[i for i in range(5)]
# print(x)
#
# #comprehensions
# #if[i for i in line if "some term" in i]:
#
# x=['1','2','3','4','5']
# y=[float(i) for i in x]
# print(y)
# comp=[[1,2,3],[4,5,6],[7,8,9]]
# print([i for num in comp for i in num])
# print({i: "i" for i in range(90, 101)})
# print({i:float(i) for i in range(90, 101)})
# print({i: str(i) for i in range(90, 101)})

#
# No_of_students = int(input("Enter number of students : "))
# No_of_days = int(input("Enter number of days : "))
# Students = []
# for i in range(No_of_students):
#     i = input("Enter student name:"+str(i+1)+"   ")
#     Students.append(i)
# Students.sort()
# print(Students)
# empty_list = [0] * (len(Students))
# for j in range(No_of_days):
#     for k in range(No_of_students):
#         l = input("If %s was present today: Enter p if NOT Enter a :     " % Students[k])
#         if l == 'p':
#             ndx = Students.index(Students[k])
#             empty_list[ndx] += 1
# Total_attendance = empty_list
# print("Roll_no" "NAMES        ""Attendance_percentage")
# for i in range(len(Students)):
#     Roll_no = i+1
#     Day_attendance = Total_attendance[i]
#     Attendance_percentage = (Day_attendance/No_of_days)*100
#     print(Roll_no, Students[i].ljust(10, ' '), Attendance_percentage)
#
#
# No_of_students = int(input("Enter number of students : "))
# No_of_days = int(input("Enter number of days : "))
# Students = []
# for i in range(No_of_students):
#     i = input("Enter student name:"+str(i+1)+"   ")
#     Students.append(i)
# Students.sort()
# print(Students)
# empty_list = [0] * (len(Students))
# for j in range(No_of_days):
#     for k in range(No_of_students):
#         l = input("If %s was present today: Enter p if NOT Enter a :     " % Students[k])
#         if l.lower() == 'p':
#             ndx = Students.index(Students[k])
#             empty_list[ndx] += 1
# Total_attendance = empty_list
# for i in range(No_of_students):
#     Roll_no = i+1
#     Day_attendance = Total_attendance[i]
#     Attendance_percentage = (Day_attendance/No_of_days)*100
#     print(Roll_no, Students[i].ljust(10, ' '), Attendance_percentage)

# t = [[1, 2], [3], [4, 5, 6]]
#
# s=sum([ sum(i) for i in t ])
#print(s)
# t=[1,3,5]
# cumsum=[]
# sum=0
# # for i in range(len(t)):
#     # sum+=t[i]
#     # cumsum.append(sum)
# print(cumsum)
# t=[1,2,3]
# x=[t[0]]
# for num in t[1:]:
#     y=x[-1]+num
#     x.append(y)
# print(x)

# t=[1,2]
# t.remove(t[0])
# t.remove(t[-1])
# print(t)
# t=[1,10,5,6,11,15,19,30]
# t.sort()
# x=len(t)//2
# if len(t)%2==0:
#     median=(t[x-1]+t[x])/2
# else:
#     median=t[x]
# print(median)

# s="a boy was playing"
# for letter in s:
#         if letter==vowels[i]:

# s="a boy was playing"
# vowels=['a','e','i','o','u']
# for j in range(len(vowels)):
#       for i in range(len(s)):
#           if s[i] in vowels:
#               s=s.replace(vowels[j],'x')
# for i in s:
#     print(i)
#     if i in vowels[:]:
#         s.replace(i,'x')
# for v in vowels:
#     print(v)
#     s=s.replace(v,'x')
#print(s)

# items={"toy":[100,5,5],"ball":[20,2,3.5],"pen":[10,3,10]}
# item=list(items.keys())
# print(item)
# y=input("select items in the above list:")
# # cost=items[y][0]
# # quantity=items[y][1]
# # discount=items[y][2]
# cost,quantity,discount=items[y][0],items[y][1],items[y][2]
# print("{} :\n COST:{} \n NO.OF QUANTITY:{} \n DISCOUNT:{}".format(y,cost,quantity,discount))
# z=int(input("enter no.of quantity of {} you want :  ".format(y)))
# if z>quantity:
#     print(f'{y} is out of stock')
# elif z<=quantity:
#     items[y][1]=quantity-z
     #price=(cost*z)-(cost*z*discount/100)
#     discount=(cost*z*items[y][2])/100
#     price=(cost*z)-discount
#     print(price)
#     #print(items[y][1])
# print(items)


# items={"toy":[100,5,5],"ball":[20,2,3.5],"pen":[10,3,10]}
# item=list(items.keys())
# #print(item)
# cart_list=[]
# for each_item in item:
#     y=each_item
#     cost,quantity,discount=items[y][0],items[y][1],items[y][2]
#     print("{} :\n COST:{} \n NO.OF QUANTITY:{} \n DISCOUNT:{}".format(y,cost,quantity,discount))
#     z=int(input("enter no.of quantity of {}'s you want :  ".format(y)))
#     # if z>quantity:
#     #     print("enter no.of quantitity less {}".format(items[y][1]))
#     if z<=quantity:
#         items[y][1]=quantity-z
#         discount=(cost*z*items[y][2])/100
#         price=(cost*z)-discount
#         cart_list.append(y)
#
#
#         #print(price)
#     #print(items[y][1])
#     elif z>quantity:
#         print("out of range")
#
#
# print(items)
# print(cart_list)
#
# a=3
# b=4
# c=[a, b]
# d=[c, a]
# e=d+d
# print(e)
#print(e[2])

# x=[2, 3, 4, 5, 'a', 'bee', 'c', 'dee']
# x.append(3.14)
# print(x)
# x.extend(['m', 5.6, 'gee'])
# print(x)
# x.pop()
# print(x)
# x.pop(3)
# print(x)

# x=[ ]
# for i in range(2):
#     x.append(i)
#     x.extend(x)
# print(x)

# xvals=['there', 'everywhere', 'herehere', 'zero', 'nowhere']
# y=[]
# for x in xvals:
#     x.find("ere")
#     print(x)
#     y.append(x.find('ere'))
# print(y)
# y=['g', 'j', 'k','z', 'd','d', 'w']
# y.sort()
# print(y)
#
# x=[2, 3, 4, 5, 'a', 'bee', 'c', 'dee']
# print(x[::2])
# print(x[2:len(x)])

# x=[1, 2, 3, 4, 5, 6, 7, 8]
# y=x[::2]
# z=y.copy()
# y.append(x[1::2])
#
# z.extend(x[1::2])
# print(y)
# print(z)
# x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# y=x[-1:-5:-1]
# z=x[::3]
# for i in range(len(z)):
#     print(y[i] ,z[i])

# import math
# import matplotlib.pyplot as plt
# maxpoints=1000
# t=[ ]
# y=[ ]
# dx=0.01
# w0=5;
# for point_count in range(maxpoints):
#     tp=point_count*dx
#     t.append(tp)
#     y.append(math.sin(w0*tp))
# plt.plot(t,y)
# plt.xlabel('t value (sec)')
# plt.ylabel('y value')
# plt.savefig('plot.png')

# nvals=8
# message='Input a number: '
# a=[ ]
# for i in range(nvals):
#   a.append(float(input(message)))
# print('The list = ',a)

# print('{:,}'.format(1223334444))
# msg = input("enter a message:")
# print("Message is (msg)")
# print(98.6)
# _2esd="ers"
# print(_2esd)
# x = int(98.9)
# print(x)
# hrs = input("Enter Hours:")
# rate=2.75
# gross=float(hrs)*rate
# print("Pay: ",gross)
# import math
# degrees = 45
# radians = degrees / 180.0 * math.pi
# x=math.sin(radians)
# print(x)
# y= math.sin(math.radians(30))
# print(y)
# print(math.sin(math.radians(90)))
# print( math.sqrt(2))


# print(print_lyrics)
# type(print_lyrics)
# def print_lyrics():
#     print("I'm a lumberjack, and I'm okay.")
#     print("I sleep all night and I work all day.")
# print_lyrics()
# def repeat_lyrics():
#     print_lyrics()
# repeat_lyrics()
# !/bin/python3
#
# import math
# import os
# import random
# import re
# import sys
#

#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

# def fizzBuzz(n):
#     # Write your code here
#     for i in range(1, n + 1):
#         if ((i % 3) == 0) and ((i % 5) == 0):
#             print("FizzBuzz\t");
#         elif ((i % 3) == 0) and ((i % 5) != 0):
#             print("Fizz\t");
#         elif ((i % 5) == 0) and ((i % 3) != 0):
#             print("Buzz\t");
#
#         elif ((i % 3) != 0) and ((i % 5) != 0):
#             print(i);
#     return 0;
#
#
# if __name__ == '__main__':
#     n = int(input().strip())
#
#     fizzBuzz(n)
#
# x = 0
# if x < 2:
#     print('Small')
# elif x < 10 :
#     print('Medium')
# else :
#     print('LARGE')
# print('All done')
#
#
# x=2.0
# if x < 2:
#     print('Below 2')
# elif x >= 2:
#     print('Two or more')
# else:
#     print('Something else')
#
# # astr ="hello Bob"
# # istr = int(astr)
# # print('First', istr)
# # astr = '123'
# # istr = int(astr)
# # print('Second', istr)
#
# astr = 'Hello Bob'
# istr = 0
# try:
#     istr = int(astr)
# except:
#     istr = -1
# print(istr)
# import math
# friends=int(input("enter no:"))
# K=int(input())
# list = []
# for i in range(1,K+1):
#     A=i
#     if (K%A)==0:
#         B=int(K/A)
#         # print(A , B)
#         if (A/2)!=0:
#             # print("If A="+str(A),",B="+str(B),".GCD(A,B)=",+str(math.gcd(A,B)))
#             GCD=math.gcd(A,B)
#             list.append(GCD)
#             list.sort()
# print(list[-1])
# max=list[-1]
# if list[-1]==max:
#     print(A//6,B*6)
#     # print(B*6)
#
# # your code goes here
# import math
#
# friends = int(input("enter no:"))
# K = int(input())
# list = []
# for i in range(1, K + 1):
#     A = i
#     if (K % A) == 0:
#         B = int(K / A)
#         # print(A , B)
#         if (A / 2) != 0:
#             # print("If A="+str(A),",B="+str(B),".GCD(A,B)=",+str(math.gcd(A,B)))
#             GCD = math.gcd(A, B)
#             list.append(GCD)
#         list.sort()
#         else:
#         print("-1-1")
# # print(list[-1])
# max = list[-1]
# if list[-1] == max:
# #     print(A // 6, B * 6)
# #
#
# def thing():
#     print('Hello')
#
# print('There')
#
# def func(x) :
#     print(x)
#
# func(10)
# func(20)
# def stuff():
#     print('Hello')
#     return
#     print('World')
#
# stuff()
# def greet(lang):
#     if lang == 'es':
#         return 'Hola'
#     elif lang == 'fr':
#         return 'Bonjour'
#     else:
#         return 'Hello'
#
# print(greet('fr'),'Michael')
# def addtwo(a, b):
#     added = a + b
#     return a
#
# x = addtwo(2, 7)
# print(x)
#
# def greet(lang):
#     if lang == 'es':
#         return 'Hola'
#     elif lang == 'fr':
#         return 'Bonjour'
#     else:
#         return 'Hello'
#
# print(greet('fr'),'Michael')
#
# list1 = [10, 20, 30, 40, 50]
# list1.insert(7, 25)
# print(list1)
#
#
# def modify_list(arg_list):
#     arg_list = arg_list + [60, 70, 80]
#     print("Inside function:", arg_list)
#
#
# i_list = [10, 20, 30, 40, 50]
# print("Before function call:", i_list)
# modify_list(i_list)
# print("After function call:", i_list)
#
# my_list = [0] * 5
# for index in range(1, 5):
#     my_list[index] = (index - 1) * index
#
# print(my_list)
#
# FHW=open("data.txt","w")
# FHW.write("written some thing")
# print(FHW.tell())
# print("closed?",FHW.closed)
# FHW.close()
# print("after closing the file closed?",FHW.closed)
#
# set_1 = {1, 2, 3, 1, 2, 4, 5, 3, 4, 8, 9, 7, 10}
# for index in range(len(set_1)):
#     print(index, end=" ")
#
# def find_sum(a,b):
#     try:
#         print(a+c)
#     except ValueError:
#         print("Function name error")
#     finally:
#         print("Sum finally")
# try:
#     find_sum(12,13)
# except NameError:
#     print("Invocation name error")
# finally:
#     print("Invocation finally")
#
# def value(num1):
#     list1=[]
#     while num1!=0:
#         if num1%2==0:
#             list1.append(num1)
#         else:
#             break
#         num1-=2
#     print(list1)
# value(10)
#
#
# def sample(value):
#     sum1 = 0
#     print(value)
#     for i in value:
#
#         if i % 2 != 0:
#             sum1 += value[i]
#
#         else:
#             sum1 -= i
#     print(sum1)
#
#
# dict1 = {1: 2, 2: 4, 3: 6, 5: 8}
# sample(dict1)
#
# tuple1=(10)
# print(tuple1)
# print(type(tuple1))
#
# sample_dict={'a':"apple",'b':"ball"}
# sample_dict.update({'b':"boy", 'c':'cat' })
# print(sample_dict['a'],sample_dict.get('b'),sample_dict.get('c'))
#
#
# n = 5
# while n > 0:
#     print(n)
# print('All done')
# tot = 0
# for i in [5, 4, 3, 2, 1] :
#     tot = tot + 1
# print(tot)

# smallest_so_far = -1
# for the_num in [9, 41, 12, 3, 74, 15] :
#    if the_num < smallest_so_far :
#       smallest_so_far = the_num
# print(smallest_so_far)
# if smallest_so_far is None:
#     smallest_so_far= value
# n = int(input())
# for i in range(n):
    # if i<n:
        # print(i**i)
#
# largest = None
# smallest = None
# while True:
#     num = input("Enter a number:")
#     if num == "done":
#         break
#     try:
#         num = int(num)
#         for number in range(num):
#             if largest is None or largest<num:
#                 largest=num
#                 continue
#             elif smallest is None or smallest>num:
#                 smallest=num
#     except ValueError:
#         print("Invalid Number")
# print("Maximum is", largest)
# print("Minimum is", smallest)
#
# largest = None
# smallest = None
#
# while True:
#
#     num = input("Enter a number: ")
#     if num == "done":
#         break
#     if smallest == None and largest == None:
#         largest = smallest = num
#
#     try:
#         if int(num) > int(largest):
#             largest = num
#         if int(num) < int(smallest):
#             smallest = num
#     except ValueError:
#         print("Invalid input")
#
# print("Maximum is", largest)
# print("Minimum is", smallest)
# airline="AirIndia"
# luggage_weight=28
# AI_weight_limit=30
# EM_weight_limit=35
# if(airline=="AirIndia"):
#     if(luggage_weight<=AI_weight_limit):
#         print("Check-in cleared")
#     else:
#         print("Remove some luggage and come back")
# elif(airline=="Emirates"):
#     if(luggage_weight<=EM_weight_limit):
#         print("Check in cleared")
#     else:
#         print("Remove some luggage and come back")
# else:
#     print("Invalid airline")
#
# print(type(3))
# print(type("Hello World"))
# print(type(False))
# print(type(2.0))

# import turtle # allows us to use the turtles library
#
# wn = turtle.Screen() # creates a graphics window
# wn.setup(400,400) # set window dimension
#
# circle_rad=60 # setthe radius
# rectangle_width=240 #set the width
# rectangle_height=30 #set the height
#
# alex = turtle.Turtle() # create a turtle named alex
# alex.shape("turtle") # alex looks like a turtle
# alex.color('green') # alex has a color
# alex.circle(circle_rad)
# # alex.backward(rectangle_width/2)
# alex.forward(rectangle_width/2)
# alex.right(90)
# alex.forward(rectangle_height)
# alex.right(90)
# alex.forward(rectangle_width)
# alex.right(90)
# alex.forward(rectangle_height)
# alex.right(90)
# alex.forward(rectangle_width/2)
# n = int(input())
# if (2<=n<=20):
#     for i in range(1,11):
#         mul=n*i
#         print(str(n) +'x'+str(i)+'='+str(mul))
#
# radius=int(input())
# area=3.14*radius*radius
# print(area)

# print("Let's see some examples.\n\nDid you notice the empty lines?")
# print("Do you notice\t the tab space?\nDid you see that I have moved to next line?")
# print("Do you want a \" in your text?")
# print("Are you going to store more info about escape sequence in Z:\\\\user\\escape_sequence.txt??")
# #Every print starts with a new line, end can change that behavior by specifying your own character
# print("Did you see I start here", end=" ")
# print("and I end in the same line although from a different print?")
# print("As observed escape sequences help you to format your output.")

# import re
# a=[]
# No_of_integers=int(input())
# for i in range(No_of_integers):
#     n = int(input())
#     a.append(n)
# print(a)
# print(*a[::-1],sep=" ")
# print(" ".join(map(str,a[::-1])))


# n = int(input().strip())
# arr = list(map(int, input().rstrip().split()))
# print (*arr[::-1], sep=' ')

# s=a[::-1]
# b=" ".join(s)
# print(b)
# b=len(a)-1
# result=0
# while(b>=0):
#     result=(result+a[b]+" ")
#     b-=1
#     print(result)
import sys

# Read input and assemble Phone Book
# n = int(input())
# phoneBook = dict(input().split()for i in range(n))
# for keys,values in phoneBook.items():
#     print(keys+" "+values)
# for i in range(10000):
#     query=input()
#     if query in phoneBook.keys():
#         print(phoneBook[query])
#     else:
#         print("Not found")
#         break
#
#  for i in range(n):

#     contact = input().split(' ')
#     phoneBook[contact[0]] = contact[1]
#
# # Process Queries
# lines = sys.stdin.readlines()
# for i in lines:
#     name = i.strip()
#     if name in phoneBook:
#         print(name + '=' + str( phoneBook[name] ))
#     else:
#         print('Not found')

#
# n = int(input())
# def factorial(n):
#     # Write your code here
#     if n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(n))

# DecimalToBinary(num // 2)
         # print(num % 2,end='')


# num =int(input())
# def DecimalToBinary(num):
#     binary=bin(num).replace("0b","")
#     # binary=bin(num)[2:]
#     return str(binary)
# print(DecimalToBinary(num))


# def find_max_ones(num):
#     bin_num = bin(num)[2:]
#     # print(bin_num)
#     return len(max(bin_num.replace('0', ' ').split()))
#
# num = int(input())
# max_ones = find_max_ones(num)
# print(max_ones)
# rows=int(input())
# col=int(input())
# matrix=[]
# for i in range(6):
#     a=[]
#     for j in range(6):
#         a.append(int(input()))
#     matrix.append(a)
#     # print(matrix)
# for i in range(6):
#     for j in range(6):
#         print(matrix[i][j],end=" ")
#     print()
# def hourglassSum(matrix):
#     # want to find the maximum hourglass sum
#     # minimum hourglass sum = -9 * 7 = -63
#     new_list = []
#     for i in range(0,4):
#         for j in range(0,4):
#             # sum of top 3 elements
#             level1 = sum(matrix[i][j:j+3])
#
#             # sum of mid element
#             level2 = sum(matrix[i+1][j:j+1])
#
#             # sum of bottom 3 elements
#             level3 = sum(matrix[i+2][j:j+3])
#
#             max_number = level1+level2+level3
#             new_list.append(max_number)
#     max_sum = max(new_list)
#     return max_sum
#
# print(hourglassSum(matrix))
# arr = []
#
# for _ in range(6):
#     tmp = [int(x) for x in str(input()).split(" ")]
#     arr.append(tmp)
# print(arr)
# print(tmp)
#
# maximum = -9 * 7
#
# for i in range(6):
#     for j in range(6):
#         if j + 2 < 6 and i + 2 < 6:
#             result = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
#             if result > maximum:
#                 maximum = result
#
# print(maximum)
#!/usr/bin/env python3
#import csv
#import re
#Import libraries

# def contains_domain(address, domain):
#   """Returns True if the email address contains the given domain,
#     in the domain position, false if not."""
#   domain_pattern = r'[\w\.-]+@'+domain+'$'
#   if re.match(domain_pattern, address):
#       return True
#   return False
#
# def replace_domain(address, old_domain, new_domain):
#   """Replaces the old domain with the new domain in
#     the received address."""
#   old_domain_pattern = r'' + old_domain + '$'
#   address = re.sub(old_domain_pattern, new_domain, address)
#   return address
#
# def main():
#   """Processes the list of emails, replacing any instances of the
#     old domain with the new domain."""
#   old_domain, new_domain = 'abc.edu', 'xyz.edu'
#   csv_file_location = '<csv-file-location>'
#   report_file =  '<data-directory>' + '/updated_user_emails.csv'
#   user_email_list = []
#   old_domain_email_list = []
#   new_domain_email_list = []
#   with open(csv_file_location, 'r') as f:
#       user_data_list = list(csv.reader(f))
#       user_email_list = [data[1].strip() for data in user_data_list[1:]]
#   for email_address in user_email_list:
#       if contains_domain(email_address, old_domain):
#           old_domain_email_list.append(email_address)
#           replaced_email = replace_domain(email_address, old_domain, new_domain)
#           new_domain_email_list.append(replaced_email)
#   email_key = ' ' + 'Email Address'
#   email_index = user_data_list[0].index(email_key)
#   for user in user_data_list[1:]:
#       for old_domain, new_domain in zip(old_domain_email_list, new_domain_email_list):
#           if user[email_index] == ' ' + old_domain:
#               user[email_index] = ' ' + new_domain
#   f.close()
#   with open(report_file, 'w+') as output_file:
#       writer = csv.writer(output_file)
#       writer.writerows(user_data_list)
#       output_file.close()
# main()
#
# import re
# def error_search(log_file):
#     error = input("What is the error? ")
#     returned_errors = []
#     with open(log_file, mode='r', encoding='UTF-8') as file:
#         for log in file.readlines():
#             error_patterns = ["error"]
#             for i in range(len(error.split(' '))):
#                 error_patterns.append(r"{}".format(error.split(' ')[i].lower()))
#             if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
#                 returned_errors.append(log)
#         file.close()
#     return returned_errors
# def file_output(returned_errors):
#     with open(os.path.expanduser('~') + '/data/errors_found.log', 'w') as file:
#         for error in returned_errors:
#             file.write(error)
#         file.close()
# if __name__ == "__main__":
#   log_file = sys.argv[1]
#   returned_errors = error_search(log_file)
#   file_output(returned_errors)
#   sys.exit(0)

#!/usr/bin/env python3
# import unittest
# from emails import find_email
# class TestFile(unittest.TestCase):
#   def test_basic(self):
#     testcase = [None, "Bree", "Campbell"]
#     expected = "breee@abc.edu"
#     self.assertEqual(find_email(testcase), expected)
#   def test_one_name(self):
#     testcase = [None, "John"]
#     expected = "Missing parameters"
#     self.assertEqual(find_email(testcase), expected)
# if __name__ == '__main__':
#   unittest.main()
#
#!/usr/bin/env python3
# import unittest
# from emails import find_email
# class EmailsTest(unittest.TestCase):
#     def test_basic(self):
#         testcase = [None, "Bree", "Campbell"]
#         expected = "breee@abc.edu"
#         self.assertEqual(find_email(testcase), expected)
# if __name__ == '__main__':
#   unittest.main()

#!/usr/bin/env python3

# import sys
# import csv
#
# def populate_dictionary(filename):
#   """Populate a dictionary with name/email pairs for easy lookup."""
#   email_dict = {}
#   with open(filename) as csvfile:
#     lines = csv.reader(csvfile, delimiter = ',')
#     for row in lines:
#       name = str(row[0].lower())
#       email_dict[name] = row[1]
#   return email_dict
#
# def find_email(argv):
#   """ Return an email address based on the username given."""
#   # Create the username based on the command line input.
#   try:
#       fullname = str(argv[1] + " " + argv[2])
#   # Preprocess the data
#       email_dict = populate_dictionary('/home/student-04-76348e1477d9/data/user_emails.csv')
#   # Find and print the email
#       return email_dict.get(fullname.lower())
#   except IndexError:
#       return "Missing parameters"
#
# def main():
#   print(find_email(sys.argv))
#
# if __name__ == "__main__":
#   main()

# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a + b
# print(len(c))
#
# fruit = 'Banana'
# fruit[0] = b
# print(fruit)

# fname = input("Enter file name: ")
# fhand = open(fname)
# lst = list()
# for line in fhand:
#     word= line.rstrip().split()
#     for element in word:
#         if element in lst:
#             continue
#         else :
#             lst.append(element)
# lst.sort()
# print(lst)

#!/usr/bin/env python3
# import sys
# import subprocess
#
# f=open(sys.argv[1],"r")
# for line in f.readlines():
#   old_name=line.strip()
#   new_name=old_name.replace("janez","jdoe")
#   subprocess.run(["mv", old_name, new_name])
# f.close()

# stuff = dict()
# print(stuff['candy'])
# stuff = dict()
# print(stuff.get('candy',-1))

# x = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
# y = x.items()
# print(y)
#
# x=(5,1,3)
# y=[(4, 100, 200),(6, 0, 0),(0, 1000, 2000),(5, 0, 300)]
# for i in y:
#     if i>x:
#         print(i)
# c = {'a':10, 'b':1, 'c':22}
# for k, v in c.items() :
#     print(k,v)
# print(c.items())
#
# for p,q in c:
#     print(p,q)


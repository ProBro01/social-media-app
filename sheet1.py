# Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license()" for more information.
# >>> 5**9
# 1953125
# >>> 3//2
# 1
# >>> 7//3
# 2
# >>> 7/3
# 2.3333333333333335
# >>> 6==6
# True
# >>> True * False
# 0
# >>> True & False
# False
# >>> True and False
# False
# >>> ((6>3) and (7>4) or (18==3) and(9>3))
# True
# >>> True is False
# False
# >>> False in 'False'
# Traceback (most recent call last):
#   File "<pyshell#10>", line 1, in <module>
#     False in 'False'
# TypeError: 'in <string>' requires string as left operand, not bool
# >>> ((True == False) or (False > True) and (False <= True))
# False
# >>> s1= "Nice to have it"
# >>> s2 = "here"
# >>> s1+s2
# 'Nice to have ithere'
# >>> a = [1, 2, [3, 4], [5,[100, 200, ['hello']], 23, 11], 1, 7]
# >>> a[3][1][2][0]
# 'hello'
# >>> a.insert(0, s1)
# >>> a.append(s2)
# >>> a
# ['Nice to have it', 1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7, 'here']
# >>> numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 743, 527]
# >>> for var in numbers:
# 	if var%2 == 0 and var<237:
# 		print(var)

		
# 236
# 162
# 104
# 58
# 24
# >>> color_list_1 = set(["White", "Black", "Red"])
# >>> color_list_2 = set(["Red", "Green"])
# >>> for colors in color_list_1:
# 	if colors not in color_list_2:
# 		print(colors)

		
# White
# Black
# >>> a = "Hello everyone"
# >>> alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# >>> for alphabet in alphabets:
# 	if alphabet not in a:
# 		print("String is not Pangram")
# 	else:
# 		print("String is pangram")

		
# String is not Pangram
# String is not Pangram
# String is not Pangram
# String is not Pangram
# String is pangram
# String is not Pangram
# String is not Pangram
# String is not Pangram
# String is not Pangram
# String is not Pangram
# String is not Pangram
# String is pangram
# String is not Pangram
# String is pangram
# String is pangram
# String is not Pangram
# String is not Pangram
# String is pangram
# String is not Pangram
# String is not Pangram
# String is not Pangram
# String is pangram
# String is not Pangram
# String is not Pangram
# String is pangram
# String is not Pangram
# >>> for alphabet in alphabets:
# 	if alphabet not in a:
# 		print("String is not Pangram")
# 		break
# print("String is pangram")
# SyntaxError: invalid syntax
# >>> for alphabet in alphabets:
# 	if alphabet not in a:
# 		print("String is not Pangram")
# 		break

	
# String is not Pangram
# n = 5
# 5 + (5*10+5) + (55*10+5)
# number = 5
# sum = number
# for var in range(2):
#   number = (number * 10) + 5
#   sum += number
# print(sum)

# question 10

# a = input()
# a = a.split('#')
# x = a[0].split()
# print(x)
# y = a[1].split()
# print(y)
# for var in range(len(x)):
# 	x[var] = int(x[var])
# for var in range(len(y)):
# 	y[var] = int(y[var])

# print(x)
# print(y)
#========================================================================
# question 11
# wordseq = ["without", "hello", "bag", "world"]
# wordseq.sort()
# print(wordseq)
#========================================================================

#========================================================================
#question 12
# def getmax(lst):
# 	mxnum = lst[0]
# 	for var in lst:
# 		if var > mxnum:
# 			mxnum = var
# 	return mxnum
# d = {
# 	'Student' : ['Rahul', 'Kishore', 'Vidhya', 'Raakhi'],
# 	'Marks' : [57, 87, 67, 79],
# }
# maxmarks = getmax(d['Marks'])
# print(d['Student'][d['Marks'].index(maxmarks)])
#========================================================================
#========================================================================
#question 13
# sentence = 'hello world! 123'
# letters = 0
# number = 0
# for var in sentence:
# 	if var.isalpha():
# 		letters += 1
# 	elif var.isdigit():
# 		number += 1
# print(letters)
# print(number)
#========================================================================
#========================================================================
#question 14
# d = {
# 	'Name' : ['Akash', 'Soniya', 'Vishakha', 'Akshay', 'Rahul', 'vikas'],
# 	'Subject' : ['python', 'Java', 'python', 'C', 'python', 'Java'],
# 	'Rating' : [8.4, 7.8, 8, 9, 8.2, 5.6],
# }
# newdata = {
# 	'Name' : [],
# 	'Subject' : [],
# 	'Rating' : []
# }
# index = -1
# for var in d['Subject']:
# 	index += 1
# 	if var == 'python':
# 		try:
# 			print(d['Name'][index])
# 			newdata['Name'].append(d['Name'][index])
# 			print(d['Subject'][index])
# 			newdata['Subject'].append(d['Subject'][index])
# 			newdata['Rating'].append(d['Rating'][index])
# 		except Exception as e:
# 			pass

# print(newdata)
#========================================================================
#========================================================================
# question 16
# import math
# movements = {
# 	'UP' : 0,
# 	'DOWN' : 0,
# 	'LEFT' : 0,
# 	'RIGHT' : 0,
# }
# while True:
# 	direction = input("direction>>> ")
# 	if direction == 'UP' or direction == 'up':
# 		movements['UP'] += 1
# 	elif direction == 'DOWN' or direction == 'down':
# 		movements['DOWN'] += 1 
# 	elif direction == 'LEFT' or direction == 'left':
# 		movements['LEFT'] += 1 
# 	elif direction == 'RIGHT' or direction == 'right':
# 		movements['RIGHT'] += 1
# 	elif direction == 'DONE' or direction == 'done':
# 		break
# for var in movements.items():
# 	print(var)
# x, y = movements['RIGHT'] - movements['LEFT'], movements['UP'] - movements['DOWN']
# displacement = math.sqrt((y**2)+(x**2))
# print(f'''
# intial point: (0, 0)
# final point :({x}, {y})
# distance : {displacement}
# 	''')
#========================================================================
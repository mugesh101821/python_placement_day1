from functools import reduce

# a = 0
# b = 1
# while a <= 100:
#     print(a, end=" ")
#     a, b = b, a + b



# a = 0
# b = 1
# c = 1
# while a <= 100:
#     print(a, end=" ")
#     a,b,c=b,c,a+b+c



# List
# list=[1,2,3,45,2]
# print(list[4])
#list slicing makes a new data
#syntax[start:stop:step]
# print(list[1:4])


# list operator
# 1.concatenation operator(+)
# a=[1,2,3]
# b=[4,5]
# print(a+b)
# 2.repetition operator(*)
# num=[1,2]
# print(num*3)
# 3.membership operator(in,not in)
# fruits=["apple","banana","grapes"]
# print("apple" in fruits)
# print("orange" not in fruits)
#4.comparison operator(==,!=,>,<,>=,<=)
# list1=[1,2,3]
# list2=[1,2,3]
# list3=[1,2,4]
# print(list1==list2)
# print(list1==list3)
# print(list1!=list3)
# print(list1>list3)
# print(list1<list3)




# a=[1,2,3,4,5]
# b=[6,7,8,9,10]
# print(a[4])
# print(b[1:4:2])
# print(a+b)
# print(b*2)
# print(3 in a)
# print(11 not in b)
# print(a==b)
# print(a!=b)
# print(a>b)
# print(a<b)
# print(a>=b)
# print(a<=b)


# list methods
# 1.append() - adds an element to the end of the list
# num=[1,2,3]
# num.append(4)
# print(num)
# 2.insert() - adds an element at a specific index
# syntax: list.insert(index, element)
# num.insert(2,5)
# print(num)
# 3.extend() - adds all elements of an iterable to the end of the list
# a=[1,2,3]
# b=[4,5,6]
# a.extend(b)
# print(a)
# 4.remove() - removes the first occurrence of an element from the list
# num=[1,2,3,4,5]
# num.remove(3) # removes the first occurrence of 3 from the list
# print(num)
# 5.pop(index) - removes and returns the element at a specific index (default is the last element)
# num=[10,20,30]
# num.pop(1) # removes and returns the element at index 1 (20 in this case)
# print(num)
# 6.clear() - removes all elements from the list
# num=[1,2,3]
# num.clear() # removes all elements from the list
# print(num)
# 7.index(element) - returns the index of the first occurrence of an element in the list
# num=[1,2,3,4,5]
# print(num.index(3)) # returns the index of the first occurrence of 3 in the list
# 8.count(element) - returns the number of occurrences of an element in the list
# num=[1,2,3,2,4,2]
# print(num.count(2)) # returns the number of occurrences of 2 in the list
# 9.sort() - sorts the elements of the list in ascending order
# a=[4,6,34,9,23]
# a.sort() # sorts the elements of the list in ascending order
# print(a)
# 10.reverse() - reverses the order of the elements in the list
# a=[1,2,3,4,5]
# a.reverse() # reverses the order of the elements in the list
# print(a)
# 11.copy() - returns a shallow copy of the list
# a=[1,2,3]
# b=a.copy() # returns a shallow copy of the list
# print(b)


# num1=[1,2,3,4,5]
# num2=[6,7,8,9,10]
# num1.append(6)
# print(num1)
# num1.insert(2,7)
# print(num1)
# num1.extend(num2)
# print(num1)
# num1.remove(3)
# print(num1)
# num1.pop(4)
# print(num1)
# num1.clear()
# print(num1)
# num1=[1,2,3,4,5]
# print(num1.index(3))
# print(num1.count(2))
# num1.sort()
# print(num1)
# num1.reverse()
# print(num1)
# num3=num1.copy()
# print(num3)


# map(),filter() and list()--->functional programming---->iterates
# should use only on list
# num=[1,2,3,4,5]
# result=list(map(lambda x:x**2,num)) 
# print(result)


# def func(x):
#     return x**2
# result=list(map(func,num))
# print(result)


# num1=[1,2,3,4,5]
# result1=list(filter(lambda x:x%2==0,num1))
# print(result1)



# reduce-->convert into a single value-->functools module
# syntax
# reduce(func,iterable)
# from functools import reduce
# num=[1,2,3,4,5]
# result=reduce(lambda a,b:a+b,num)
# print(result)

# num = 1,2,3,4,5,6,7,8,9,10
# even_numbers = list(filter(lambda x: x % 2 == 0, num))
# even_sum = reduce(lambda a, b: a + b, even_numbers)
# print("Even numbers:", even_numbers)
# print("Sum of even numbers:", even_sum)
# odd_numbers = list(filter(lambda x: x % 2 != 0, num))
# odd_sum = reduce(lambda a, b: a + b, odd_numbers)
# print("Odd numbers:", odd_numbers)
# print("Sum of odd numbers:", odd_sum)




# palindrome
# 1st method - using slicing
# word=input("Enter a word: ")
# if word==word[::-1]:
#     print("It is a palindrome.")
# else:
#     print("It is not a palindrome.")

# 2nd method - using loop
# word=input("Enter a word: ")
# reversed_word=""
# for char in word:
#     reversed_word=char+reversed_word
# if word==reversed_word:
#     print("It is a palindrome.")
# else:
#     print("It is not a palindrome.")


# using loop only for integer
# num=int(input("Enter a number: "))
# original_num=num
# reversed_num=0
# while num>0:
#     digit=num%10
#     reversed_num=reversed_num*10+digit
#     num=num//10
# print(reversed_num)
# if original_num==reversed_num:
#     print("It is a palindrome.")
# else:
#     print("It is not a palindrome.")



# nums = list(map(int(input("Enter sorted numbers separated by space: ").split())))

# if len(nums) == 0:
#     print("New length:", 0)
# else:
#     index = 1

#     for i in range(1, len(nums)):
#         if nums[i] != nums[i - 1]:
#             nums[index] = nums[i]
#             index += 1

#     print("New length:", index)
#     print("Array after removing duplicates:", nums[:index])



# leet code program
# class Solution:
#     def removeDuplicates(self, nums):
#         if not nums:
#             return 0
        
#         index = 1
        
#         for i in range(1, len(nums)):
#             if nums[i] != nums[i - 1]:
#                 nums[index] = nums[i]
#                 index += 1
        
#         return index
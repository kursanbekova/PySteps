# import random
# random #librery
# # 1. Создание списка из случайных чисел от 1 до 100 и вывести только чётные.
# import random
# list = []
# for i in range(100):
#     r = random.randint(1, 100) 
#     if(r%2==0):
#      list.append(r)
# print(list)

# # Пользователь вводит слово. Определи, является ли оно палиндромом.
# userWord=input("enter some word : ")
# if userWord == userWord[::-1]:
#     print("Это палиндром!")
# else:
#     print("Это не палиндром.")


# # ✅ Задание 3: Найди сумму всех чисел в списке
# Sumalist=[3,76,9,212]
# total=0
# for i in list:
#    total+=i
# print("Сумма всех чисел:", total)

#✅ Task 4: Count the number of vowels in a word

# word = input("Enter a word: ").lower()
# vowels = "aeiouAEIOU"
# count = 0
# for letter in word:
#     if letter in vowels:
#         count += 1
# print("Number of vowels:", count)


# #✅ Task: Create a Person class
# class Person:
#    def __init__(self,name ,age):
#       self.name=name
#       self.age=age
#    def greet(self):
#       print("Hello my name is",self.name,".And I'm",self.age,"years old.")
# p=Person("Aliya",12)
# p.greet()
      

# ✅ Task 2: Class Rectangle
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height
rect = Rectangle(5, 10)
print("Площадь:", rect.get_area())         
print("Периметр:", rect.get_perimeter())     

rect.set_width(7)
rect.set_height(3)
print("Новая площадь:", rect.get_area()) 

class Robot:
    def __init__(self,name,color,weight):
        self.name=name
        self.color=color
        self.weight=weight
    def introduceSelf(self):
        print("Hello my name is",self.name,"color ",self.color,self.weight)
r=Robot("EVA","white",45)
r.introduceSelf()

        
      
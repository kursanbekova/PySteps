import random
random #librery
# 1. Создание списка из случайных чисел от 1 до 100 и вывести только чётные.
import random
list = []
for i in range(100):
    r = random.randint(1, 100) 
    if(r%2==0):
     list.append(r)
print(list)

# Пользователь вводит слово. Определи, является ли оно палиндромом.
userWord=input("enter some word : ")
if userWord == userWord[::-1]:
    print("Это палиндром!")
else:
    print("Это не палиндром.")




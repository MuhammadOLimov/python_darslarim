# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 14:17:25 2024

@author: User
"""
"""
1/5/2024
Dasturlash asoslari
#12-dars: Xatolar bilan ishlash
Muallif:Muhammad Olimov
"""
# SintaxError
# print("Hello World!")
# print("Hello World!")
# print("Assalom alykum!")

# IndentationError
# print("Hello World!")
# print("O'ngacha sanaymiz")
# for i in range(10):
#     print(i+1)

# Run time Error
# TypeError
# son=input("Istalgan son kiriting: ")
# son=int(son)
# print(f"{son} ning kvadrati {son**2} ga teng")

# NameError
# print("Hello World!")
# mevalar=['olma','uzum','nok','anor','anjir']
# for meva in mevalar:
#     print(meva)

#ValueError
# son=float(input("Istalgan son kiriting: "))
# if son>=0:
#     print("Musbat son")
# else:
#     print("Manfiy son")

# IndexError
# mevalar=['olma','anor','uzum']
# print(mevalar[2])

# ZeroDivisionError
# x,y=60,50
# z=250/(x-y)

# Mantiqiy xatolar
# radius=5
# pi=3.14
# aylana_yuzi=pi*radius**2
# print(aylana_yuzi)

# son=float(input("Istalgan son kiriting: "))  
# ildiz=son**(1/2)
# print(f"{son} ning ildizi {ildiz} ga teng")

# mevalar=['olma','uzum','nok','anor','anjir']
# for meva in mevalar:
#     print(meva)
# print("Dastur tugadi")

son = float(input("Juft son kiriting: "))
if son%2==1:
    print("Bu son juft emas.")
else:
    print("Rahmat!")

yosh =int(input("Yoshingiz nechida?"))

if yosh<=4 or yosh>=60:
    narh = 0
elif yosh < 18:
    narh = 10000
else:
    narh = 20000
print(f"Chipta {narh} so'm")

x = float(input("Birinchi sonni kiriting: "))
y = float(input("Ikkinchi sonni kiriting: "))
if x==y:
    print(f"{x}={y}")
elif x<y:
    print(f"{x}<{y}")
else:
    print(f"{x}>{y}")

mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
savat=[]

for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

if savat:
    for mahsulot in savat:
        if mahsulot in mahsulotlar:
            print(f"Do'konimizda {mahsulot} bor")
        else:
            print(f"Do'konimizda {mahsulot} yo'q")
else: 
    print("Savatingiz bo'sh")  

mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)

if mavjud_emas:
  print("Do'konimizda quyidagi mahsulotlar yo'q:")
for mahsulot in mavjud_emas:
  print(mahsulot)
else:
  print("Siz so'ragan barcha mahsulotlar do'konimizda bor")

users = ['alisher1983','aziza','yasina' 'umar']

login = input("Yangi login tanlang:")

if login in users:
    print('Login band, yangi login tanalng!')
else:
    print("Xush kelibsiz!")

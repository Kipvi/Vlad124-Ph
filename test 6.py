#условие if_else
# if если True
is_rainy = True # дождь будет
if is_rainy:
    print('Беру зонт')
    print('Надеть сапоги')
else:
    print('Не беру зонт')
print('Иду гулять') #Печатает Беру зонт, Надеть сапоги, Иду гулять

# else если False
is_rainy = False # дождь будет
if is_rainy:
    print('Беру зонт')
    print('Надеть сапоги')
else:
    print('Не беру зонт')
print('Иду гулять') #Печатает Не беру зонт, Иду гулять

#условие if_безelse
# if если True
is_rainy = True # дождь будет
if is_rainy:
    print('Беру зонт')
print('Иду гулять') #Печатает Беру зонт, Иду гулять

# else если False
is_rainy = False # дождь будет
if is_rainy: #Ничего распечатано не будет
    print('Беру зонт')
print('Иду гулять') #Печатает Иду гулять

#Вложенный условный оператор
is_rainy = True # дождь будет
heavy_rain = False # не сильный дождь
if is_rainy:
    if heavy_rain:
        print('Беру зонт')
    else:
        print("Беру дождевик")
else:
    print('Не беру зонт')
print('Иду гулять') #Печатает беру дождевик, Иду гулять

#Операторы in и is
list_ = [1,2,3,4,5]
print("В списке есть число 7?", 7 in list_) #False

some_var = None
other_var = None
print(some_var is other_var) #True

#Конструкция if-elif-else
#Плохо
if a>10:
    print('a больше 10')
else:
    if a<10:
        print('a меньше 10')
    else:
        print('a равно 10')

#Хорошо
if a>10:
    print('a больше 10')
elif a<10:
    print('a меньше 10')
else:
    print('a равно 10')
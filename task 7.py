#7_1
month = 15
# Создание списков с месяцами для каждого сезона
# spring_months = [3, 4, 5] #Весна
# summer_months = [6, 7, 8] #Лето
# autumn_months = [9, 10, 11] #Осень
# winter_months = [12, 1, 2] #Зима
# Проверка значения переменной month для определения сезона
if month in spring_months:
print("Весна") # Если month находится в списке весенних месяцев, выводим "Весна"
elif month in summer_months:
print("Лето")  # Если month находится в списке летних месяцев, выводим "Лето"
elif month in autumn_months:
print("Осень") # Если month находится в списке осенних месяцев, выводим "Осень"
elif month in winter_months:
print("Зима") # Если month находится в списке зимних месяцев, выводим "Зима"
else:
print("Некорректный номер месяца")# TODO Добавьте блок else c обработкой некорректного номера месяца

month = 14
if month in [3, 4, 5]:
    print("Весна")
elif month in [6, 7, 8]:
    print("Лето")
elif month in [9, 10, 11]:
    print("Осень")
elif month in [12, 1, 2]:
    print("Зима")
else:
    print("Некорректный номер месяца")

#7_3
number = int(input("Введите число:"))
if number in [7, 13, 21]:
    print("Счастливое число!")
elif number in range(1 , 101):
    print("Число в указанном диапазоне")
else:
    print("Не повезло")

#7_2
is_logged_in = True
has_items_in_cart = True
has_shipping_address = False
has_order = True
if is_logged_in and has_items_in_cart and has_shipping_address:
    print("Все критерии для оформления заказа выполнены. Заказ может быть оформлен")
    has_order = True
else:
    print("Не все критерии для оформления заказа выполнены. Пожалуйста, проверьте информацию")
user_first_order = False
min_purchase = 1000
total_purchase = 1500
if has_order and (total_purchase >= min_purchase) or user_first_order:
    print("Вы получаете скидку!")
else:
    print("Скидка не доступна.")
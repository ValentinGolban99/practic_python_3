# Перед изучением функций из программирования Саша решил оживить свои знания о функциях математики. 
# Помогите Саше написать программу, которая будет считать значение функции 
# в каждой точке отрезка с нужным шагом, начиная с конца).
# Напишите программу, которая получает на вход начало и конец отрезка, 
# а также шаг (отрицательный), а затем высчитывает функцию y в каждой точке отрезка 
# и выводит ответ на экран с нужным шагом, начиная с конца.

first_number = int(input("Введите начало отрезка: "))
ending_number = int(input("Введите конец отрезка: "))
step = int(input("Введите шаг: "))

for i in range(ending_number, first_number - 1, step):
    result = (i ** 3) + (2 * i ** 2) - (4 * i) + 1 # Скобки для себя поставил, чтоб понятнее было.
    print (f"В точке {i} функция равна {result}")
    



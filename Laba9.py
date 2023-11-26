from scipy.optimize import minimize

# Задаем данные для двух объектов недвижимости
# Объект в Пресненском районе
price1 = 10_000_000  # Цена в рублях
distance1 = 300  # Расстояние до общественного транспорта в метрах
area1 = 100  # Площадь в квадратных метрах
ecology1 = 8  # Экологическая оценка (по шкале)
accessibility1 = 9  # Доступность культурных и образовательных учреждений

# Объект в Центральном районе
price2 = 12_000_000  # Цена в рублях
distance2 = 200  # Расстояние до общественного транспорта в метрах
area2 = 80  # Площадь в квадратных метрах
ecology2 = 7  # Экологическая оценка (по шкале)
accessibility2 = 8  # Доступность культурных и образовательных учреждений

# Веса для критериев (по вашему усмотрению)
weight_price = 1.0
weight_distance = 0.5
weight_area = 0.5
weight_ecology = 0.2
weight_accessibility = 0.3

# Описываем функцию, которую хотим минимизировать
def func_to_minimize(x, price, distance, area, ecology, accessibility):
    # Формула для определения значения функции минимизации
    total_cost = (weight_price * price) + (weight_distance * distance) + (weight_area * area) + (weight_ecology * ecology) + (weight_accessibility * accessibility)
    return total_cost

# Зададим начальное значение x для первого объекта
x1 = 0

# Минимизируем нашу функцию для первого объекта
result1 = minimize(func_to_minimize, x1, args=(price1, distance1, area1, ecology1, accessibility1))
print("Результат для объекта в ЮВАО:", result1)

# Зададим начальное значение x для второго объекта
x2 = 0

# Минимизируем нашу функцию для второго объекта
result2 = minimize(func_to_minimize, x2, args=(price2, distance2, area2, ecology2, accessibility2))
print("Результат для объекта в ЮЗАО:", result2)
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import circle
import square
import math

print("ТЕСТИРОВАНИЕ ФУНКЦИЙ ДЛЯ КРУГА")

print("\nТест из задания (радиус = 9):")
r = 9
expected_area = 254.46900494077323
expected_perimeter = 56.54866776461627

area_result = circle.area(r)
perimeter_result = circle.perimeter(r)

print(f"Радиус круга: {r}")
print(f"Вычисленная площадь: {area_result}")
print(f"Ожидаемая площадь:   {expected_area}")
print(f"Совпадает? {'ДА' if abs(area_result - expected_area) < 0.0001 else 'НЕТ'}")

print(f"Вычисленная длина окружности: {perimeter_result}")
print(f"Ожидаемая длина окружности:   {expected_perimeter}")
print(f"Совпадает? {'ДА' if abs(perimeter_result - expected_perimeter) < 0.0001 else 'НЕТ'}")

print("\nТест с разными радиусами:")
test_cases = [
    (1, math.pi, 2 * math.pi, "r = 1"),
    (2, 4 * math.pi, 4 * math.pi, "r = 2"),
    (0.5, math.pi * 0.25, math.pi, "r = 0.5"),
    (10, 100 * math.pi, 20 * math.pi, "r = 10"),
]

all_correct = True
for r, exp_area, exp_perim, description in test_cases:
    area_result = circle.area(r)
    perimeter_result = circle.perimeter(r)

    area_ok = abs(area_result - exp_area) < 0.0001
    perim_ok = abs(perimeter_result - exp_perim) < 0.0001

    print(f"{description}:")
    print(f"Площадь: {area_result:.4f} (ожидалось {exp_area:.4f}) - {'OK' if area_ok else 'ERROR'}")
    print(f"Периметр: {perimeter_result:.4f} (ожидалось {exp_perim:.4f}) - {'OK' if perim_ok else 'ERROR'}")

    if not (area_ok and perim_ok):
        all_correct = False

print("ТЕСТИРОВАНИЕ ФУНКЦИЙ ДЛЯ КВАДРАТА")

print("\nТест из задания (сторона = 2):")
a = 2
expected_area = 4
expected_perimeter = 8

area_result = square.area(a)
perimeter_result = square.perimeter(a)

print(f"Сторона квадрата: {a}")
print(f"Вычисленная площадь: {area_result}")
print(f"Ожидаемая площадь:   {expected_area}")
print(f"Совпадает? {'ДА' if area_result == expected_area else 'НЕТ'}")

print(f"Вычисленный периметр: {perimeter_result}")
print(f"Ожидаемый периметр:   {expected_perimeter}")
print(f"Совпадает? {'ДА' if perimeter_result == expected_perimeter else 'НЕТ'}")

print("\n2. Тест с разными сторонами:")
test_cases = [
    (1, 1, 4, "a = 1"),
    (3, 9, 12, "a = 3"),
    (5, 25, 20, "a = 5"),
    (2.5, 6.25, 10, "a = 2.5"),
    (0.5, 0.25, 2, "a = 0.5"),
]

all_correct_square = True
for a, exp_area, exp_perim, description in test_cases:
    area_result = square.area(a)
    perimeter_result = square.perimeter(a)

    area_ok = abs(area_result - exp_area) < 0.0001
    perim_ok = abs(perimeter_result - exp_perim) < 0.0001

    print(f"{description}:")
    print(f"Площадь: {area_result} (ожидалось {exp_area}) - {'OK' if area_ok else 'ERROR'}")
    print(f"Периметр: {perimeter_result} (ожидалось {exp_perim}) - {'OK' if perim_ok else 'ERROR'}")

    if not (area_ok and perim_ok):
        all_correct_square = False


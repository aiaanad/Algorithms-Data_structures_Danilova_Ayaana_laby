# Задание №2 по варианту:  Анти-quick sort
Студент(ка) ИТМО, Данилова Айаана Васильевна

## Вариант 6

## Задание 
Хотя QuickSort является очень быстрой сортировкой в среднем, существуют тесты, на которых она работает очень долго. Оценивать время работы алгоритма
будем числом сравнений с элементами массива (то есть, суммарным числом сравнений в первом и втором while). Требуется написать программу, генерирующую
тест, на котором быстрая сортировка сделает наибольшее число таких сравнений.

• Формат входного файла (input.txt). 

В первой строке находится единственное число n (1 ≤ n ≤ 10^6).

• Формат выходного файла (output.txt). 

Вывести перестановку чисел от 1 до n, на которой быстрая сортировка выполнит максимальное число сравнений.
Если таких перестановок несколько, вывести любую из них.

## Input / Output 

| Input | Output |
|-------|--------|
| 3     | 1 3 2  |

## Ограничения по времени и памяти

- Ограничение по времени. 2сек.
- Ограничение по памяти. 256 мб.


## Запуск проекта
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/aiaanad/asd.git
   ```
2. Перейдите в папку с проектом:
   ```bash
   cd folder/where/cloned/asd
   ```
3. Запустите программу:
   ```bash
   python -m lab_3.task2.src.task2
   ```

4. Запуск тестов:
   ```bash
   python -m unittest lab_3.task2.tests.test_task2
   ```


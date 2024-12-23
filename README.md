# Практика по Алгоритмам и Cтруктурам Данных ИТМО 

**Студентка ИТМО,  Данилова Айаана Васильевна  465714**  
## Вариант 6

### Навигация

-  [Лабораторная 0 - Вводная лабораторная ](lab_0)
-  [Лабораторная 1 - Сортировка вставками, выбором, пузырьковая ](lab_1)
-  [Лабораторная 2 - Сортировка слиянием. Метод декомпозиции ](lab_2)
-  [Лабораторная 3 - Быстрая сортировка, сортировки за линейное время ](lab_3)
-  [Лабораторная 4 - Стек, очередь, связанный список ](lab_4)
-  [Лабораторная 5 - Деревья. Пирамида, пирамидальная сортировка. Очередь с приоритетами ](lab_5)
-  [Лабораторная 6 - Хеширование. Хеш-таблицы ](lab_6)
-  [Лабораторная 7 - Динамическое программирование №1 ](lab_7)



### Описание 
   

### Цели и задачи

- Изучить основные команды Git
- Научиться создавать и управлять репозиториями
- Освоить работу с ветками и слияниями
- Понять основы работы с удаленными репозиториями
- Научиться правильно оформлять репозиторий
- Упражняться в решении задач на алгоритмы сортировки, ... и т.д.

### Технологии и инструменты

- **Git** — система контроля версий
- **GitHub** — платформа для хостинга репозиториев
- **Markdown** — язык разметки для оформления документации
- **PyCharm** - IDE для языка программирования Python

### Инструкция по запуску

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/aiaanad/asd.git
   ```
2. Перейдите в папку с проектом:
   ```bash
   cd asd/lab1
   ```
3. **Запуску всех лабораторных**
    ```bash
   for f in {1..7}; do cd lab_"$f" && for l in task*/src/*.py; do python "$l" ; done; cd .. ; done


4. **Запуску всех тестов**
    ```bash
        python -m unittest discover -v
   
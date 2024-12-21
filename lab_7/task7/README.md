# Задание №7 по варианту: Наибольшая возрастающая подпоследовательность

Студент(ка) ИТМО, Данилова Айаана Васильевна

## Вариант 6

## Задание 
Многие операционные системы используют шаблоны для ссылки на группы
объектов: файлов, пользователей, и т. д. Ваша задача – реализовать простейший
алгоритм проверки шаблонов для имен файлов.

В этой задаче алфавит состоит из маленьких букв английского алфавита и точки («.»). Шаблоны могут содержать произвольные символы алфавита, а также два
специальных символа: «?» и «*». Знак вопроса («?») соответствует ровно одному
произвольному символу. Звездочка «+» соответствует подстроке произвольной
длины (возможно, нулевой). Символы алфавита, встречающиеся в шаблоне, отображаются на ровно один такой же символ в проверяемой строчке. Строка считается
подходящей под шаблон, если символы шаблона можно последовательно отобразить на символы строки таким образом, как описано выше. Например, строчки
«ab», «aab» и «beda.» подходят под шаблон «*a?», а строчки «bebe», «а» и «ba»
–нет.

• Формат ввода / входного файла (input.txt). 

Первая строка входного файла
определяет шаблон . Вторая строка S состоит только из символов алфавита.
Ее необходимо проверить на соответствие шаблону. Длины обеих строк не
превосходят 10 000. Строки могут быть пустыми – будьте внимательны!

• Формат вывода / выходного файла (output.txt). 

Если данная строка подходит под шаблон, выведите YES. Иначе выведите NO.

## Input / Output 

| Input              | Output |
|--------------------|--------|
| k?t*n <br/> kitten | YES    |
| k?t?n <br/> kitten | NO     |

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
   python -m lab_7.task7.src.task7
   ```

4. Запуск тестов:
   ```bash
   python -m unittest lab_7.task7.tests.test_task7
   ```
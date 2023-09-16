# bioinf2022

1_homework_semester_2
(Python) написать программу, которая читает файл в формате fasta и возвращает список последовательностей

2_homework_semester_2
(Python) написать программу, которая читает файл в формате fasta с последовательностями ДНК, находит в них все неперекрывающиеся рамки считывания и записывает соответствующие им белки в отдельные файлы в заданной директории

3_homework_semester_2
(Python) написать скрипт на Python, который представляет пару вырожденных праймеров в виде регулярного выражения и ищет ампликоны в референсном геноме. Геном в формате FASTA

4_homework_semester_2
(bash)  объединить файлы из задачи 2 в один файл

5_homework_semester_2
5. (bash) для полученного в 4 файлы преобразовать последовательности, чтобы каждая последовательность записывалась в одну строчку или обратно - по 60 символов на строку.

6_homework_semester_2
(bash) для полученного в 4 файла - для каждой последовательности вывести статистику встречаемости каждой АК (в штуках)

1_homework 

Написать программу, которая запрашивает число и возвращает все его простые делители
Последовательность Фибоначчи – это последовательность чисел, в которых каждое число является суммой двух предыдущих членов последовательности. Два первых числа задают последовательность, в частном случае это (1, 1). Программа запрашивает число и возвращает первые 15 членов последовательности Фибоначчи, заданной двумя самыми большими простыми числами, меньшими или равными заданному.
Написать программу, которая запрашивает число, а затем выводит квадрат из *, где длина стороны равна данному числу.
Написать программу, которая запрашивает два числа, а затем выводит прямоугольник из *, где длины сторон равны данным числам.
Написать программу, которая запрашивает два числа и выводит на экран прямоугольник, в котором змейкой по вертикали записаны числа, начиная с 1. 

2_homework

Написать программу: пользователь вводит числа, разделенные новой строкой. Окончание ввода – пустая строка. Программа выводит числа парами: четное-нечетное. Если каких-то чисел больше, то лишние выводятся в конце.
Пара чисел задают отрезок на прямой. Пользователь вводит числа, которые разбиваются на пары. Прекращение ввода пустой строкой. Если два введенных отрезка пересекаются, то они объединяются в один. Программа выводит итоговый набор отрезков.
Пара чисел задают отрезок на прямой. Пользователь вводит числа, которые разбиваются на пары. Прекращение ввода пустой строкой. Изначально для каждого отрезка покрытие 1. Если два введенных отрезка пересекаются, то их пересечение – это новый отрезок с суммарным покрытием двух исходных. В итоге программы выводит отрезок с максимальным покрытием.
Координаты задаются парой чисел. Пользователь вводит числа, которые разбиваются на пары. Прекращение ввода пустой строкой. Точки группируются с точностью до 5 градусов. Выводится точка, около которой было указано больше всего координат, и количество таких введенных точек.

3_homework

Используя наборы символов из пакета string написать функцию, которая получает на вход строку и возвращает строку, в которой все буквы латинского алфавита из исходной строки преобразованы в заглавные символы. Использовать функции стандартной библиотеки upper() и find() нельзя.

Добавить к предыдущему заданию функцию с преобразованием всех символов в прописные и функцию с отражением (все заглавные становятся прописными и наоборот), минимально дублируя код. Использовать функции стандартной библиотеки lower() и find() нельзя.

Написать программу на Python3, которая сначала запрашивает положительное число-основание системы счисления, затем два числа в системе счисления с этим основанием, и потом четвертое число-основание системы счисления, в которой надо вывести результат. В ходе выполнения программа возвращает результат сложения двух чисел в требуемой системе счисления. Нельзя использовать для перевода функцию int().

4_homework

Крестики-нолики

5_homework

Написать программу, которая позволяет двум людям, вводя поочередно ходы, играть в шашки до победы одного из них. Программа должна действовать в соответствии с правилами игры.

6_homework

Шахматы

7_homework

Создать классы, описывающие биологические последовательности ДНК, РНК, белков, наследующие от общего класса «последовательность». Каждый класс должен иметь свойство алфавит, уметь возвращать название последовательности, саму последовательность, ее длину, статистику по использованию в ней символов, ее молекулярную массу, а также специфичные функции (возврат комплементарной последовательности, транскрипция ДНК --> РНК, трансляция РНК --> белок)

8_homework

1. Написать функцию, которая принимает как аргумент алфавит последовательности, а возвращает функцию получения статистики встречаемости символов в последовательности
2. Добавить к классу последовательностей из прошлого домашнего задания метод, который принимает в качестве аргумента функцию, задающую правила замены символов, и который заменяет по этому правилу символы в последовательности
3. Модифицировать метод из предыдущей задачи так, что функция с правилом замены принимает не только заменяемый символ, но и предыдущий

9_homework

1. Написать класс, описывающий бинарные деревья поиска
2. Написать функцию, преобразующую бинарное дерево в красно-черное дерево (алгоритмы вставок и удалений для него реализовывать не обязательно)

10_homework

Написать программу, которая принимает в качестве параметра размер k-mer (до 11нт), на вход последовательность нуклеотидов, на выходе возвращает таблицу, где строке соответствует k-mer , для него дано количество вхождений, позиция первого вхождения, последнего, и среднее по всем позициям. Из встроенных структур данных можно использовать только 










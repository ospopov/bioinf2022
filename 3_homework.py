# Используя наборы символов из пакета string написать функцию, которая получает на вход строку и возвращает строку, в которой все буквы латинского алфавита из исходной строки преобразованы в заглавные символы. Использовать функции стандартной библиотеки upper() и find() нельзя.

import string


def capitals(input_l, letters_in=string.ascii_uppercase, letters_out=string.ascii_lowercase):
    new_l = str()
    for i in input_l:
        if i in letters_in:
            new_l += i
        else:
            for j in range(len(letters_out) - 1):
                if i == letters_out[j]:
                    new_l += letters_in[j]
    return new_l


capitals(input('Enter a string '))

# Добавить к предыдущему заданию функцию с преобразованием всех символов в прописные и функцию с отражением (все заглавные становятся прописными и наоборот), минимально дублируя код. Использовать функции стандартной библиотеки lower() и find() нельзя.

capitals(input_l=input('Enter a string '), letters_in=string.ascii_lowercase, letters_out=string.ascii_uppercase)

# Написать программу на Python3, которая сначала запрашивает положительное число-основание системы счисления, затем два числа в системе счисления с этим основанием, и потом четвертое число-основание системы счисления, в которой надо вывести результат. В ходе выполнения программа возвращает результат сложения двух чисел в требуемой системе счисления. Нельзя использовать для перевода функцию int().

system_in = int(input('Введите основание системы счисления  '))
num_1 = input('Введите первое число  ')
num_2 = input('Введите второе число  ')
system_out = int(input('Введите основание системы счисления для вывода '))


def system_trans_10(transfer, system):
    transfer_end = int()
    for i in range(len(transfer)):
        transfer_end += int(transfer[i]) * (system ** (len(transfer) - 1 - i))
    return transfer_end


def system_trans_end(transfer, system):
    while_transfer = int(transfer)
    transfer_end = str()
    while while_transfer // system != 0:
        transfer_end = str(while_transfer % system) + transfer_end
        while_transfer = while_transfer // system
    if while_transfer != 0:
        transfer_end = str(while_transfer) + transfer_end
    return int(transfer_end)


system_trans_end(transfer=system_trans_10(num_1, system_in) + system_trans_10(num_2, system_in), system=system_out)

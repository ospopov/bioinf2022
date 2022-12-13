# Написать программу: пользователь вводит числа, разделенные новой строкой. Окончание ввода – пустая строка. Программа выводит числа парами: четное-нечетное. Если каких-то чисел больше, то лишние выводятся в конце.

inp_num = []

while True:
    temp = input('Enter a number ')
    if temp == '':
        break
    else:
        temp = int(temp)
        inp_num.append(temp)

inp_num_even = []
inp_num_odd = []

for i in range(0, len(inp_num)):
    if inp_num[i] % 2 == 0:
        inp_num_even.append(inp_num[i])
    else:
        inp_num_odd.append(inp_num[i])

for i in range(0, max([len(inp_num_even), len(inp_num_odd)])):
    if i >= len(inp_num_even):
        print(inp_num_odd[i])
    elif i >= len(inp_num_odd):
        print(inp_num_even[i])
    else:
        print(inp_num_even[i], inp_num_odd[i])

# Пара чисел задают отрезок на прямой. Пользователь вводит числа, которые разбиваются на пары. Прекращение ввода пустой строкой. Если два введенных отрезка пересекаются, то они объединяются в один. Программа выводит итоговый набор отрезков.


def for_sort(x):
    return x[0]

inp_num = []

while True:
    temp_1 = input('Enter a number 1 ')
    temp_2 = input('Enter a number 2 ')
    if temp_1 == '' or temp_2 == '':
        break
    else:
        inp_num.append([min(int(temp_1), int(temp_2)), max(int(temp_1), int(temp_2))])
        
inp_num.sort(key=for_sort)


def unite(x_list=inp_num):
    for i in range(0, len(x_list) - 1):
        if x_list[i][1] >= x_list[i + 1][0]:
            x_list[i] = [x_list[i][0], x_list[i + 1][1]]
            x_list.remove(x_list[i + 1])
            new_x_list = x_list
            unite(x_list=new_x_list)
    return x_list


unite()

# максимальный отрезок

inp_num = unite()

j = 0
j_max = inp_num[0][1] - inp_num[0][0]
for i in range(0, len(inp_num)):
    if inp_num[i][1] - inp_num[i][0] > j_max:
        j_max = inp_num[i][1] - inp_num[i][0]
        j = i

print(inp_num[j])


# Координаты задаются парой чисел. Пользователь вводит числа, которые разбиваются на пары. Прекращение ввода пустой строкой. Точки группируются с точностью до 5 градусов. Выводится точка, около которой было указано больше всего координат, и количество таких введенных точек.

inp_num = []

while True:
    temp_1 = input('Enter a number 1 ')
    temp_2 = input('Enter a number 2 ')
    if temp_1 == '' or temp_2 == '':
        break
    else:
        inp_num.append([float(temp_1), float(temp_2)])

inp_num_match = [0] * len(inp_num)

for i in range(0, len(inp_num)):
    for j in range(i+1, len(inp_num)):
        if abs(inp_num[i][0] - inp_num[j][0]) <= 5 and abs(inp_num[i][1] - inp_num[j][1]) < 5:
            inp_num_match[i] += 1
            inp_num_match[j] += 1

print(max(inp_num_match),
      inp_num[inp_num_match.index(max(inp_num_match))])



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

inp_num = []


def for_sort(x):
    return x[0]


while True:
    temp_1 = input('Enter a number 1 ')
    temp_2 = input('Enter a number 2 ')
    if temp_1 == '' or temp_2 == '':
        break
    else:
        inp_num.append([min(int(temp_1), int(temp_2)), max(int(temp_1), int(temp_2))])

inp_num = [[3, 4], [5, 7], [8, 9], [5, 6], [3, 4], [1, 2], [5, 9], [3, 4], [2, 3], [4, 5], [6, 7]]

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

while True:
    temp_1 = input('Enter a number 1 ')
    temp_2 = input('Enter a number 2 ')
    if temp_1 == '' or temp_2 == '':
        break
    else:
        inp_num.append([float(temp_1), float(temp_2)])

inp_num = [[55.813949, 37.663833], [54.203344, 37.850854], [52.989674, 49.913877], [56.148962, 44.239890], [54.780190, 55.821042], [58.134365, 56.287397], [57.133909, 65.769952], [48.713038, 44.550793], [55.315703, 61.520937], [53.691432, 55.608373]]
inp_num_match = [0] * len(inp_num)


for i in range(0, len(inp_num)):
    for j in range(i+1, len(inp_num)):
        if abs(inp_num[i][0] - inp_num[j][0]) <= 5 and abs(inp_num[i][1] - inp_num[j][1]) < 5:
            inp_num_match[i] += 1
            inp_num_match[j] += 1

print(max(inp_num_match),
      inp_num[inp_num_match.index(max(inp_num_match))])



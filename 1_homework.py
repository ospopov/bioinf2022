# простые делители

int_num = int(input("enter a number "))
for i in range(int_num - 1, 1, -1):
    prime = 0
    if int_num % i == 0:
        for j in range(i - 1, 1, -1):
            if i % j == 0:
                prime = prime + 1
        if prime == 0:
            print(i, end=" ")


# Фибоначчи

def max_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return max_prime(n - 1)
    return n


def fibonacci(n1, n2, length_Fibonacci=15):
    fib = [n1, n2]
    for i in range(3, length_Fibonacci):
        fib.append(fib[i - 2] + fib[i - 3])
    return fib


n = max_prime(int(input("enter the number ")))
if n == 1:
    m = 1
else:
    m = max_prime(n-1)
fibonacci(n1=m, n2=n, length_Fibonacci=15)

# Square

square_length = int(input("enter the number "))


def square_plot(square_length):
    for i in range(1, square_length):
        print(" * " * square_length)


square_plot(square_length)

# rectangle

rectangle_1 = int(input("enter a number (1)"))
rectangle_2 = int(input("enter a number (2)"))


def rectangle_plot(rectangle_1, rectangle_2):
    for i in range(1, rectangle_1_):
        print(" * " * rectangle_2)


rectangle_plot(rectangle_1_=rectangle_1, rectangle_2_=rectangle_2)

# n_rectangle

rectangle_1 = int(input("Введите длину: "))
rectangle_2 = int(input("Введите высоту: "))

def rectangle_n(rectangle_1_, rectangle_2_):
    for i in range(1, rectangle_2_+1):
        string_j = [i]
        for j in range(2, rectangle_1_+1):
            string_j.append(string_j[j - 2] + rectangle_2_)
        print(string_j)

rectangle_n(rectangle_1, rectangle_2)

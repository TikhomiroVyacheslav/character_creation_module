from math import sqrt


def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Проверяет число на положительность."""
    if your_number <= 0:
        return False
    return True


if __name__ == '__main__':
    message = ('Добро пожаловать в самую лучшую программу для вычисления '
               'квадратного корня из заданного числа')
    print(message)
    your_number = 25.5
    if calc(your_number) is True:
        print(f'Мы вычислили квадратный корень из введённого вами числа. '
              f'Это будет: {calculate_square_root(your_number)}')

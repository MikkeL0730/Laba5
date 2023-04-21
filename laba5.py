def F_rec(n):
    if n == 1:
        return 1
    else:
        return F_rec(n-1) * (2*n-1)
def F_it(n):
    f_n = [1]*(n+1)
    for i in range(3, n+1):
        f_n[i] = f_n[i-2] * (i-1)
    return f_n[n]

import time
import matplotlib.pyplot as plt

recursive_times = []
iterative_times = []
try:
    print("Введите натуральное число n:")
    n = int(input())
    while n < 1:
        n = int(input("\nВы указали не натуральное число. Введите натуральное число n:"))

    print("Введите шаг изменения s (натуральное число):")

    s = int(input())
    while s < 1:
        s = int(input("\nВы указали не натуральное число. Введите шаг изменения s (натуральное число):"))


    start_time = time.time()
    result = F_it(n)
    print("\nРезультат итерации -", result, "\nВремя работы -", time.time() - start_time)
    start_time = time.time()
    result = F_rec(n)
    print("\nРезультат рекурсии -", result, "\nВремя работы -", time.time() - start_time)


    rec_times = []
    rec_values = []
    it_times = []
    it_values = []
    n_values = list(range(1, n+1, s))

    for n in n_values:
        start_time = time.time()
        rec_values.append(F_rec(n))
        end_time = time.time()
        result_time = end_time - start_time
        rec_times.append(result_time)
        print(start_time, end_time)

        start_time = time.time()
        it_values.append(F_it(n))
        end_time = time.time() - start_time
        it_times.append(end_time)

    t_data = []
    for i, n in enumerate(n_values):
        t_data.append([n, rec_times[i],rec_values[i],it_times[i],it_values[i]])
    print('{:<5}|{:<20}|{:<20}|{:<20}|{:<20}'.format('n', 'Время рекурсии', 'Значение рекурсии', 'Время итерации', 'Значение итерации'))
    for data in t_data:
        print('{:<5}|{:<20}|{:<20}|{:<20}|{:<20}'.format(data[0], data[1], data[2], data[3], data[4]))
    #'''
    plt.plot(n_values, rec_times, label="Recursive")
    plt.plot(n_values, it_times, label="Iterative")
    plt.legend()
    plt.show()
    #'''

    print(time.time())

except ValueError:
    print("\nВы ввели не натуральное число. Перезапустите программу.")

except RecursionError:
    print(
        "\nВы ввели слишком большое число. Перезапустите программу.")
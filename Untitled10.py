#!/usr/bin/env python
# coding: utf-8

# In[1]:


import hashlib
import time

def generate_random_numbers1(num, seed=None):
    """
    Генерирует случайные числа с использованием хэш-функции MD5.

    :param num: количество случайных чисел для генерации
    :param seed: начальное значение генератора (по умолчанию - текущее время в миллисекундах)
    :return: список сгенерированных случайных чисел
    """
    if not seed:
        seed = int(time.time() * 1000)  # задаем начальное значение генератора равное текущему времени в миллисекундах
    random_numbers = []
    for i in range(num):
        seed = int(hashlib.md5(str(seed).encode('utf-8')).hexdigest(), 16)  # применяем хэш-функцию MD5 к seed
        random_numbers.append(seed)
    return random_numbers


def generate_random_numbers2(num, seed=None, mask=0xAAAAAAAA):
    """
    Генерирует случайные числа с использованием операции XOR-шифрования.

    :param num: количество случайных чисел для генерации
    :param seed: начальное значение генератора (по умолчанию - текущее время в миллисекундах)
    :param mask: маска для XOR-шифрования (по умолчанию - 0xAAAAAAAA)
    :return: список сгенерированных случайных чисел
    """
    if not seed:
        seed = int(time.time() * 1000)  # задаем начальное значение генератора равное текущему времени в миллисекундах
    random_numbers = []
    for i in range(num):
        seed ^= mask  # применяем XOR-шифрование к seed
        random_numbers.append(seed)
    return random_numbers


def calc_stats(data):
    """
    Вычисляет статистические показатели для списка данных.

    :param data: список данных
    """
    n = len(data)
    mean = sum(data) / n
    variance = sum((x - mean) ** 2 for x in data) / (n - 1)
    stdev = math.sqrt(variance)
    cv = stdev / mean * 100
    print("Среднее значение: ", mean)
    print("Стандартное отклонение: ", stdev)
    print("Коэффициент вариации: ", cv)


def test_uniformity(data, alpha=0.05):
    """
    Проверяет равномерность распределения выборки на основе критерия Хи-квадрат.

    :param data: список наблюдаемых частот
    :param alpha: уровень значимости (по умолчанию, 0.05)
    :return: True, если выборка однородна; False, если выборка неоднородна
    """
    chi2_stat, p_val = chi_square_test(data)
    if p_val < alpha:
        return False
    else:
        return True


def chi_square_test(data):
    """
    Вычисляет критерий Хи-квадрат и соответствующее P-значение для заданной выборки и оценки ожидаемых частот на основе наблюдаемых.

    :param data: список наблюдаемых частот
    :return: кортеж из двух элементов: статистику критерия Хи-квадрат и P-значение
    """
    n = sum(data)
    k = len(data)
    f_exp = [n / k] * k
    chi2_stat, p_val = chisquare(data, f_exp=f_exp)
    return chi2_stat, p_val


# Генерируем случайные числа и выполняем статистические тесты

random_numbers11 = generate_random_numbers1(100)
random_numbers12 = generate_random_numbers1(200)
random_numbers13 = generate_random_numbers1(300)
random_numbers14 = generate_random_numbers1(1000)
random_numbers15 = generate_random_numbers1(10000)

random_numbers21 = generate_random_numbers2(100)
random_numbers22 = generate_random_numbers2(200)
random_numbers23 = generate_random_numbers2(300)
random_numbers24 = generate_random_numbers2(1000)
random_numbers25 = generate_random_numbers2(10000)

sample = [random.randint(0, 5) for _ in range(10000000)]
calc_stats(sample)
calc_stats(random_numbers12)
calc_stats(random_numbers13)
calc_stats(random_numbers14)

sample = [random.randint(0, 5) for _ in range(10000000)]
if test_uniformity(sample):
    print("Выборка однородна")
else:
    print("Выборка неоднородна")

# Выполняем замеры времени выполнения

start_time = time.perf_counter()
generate_random_numbers1(1000)
end_time = time.perf_counter()
print("Время выполнения generate_random_numbers1 для 1000 элементов: ", end_time - start_time)

start_time = time.perf_counter()
generate_random_numbers1(10000)
end_time = time.perf_counter()
print("Время выполнения generate_random_numbers1 для 10000 элементов: ", end_time - start_time)

start_time = time.perf_counter()
generate_random_numbers1(100000)
end_time = time.perf_counter()
print("Время выполнения generate_random_numbers1 для 100000 элементов: ", end_time - start_time)

start_time = time.perf_counter()
generate_random_numbers1(1000000)
end_time = time.perf_counter()
print("Время выполнения generate_random_numbers1 для 1000000 элементов: ", end_time - start_time)

start_time = time.perf_counter()
generate_random_numbers2(1000)
end_time = time.perf_counter()
print("Время выполнения generate_random_numbers2 для 1000 элементов: ", end_time - start_time)

start_time = time.perf_counter()
generate_random_numbers2(10000)
end_time = time.perf_counter()
print("Время выполнения generate_random_numbers2 для 10000 элементов: ", end_time - start_time)

start_time = time.perf_counter()
generate_random_numbers2(100000)
end_time = time.perf_counter()
print("Время выполнения generate_random_numbers2 для 100000 элементов: ", end_time - start_time)

start_time = time.perf_counter()
generate_random_numbers2(1000000)
end_time = time.perf_counter()
print("Время выполнения generate_random_numbers2 для 1000000 элементов: ", end_time - start_time)


# In[ ]:





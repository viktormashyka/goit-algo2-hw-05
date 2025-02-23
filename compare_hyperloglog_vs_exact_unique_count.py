from datasketch import HyperLogLog
from time import time
import json

# Завантаження даних з файлу
with open('/Users/viktormashyka/Documents/GitHub/goit-algo2-hw-05/lms-stage-access.log', 'r') as file:
    logs = [json.loads(line) for line in file]

def hyperloglog_unique_count(logs, key='remote_addr'):
    # Ініціалізація HyperLogLog
    hll = HyperLogLog(p=14)

    for log in logs:
        if key in log:
            hll.update(log[key].encode('utf-8'))

    return hll.count()

def exact_unique_count(logs, key='remote_addr'):
    unique_ips = set()

    for log in logs:
        if key in log:
            unique_ips.add(log[key])

    return len(unique_ips)

if __name__ == "__main__":
    # Оцінка кількості унікальних елементів за допомогою HyperLogLog
    start_time = time()
    unique_count_hll = hyperloglog_unique_count(logs)
    hll_time = time() - start_time

    # Точний підрахунок унікальних елементів за допомогою set
    start_time = time()
    unique_count_exact = exact_unique_count(logs)
    exact_time = time() - start_time

    # Виведення результатів
    print(f"{'Результати порівняння:':<30}")
    print(f"{'':<30}{'Точний підрахунок':<20}{'HyperLogLog':<20}")
    print(f"{'Унікальні елементи':<30}{unique_count_exact:<20}{unique_count_hll:<20}")
    print(f"{'Час виконання (сек.)':<30}{exact_time:<20.2f}{hll_time:<20.2f}")

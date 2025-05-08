import time
# import mmh3

from hyperloglog import HyperLogLog
import json


# 1. Завантажуння набору даних
def load_ip_addresses(file_path):
    ip_list = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            try:
                log = json.loads(line)
                ip = log.get("remote_addr")
                if ip:
                    ip_list.append(ip)
            except json.JSONDecodeError:
                continue
    print(f"Усього IP-адрес: {len(ip_list)}")
    return ip_list


# 2. Точний підрахунок
def count_unique_ips_exact(ip_list):
    return len(set(ip_list))

# 3. Наближений підрахунок
def count_unique_ips_approx(ip_list):
    hll = HyperLogLog(14)  # 1% похибка
    for ip in ip_list:
        hll.add(ip)
    return hll.count()
    
# 4. Порівняння часу виконання
if __name__ == "__main__":
    file_path = "lms-stage-access.log"
    ip_list = load_ip_addresses(file_path)

    # Точний метод
    start = time.time()
    exact_count = count_unique_ips_exact(ip_list)
    exact_time = time.time() - start

    # Наближений метод
    start = time.time()
    approx_count = count_unique_ips_approx(ip_list)
    approx_time = time.time() - start

    print("\nРезультати порівняння:")
    print(f"                       Точний підрахунок      HyperLogLog")
    print(f"Унікальні елементи:        {exact_count}                   {approx_count:.4f}")
    print(f"Час виконання:             {exact_time:.6f}             {approx_time:.6f} ")
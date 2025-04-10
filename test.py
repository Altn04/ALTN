import time
from threading import Thread # необойтись надо же как то сказать, что параллельно

def prepare_vegetables():
    print("Режем овощи для супа (10 мин)...")
    time.sleep(10)
    print("Овощи для супа готовы!")

def cook_soup():
    prepare_vegetables()
    print("Варим суп (30 мин)...")
    time.sleep(30)
    print("Суп готов!")
    make_tea()


def make_mashed_potatoes():
    print("Чистим картошку (5 мин)...")
    time.sleep(5)
    print("Варим картофель (15 мин)...")
    time.sleep(15)
    print("Пюре готово!")
    make_salad()
    

def make_salad():
    print("Режем овощи для салата (10 мин)...")
    time.sleep(10)
    print("Заправляем салат (2 мин)...")
    time.sleep(2)
    print("Салат готов!")

def make_tea():
    print("Кипятим воду (5 мин)...")
    time.sleep(5)
    print("Завариваем чай (2 мин)...")
    time.sleep(2)
    print("Чай готов!")

# Запуск всех  задач в параллельных потоках
if __name__ == "__main__":
    start_time = time.time()

    # Параллельные процессы
    Thread(target=cook_soup).start()       # Суп (10 + 30 мин)
    Thread(target=make_mashed_potatoes).start()  # Пюре (5 + 15 мин)
    Thread(target=make_salad).start()      # Салат (10 + 2 мин)
    Thread(target=make_tea).start()        # Чай (5 + 2 мин)

    # Ждём завершения всех процессов
    time.sleep(42)  # Максимальное время (суп)
    print(f"Обед готов! Время выполнения: {time.time() - start_time:.0f} минут")
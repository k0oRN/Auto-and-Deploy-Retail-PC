import configparser
import os
import random
from datetime import datetime, timedelta
import ast
import pandas as pd

print("Скрипт запущен успешно. Текущая дата:", datetime.today().strftime("%Y-%m-%d"), "День недели:", datetime.today().weekday())

dirname = os.path.dirname(__file__)

config = configparser.ConfigParser()
config.read(os.path.join(dirname, "config.ini"), encoding="utf-8")

DATA_FOLDER = config["Files"]["DATA_FOLDER"]
NUM_SHOPS = int(config["Shops"]["NUM_SHOPS"])
CATEGORIES = ast.literal_eval(config["Shops"]["CATEGORIES"])
ITEMS = ast.literal_eval(config["Shops"]["ITEMS"])

today = datetime.today()
if today.weekday() == 6:  # 6 - воскресенье
    print("Сегодня воскресенье, генерация данных пропущена.")
    exit()

yesterday = today - timedelta(days=1)
os.makedirs(DATA_FOLDER, exist_ok=True)

for shop_num in range(1, NUM_SHOPS + 1):
    num_cashes = random.randint(2, 5)  # Случайное кол-во касс в магазине
    for cash_num in range(1, num_cashes + 1):
        data = []
        num_checks = random.randint(5, 20)  # Чеки на кассу
        for check in range(num_checks):
            doc_id = f"CHK-{shop_num:02d}-{cash_num:02d}-{random.randint(10000, 99999)}"
            num_items = random.randint(1, 8)  # Позиции в чеке
            for _ in range(num_items):
                item = random.choice(ITEMS)
                category = random.choice(CATEGORIES)
                amount = random.randint(1, 5)  # 
                price = random.randint(1000, 100000)
                discount = round(random.uniform(0, 0.15) * price, 2)  # 0-15%
                data.append({
                    "doc_id": doc_id,
                    "item": item,
                    "category": category,
                    "amount": amount,
                    "price": price,
                    "discount": discount
                })
        
        df = pd.DataFrame(data)
        filename = f"{shop_num}_{cash_num}.csv"
        df.to_csv(os.path.join(DATA_FOLDER, filename), index=False, encoding="utf-8")
        print(f"Сгенерирован файл: {filename}")
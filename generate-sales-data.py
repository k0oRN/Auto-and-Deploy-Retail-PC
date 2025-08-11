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

# Создаём mapping: категория -> список подходящих товаров
category_to_items = {
    "graphics cards": [
        "NVIDIA GeForce RTX 4090", "AMD Radeon RX 7900 XTX",
        "NVIDIA GeForce RTX 3080 Ti", "AMD Radeon RX 6800 XT"
    ],
    "processors": [
        "Intel Core i9-13900K", "AMD Ryzen 9 7950X", "AMD Ryzen 5 7500F",
        "Intel Core i7-13700K", "AMD Ryzen 7 7700X", "Intel Core i5-12400F"
    ],
    "motherboards": [
        "ASUS ROG Strix Z790-E", "MSI MPG B650 Carbon",
        "ASRock B550 Phantom Gaming", "Biostar X670E Valkyrie",
        "Gigabyte Aorus Z790 Master", "MSI MAG Z790 Tomahawk"
    ],
    "RAM": [
        "Corsair Vengeance 32GB DDR5", "G.Skill Trident Z5 64GB DDR4",
        "Kingston Fury Beast 16GB DDR4", "Crucial Ballistix 32GB DDR4",
        "HyperX Predator 64GB DDR5", "Patriot Viper Steel 32GB DDR4"
    ],
    "coolers": [
        "Noctua NH-D15 CPU Cooler", "be quiet! Dark Rock Pro 4",
        "Arctic Liquid Freezer II 360", "Cooler Master Hyper 212",
        "Deepcool AK620 CPU Cooler", "EK AIO Elite 360 D-RGB Cooler"
    ],
    "cases": [
        "Fractal Design Meshify 2", "Lian Li Lancool III",
        "NZXT H510 Case", "Corsair 4000D Airflow Case",
        "Phanteks Eclipse P400A", "Silverstone RL06 Case"
    ],
    "SSDs": [
        "Samsung 990 PRO 1TB SSD", "Western Digital Black SN850X 2TB",
        "Crucial P5 Plus 500GB SSD", "Seagate FireCuda 520 1TB"
    ],
    "power supplies": [
        "Corsair RM850x PSU", "EVGA SuperNOVA 1000 G+",
        "Seasonic Focus GX-750 PSU", "Thermaltake Toughpower GF1 850W"
    ]
}

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
                category = random.choice(CATEGORIES)  # Сначала выбираем категорию
                item = random.choice(category_to_items[category])  # Затем товар только из этой категории
                amount = random.randint(1, 5)
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

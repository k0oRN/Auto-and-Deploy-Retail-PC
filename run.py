import configparser
import os
import re
import pandas as pd
from database import PGDatabase

dirname = os.path.dirname(__file__)

config = configparser.ConfigParser()
config.read(os.path.join(dirname, "config.ini"), encoding="utf-8")

DATA_FOLDER = config["Files"]["DATA_FOLDER"]

print("Конфиг загружен успешно. Секции:", config.sections())
print("DATABASE_CREDS:", dict(config["Database"]))

DATABASE_CREDS = config["Database"]

# Подключение к БД
try:
    database = PGDatabase(
        host=DATABASE_CREDS["HOST"],
        database=DATABASE_CREDS["DATABASE"],
        user=DATABASE_CREDS["USER"],
        password=DATABASE_CREDS["PASSWORD"],
    )
except Exception as e:
    print(f"Ошибка подключения к базе данных: {e}")
    exit()

# Регулярка для файлов: \d+_\d+\.csv
file_pattern = re.compile(r'(\d+)_(\d+)\.csv')

for filename in os.listdir(DATA_FOLDER):
    match = file_pattern.match(filename)
    if not match:
        print(f"Игнорирую файл: {filename}")
        continue
    
    shop_num = int(match.group(1))
    cash_num = int(match.group(2))
    filepath = os.path.join(DATA_FOLDER, filename)
    
    try:
        df = pd.read_csv(filepath, encoding="utf-8")
        print(f"Обработка файла: {filename}, строк: {len(df)}")
        
        for i, row in df.iterrows():
            query = """
            INSERT INTO sales (shop_num, cash_num, doc_id, item, category, amount, price, discount)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (
                shop_num, cash_num, row['doc_id'], row['item'], row['category'],
                row['amount'], row['price'], row['discount']
            )
            database.post(query, values)
        
        os.remove(filepath)
        print(f"Файл {filename} загружен и удален.")
    except Exception as e:
        print(f"Ошибка при обработке {filename}: {e}")
# Sales Data Generate and Loader

Этот проект генерирует CSV-файлы чеков с продажами компьютерных комплектующих. Всего 5 магазинов, для каждого магазина генерируется случайное количество касс (от 2 до 5), и для каждой кассы — от 5 до 20 чеков с позициями (случайно).
Автоматизирует загрузку CSV-файлов с данными о продажах в базу данных PostgreSQL.  
Файлы с данными автоматически считываются из указанной папки, валидируются по имени, загружаются в таблицу `sales` и удаляются после успешной обработки.

## 📂 Структура проекта
├── run.py # Основной скрипт для запуска обработки файлов

├── generate-sales-data.py # Скрипт генерации данных

├── database.py # Класс для работы с PostgreSQL

├── config.ini # Конфигурационный файл (путь к данным, настройки БД)

├── .gitignore # Исключения для Git

└── requirements.txt - # Список всех пакетов и их их версий необходимых для проекта

## ⚙️ Настройка окружения
1. **Клонируйте репозиторий**
   ```bash
   git clone https://github.com/k0orn/AutoDep_Retail_PC.git
   cd AutoDep_Retail_PC
2. **Создайте и активируйте виртуальное окружение**
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
3. **Установите зависимости**
   ```bash
   pip install -r requirements.txt
4. **Отредактируйте config.ini**
   ```bash
   HOST = "Адресс БД"
   DATABASE = "Имя БД"
   USER = "Пользователь БД"
   PASSWORD = "Пароль БД"
5. **Создайте базу данных в PostgreSQL**
   ```bash
    CREATE DATABASE electronics_bd #Или любое другое название     
6. **Подготовьте таблицу в PostgreSQL**
   ```bash
   CREATE TABLE IF NOT EXISTS sales (
    id SERIAL PRIMARY KEY,
    shop_num INTEGER NOT NULL,
    cash_num INTEGER NOT NULL,
    doc_id VARCHAR(50) NOT NULL,
    item VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    amount INTEGER NOT NULL,
    price NUMERIC(10, 2) NOT NULL,
    discount NUMERIC(10, 2) NOT NULL );
7. **Запуск**
   ```bash
     python generate-sales-data.py
     python run.py
   
     





import sqlite3


# Подключаемся к базе данных (создается новая, если её нет)
conn = sqlite3.connect('./bd/example.db')
cursor = conn.cursor()

# Создаем таблицу users
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)
''')

# Добавляем пару примеров записей
cursor.execute("INSERT INTO users (first_name, last_name, email) VALUES ('Иван1', 'Иванов', 'ivan@example.com')")
cursor.execute("INSERT INTO users (first_name, last_name, email) VALUES ('Анна', 'Петрова', 'anna@example.com')")

# Сохраняем изменения
conn.commit()

# Читаем данные из таблицы
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
print("Пользователи:")
for row in rows:
    print(f"{row[0]} | Имя: {row[1]}, Фамилия: {row[2]}, Email: {row[3]}")

# Закрываем соединение
conn.close()
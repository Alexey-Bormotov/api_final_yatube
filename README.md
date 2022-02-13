### 1. Описание:

Проект сервиса API для Yatube.
Позволяет создавать, читать, изменять и удалять свои посты,
а так же читать чужие посты и подписываться на их авторов.
Для неавторизованных пользователей API доступен только для чтения.

### 2. Установка:

# Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/DIABLik666/api_final_yatube.git
```
```
cd api_final_yatube
```

# Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
```
```
source env/bin/activate
```

# Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```

# Выполнить миграции:
```
python3 manage.py migrate
```

# Запустить проект:
```
python3 manage.py runserver
```

### 3. Доступные эндпоинты:

# Посты:
```
"/api/v1/posts/" (Параметры для фильтрации "?limit=0&offset=0"),
"/api/v1/posts/{id}/"
```

# Группы:
```
"/api/v1/groups/",
"/api/v1/groups/{id}/"
```

# Комментарии:
```
"/api/v1/posts/{id}/comments/",
"/api/v1/posts/{id}/comments/{id}/"
```

# Подписки (Только для авторизованных пользователей):
```
"/api/v1/follow/" (Параметр для поиска "?search=''")
```

# Получение токена для доступа к API (Для зарегистрированных пользователей):
```
"/api/v1/auth/jwt/create/"
```

### 4. Примеры запросов к API:

# Получение списка всех постов:
```
Method: GET
Endpoint: "/api/v1/posts/"
```

# Публикация поста:
```
Method: POST
Endpoint: "/api/v1/posts/"
Payload:
{
    "text": "string",
    "image": "string",
    "group": 0
}
```

# Получение JWT-токена:
```
Method: POST
Endpoint: "/api/v1/auth/jwt/create/"
Payload:
{
    "username": "string",
    "password": "string"
}
```

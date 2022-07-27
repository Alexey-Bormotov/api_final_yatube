# API для проекта Yatube

## 1. [Описание](#1)
## 2. [Команды для запуска](#2)
## 3. [Доступные эндпоинты](#3)
## 4. [Примеры запросов](#4)
## 5. [Техническая информация](#5)
## 6. [Об авторе](#6)

---
## 1. Описание <a id=1></a>

Проект API для социальной сети [Yatube](https://github.com/DIABLik666/hw05_final).  
Позволяет создавать, читать, изменять и удалять свои посты, а так же читать чужие посты и подписываться на их авторов посредством API-запросов.  
Для неавторизованных пользователей API доступен только для чтения.

---
## 2. Команды для запуска <a id=2></a>

Перед запуском необходимо склонировать проект:
```bash
HTTPS: git clone https://github.com/DIABLik666/api_final_yatube.git
SSH: git clone git@github.com:DIABLik666/api_final_yatube.git
```

Cоздать и активировать виртуальное окружение:
```bash
python -m venv venv
```
```bash
Linux: source venv/bin/activate
Windows: source venv/Scripts/activate
```

И установить зависимости из файла requirements.txt:
```bash
python3 -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```

Выполнить миграции:
```bash
python3 manage.py migrate
```

Запустить проект:
```bash
python3 manage.py runserver
```

Теперь доступность проекта можно проверить по адресу [http://localhost/admin/](http://localhost/admin/)

---
## 3. Доступные эндпоинты <a id=3></a>

Посты:
```
"/api/v1/posts/" (Параметры для фильтрации "?limit=0&offset=0"),
"/api/v1/posts/{id}/"
```

Группы:
```
"/api/v1/groups/",
"/api/v1/groups/{id}/"
```

Комментарии:
```
"/api/v1/posts/{id}/comments/",
"/api/v1/posts/{id}/comments/{id}/"
```

Подписки (Только для авторизованных пользователей):
```
"/api/v1/follow/" (Параметр для поиска "?search=''")
```

Получение токена для доступа к API (Для зарегистрированных пользователей):
```
"/api/v1/auth/jwt/create/"
```

---
## 4. Примеры запросов <a id=4></a>

Получение списка всех постов:
```
Method: GET
Endpoint: "/api/v1/posts/"
```

Публикация поста:
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

Получение JWT-токена:
```
Method: POST
Endpoint: "/api/v1/auth/jwt/create/"
Payload:
{
    "username": "string",
    "password": "string"
}
```

---
## 5. Техническая информация <a id=5></a>

Стек технологий: Python 3, Django, Django Rest, simple JWT.

---
## 6. Об авторе <a id=6></a>

Бормотов Алексей Викторович  
Python-разработчик (Backend)  
Россия, г. Кемерово  
E-mail: di-devil@yandex.ru  
Telegram: @DIABLik666

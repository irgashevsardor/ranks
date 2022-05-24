Для запуска:

1. Склонируйте репозиторий
2. ```cd ranks/```
3. ```pip install -r requirements.txt```
4. Создайте файл .env и внесите соответствующие ключи (пример в .env.dist; для генерации SECRET_KEY: https://djecrety.ir/)
5. ```./manage.py migrate```
6. Создайте суперпользователя
6. ```./manage.py runserver```
7. Внесите данные в базу данных через панель администратора

Готово!

Пример запроса: ```curl -X GET http://localhost:8000/item/1```

# TermProject

- 'poetry shell' - вход в виртуальное окружение.

- 'poetry install' - установка зависимостей.

- 'python manage.py migrate' - выполнить миграции.

- 'python manage.py runserver' - запуск сервера для разработки на 'http://localhost:8000'.

---

- 'docker-compose -f deploy/docker-compose.yml -p termproject up' - Запуск через Docker

---

- 'poetry env info -p' - Узнать расположение интерпретатора для настройки проекта в PyCharm.

- 'python manage.py test' - Чтобы запустить тесты для проверки.

- 'python manage.py dumpdata имя приложения.название модели > название.json' - Для сохранения данных в БД.

- 'python manage.py loaddata путь/название.json' - Для скачивание данных.

- 'python manage.py test && coverage report' - Проверка покрытия тестов.

- 'celery -A myweb worker -l info' - Запуск воркера celery.
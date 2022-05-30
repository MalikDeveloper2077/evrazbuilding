> docker-compose up --build

### В интерфейсе докера
> cd evraz
> python manage.py migrate
> python manage.py createsuperuser

* Переходим на localhost:8000/admin
* Открываем вкладку запуск импорта и создаем там объект
* Теперь проверяем остальные вкладки на наличие новых данных
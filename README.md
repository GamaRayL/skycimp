# Skychimp
Проект представляет собой веб-приложение для управления рассылками и ведения блога. Сервис позволяет создавать, администрировать и отслеживать статистику рассылок.

## Содержание
- [Технологии](#технологии)
- [Начало работы](#начало-работы)
- [Функциональные возможности](#функциональные-возможности)

## Технологии
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [Redis](https://redis.io/)
- [Bootstrap](https://getbootstrap.com/)
- [HTML](https://developer.mozilla.org/ru/docs/Learn/Getting_started_with_the_web/HTML_basics)
- [CSS](https://developer.mozilla.org/ru/docs/Learn/Getting_started_with_the_web/CSS_basics)


## Начало работы
После клонирования проекта, рекомендуется:

Установить виртуальное окружение:
```sh
$ python3 -m vevn venv
```

Установить список зависимостей:
```sh
$ pip install -r requirements.txt
```

Отредактировать .env файл под себя:
```python
# Debug
DEBUG=True
...
```

Зависимости:
```python
django
psycopg2-binary
redis
apscheduler
django-apscheduler
python-dotenv
pillow
ipython
```

## Функциональные возможности
1. **CRUD для рассылок**: реализован механизм создания, чтения, обновления и удаления рассылок. Пользователи могут добавлять новые рассылки, просматривать существующие и удалять те, которые им больше не нужны.
2. **Скрипт рассылки**: разработан скрипт рассылки, который работает как из командной строки, так и по расписанию. Скрипт позволяет отправлять письма клиентам в соответствии с настройками рассылки. Скрипт запускается командой ```sh $ python3 manage.py run_mailing.py``
3. **Периодические задачи**: для периодического выполнения рассылок использованы crontab-задачи. Они позволяют запускать рассылки по расписанию без участия пользователя. Скрипт для периодического выполнения ``sh $ python3 manage.py run_apscheduler.py```
4. **Регистрация и верификация пользователей**: реализована регистрация пользователей через почту, а также механизм верификации для подтверждения почтового ящика.
5. **Ограничение доступа**: разделены права доступа для разных пользователей. Менеджер имеет право блокировать пользователей и отключать рассылки, но не может редактировать рассылки. Пользователи могут управлять только своими списками клиентов и рассылок.
6. **Интерфейс менеджера**: разработан интерфейс для менеджера, который позволяет просматривать рассылки и список пользователей, блокировать пользователей и отключать рассылки.

### Сущности системы
* **Клиент сервиса**: для каждого клиента хранится контактный email, имя и комментарий.
* **Рассылка (настройки)**: рассылки имеют настройки времени рассылки, периодичности (ежедневно, еженедельно, ежемесячно) и статус рассылки (создана, запущена, завершена).
* **Сообщение для рассылки**: для каждого сообщения хранятся тема письма и его тело.
* **Логи рассылки**: хранятся данные о дате и времени последней попытки рассылки, статусе попытки и ответе почтового сервера, если он был.

### Логика работы системы
* **Автоматическая Рассылка**: после создания новой рассылки, если текущее время находится в заданном временном интервале, система автоматически выбирает клиентов из настроек рассылки и отправляет сообщения.
* **Планирование Рассылок**: если рассылка запланирована на будущее, рассылка начинается автоматически по наступлению указанного времени, не требуя дополнительных действий пользователя.
* **Статистика и Логирование**: во время отправки сообщений собирается статистика для последующего формирования отчетов. Логи рассылки содержат информацию о статусе попыток и ответах почтового сервера.

### Функционал Менеджера
* Просмотр всех рассылок.
* Просмотр списка пользователей сервиса.
* Блокировка пользователей сервиса.
* Отключение рассылок.
* Не имеет права редактировать рассылки.

### Функционал Пользователя
* Управление своими списками клиентов и рассылок.
* Запрет изменения чужих рассылок.

### Главная Страница
* Реализована главная страница, отображающая информацию о количестве рассылок, активных рассылках, уникальных клиентах для рассылок и три случайные статьи из блога.

#### Кеширование
* Произведено кеширование логов и главной страницы для оптимизации производительности.
---
Эти функции позволяют пользователям эффективно управлять рассылками и блогом, а также обеспечивают продвижение сервиса через интересный и информативный контент.

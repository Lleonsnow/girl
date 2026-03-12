# Girl

Лендинг-сайт с админкой: главная, страницы «Обо мне», «Фото», «Контакты», FAQ, политика и соглашение. Контент и изображения настраиваются через Django Admin.

## Стек

| Часть     | Технологии |
|----------|------------|
| Backend  | Python 3.12, Django 5+, Gunicorn, PostgreSQL 16 |
| Frontend | Nuxt 3, Vue 3, Pinia, i18n (ru/en), SCSS |
| Инфра    | Docker, Docker Compose, Nginx |

Админка: [django-unfold](https://github.com/unfoldadmin/django-unfold). API отдаёт единый endpoint конфигурации сайта (`/api/site-config/`) для героя, карусели, фото и соцсетей.

## Требования

- [Docker](https://docs.docker.com/get-docker/) и Docker Compose
- Для локальной разработки без Docker: Node 20+, Yarn, Python 3.12+, PostgreSQL 16

## Быстрый старт (Docker)

1. **Клонировать и перейти в каталог**
   ```bash
   cd girl
   ```

2. **Настроить переменные окружения**
   - `backend/.env` — обязательно (БД, Django, суперпользователь). Пример:
     ```env
     DJANGO_SECRET_KEY=your-secret-key
     DJANGO_DEBUG=1
     DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
     POSTGRES_DB=girl
     POSTGRES_USER=girl
     POSTGRES_PASSWORD=girl
     POSTGRES_HOST=postgres
     POSTGRES_PORT=5432
     DJANGO_SUPERUSER_USERNAME=admin
     DJANGO_SUPERUSER_EMAIL=admin@local
     DJANGO_SUPERUSER_PASSWORD=admin
     ADMIN_SECRET_KEY=your-admin-secret
     ```
   - `frontend/.env` — опционально для продакшена за nginx:
     ```env
     NUXT_PUBLIC_API_BASE=http://localhost:8000
     ```
     В Docker за nginx фронт ходит на бэкенд по внутреннему имени, поэтому для `docker compose --profile prod` можно оставить значение по умолчанию или указать `http://backend:8000` при необходимости.

3. **Запуск**
   - Только бэкенд + Nginx + PostgreSQL (главная будет отдаваться с бэкенда или можно смотреть только API/админку):
     ```bash
     docker compose up -d
     ```
   - Сборка и запуск с фронтом (один ряд, через Nginx):
     ```bash
     docker compose --profile prod up -d --build
     ```

4. **Открыть**
   - Сайт: http://localhost  
   - Админка: http://localhost/admin/ (логин/пароль из `DJANGO_SUPERUSER_*`)

При первом запуске выполняются миграции, создаётся суперпользователь, заполняются дефолтные изображения из `frontend/public` (если есть) и сбор статики.

## Переменные окружения

### Backend (`backend/.env`)

| Переменная | Описание |
|------------|----------|
| `DJANGO_SECRET_KEY` | Секретный ключ Django |
| `DJANGO_DEBUG` | `1` — debug, иначе выключен |
| `DJANGO_ALLOWED_HOSTS` | Через запятую (например `localhost,127.0.0.1`) |
| `POSTGRES_*` | Подключение к PostgreSQL (`HOST` в Docker — `postgres`) |
| `DJANGO_SUPERUSER_USERNAME` / `EMAIL` / `PASSWORD` | Данные суперпользователя при первом запуске |
| `ADMIN_SECRET_KEY` | Секрет для входа в админку (опционально, см. middleware) |
| `CORS_ALLOWED_ORIGINS` / `CSRF_TRUSTED_ORIGINS` | При деплое добавить свой домен |
| `SITE_ORIGIN` | Публичный URL сайта (для CORS/CSRF) |
| `AUTHOR_*`, `SITE_*` | Имя, псевдоним, соцсети, контакты — подставляются в API и админку |

### Frontend (`frontend/.env`)

| Переменная | Описание |
|------------|----------|
| `NUXT_PUBLIC_API_BASE` | URL бэкенда (по умолчанию `http://localhost:8000`) |

## Разработка без Docker

- **Backend:** создать виртуальное окружение, установить зависимости из `backend/requirements.txt`, поднять PostgreSQL, создать БД и прописать в `.env`. Запуск: `python manage.py runserver` (порт 8000).
- **Frontend:** в каталоге `frontend` выполнить `yarn install` и `yarn dev` (порт 3000). В `.env` указать `NUXT_PUBLIC_API_BASE=http://localhost:8000`.

Статика и медиа бэкенда при локальном запуске — по настройкам Django (например `STATIC_URL`, `MEDIA_*`).

## Структура репозитория

```
├── backend/          # Django: config (settings, urls, models, API, admin), manage.py
├── frontend/         # Nuxt 3: pages, components, stores, i18n, assets
├── nginx/            # Конфиг и Dockerfile для Nginx
├── docker-compose.yml
└── README.md
```

- **Backend:** приложение `config` — модели (в т.ч. изображения по категориям), `site_config_views` (API конфига), `consent_views`, админка Unfold, команды `ensure_superuser`, `ensure_site_images`.
- **Frontend:** главная, страницы about/photos/contacts/privacy/terms, галерея, FAQ, CTA, попапы; store `siteConfig` запрашивает `/api/site-config/`.

## Полезные команды

```bash
# Остановить всё
docker compose --profile prod down

# Логи
docker compose logs -f backend
docker compose logs -f frontend
```

## Лицензия

По желанию правообладателя.

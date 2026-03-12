FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /app

RUN pip install --no-cache-dir -q pip

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate --noinput && python manage.py ensure_superuser && python manage.py ensure_site_images && python manage.py collectstatic --noinput && gunicorn --bind 0.0.0.0:8000 --workers 4 config.wsgi:application"]

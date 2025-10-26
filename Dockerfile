# ===== Dockerfile =====
FROM python:3.11-slim

# تنظیمات محیطی برای تمیزتر بودن اجرا
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# محل پروژه در داخل کانتینر
WORKDIR /app

# نصب پکیج‌های موردنیاز
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# کپی کل پروژه داخل کانتینر
COPY . .

# اکسپوز پورت 8000 برای دسترسی از بیرون
EXPOSE 8000

# اجرای سرور توسعه جنگو
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
